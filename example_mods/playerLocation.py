import ctypes
from logging import getLogger

from pymhf import Mod
from pymhf.gui.decorators import BOOLEAN, FLOAT, INTEGER, gui_button

import nmspy.data.basic_types as basic
import nmspy.data.types as nms
from nmspy.common import gameData
from nmspy.engine import GetNodeAbsoluteTransMatrix
from nmspy.globals import globals

logger = getLogger(__name__)


class PlayerLocation(Mod):
    __author__ = "monkeyman192"
    __description__ = "Player Location Test Mod"

    @property
    @FLOAT("Ground walk speed")
    def ground_walk_speed(self):
        return globals.GcPlayerGlobals.GroundWalkSpeed

    @property
    @FLOAT("Jetpack fuel")
    def jetpack_fuel(self):
        if (player := gameData.player) is not None:
            return player.mfJetpackTank
        return 0

    @property
    @INTEGER("Voxel X")
    def voxel_x(self):
        if (player_state := gameData.player_state) is not None:
            return player_state.mLocation.GalacticAddress.VoxelX
        return 0

    @property
    @INTEGER("Voxel Y")
    def voxel_y(self):
        if (player_state := gameData.player_state) is not None:
            return player_state.mLocation.GalacticAddress.VoxelY
        return 0

    @property
    @INTEGER("Voxel Z")
    def voxel_z(self):
        if (player_state := gameData.player_state) is not None:
            return player_state.mLocation.GalacticAddress.VoxelZ
        return 0

    @gui_button("Add 10 nanites")
    def add_nanites(self):
        if (player_state := gameData.player_state) is not None:
            player_state.AwardNanites(10)

    @nms.cGcPlayerState.AwardNanites.after
    def awarded_nanites(self, this, liChange: int):
        logger.info(f"Player was just given {liChange} nanites")

    @property
    @BOOLEAN("Player is running")
    def player_is_running(self):
        if (player := gameData.player) is not None:
            return player.mbIsRunning
        return False

    @property
    @FLOAT("Player x position")
    def player_x_pos(self):
        return self.player_position.x

    @property
    @FLOAT("Player y position")
    def player_y_pos(self):
        return self.player_position.y

    @property
    @FLOAT("Player z position")
    def player_z_pos(self):
        return self.player_position.z

    @property
    def player_position(self) -> basic.cTkVector3:
        if (player := gameData.player) is not None:
            mat = GetNodeAbsoluteTransMatrix(player.mRootNode)
            return mat.pos
        return basic.cTkVector3(0, 0, 0)

    @ground_walk_speed.setter
    def ground_walk_speed(self, value: float):
        globals.GcPlayerGlobals.GroundWalkSpeed = value

    @nms.cGcPlayer.SetToPosition.before
    def set_player_pos(
        self,
        this,
        lPos: ctypes._Pointer[basic.cTkBigPos],
        lDir: ctypes._Pointer[basic.cTkVector3],
        lVel: ctypes._Pointer[basic.cTkVector3],
    ):
        logger.info(
            f"Setting player pos to (local: {lPos.contents.local}, offset: {lPos.contents.offset}), "
            f"lDir: {lDir.contents}, lVel: {lVel.contents}"
        )
