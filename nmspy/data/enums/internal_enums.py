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
    Ship_Tech = 0x5
    Ship_Cargo = 0x6
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


class eOptionsMenu(IntEnum):
    General = 0x0
    Accessibility = 0x1
    Controls = 0x2
    Camera = 0x3
    Display = 0x4
    MotionSensor = 0x5
    Options = 0x6
    Network = 0x7


class eNGuiGameElementType(IntEnum):
    Layer = 0x0
    Text = 0x1
    Text_Special = 0x2
    Graphic = 0x3
    Spacing = 0x4


class eFrontendPage(IntEnum):
    Suit = 0x0
    Ship = 0x1
    Vehicle = 0x2
    Freighter = 0x3
    Weapon = 0x4
    Discovery = 0x5
    Journey = 0x6
    MissionLog = 0x7
    Wiki = 0x8
    Catalogue = 0x9
    InfoPortal = 0xA
    Season = 0xB
    Options = 0xC
    Switcher = 0xD
    Controls = 0xE
    ControlsRemap = 0xF
    Network = 0x10
    NetworkPlayers = 0x11
    NetworkManageFriends = 0x12
    NetworkManageBlocked = 0x13
    Difficulty = 0x14
    Credits = 0x15
    Redeem = 0x16
    Interact = 0x17
    InteractDialog = 0x18
    InteractConsole = 0x19
    InteractShip = 0x1A
    Trade = 0x1B
    TechTrade = 0x1C
    BuildingTrade = 0x1D
    SpecialsTrade = 0x1E
    RepTrade = 0x1F
    CookTrade = 0x20
    MissionList = 0x21
    MissionHandInList = 0x22
    MissionRenounce = 0x23
    MissionDescription = 0x24
    MissionDescription2 = 0x25
    BuyScreen = 0x26
    CompareScreen = 0x27
    DisplayTech = 0x28
    DisplayProduct = 0x29
    DisplayPatchNotes = 0x2A
    FreighterTransferScreen = 0x2B
    InventoryTransferScreen = 0x2C
    Message = 0x2D
    PhotoMode = 0x2E
    ReportBase = 0x2F
    PhotoBaseForUpload = 0x30
    BaseUpload = 0x31
    BasePartsMenu = 0x32
    BasePartPalette = 0x33
    Popup = 0x34
    Maintenance = 0x35
    Portal = 0x36
    PortalRunes = 0x37
    PortalActivate = 0x38
    PortalUaDisplay = 0x39
    Refiner = 0x3A
    SystemHoover = 0x3B
    EggMachine = 0x3C
    VehicleRace = 0x3D
    ManageFleet = 0x3E
    ManageExpeditions = 0x3F
    ExpeditionDebrief = 0x40
    FrigateDetails = 0x41
    FrigateCaptain = 0x42
    ExpeditionDetails = 0x43
    ExpeditionSelection = 0x44
    ExpeditionOutfitting = 0x45
    Customisation = 0x46
    Teleporter = 0x47

    Teleporter_Nexus = 0x4A
    ByteBeat = 0x4B
    BaseGridPart = 0x4C
    UnlockItemTree = 0x4D
    CreatureFeeder = 0x4E
    CreatureHarvester = 0x4F
    Multiplayer_MissionList = 0x50
    Multiplayer_MissionDescription = 0x51
    CraftingTree = 0x52
    ByteBeatSwitch = 0x53
    RadialInteraction = 0x54
    Pet = 0x55
    IntermediateInteraction = 0x56
    ByteBeatLibrary = 0x57
    SettlementHub = 0x58
    SettlementJudgement = 0x59
    SettlementOverview = 0x5A
    SettlerNPCDetails = 0x5B
    SettlementBuildingDetails = 0x5C
    SettlementHistory = 0x5D
    RocketLockerInventory = 0x5E
    SquadronRecruitment = 0x5F
    SquadronManagement = 0x60
    SquadronPilotDetails = 0x61
    WonderSelector = 0x62
    SaveContextTerminal = 0x63
    SeasonEndRewards = 0x64
    TrialUpsell = 0x65
    FishBaitBox = 0x66
    Teleporter_SomewhereElse = 0x67  # TODO: Where?
    FoodUnit = 0x68
    ArchiveManagement1 = 0x69
    ArchiveManagement2 = 0x6A
    GameTable = 0x6B
    PetBattleTeamManagement = 0x6C
    SwarmBulletin = 0x6D
    PersonalityTest = 0x6E
    SolarSystemMap = 0x6F
    AlliancesWindow = 0x70
    StationOwnership = 0x71


class eNGuiInputButtonState(IntEnum):
    None_ = 0x0
    Released = 0x1
    Pressed = 0x2
    Held = 0x3


class eNGuiInputType(IntEnum):
    None_ = 0x0
    Released = 0x1
    Click = 0x2
    RightReleased = 0x3
    RightClick = 0x4
    RightDragged = 0xF8  # -0x8
    RightPressed = 0xF9  # -0x7
    RightHeld = 0xFA  # -0x6
    Hover = 0xFB  # -0x5
    Dragged = 0xFC  # -0x4
    TouchPressReady = 0xFD  # -0x3
    Pressed = 0xFE  # -0x2
    Held = 0xFF  # -0x1
