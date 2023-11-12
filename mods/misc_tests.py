import logging

from nmspy.hooking import one_shot, disable, main_loop
import nmspy.extractors.metaclasses as metaclass_extractor
import nmspy.common as nms
from nmspy.memutils import map_struct
import nmspy.data.structs as nms_structs
import nmspy.data.function_hooks as hooks
from nmspy.mod_loader import NMSMod


class MiscMod(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Misc stuff..."
    __version__ = "1.0"

    def __init__(self):
        self.counter = 0
        super().__init__()

    @hooks.AK.SoundEngine.PostEvent.before
    @disable
    def before_sound_event(self, *args):
        logging.info(f"Played sound with params: {args}")

    @hooks.cTkMetaData.GetLookup.before
    @disable
    def before_lookup_metadata(self, luiNameHash):
        logging.info(f"Hook 1, namehash: 0x{luiNameHash:X}")

    @hooks.cTkMetaData.GetLookup.after
    @disable
    def after_lookup_metadata(self, lpacName, _result_):
        logging.info(f"Looking: {lpacName}, {_result_}")
        data = map_struct(_result_, nms_structs.cTkMetaDataXMLFunctionLookup)
        logging.info(f"Looked up: {data.name}")

    @hooks.cTkMetaData.GetLookup.after
    @disable
    def after_lookup_metadata2(luiNameHash, _result_):
        logging.info(f"Hook 1, namehash: 0x{luiNameHash:X}, return val: {_result_}")

    @hooks.cTkMetaData.GetLookup.after
    @disable
    def after_lookup_metadata3(self, luiNameHash, _result_):
        if _result_:
            data = map_struct(_result_, nms_structs.cTkMetaDataFunctionLookup)
            logging.info(f"Looked up: {data.classMetadata}")

    @hooks.cGcApplicationDeathState.Update.before
    def update_application_deathstate(self, this, lfTimeStep: float):
        logging.info(f"Called cGcApplicationDeathState::Update: {this}, {lfTimeStep}")

    @hooks.cTkMetaData.Register.after
    @disable
    def detour(self, lpClassMetadata, *args, _result_):
        if lpClassMetadata:
            meta: nms_structs.cTkMetaDataClass = lpClassMetadata.contents
            # metaclass_extractor.extract_members(meta, metadata_registry)
            logging.info(f"Added {meta.name} to metadata registry")

    @hooks.cGcSolarSystem.Generate.after
    def generate_solarsystem(self, this, lbUseSettingsFile, lSeed):
        data = map_struct(this, nms_structs.cGcSolarSystem)
        logging.info(f"Number of planets: {data.solarSystemData.planets} in system {data.solarSystemData.name}")

    # @hook_function("cTkInputPort::SetButton", pattern="40 57 48 83 EC 40 48 83")
    # class GetInput_Hook(NMSHook):
    #     def detour(self, this, leIndex):
    #         logging.info(f"cTkInputPort*: {this}")
    #         IP = map_struct(this, nms_funcs.cTkInputPort)
    #         if leIndex == local_types.eInputButton.EInputButton_Space:
    #             IP.SetButton(local_types.eInputButton.EInputButton_Mouse1)
    #         else:
    #             return self.original(this, leIndex)

    @one_shot
    @hooks.cGcGameState.LoadSpecificSave
    def load_specific_save(self, this, leSpecificSave):
        logging.info(f"cGcGameState*: {this}, save type: {leSpecificSave}")
        ret = hooks.cGcGameState.LoadSpecificSave.original(this, leSpecificSave)
        logging.info(str(ret))
        return ret

    def slow_thing(self):
        import time
        logging.info("starting to sleep!")
        time.sleep(10)
        logging.info("I'm awake!")

    @one_shot
    @hooks.cGcApplication.Construct.before
    def construct_gcapp(self, this):
        logging.info(f"cGcApplication* construct: 0x{this:X}")
        logging.info(f"Diff: 0x{this - nms.BASE_ADDRESS:X}")
        nms.executor.submit(self.slow_thing)
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

    @hooks.cGcApplicationGameModeSelectorState.UpdateStartUI.after
    def start_updating_UI(self, this, _result_):
        try:
            logging.info(f"cGcApplicationGameModeSelectorState*: {this}")
            logging.info(str(_result_))
        except:
            logging.info("Something went wrong!!!")

    # TODO: Re-add the functionality for conditionally applied hooks?
    # @main_loop.after
    # def lala(self):
    #     if self.counter < 100:
    #         logging.info(self.counter)
    #     self.counter += 1
