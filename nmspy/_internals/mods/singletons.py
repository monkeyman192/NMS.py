from logging import getLogger
import traceback

from pymhf.core._types import DetourTime
from pymhf.gui.decorators import no_gui
import pymhf.core._internal as _internal
from pymhf.core.hooking import one_shot, hook_manager
from pymhf.core.memutils import map_struct
import nmspy.common as nms
import nmspy._internals.staging as staging
import nmspy.data.structs as structs
import nmspy.data.functions.hooks as hooks
from nmspy._types import NMSMod
from nmspy.states import StateEnum


logger = getLogger()


@no_gui
class _INTERNAL_LoadSingletons(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Load singletons and other important objects"
    __version__ = "0.1"

    @one_shot
    @hooks.cTkDynamicGravityControl.Construct.before
    def load_gravity_singleton(self, this):
        nms.gravity_singleton = map_struct(this, structs.cTkDynamicGravityControl)

    @one_shot
    @hooks.cTkMemoryManager.Construct.after
    def construct_cTkMemoryManager(self, this, *args):
        nms.memory_manager = this

    @one_shot
    @hooks.cGcApplication.cGcApplication.after
    def load_cGcApplication(self, this):
        staging._cGcApplication = map_struct(this + 0x50, structs.cGcApplication)  # WHY??

    @one_shot
    @hooks.cGcRealityManager.cGcRealityManager.after
    def cGcRealityManager_initializer(self, this):
        # At this point we can move cGcApplication out of staging.
        nms.GcApplication = staging._cGcApplication

    @hooks.cTkFSMState.StateChange.after
    def state_change(self, this, lNewStateID, lpUserData, lbForceRestart):
        logger.info(f"New State: {lNewStateID}")
        if lNewStateID == StateEnum.ApplicationGameModeSelectorState.value:
            curr_gamestate = _internal.GameState.game_loaded
            _internal.GameState.game_loaded = True
            if _internal.GameState.game_loaded != curr_gamestate:
                # Only call this the first time the game loads
                hook_manager.call_custom_callbacks("MODESELECTOR", DetourTime.AFTER)
                hook_manager.call_custom_callbacks("MODESELECTOR", DetourTime.NONE)
        else:
            hook_manager.call_custom_callbacks(lNewStateID.decode(), DetourTime.AFTER)
            hook_manager.call_custom_callbacks(lNewStateID.decode(), DetourTime.NONE)

    # @one_shot
    # @hooks.cGcRealityManager.Construct.after
    # def cGcRealityManager_construct(self, this):
    #     logging.info(f"cGcRealityManager::Construct: 0x{this:X}")
    #     try:
    #         reality_manager = nms.GcApplication.data.contents.RealityManager
    #         logging.info(f"cGcRealityManager: {ctypes.addressof(reality_manager)}")
    #     except:
    #         logging.info(traceback.format_exc())

    @hooks.cGcApplication.Update.before
    def _main_loop_before(self, *args):
        """ The main application loop. Run any before functions here. """
        hook_manager.call_custom_callbacks("MAIN_LOOP", DetourTime.BEFORE)

    @hooks.cGcApplication.Update.after
    def _main_loop_after(self, *args):
        """ The main application loop. Run any after functions here. """
        hook_manager.call_custom_callbacks("MAIN_LOOP", DetourTime.AFTER)
