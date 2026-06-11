from logging import getLogger

from pymhf import Mod
from pymhf.gui.decorators import gui_button

from nmspy.common import gameData

logger = getLogger("visitedSystems")


class VisitedSystems(Mod):
    @gui_button("where have I been?")
    def been(self):
        if (gs := gameData.game_state) is not None:
            mVisitedSystemsBuffer = gs.mSavedInteractionsManager.mVisitedSystemsBuffer
            # self.pymhf_gui.hex_view.add_snapshot(get_addressof(mVisitedSystemsBuffer), 0x1804)
            logger.info(f"I have been to {mVisitedSystemsBuffer.miVisitedSystemsCount} systems:")
            for i in range(mVisitedSystemsBuffer.miVisitedSystemsCount):
                vs = mVisitedSystemsBuffer.mVisitedSystems[i]
                vox = vs.mVoxel
                visited_planets = []
                for idx, char in enumerate(bin(vs.miPlanetsVisited)[2:]):
                    if char == "1":
                        visited_planets.append(idx)
                logger.info(
                    f"System {i}: ({vox.mX}, {vox.mY}, {vox.mZ} - {vs.miSystemIndex})"
                    f" -> Saw planets {visited_planets}"
                )
