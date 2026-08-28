# These enums are "internal" ones. Ie. ones which are not serialized as part of the metaclass data.

from enum import Enum, IntEnum


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


class EnvironmentLocation:
    class Enum(IntEnum):
        None_ = 0x0
        Default = 0x1
        SpaceStation = 0x2
        PlanetOnFoot = 0x3
        PlanetInShip = 0x4
        PlanetInVehicle = 0x5
        Underwater = 0x6
        Cave = 0x7
        IndoorInBase = 0x8
        Freighter = 0x9
        FreighterInternals = 0xA
        AbandonedFreighter = 0xB
        InFleet = 0xC
        InSpaceObject = 0xD
        Nexus = 0xE
        Anomaly = 0xF


class EPulseDriveState(IntEnum):
    None_ = 0x0
    Charge = 0x1
    Jumping = 0x2
    CrashStop = 0x3
    Cooldown = 0x4


class eFileOpenMode(IntEnum):
    Read = 0x0
    Write = 0x1
    Append = 0x2


class eGraphicsDetail(IntEnum):
    Low = 0x0
    Medium = 0x1
    High = 0x2
    Ultra = 0x3


class TryStoreMode(IntEnum):
    Commit = 0x0
    Peek = 0x1


class InventoryChoice(IntEnum):
    Suit = 0x0
    Suit_Tech = 0x1
    Suit_Cargo = 0x2
    Weapon = 0x3
    Ship = 0x4
    Ship_Cargo = 0x5
    Ship_Tech = 0x6
    Freighter = 0x7
    Freighter_Tech = 0x8
    Freighter_Cargo = 0x9
    Vehicle = 0xA
    Vehicle_Tech = 0xB
    Unknown0xC = 0xC  # BUIDING_STORAGE
    Unknown0xD = 0xD  # BUIDING_STORAGE
    Unknown0xE = 0xE  # BUIDING_STORAGE
    Unknown0xF = 0xF  # BUIDING_STORAGE
    Unknown0x10 = 0x10  # BUIDING_STORAGE
    Unknown0x11 = 0x11  # BUIDING_STORAGE
    Unknown0x12 = 0x12  # BUIDING_STORAGE
    Unknown0x13 = 0x13  # BUIDING_STORAGE
    Unknown0x14 = 0x14  # BUIDING_STORAGE
    Unknown0x15 = 0x15  # BUIDING_STORAGE
    Unknown0x16 = 0x16  # BASE_CACHE?
    Unknown0x17 = 0x17  # BASE_CACHE?
    Unknown0x18 = 0x18  # Frontend stroe
    Unknown0x19 = 0x19  # Temporary frontend store
    Unknown0x1A = 0x1A  # PANTRY?
    Unknown0x1B = 0x1B  # SUIT_ROCKET?
    Unknown0x1C = 0x1C
    Unknown0x1D = 0x1D
    Unknown0x1E = 0x1E
    Unknown0x1F = 0x1F
    Unknown0x20 = 0x20
