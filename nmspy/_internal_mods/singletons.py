import ctypes
from dataclasses import dataclass
from logging import getLogger

from pymhf import Mod, ModState
from pymhf.core._types import DetourTime
from pymhf.core.hooking import hook_manager, one_shot
from pymhf.core.memutils import get_addressof, map_struct
from pymhf.gui.decorators import no_gui

import nmspy.data.basic_types as basic
import nmspy.data.types as nms
from nmspy.common import gameData
from nmspy.data.enums import StateEnum

logger = getLogger()


@dataclass
class InternalState(ModState):
    game_loaded: bool = False


@no_gui
class _INTERNAL_LoadSingletons(Mod):
    __author__ = "monkeyman192"
    __description__ = "Load singletons and other important objects"
    __version__ = "0.1"

    internal_state = InternalState()

    @one_shot
    @nms.cTkFSM.StateChange.after
    def fsm_state_change(self, this: ctypes._Pointer[nms.cTkFSM], *args):
        # One shot to instantiate the cGcApplication object.
        # This logic looks funny, but it's because the cGcApplication has cTkFSM as a base class.
        gameData.GcApplication = map_struct(get_addressof(this), nms.cGcApplication)

    @nms.cTkFSMState.StateChange.after
    def state_change(
        self,
        this,
        lNewStateID: ctypes._Pointer[basic.cTkFixedString[0x10]],
        lpUserData,
        lbForceRestart,
    ):
        new_state_id = lNewStateID.contents
        logger.info(f"New State: {new_state_id}")
        if new_state_id == StateEnum.ApplicationGameModeSelectorState:
            curr_gamestate = self.internal_state.game_loaded
            self.internal_state.game_loaded = True
            if self.internal_state.game_loaded != curr_gamestate:
                # Only call this the first time the game loads
                hook_manager.call_custom_callbacks(
                    StateEnum.ApplicationGameModeSelectorState, DetourTime.AFTER
                )
                hook_manager.call_custom_callbacks(
                    StateEnum.ApplicationGameModeSelectorState, DetourTime.NONE
                )
        else:
            hook_manager.call_custom_callbacks(str(new_state_id), DetourTime.AFTER)
            hook_manager.call_custom_callbacks(str(new_state_id), DetourTime.NONE)

    @nms.cGcApplication.Update.before
    def _main_loop_before(self, this):
        """The main application loop. Run any before functions here."""
        hook_manager.call_custom_callbacks("MAIN_LOOP", DetourTime.BEFORE)

    @nms.cGcApplication.Update.after
    def _main_loop_after(self, this):
        """The main application loop. Run any after functions here."""
        hook_manager.call_custom_callbacks("MAIN_LOOP", DetourTime.AFTER)
