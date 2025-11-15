from typing import Optional

import nmspy.data.types as nms


class GameData:
    GcApplication: nms.cGcApplication = None  # type: ignore

    @property
    def game_state(self) -> Optional[nms.cGcGameState]:
        if self.GcApplication is not None:
            return self.GcApplication.mpData.contents.mGameState

    @property
    def simulation(self) -> Optional[nms.cGcSimulation]:
        if self.GcApplication is not None:
            return self.GcApplication.mpData.contents.mSimulation

    @property
    def player(self) -> Optional[nms.cGcPlayer]:
        if (sim := self.simulation) is not None:
            return sim.mPlayer

    @property
    def player_state(self) -> Optional[nms.cGcPlayerState]:
        if (game_state := self.game_state) is not None:
            return game_state.mPlayerState


gameData = GameData()
