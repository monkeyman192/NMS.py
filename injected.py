try:
    import asyncio
    import builtins
    import ctypes
    import ctypes.wintypes
    from functools import partial
    import json
    import logging
    import logging.handlers
    import os
    import os.path as op
    import time
    import traceback
    import sys

    import nmspy.common as nms
    import nmspy._internal as _internal

    # Before any nmspy.data imports occur, set the os.environ value for the
    # binary hash:
    if _internal.BINARY_HASH:
        os.environ["NMS_BINARY_HASH"] = _internal.BINARY_HASH
    else:
        # If there is no binary hash, something has gone wrong. Exit now since
        # we can't continue.
        sys.exit(-1)

    import nmspy.data.structs as nms_structs
    import nmspy.data.functions as nms_funcs
    import nmspy.extractors.metaclasses as metaclass_extractor
    import nmspy.data.enums as enums
    from nmspy.hooking import (
        one_shot, HookManager, hook_function, conditionally_enabled_hook,
        NMSHook, after, before
    )
    from nmspy.protocols import (
        ExecutionEndedException,
        custom_exception_handler,
        ESCAPE_SEQUENCE
    )
    from nmspy.memutils import map_struct, pprint_mem, get_addressof
    from nmspy.mod_loader import ModManager
    from nmspy.caching import globals_cache, load_caches

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.INFO)
    socketHandler = logging.handlers.SocketHandler(
        "localhost",
        logging.handlers.DEFAULT_TCP_LOGGING_PORT
    )
    rootLogger.addHandler(socketHandler)
    logging.info("Loading NMS.py...")
    logging.info(nms.BASE_ADDRESS)

    hook_logger = logging.getLogger("HookManager")

    # Some variables to handle some globally defined objects or contexts.
    # Note that depending on the game version one or more of these may never be
    # set.
    metadata_registry = {}
    gravity_singleton = None
    nvg_context = None

    # Before any hooks are registered, load the caches.
    load_caches(_internal.BINARY_HASH)

    # Since we are running inside a thread, `asyncio.get_event_loop` will
    # generally fail.
    # Detect this and create a new event loop anyway since we are running in a
    # thread under the process we have been injected into, and not the original
    # python thread that is running the show.
    try:
        loop = asyncio.get_event_loop()
    except (RuntimeError, ValueError) as e:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Set the custom exception handler on the loop
    loop.set_exception_handler(custom_exception_handler)

    # NOTE: This class MUST be defined here. If it's defined in a separate file
    # then the hack done to persist data to the current global context will not
    # work.
    class ExecutingProtocol(asyncio.Protocol):
        """ A protocol factory to be passed to a asyncio loop.create_server call
        which will accept requests, execute them and persist any variables to
        globals()."""
        def connection_made(self, transport):
            peername = transport.get_extra_info('peername')
            self.transport = transport
            builtins.print('Connection from {}'.format(peername))
            # Overwrite print so that any `print` statements called in the commands
            # to be executed will be written back out of the socket they came in.
            globals()['print'] = partial(builtins.print, file=self)

        def write(self, value: str):
            """ Method to allow this protocol to be used as a file to write to.
            This allows us to have `print` write to this protocol."""
            self.transport.write(value.encode())

        def data_received(self, __data: bytes):
            # Have an "escape sequence" which will force this to exit.
            # This way we can kill it if need be from the other end.
            if __data == ESCAPE_SEQUENCE:
                print("\nReceived exit command!")
                raise ExecutionEndedException
            try:
                exec(__data.decode())
            except:
                print(traceback.format_exc())
            else:
                self.persist_to_globals(locals())

        def persist_to_globals(self, data: dict):
            """ Take the dictionary which was determined by calling `locals()`, and
            update `gloabsl()` with it."""
            data.pop("self")
            data.pop(f"_{type(self).__name__}__data")
            globals().update(data)

        def eof_received(self):
            # Do nothing.
            pass

        def connection_lost(self, exc):
            # Once the connection is lost. Restore `print` back to normal.
            globals()['print'] = builtins.print


    # Load any globals based on any cached offsets.
    for global_name, relative_offset in globals_cache.items():
        # For each global, construct the object and then assign it to the
        # nms.<global_name>
        setattr(
            nms,
            global_name,
            map_struct(
                nms.BASE_ADDRESS + relative_offset,
                getattr(nms_structs, "c" + global_name)
            )
        )

    @conditionally_enabled_hook(nms.GcWaterGlobals is None)
    @hook_function("cTkMetaData::ReadGlobalFromFile<cGcWaterGlobals>")
    class cTkMetaData__ReadGlobalFromFile_cGcWaterGlobals(NMSHook):
        def detour(self, lpData: int, lpacFilename: bytes):
            try:
                logging.info(f"cGcWaterGlobals*: 0x{lpData:X}, filename: {lpacFilename}")
                globals_cache.set("GcWaterGlobals", lpData - nms.BASE_ADDRESS)
                ret = self.original(lpData, lpacFilename)
                data = map_struct(lpData, nms_structs.cGcWaterGlobals)
                nms.GcWaterGlobals = data
                for field in data._fields_:
                    logging.info(f"{field[0]}: {getattr(data, field[0])}")
                nms.GcWaterGlobals.UseNewWater = 0
            except:
                logging.error(traceback.format_exc())
            finally:
                return ret


    # @hook_function("AK::SoundEngine::PostEvent")
    # class PlaySound_Hook(NMSHook):
    #     def detour(self, *args):
    #         logging.info(f"Played sound with params: {args}")
    #         return self.original(*args)

    # @hook_function("cTkMetaData::GetLookup")
    # class LookupMetadata(NMSHook):
    #     @after
    #     def detour(self, lpacName, result):
    #         logging.info(f"Looking: {lpacName}, {result}")
    #         data = map_struct(result, nms_structs.cTkMetaDataXMLFunctionLookup)
    #         logging.info(f"Looked up: {data.name}")


    # @hook_function("cTkMetaData::GetLookup")
    # class LookupMetadata(NMSHook):
    #     @before
    #     def detour(self, luiNameHash):
    #         logging.info(f"Hook 1, namehash: 0x{luiNameHash:X}")


    # @hook_function("cTkMetaData::GetLookup")
    # class LookupMetadata(NMSHook):
    #     @after
    #     def detour(self, luiNameHash, result):
    #         if result:
    #             data = map_struct(result, nms_structs.cTkMetaDataFunctionLookup)
    #             logging.info(f"Looked up: {data.classMetadata}")


    @hook_function("cGcApplicationDeathState::Update")
    class DeathStateUpdate(NMSHook):
        def detour(self, this, lfTimeStep: float):
            logging.info(f"Called cGcApplicationDeathState::Update: {this}, {lfTimeStep}")
            self.original(this, lfTimeStep)


    @hook_function("cTkMetaData::Register")
    class RegisterMetadata(NMSHook):
        def detour(self, lpClassMetadata, *args):
            result = self.original(lpClassMetadata, *args)
            if lpClassMetadata:
                meta: nms_structs.cTkMetaDataClass = lpClassMetadata.contents
                metaclass_extractor.extract_members(meta, metadata_registry)
                logging.info(f"Added {meta.name} to metadata registry")
            return result


    @hook_function("cGcSolarSystem::Generate")
    class GenerateSolarSystem(NMSHook):
        def detour(self, this, lbUseSettingsFile, lSeed):
            ret = self.original(this, lbUseSettingsFile, lSeed)
            data = map_struct(this, nms_structs.cGcSolarSystem)
            logging.info(f"Number of planets: {data.solarSystemData.planets} in system {data.solarSystemData.name}")
            return ret


    @hook_function("cTkInputPort::SetButton", pattern="40 57 48 83 EC 40 48 83")
    class GetInput_Hook(NMSHook):
        def detour(self, this, leIndex):
            logging.info(f"cTkInputPort*: {this}")
            IP = map_struct(this, nms_funcs.cTkInputPort)
            if leIndex == enums.eInputButton.EInputButton_Space:
                IP.SetButton(enums.eInputButton.EInputButton_Mouse1)
            else:
                return self.original(this, leIndex)

    @one_shot
    @hook_function("cGcGameState::LoadSpecificSave")
    class cGcGameState__LoadSpecificSave_Hook(NMSHook):
        def detour(self, this, leSpecificSave):
            logging.info(f"cGcGameState*: {this}, save type: {leSpecificSave}")
            ret = self.original(this, leSpecificSave)
            logging.info(str(ret))
            return ret

    @one_shot
    @hook_function("cGcApplication::cGcApplication")
    class cGcApplication__cGcApplication(NMSHook):
        def detour(self, this):
            logging.info(f"cGcApplication constructor: 0x{this:X}")
            logging.info(f"Diff: 0x{this - nms.BASE_ADDRESS:X}")
            nms.GcApplication = this + 0x50  # WHY??
            return self.original(this)


    @one_shot
    @hook_function("cGcApplication::Construct")
    class cGcApplication__Construct(NMSHook):
        def detour(self, this):
            logging.info(f"cGcApplication* construct: 0x{this:X}")
            logging.info(f"Diff: 0x{this - nms.BASE_ADDRESS:X}")
            return self.original(this)
            # try:
            #     logging.info(pprint_mem(nms.GcApplication, 0x100, 0x10))
            #     gcapp = map_struct(nms.GcApplication, nms_structs.cGcApplication)
            #     logging.info(gcapp.data)
            #     logging.info(f"{get_addressof(gcapp.data):X}")
            #     logging.info(dir(gcapp.data))
            #     logging.info(gcapp.data.contents)
            #     logging.info(gcapp.data.contents.firstBootContext.state)
            # except:
            #     logging.error(traceback.format_exc())
            # finally:
            #     return ret


    @hook_function("cGcApplication::Update")
    class cGcApplication__Update(NMSHook):
        def detour(self, this):
            return self.original(this)


    @one_shot
    @hook_function("cTkDynamicGravityControl::Construct")
    class cTkDynamicGravityControl__Construct(NMSHook):
        def detour(self, this):
            logging.info("Loaded grav singleton")
            globals()["gravity_singleton"] = this
            return self.original(this)


    @hook_function("cGcApplicationGameModeSelectorState::UpdateStartUI")
    class cGcApplicationGameModeSelectorState__UpdateStartUI(NMSHook):
        def detour(self, this):
            try:
                logging.info(f"cGcApplicationGameModeSelectorState*: {this}")
                ret = self.original(this)
                logging.info(str(ret))
                return ret
            except:
                logging.info("Something went wrong!!!")

    hook_manager = HookManager()
    hook_manager.register(cGcGameState__LoadSpecificSave_Hook)
    hook_manager.register(cTkMetaData__ReadGlobalFromFile_cGcWaterGlobals)
    hook_manager.register(cGcApplicationGameModeSelectorState__UpdateStartUI)
    hook_manager.register(cGcApplication__Construct)
    # hook_manager.register(LookupMetadata)
    # hook_manager.register(RegisterMetadata)
    hook_manager.register(DeathStateUpdate)
    hook_manager.register(cTkDynamicGravityControl__Construct)
    hook_manager.register(GenerateSolarSystem)
    hook_manager.register(GetInput_Hook)
    hook_manager.register(cGcApplication__cGcApplication)
    logging.info("NMS.py injection complete!")
    logging.info("Current hook states:")
    for state in hook_manager.states:
        logging.info(state)

    mod_manager = ModManager(hook_manager)

    # Also load any mods after all the internal hooks:
    start_time = time.time()
    mod_manager.load_mod_folder(op.join(_internal.CWD, "mods"))
    end_time = time.time()
    logging.info(f"Found {len(mod_manager.mods)} in {end_time - start_time:.3f}s")
    mod_manager.enable_all()
    logging.info(f"Loaded {len(mod_manager.mods)} in {time.time() - end_time:.3f}s")

    for func_name, hook_class in hook_manager.failed_hooks.items():
        offset = hook_class.target
        _data = (ctypes.c_char * 0x20).from_address(offset)
        hook_logger.error(f"Hook {func_name} first 0x20 bytes: {_data.value.hex()}")

    # Each client connection will create a new protocol instance
    coro = loop.create_server(ExecutingProtocol, '127.0.0.1', 6770)
    server = loop.run_until_complete(coro)

    logging.info(f'Serving on executor {server.sockets[0].getsockname()}')
    loop.run_forever()

    # Close the server.
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

except Exception as e:
    # If we hit this, something has gone wrong. Log to the current directory.
    import traceback
    import os.path as op

    try:
        # Try and log to the current working directory.
        # Sometimes this may fail as the error is an "internal" one, so we will
        # add a fail-safe to log to the users' home directory so that it at
        # least is logged somewhere.
        # TODO: Document this behaviour.
        import nmspy._internal as _internal

        with open(op.join(_internal.CWD, "CRITICAL_ERROR.txt"), "w") as f:
            traceback.print_exc(file=f)
    except:
        with open(op.join(op.expanduser("~"), "CRITICAL_ERROR.txt"), "w") as f:
            traceback.print_exc(file=f)
