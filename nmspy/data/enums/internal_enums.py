# These enums are "internal" ones. Ie. ones which are not serialized as part of the metaclass data.

from enum import IntEnum, Enum


class ResourceTypes(IntEnum):
    Undefined = 0x0
    SceneGraph = 0x1
    Geometry = 0x2
    Animation = 0x3
    Material = 0x4
    Code = 0x5
    Shader = 0x6
    Texture = 0x7
    Pipeline = 0x8
    Metadata = 0x9


class RespawnReason(IntEnum):
    FreshStart = 0x0
    LoadSave = 0x1
    LoadToLocation = 0x2
    RestorePreviousSave = 0x3
    Unknown = 0x4
    DeathInSpace = 0x5
    DeathOnPlanet = 0x6
    DeathInOrbit = 0x7
    DeathOnAbandonedFreighter = 0x8
    WarpInShip = 0x9
    Teleport = 0xA
    Portal = 0xB
    UpgradeSaveAfterPatch = 0xC
    SwitchAmbientPlanet = 0xD
    BaseViewerMode = 0xE
    WarpInFreighter = 0xF
    JoinMultiplayer = 0x10


class StateEnum(str, Enum):
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


class eStormState(IntEnum):
    Inactive = 0x0
    Warning = 0x1
    TransitionIn = 0x2
    Active = 0x3
    TransitionOut = 0x4


class eLanguageRegion(IntEnum):
    English = 0x0
    USEnglish = 0x1
    French = 0x2
    Italian = 0x3
    German = 0x4
    Spanish = 0x5
    Russian = 0x6
    Polish = 0x7
    Dutch = 0x8
    Portuguese = 0x9
    LatinAmericanSpanish = 0xA
    BrazilianPortuguese = 0xB
    Japanese = 0xC
    TraditionalChinese = 0xD
    SimplifiedChinese = 0xE
    TencentChinese = 0xF
    Korean = 0x10
