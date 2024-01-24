# import ctypes
import logging

from nmspy.hooking import one_shot, disable, manual_hook
import nmspy.common as nms
from nmspy.memutils import map_struct
import nmspy.data.structs as nms_structs
import nmspy.data.function_hooks as hooks
from nmspy.mod_loader import NMSMod
# from nmspy._types import FUNCDEF


# funcdef = FUNCDEF(
#     restype=ctypes.c_uint64,  # unsigned __int64
#     argtypes=[
#         ctypes.c_ulonglong,  # TkID<128> *this
#     ]
# )


class MiscMod(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Misc stuff..."
    __version__ = "1.0"
    __NMSPY_required_version__ = "0.6.5"

    def __init__(self):
        self.counter = 0
        super().__init__()


    # @manual_hook("TkID<128>_hook", 0xC726C0, funcdef)
    # def thing(self, this, _result_):
    #     logging.info("TkID<128> hash thing...")
    #     logging.info(this)
    #     logging.info(_result_)

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
    @disable
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
    @disable
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

    @hooks.cGcApplicationGameModeSelectorState.UpdateStartUI.after
    @disable
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
