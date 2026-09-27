from typing import Literal

# List of node names which are associated with the different node groups. These are the "keys" to the values
# in cGcSimulation.maGroupNodes
kaNodeNames = Literal[
    "Player",
    "Sky",
    "Scan",
    "Effects",
    "Objects",
    "Creatures",
    "NetPending",
    "RegionDecorator",
    "Terrain",
    "Space",
    "FakeSpace",
    "Spaceships",
    "RemotePlayers",
]
