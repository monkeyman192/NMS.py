import logging

from nmspy.hooking import one_shot, disable
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

    @disable
    @hooks.AK.SoundEngine.PostEvent.before
    def before_sound_event(self, *args):
        logging.info(f"Played sound with params: {args}")

    @disable
    @hooks.cTkMetaData.GetLookup.before
    def before_lookup_metadata(self, luiNameHash):
        logging.info(f"Hook 1, namehash: 0x{luiNameHash:X}")

    @disable
    @hooks.cTkMetaData.GetLookup.after
    def after_lookup_metadata(self, lpacName, __result):
        logging.info(f"Looking: {lpacName}, {__result}")
        data = map_struct(__result, nms_structs.cTkMetaDataXMLFunctionLookup)
        logging.info(f"Looked up: {data.name}")

    @disable
    @hooks.cTkMetaData.GetLookup.after
    def after_lookup_metadata2(luiNameHash, __result):
        logging.info(f"Hook 1, namehash: 0x{luiNameHash:X}, return val: {__result}")

    @disable
    @hooks.cTkMetaData.GetLookup.after
    def after_lookup_metadata3(self, luiNameHash, __result):
        if __result:
            data = map_struct(__result, nms_structs.cTkMetaDataFunctionLookup)
            logging.info(f"Looked up: {data.classMetadata}")

    @hooks.cGcApplicationDeathState.Update.before
    def update_application_deathstate(self, this, lfTimeStep: float):
        logging.info(f"Called cGcApplicationDeathState::Update: {this}, {lfTimeStep}")

    @disable
    @hooks.cTkMetaData.Register.after
    def detour(self, lpClassMetadata, *args, __result):
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

    @one_shot
    @hooks.cGcApplication.Construct.before
    def construct_gcapp(self, this):
        logging.info(f"cGcApplication* construct: 0x{this:X}")
        logging.info(f"Diff: 0x{this - nms.BASE_ADDRESS:X}")
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
    def start_updating_UI(self, this, __result):
        try:
            logging.info(f"cGcApplicationGameModeSelectorState*: {this}")
            logging.info(str(__result))
        except:
            logging.info("Something went wrong!!!")
