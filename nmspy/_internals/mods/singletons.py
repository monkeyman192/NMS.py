import nmspy.common as nms
import nmspy._internal as _internal
import nmspy._internals.staging as staging
import nmspy.data.structs as structs
import nmspy.data.function_hooks as hooks
from nmspy.hooking import one_shot, hook_manager
from nmspy.memutils import map_struct
from nmspy.mod_loader import NMSMod
from nmspy.states import StateEnum


class _INTERNAL_LoadSingletons(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Load singletons and other important objects"
    __version__ = "0.1"

    def run_on_fully_booted_funcs(self):
        # Call any functions which are to be called once the GcApplication
        # is ready to be used.
        for func in hook_manager.on_fully_booted_funcs:
            func()

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
        if lNewStateID == StateEnum.ApplicationGameModeSelectorState.value:
            curr_gamestate = _internal.GameState.game_loaded
            _internal.GameState.game_loaded = True
            if _internal.GameState.game_loaded != curr_gamestate:
                # Only call this the first time the game loads
                _internal._executor.submit(self.run_on_fully_booted_funcs)
        # TODO: We can add hooks for each of the game states to make it easier
        # to handle when an event like this happens...

    # @one_shot
    # @hooks.cGcRealityManager.Construct.after
    # def cGcRealityManager_construct(self, this):
    #     logging.info(f"cGcRealityManager::Construct: 0x{this:X}")
    #     try:
    #         reality_manager = nms.GcApplication.data.contents.RealityManager
    #         logging.info(f"cGcRealityManager: {ctypes.addressof(reality_manager)}")
    #     except:
    #         logging.info(traceback.format_exc())

    @hooks.cGcApplication.Update
    def _main_loop(self, *args):
        """ The main application loop. Run any before or after functions here. """
        for func in hook_manager.main_loop_before_funcs:
            func()
        hooks.cGcApplication.Update.original(*args)
        for func in hook_manager.main_loop_after_funcs:
            func()
