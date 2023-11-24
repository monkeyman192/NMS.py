# An array of the various states the game can be in.
# TODO: Make it so that we can bind callbacks to when these states change.

from enum import Enum

STATES = [
    b"FSM_NOSTATE",
    b"SCRATCHPAD",
    b"MODESELECTOR",
    b"GALAXYMAP",
    b"AMBIENT",
    b"APPGLOBALLOAD",
    b"APPLOCALLOAD",
    b"APPVIEW",
    b"APPSHUTDOWN",
    b"APPBOOT",
    b"APPCORESERVICES",
    b"YOUAREDEAD",
]

class StateEnum(Enum):
    TkFSMNoState = b"FSM_NOSTATE"
    ApplicationScratchpadState = b"SCRATCHPAD"
    ApplicationGameModeSelectorState = b"MODESELECTOR"
    ApplicationGalacticMapState = b"GALAXYMAP"
    ApplicationAmbientGameState = b"AMBIENT"
    ApplicationGlobalLoadState = b"APPGLOBALLOAD"
    ApplicationLocalLoadState = b"APPLOCALLOAD"
    ApplicationSimulationState = b"APPVIEW"
    ApplicationShutdownState = b"APPSHUTDOWN"
    ApplicationBootState = b"APPBOOT"
    ApplicationCoreServicesState = b"APPCORESERVICES"
    ApplicationDeathState_0 = b"YOUAREDEAD"
