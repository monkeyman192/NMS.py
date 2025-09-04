# ruff: noqa: E741
from enum import IntEnum


class cTkVoxelGeneratorSettingsTypes(IntEnum):
    FloatingIslands = 0x0
    GrandCanyon = 0x1
    MountainRavines = 0x2
    HugeArches = 0x3
    Alien = 0x4
    Craters = 0x5
    Caverns = 0x6
    Alpine = 0x7
    LilyPad = 0x8
    Desert = 0x9
    WaterworldPrime = 0xA
    FloatingIslandsPrime = 0xB
    GrandCanyonPrime = 0xC
    MountainRavinesPrime = 0xD
    HugeArchesPrime = 0xE
    AlienPrime = 0xF
    CratersPrime = 0x10
    CavernsPrime = 0x11
    AlpinePrime = 0x12
    LilyPadPrime = 0x13
    DesertPrime = 0x14
    FloatingIslandsPurple = 0x15
    GrandCanyonPurple = 0x16
    MountainRavinesPurple = 0x17
    HugeArchesPurple = 0x18
    AlienPurple = 0x19
    CratersPurple = 0x1A
    CavernsPurple = 0x1B
    AlpinePurple = 0x1C
    LilyPadPurple = 0x1D
    DesertPurple = 0x1E


class cTkNoiseVoxelTypeEnum(IntEnum):
    Base = 0x0
    Rock = 0x1
    Mountain = 0x2
    Sand = 0x3
    Cave = 0x4
    Substance_1 = 0x5
    Substance_2 = 0x6
    Substance_3 = 0x7
    RandomRock = 0x8
    RandomRockOrSubstance = 0x9


class cTkNoiseLayersEnum(IntEnum):
    Base = 0x0
    Hill = 0x1
    Mountain = 0x2
    Rock = 0x3
    UnderWater = 0x4
    Texture = 0x5
    Elevation = 0x6
    Continent = 0x7


class cTkCavesEnum(IntEnum):
    Underground = 0x0


class cTkFeaturesEnum(IntEnum):
    River = 0x0
    Crater = 0x1
    Arches = 0x2
    ArchesSmall = 0x3
    Blobs = 0x4
    BlobsSmall = 0x5
    Substance = 0x6


class cTkGridLayersEnum(IntEnum):
    Small = 0x0
    Large = 0x1
    Resources_Heridium = 0x2
    Resources_Iridium = 0x3
    Resources_Copper = 0x4
    Resources_Nickel = 0x5
    Resources_Aluminium = 0x6
    Resources_Gold = 0x7
    Resources_Emeril = 0x8


class cTkNoiseOffsetEnum(IntEnum):
    Zero = 0x0
    Base = 0x1
    All = 0x2
    SeaLevel = 0x3


class cTkInputValidation(IntEnum):
    Held = 0x0
    Pressed = 0x1
    HeldConfirm = 0x2
    Released = 0x3
    HeldOver = 0x4


class cTkPadEnum(IntEnum):
    None_ = 0x0
    XInput = 0x1
    GLFW = 0x2
    XBoxOne = 0x3
    XBox360 = 0x4
    DS4 = 0x5
    DS5 = 0x6
    Move = 0x7
    SteamInput = 0x8
    Touch = 0x9
    OpenVR = 0xA
    SwitchPro = 0xB
    SwitchHandheld = 0xC
    GameInput = 0xD
    SwitchDebugPad = 0xE
    SwitchJoyConDual = 0xF
    VirtualController = 0x10


class cGcInputActions(IntEnum):
    Invalid = 0x0
    Player_Forward = 0x1
    Player_Back = 0x2
    Player_Left = 0x3
    Player_Right = 0x4
    Player_SwimUp = 0x5
    Player_SwimDown = 0x6
    Player_Interact = 0x7
    Player_Melee = 0x8
    Player_Scan = 0x9
    Player_Torch = 0xA
    Player_Binoculars = 0xB
    Player_Zoom = 0xC
    Player_ShowHUD = 0xD
    Player_Jump = 0xE
    Player_Run = 0xF
    Player_Shoot = 0x10
    Player_Grenade = 0x11
    Player_Reload = 0x12
    Player_ChangeWeapon = 0x13
    Player_Deconstruct = 0x14
    Player_ChangeAltWeapon = 0x15
    Player_PlaceMarker = 0x16
    Quick_Menu = 0x17
    Build_Menu = 0x18
    Ship_AltLeft = 0x19
    Ship_AltRight = 0x1A
    Ship_Thrust = 0x1B
    Ship_Brake = 0x1C
    Ship_Boost = 0x1D
    Ship_RollLeft = 0x1E
    Ship_RollRight = 0x1F
    Ship_Exit = 0x20
    Ship_Land = 0x21
    Ship_Shoot = 0x22
    Ship_ChangeWeapon = 0x23
    Ship_Scan = 0x24
    Ship_PulseJump = 0x25
    Ship_GalacticMap = 0x26
    Ship_TurnLeft = 0x27
    Ship_TurnRight = 0x28
    Ship_FreeLook = 0x29
    Ship_AutoFollow_Toggle = 0x2A
    Ship_AutoFollow_Hold = 0x2B
    Ship_CyclePower = 0x2C
    Vehicle_Forward = 0x2D
    Vehicle_Reverse = 0x2E
    Vehicle_Left = 0x2F
    Vehicle_Right = 0x30
    Vehicle_Exit = 0x31
    Vehicle_Shoot = 0x32
    Vehicle_ChangeWeapon = 0x33
    Vehicle_Scan = 0x34
    Vehicle_Boost = 0x35
    Vehicle_Jump = 0x36
    Vehicle_Dive = 0x37
    Vehicle_Horn = 0x38
    Vehicle_AddCheckpoint = 0x39
    Vehicle_DeleteCheckpoint = 0x3A
    Fe_Select = 0x3B
    Fe_AltSelect = 0x3C
    Fe_SelectX = 0x3D
    Fe_Back = 0x3E
    Fe_Alt1 = 0x3F
    Fe_Alt1X = 0x40
    Fe_Transfer = 0x41
    Fe_Destroy = 0x42
    UI_Left = 0x43
    UI_Right = 0x44
    UI_Left_Sub = 0x45
    UI_Right_Sub = 0x46
    UI_Down_Sub = 0x47
    UI_Up_Sub = 0x48
    UI_NetworkPageShortcut = 0x49
    UI_StackSplitUp = 0x4A
    UI_StackSplitDown = 0x4B
    Fe_ExitMenu = 0x4C
    Fe_Options = 0x4D
    Fe_Quit = 0x4E
    Fe_MsgSkip = 0x4F
    Fe_TouchscreenPress = 0x50
    Quick_Left = 0x51
    Quick_Right = 0x52
    Quick_Action = 0x53
    Quick_Back = 0x54
    Quick_Up = 0x55
    Quick_Down = 0x56
    Build_Place = 0x57
    Build_Rotate_Left = 0x58
    Build_Rotate_Right = 0x59
    Build_AnalogRotateMode1 = 0x5A
    Build_AnalogRotateMode2 = 0x5B
    Build_AnalogRotateLeftY = 0x5C
    Build_AnalogRotateRightY = 0x5D
    Build_AnalogRotateY = 0x5E
    Build_AnalogRotateLeftZ = 0x5F
    Build_AnalogRotateRightZ = 0x60
    Build_AnalogRotateZ = 0x61
    Build_ScaleUp = 0x62
    Build_ScaleDown = 0x63
    Build_AnalogueScale = 0x64
    Build_SelectionMode = 0x65
    Build_Camera = 0x66
    Build_Orbit = 0x67
    Build_Quit = 0x68
    Build_ToggleCatalogue = 0x69
    Build_Purchase = 0x6A
    Build_Flip = 0x6B
    Photo_Hide = 0x6C
    Photo_Sun = 0x6D
    Photo_Cam = 0x6E
    Photo_Exit = 0x6F
    Photo_CamDown = 0x70
    Photo_CamUp = 0x71
    Photo_Capture = 0x72
    Ambient_Camera = 0x73
    Ambient_Planet = 0x74
    Ambient_System = 0x75
    Ambient_Photo = 0x76
    Ambient_NxtSong = 0x77
    Ambient_Spawn = 0x78
    Terrain_Edit = 0x79
    Terrain_ModeBack = 0x7A
    Terrain_Menu = 0x7B
    Terrain_SizeUp = 0x7C
    Terrain_SizeDown = 0x7D
    Terrain_RotTerrainLeft = 0x7E
    Terrain_RotTerrainRight = 0x7F
    Terrain_ChangeShape = 0x80
    Ship_NextTarget = 0x81
    Ship_PreviousTarget = 0x82
    Ship_ClosestTarget = 0x83
    CameraLook = 0x84
    CameraLookX = 0x85
    CameraLookY = 0x86
    PlayerMove = 0x87
    PlayerMoveX = 0x88
    PlayerMoveY = 0x89
    SpaceshipThrust = 0x8A
    SpaceshipBrake = 0x8B
    VehicleMove = 0x8C
    VehicleSteer = 0x8D
    VehicleThrust = 0x8E
    VehicleBrake = 0x8F
    ShipStrafe = 0x90
    ShipStrafeHorizontal = 0x91
    ShipStrafeVertical = 0x92
    HeldRotate = 0x93
    HeldRotateLeft = 0x94
    HeldRotateRight = 0x95
    ShipSteer = 0x96
    ShipTurn = 0x97
    ShipPitch = 0x98
    ShipLook = 0x99
    ShipLookX = 0x9A
    ShipLookY = 0x9B
    ShipLand = 0x9C
    ShipPulse = 0x9D
    PlayerSmoothTurnLeft = 0x9E
    PlayerSmoothTurnRight = 0x9F
    PlayerSnapTurnLeft = 0xA0
    PlayerSnapTurnRight = 0xA1
    PlayerSnapTurnAround = 0xA2
    PlayerMoveAround = 0xA3
    TeleportDirection = 0xA4
    PlayerAutoWalk = 0xA5
    InteractLeft = 0xA6
    MeleeLeft = 0xA7
    HandCtrlHolster = 0xA8
    ShipUp = 0xA9
    ShipDown = 0xAA
    ShipLeft = 0xAB
    ShipRight = 0xAC
    ShipZoom = 0xAD
    Inventory = 0xAE
    DiscoveryNetworkRetry = 0xAF
    QuitGame = 0xB0
    ReportBase = 0xB1
    Unbound = 0xB2
    GalacticMap_Select = 0xB3
    GalacticMap_Deselect = 0xB4
    GalacticMap_Exit = 0xB5
    GalacticMap_Scan = 0xB6
    GalacticMap_Home = 0xB7
    GalacticMap_PlanetBase = 0xB8
    GalacticMap_Accelerate = 0xB9
    GalacticMap_ExpandMenu = 0xBA
    GalacticMap_ScreenshotToggle = 0xBB
    GalacticMap_ScanChooseNext = 0xBC
    GalacticMap_ToggleWaypoint = 0xBD
    GalacticMap_ClearAllWaypoints = 0xBE
    GalacticMap_NextNavType = 0xBF
    GalacticMap_PreviousNavType = 0xC0
    GalacticMap_PreviousFilter = 0xC1
    GalacticMap_NextFilter = 0xC2
    GalacticMap_CameraLook = 0xC3
    GalacticMap_CameraLookX = 0xC4
    GalacticMap_CameraLookY = 0xC5
    GalacticMap_PlayerMove = 0xC6
    GalacticMap_PlayerMoveX = 0xC7
    GalacticMap_PlayerMoveY = 0xC8
    GalacticMap_PlayerMoveForward = 0xC9
    GalacticMap_PlayerMoveBackward = 0xCA
    GalacticMap_PlayerMoveLeft = 0xCB
    GalacticMap_PlayerMoveRight = 0xCC
    GalacticMap_Up = 0xCD
    GalacticMap_Down = 0xCE
    GalacticMap_Gesture = 0xCF
    UI_Cursor = 0xD0
    UI_CursorX = 0xD1
    UI_CursorY = 0xD2
    UI_Camera = 0xD3
    UI_CameraX = 0xD4
    UI_CameraY = 0xD5
    UI_ViewPlayerInfo = 0xD6
    UI_ToggleBuySell = 0xD7
    UI_ToggleTradeInventory = 0xD8
    UI_TouchScrollY = 0xD9
    UI_TouchScrollX = 0xDA
    CharacterCustomisation_ShowCharacter = 0xDB
    UI_CharacterCustomisation_Camera = 0xDC
    UI_CharacterCustomisation_RotateCamera = 0xDD
    UI_CharacterCustomisation_PitchCamera = 0xDE
    GameMode_TitleStart = 0xDF
    GameMode_ChangeUser = 0xE0
    Binocs_NextMode = 0xE1
    Binocs_PrevMode = 0xE2
    BaseBuilding_PinRecipe = 0xE3
    BaseBuilding_SwitchBase = 0xE4
    PhotoMode_CatLeft = 0xE5
    PhotoMode_CatRight = 0xE6
    PhotoMode_ValueIncrease = 0xE7
    PhotoMode_ValueDecrease = 0xE8
    PhotoMode_OptionUp = 0xE9
    PhotoMode_OptionDown = 0xEA
    PhotoMode_CameraRollLeft = 0xEB
    PhotoMode_CameraRollRight = 0xEC
    PhotoMode_PauseApplication = 0xED
    PhotoMode_CopyLocation = 0xEE
    PhotoMode_HideLocation = 0xEF
    UI_Up_Sub_Discovery = 0xF0
    UI_Down_Sub_Discovery = 0xF1
    Fe_Upload_Discovery = 0xF2
    Fe_Assign_Custom_Wonder = 0xF3
    HMD_Recenter = 0xF4
    HMD_Recenter2 = 0xF5
    HMD_FEOpen = 0xF6
    TextChatOpenClose = 0xF7
    TextChatSend = 0xF8
    TextChatPasteHold = 0xF9
    TextChatPaste = 0xFA
    TextChatAutocomplete = 0xFB
    TextChatAutocompleteModifier = 0xFC
    TextChatCursorLeft = 0xFD
    TextChatCursorRight = 0xFE
    TextChatCursorHome = 0xFF
    TextChatCursorEnd = 0x100
    TextChatDelete = 0x101
    Player_InteractSecondary = 0x102
    BaseBuilding_ToggleVisions = 0x103
    BaseBuilding_Browse = 0x104
    BaseBuilding_Pickup = 0x105
    BaseBuilding_Duplicate = 0x106
    BaseBuilding_Delete = 0x107
    BaseBuilding_ToggleRotationAxis = 0x108
    Build_AnalogRotateZ2 = 0x109
    BaseBuilding_ToggleSnapping = 0x10A
    BaseBuilding_ToggleWiring = 0x10B
    BaseBuilding_Paint = 0x10C
    BaseBuilding_NextPart = 0x10D
    Player_TagMarker = 0x10E
    TogglePause = 0x10F
    TogglePlanet = 0x110
    ToggleFreezeCulling = 0x111
    Suicide = 0x112
    Reset = 0x113
    AddLastToolbox = 0x114
    AddLastToolboxAtPos = 0x115
    TerrainInvalidate = 0x116
    TogglePipeline = 0x117
    TakeScreenshot = 0x118
    TakeExrScreenshot = 0x119
    ToggleDebugStats = 0x11A
    ToggleDebugSubpage = 0x11B
    DumpNodeStats = 0x11C
    ToggleTaa = 0x11D
    DebugDropMeasurementAnchor = 0x11E
    QuickWarp = 0x11F
    DumpStats = 0x120
    DiscoverOwnBase = 0x121
    ClearTerrainEdits = 0x122
    SelectRegion = 0x123
    SwitchRegionRow = 0x124
    SwitchRegionAxis = 0x125
    OpenLog = 0x126
    DumpVertStats = 0x127
    ToggleDebugCamera = 0x128
    ReturnToPlayer = 0x129
    SetTimeOfDay = 0x12A


class cTkTestBitFieldEnum(IntEnum):
    empty = 0x0
    First = 0x1
    Second = 0x2
    Third = 0x4
    Fourth = 0x8


class cTkInputHandEnum(IntEnum):
    None_ = 0x0
    Left = 0x1
    Right = 0x2


class cTkInputEnum(IntEnum):
    None_ = 0x0
    Space = 0x20
    Exclamation = 0x21
    Quotes = 0x22
    Hash = 0x23
    Dollar = 0x24
    Percent = 0x25
    Ampersand = 0x26
    Apostrophe = 0x27
    LeftBracket = 0x28
    RightBracket = 0x29
    Asterisk = 0x2A
    Plus = 0x2B
    Comma = 0x2C
    Hyphen = 0x2D
    Period = 0x2E
    Slash = 0x2F
    Key0 = 0x30
    Key1 = 0x31
    Key2 = 0x32
    Key3 = 0x33
    Key4 = 0x34
    Key5 = 0x35
    Key6 = 0x36
    Key7 = 0x37
    Key8 = 0x38
    Key9 = 0x39
    Colon = 0x3A
    Semicolon = 0x3B
    LessThan = 0x3C
    Equals = 0x3D
    GreaterThan = 0x3E
    QuestionMark = 0x3F
    At = 0x40
    KeyA = 0x41
    KeyB = 0x42
    KeyC = 0x43
    KeyD = 0x44
    KeyE = 0x45
    KeyF = 0x46
    KeyG = 0x47
    KeyH = 0x48
    KeyI = 0x49
    KeyJ = 0x4A
    KeyK = 0x4B
    KeyL = 0x4C
    KeyM = 0x4D
    KeyN = 0x4E
    KeyO = 0x4F
    KeyP = 0x50
    KeyQ = 0x51
    KeyR = 0x52
    KeyS = 0x53
    KeyT = 0x54
    KeyU = 0x55
    KeyV = 0x56
    KeyW = 0x57
    KeyX = 0x58
    KeyY = 0x59
    KeyZ = 0x5A
    LeftSquare = 0x5B
    BackSlash = 0x5C
    RightSquare = 0x5D
    Caret = 0x5E
    Underscode = 0x5F
    Grave = 0x60
    LeftCurly = 0x7B
    Bar = 0x7C
    RightCurly = 0x7D
    Tilde = 0x7E
    Special2 = 0xA2
    Escape = 0x100
    Enter = 0x101
    Backspace = 0x102
    Insert = 0x103
    Delete = 0x104
    CapsLock = 0x105
    Home = 0x106
    End = 0x107
    PageUp = 0x108
    PageDown = 0x109
    F1 = 0x10A
    F2 = 0x10B
    F3 = 0x10C
    F4 = 0x10D
    F5 = 0x10E
    F6 = 0x10F
    F7 = 0x110
    F8 = 0x111
    F9 = 0x112
    F10 = 0x113
    F11 = 0x114
    F12 = 0x115
    Tab = 0x116
    Shift = 0x117
    LShift = 0x118
    RShift = 0x119
    Alt = 0x11A
    LAlt = 0x11B
    RAlt = 0x11C
    Ctrl = 0x11D
    LCtrl = 0x11E
    RCtrl = 0x11F
    LOption = 0x120
    ROption = 0x121
    Up = 0x122
    Down = 0x123
    Left = 0x124
    Right = 0x125
    KeyboardUnbound = 0x126
    Mouse1 = 0x127
    Mouse2 = 0x128
    Mouse3 = 0x129
    Mouse4 = 0x12A
    Mouse5 = 0x12B
    Mouse6 = 0x12C
    Mouse7 = 0x12D
    Mouse8 = 0x12E
    MouseWheelUp = 0x12F
    MouseWheelDown = 0x130
    MouseUnbound = 0x131
    TouchscreenPress = 0x132
    TouchscreenTwoFingerPress = 0x133
    TouchscreenThreeFingerPress = 0x134
    TouchscreenFourFingerPress = 0x135
    TouchscreenSwipeLeft = 0x136
    TouchscreenSwipeRight = 0x137
    TouchscreenSwipeUp = 0x138
    TouchscreenSwipeDown = 0x139
    PadA = 0x13A
    PadB = 0x13B
    PadC = 0x13C
    PadD = 0x13D
    PadStart = 0x13E
    PadSelect = 0x13F
    PadLeftShoulder1 = 0x140
    PadRightShoulder1 = 0x141
    PadLeftShoulder2 = 0x142
    PadRightShoulder2 = 0x143
    PadLeftTrigger = 0x144
    PadRightTrigger = 0x145
    PadLeftThumb = 0x146
    PadRightThumb = 0x147
    PadUp = 0x148
    PadDown = 0x149
    PadLeft = 0x14A
    PadRight = 0x14B
    LeftHandA = 0x14C
    LeftHandB = 0x14D
    LeftHandC = 0x14E
    LeftHandD = 0x14F
    ChordBothShoulders = 0x150
    PadLeftTriggerSpecial = 0x151
    PadRightTriggerSpecial = 0x152
    PadSpecial0 = 0x153
    PadSpecial1 = 0x154
    PadSpecial2 = 0x155
    PadSpecial3 = 0x156
    PadSpecial4 = 0x157
    PadSpecial5 = 0x158
    PadSpecial6 = 0x159
    PadSpecial7 = 0x15A
    PadSpecial8 = 0x15B
    PadSpecial9 = 0x15C
    PadSpecial10 = 0x15D
    PadSpecial11 = 0x15E
    PadSpecial12 = 0x15F
    PadSpecial13 = 0x160
    PadSpecial14 = 0x161
    PadSpecial15 = 0x162
    PadSpecial16 = 0x163
    PadSpecial17 = 0x164
    PadSpecial18 = 0x165
    PadSpecial19 = 0x166
    PadUnbound = 0x167
    Gesture = 0x168
    GestureLeftWrist = 0x169
    GestureRightWrist = 0x16A
    GestureBinoculars = 0x16B
    GestureBackpack = 0x16C
    GestureExitVehicle = 0x16D
    GestureThrottle = 0x16E
    GestureFlightStick = 0x16F
    GestureTeleport = 0x170
    GestureLeftWrist_LeftHanded = 0x171
    GestureRightWrist_LeftHanded = 0x172
    GestureBinoculars_LeftHanded = 0x173
    GestureBackpack_LeftHanded = 0x174
    MaxEnumValue = 0x175


class cTkInputAxisEnum(IntEnum):
    None_ = 0x0
    Invalid = 0x0
    LeftStick = 0x1
    LeftStickX = 0x2
    LeftStickY = 0x3
    RightStick = 0x4
    RightStickX = 0x5
    RightStickY = 0x6
    LeftTrigger = 0x7
    RightTrigger = 0x8
    Mouse = 0x9
    MouseX = 0xA
    MouseY = 0xB
    MousePositiveX = 0xC
    MouseNegativeX = 0xD
    MousePositiveY = 0xE
    MouseNegativeY = 0xF
    MouseWheel = 0x10
    MouseWheelPositive = 0x11
    MouseWheelNegative = 0x12
    Touchpad = 0x13
    TouchpadX = 0x14
    TouchpadY = 0x15
    TouchpadPositiveX = 0x16
    TouchpadNegativeX = 0x17
    TouchpadPositiveY = 0x18
    TouchpadNegativeY = 0x19
    LeftTouchpad = 0x1A
    LeftTouchpadX = 0x1B
    LeftTouchpadY = 0x1C
    LeftTouchpadPositiveX = 0x1D
    LeftTouchpadNegativeX = 0x1E
    LeftTouchpadPositiveY = 0x1F
    LeftTouchpadNegativeY = 0x20
    LeftGrip = 0x21
    RightGrip = 0x22
    LeftStickPositiveX = 0x23
    LeftStickNegativeX = 0x24
    LeftStickPositiveY = 0x25
    LeftStickNegativeY = 0x26
    RightStickPositiveX = 0x27
    RightStickNegativeX = 0x28
    RightStickPositiveY = 0x29
    RightStickNegativeY = 0x2A
    DirectionalPadX = 0x2B
    DirectionalPadY = 0x2C
    DirectionalButtonsX = 0x2D
    DirectionalButtonsY = 0x2E
    ChordAD = 0x2F
    FakeLeftStick = 0x30
    FakeRightStick = 0x31


class cTkSketchConditions(IntEnum):
    Equal = 0x0
    NotEqual = 0x1
    Greater = 0x2
    Less = 0x3
    GreaterEqual = 0x4
    LessEqual = 0x5


class cTkTrophyEnum(IntEnum):
    None_ = 0xFFFFFFFF
    Trophy0 = 0x0
    Trophy1 = 0x1
    Trophy2 = 0x2
    Trophy3 = 0x3
    Trophy4 = 0x4


class cTkCoordinateOrientation(IntEnum):
    None_ = 0x0
    Random = 0x1


class cTkMetadataReadMask(IntEnum):
    empty = 0x0
    Default = 0x1
    SaveWhenMultiplayerClient = 0x2
    SavePlayerPosition = 0x4
    SavePlayerInventory = 0x8
    SaveDifficultySettings = 0x10


class cTkLanguages(IntEnum):
    Default = 0x0
    English = 0x1
    USEnglish = 0x2
    French = 0x3
    Italian = 0x4
    German = 0x5
    Spanish = 0x6
    Russian = 0x7
    Polish = 0x8
    Dutch = 0x9
    Portuguese = 0xA
    LatinAmericanSpanish = 0xB
    BrazilianPortuguese = 0xC
    Japanese = 0xD
    TraditionalChinese = 0xE
    SimplifiedChinese = 0xF
    TencentChinese = 0x10
    Korean = 0x11


class cTkProbability(IntEnum):
    Common = 0x0
    Uncommon = 0x1
    Rare = 0x2
    Extraordinary = 0x3


class cTkLightLayer(IntEnum):
    empty = 0x0
    Common = 0x1
    Sunlight = 0x2
    Character = 0x4
    Interior = 0x8


class cTkUserServiceAuthProvider(IntEnum):
    Null = 0x0
    PSN = 0x1
    Steam = 0x2
    Galaxy = 0x3
    Xbox = 0x4
    WeGame = 0x5
    NSO = 0x6
    GameCenter = 0x7


class cTkEqualityEnum(IntEnum):
    Equal = 0x0
    Greater = 0x1
    Less = 0x2
    GreaterEqual = 0x3
    LessEqual = 0x4


class cTkBlackboardCategory(IntEnum):
    Local = 0x0
    Archetype = 0x1
    PlayerControl = 0x2


class cTkBlackboardComparisonTypeEnum(IntEnum):
    Equal = 0x0
    NotEqual = 0x1
    GreaterThan = 0x2
    GreaterThanEqual = 0x3
    LessThan = 0x4
    LessThanEqual = 0x5


class cTkBlackboardType(IntEnum):
    Invalid = 0x0
    Float = 0x1
    Integer = 0x2
    Bool = 0x3
    Id = 0x4
    Vector = 0x5
    Attachment = 0x6


class cTkPusherType(IntEnum):
    Sphere = 0x0
    HollowSphere = 0x1


class cTkUnreachableNavDestBehaviour(IntEnum):
    ClampToFurthestReachable = 0x0
    ContinueOffMesh = 0x1


class cTkNavMeshAreaFlags(IntEnum):
    empty = 0x0
    Steep = 0x1


class cTkNavMeshAreaType(IntEnum):
    Null = 0x0
    Grass = 0x1
    Rock = 0x2
    Snow = 0x3
    Mud = 0x4
    Sand = 0x5
    Cave = 0x6
    Forest = 0x7
    Wetlands = 0x8
    Mistlands = 0x9
    GrassAlt = 0xA
    RockAlt = 0xB
    ForestAlt = 0xC
    MudAlt = 0xD
    Soil = 0xE
    Resource = 0xF
    TerrainInstance = 0x10
    Structure = 0x11
    Water = 0x12
    Auto = 0x13
    UseCollisionTileType = 0x14


class cTkNavMeshInclusionType(IntEnum):
    Auto = 0x0
    Ignore = 0x1
    Obstacle = 0x2
    Walkable = 0x3


class cTkNavMeshPathingQuality(IntEnum):
    Normal = 0x0
    High = 0x1
    Highest = 0x2


class cTkNavMeshPolyFlags(IntEnum):
    empty = 0x0
    TestFlag = 0x1


class cTkMaterialFlags(IntEnum):
    _F01_DIFFUSEMAP = 0x0
    _F02_SKINNED = 0x1
    _F03_NORMALMAP = 0x2
    _F04_FEATURESMAP = 0x3
    _F05_DEPTH_EFFECT = 0x4
    _F06 = 0x5
    _F07_UNLIT = 0x6
    _F08 = 0x7
    _F09 = 0x8
    _F10 = 0x9
    _F11 = 0xA
    _F12 = 0xB
    _F13_UV_EFFECT = 0xC
    _F14 = 0xD
    _F15_WIND = 0xE
    _F16_DIFFUSE2MAP = 0xF
    _F17 = 0x10
    _F18 = 0x11
    _F19_BILLBOARD = 0x12
    _F20_PARALLAX = 0x13
    _F21_VERTEXCUSTOM = 0x14
    _F22_OCCLUSION_MAP = 0x15
    _F23 = 0x16
    _F24 = 0x17
    _F25_MASKS_MAP = 0x18
    _F26 = 0x19
    _F27 = 0x1A
    _F28 = 0x1B
    _F29 = 0x1C
    _F30_REFRACTION = 0x1D
    _F31_DISPLACEMENT = 0x1E
    _F32_REFRACTION_MASK = 0x1F
    _F33_SHELLS = 0x20
    _F34 = 0x21
    _F35 = 0x22
    _F36_DOUBLESIDED = 0x23
    _F37_EXPLICIT_MOTION_VECTORS = 0x24
    _F38 = 0x25
    _F39 = 0x26
    _F40 = 0x27
    _F41 = 0x28
    _F42_DETAIL_NORMAL = 0x29
    _F43 = 0x2A
    _F44 = 0x2B
    _F45 = 0x2C
    _F46 = 0x2D
    _F47 = 0x2E
    _F48 = 0x2F
    _F49 = 0x30
    _F50 = 0x31
    _F51 = 0x32
    _F52 = 0x33
    _F53_COLOURISABLE = 0x34
    _F54 = 0x35
    _F55_MULTITEXTURE = 0x36
    _F56_MATCH_GROUND = 0x37
    _F57 = 0x38
    _F58_USE_CENTRAL_NORMAL = 0x39
    _F59 = 0x3A
    _F60 = 0x3B
    _F61 = 0x3C
    _F62 = 0x3D
    _F63 = 0x3E
    _F64_RESERVED_FLAG_FOR_EARLY_Z_PATCHING_DO_NOT_USE = 0x3F


class cTkMaterialFxFlags(IntEnum):
    _X01 = 0x0
    _X02_SKINNED = 0x1
    _X03_NORMALMAP = 0x2
    _X04_CLAMPED_SIZE = 0x3
    _X05 = 0x4
    _X06 = 0x5
    _X07_UNLIT = 0x6
    _X08 = 0x7
    _X09 = 0x8
    _X10 = 0x9
    _X11 = 0xA
    _X12 = 0xB
    _X13_UVANIMATION = 0xC
    _X14_UVSCROLL = 0xD
    _X15 = 0xE
    _X16 = 0xF
    _X17 = 0x10
    _X18_UVTILES = 0x11
    _X19 = 0x12
    _X20 = 0x13
    _X21 = 0x14
    _X22 = 0x15
    _X23 = 0x16
    _X24 = 0x17
    _X25 = 0x18
    _X26_IMAGE_BASED_LIGHTING = 0x19
    _X27 = 0x1A
    _X28 = 0x1B
    _X29 = 0x1C
    _X30_REFRACTION = 0x1D
    _X31_DISPLACEMENT = 0x1E
    _X32 = 0x1F
    _X33 = 0x20
    _X34_GLOW = 0x21
    _X35 = 0x22
    _X36 = 0x23
    _X37 = 0x24
    _X38 = 0x25
    _X39 = 0x26
    _X40_SUBSURFACE_MASK = 0x27
    _X41 = 0x28
    _X42 = 0x29
    _X43 = 0x2A
    _X44 = 0x2B
    _X45 = 0x2C
    _X46 = 0x2D
    _X47 = 0x2E
    _X48 = 0x2F
    _X49 = 0x30
    _X50 = 0x31
    _X51 = 0x32
    _X52 = 0x33
    _X53_COLOURISABLE = 0x34
    _X54 = 0x35
    _X55 = 0x36
    _X56 = 0x37
    _X57 = 0x38
    _X58 = 0x39
    _X59_BIASED_REACTIVITY = 0x3A
    _X60 = 0x3B
    _X61 = 0x3C
    _X62 = 0x3D
    _X63 = 0x3E
    _X64_RESERVED_FLAG_FOR_EARLY_Z_PATCHING_DO_NOT_USE = 0x3F


class cGcPaletteColourAlt(IntEnum):
    Primary = 0x0
    Secondary = 0x1
    Alternative3 = 0x2
    Alternative4 = 0x3
    Alternative5 = 0x4
    Unique = 0x5
    MatchGround = 0x6
    None_ = 0x7


class cTkNGuiForcedStyle(IntEnum):
    None_ = 0x0
    Default = 0x1
    Highlight = 0x2
    Active = 0x3
    Disabled = 0x4


class cTKNGuiEditorTextType(IntEnum):
    Text = 0x0
    Button = 0x1
    WindowTab = 0x2
    WindowTabInactive = 0x3
    TreeNode = 0x4
    CheckBox = 0x5
    TextInput = 0x6
    TextInputLabel = 0x7
    TextInputLabelHeader = 0x8
    Category = 0x9
    TaskBar = 0xA
    GroupTitle = 0xB
    TreeNodeSelected = 0xC
    DynamicPanelTitle = 0xD
    ContextMenuButton = 0xE


class cTkNGuiEditorGraphicType(IntEnum):
    Panel = 0x0
    Button = 0x1
    Text = 0x2
    Graphic = 0x3
    WindowTitleBar = 0x4
    WindowTitleBarInactive = 0x5
    WindowTabActiveActive = 0x6
    WindowTabInactiveActive = 0x7
    WindowTabActiveInactive = 0x8
    WindowTabInactiveInactive = 0x9
    WindowTabsSeparator = 0xA
    WindowBacking = 0xB
    Window = 0xC
    WindowPane = 0xD
    WindowResize = 0xE
    WindowClose = 0xF
    WindowMinimize = 0x10
    WindowMaximize = 0x11
    ScrollBarBackground = 0x12
    ScrollBarForeground = 0x13
    TreeNodeCollapsed = 0x14
    TreeNodeExpanded = 0x15
    CheckBoxTrue = 0x16
    CheckBoxFalse = 0x17
    TextInput = 0x18
    Increment = 0x19
    Decrement = 0x1A
    Cursor = 0x1B
    TextSelection = 0x1C
    Separator = 0x1D
    EditorResize = 0x1E
    EditorMove = 0x1F
    EditorOverlay = 0x20
    FileBrowser = 0x21
    ColourEdit = 0x22
    IconButton = 0x23
    SliderKnob = 0x24
    SliderBar = 0x25
    IconButtonText = 0x26
    TextInputLabel = 0x27
    Category = 0x28
    Taskbar = 0x29
    TaskbarItem = 0x2A
    TaskbarShortcutButton = 0x2B
    StartBarWindow = 0x2C
    StartBarWindowButton = 0x2D
    StartBarWindowPane = 0x2E
    StartBarWindowListItem = 0x2F
    MenuSearchBox = 0x30
    SearchBox = 0x31
    ComboBox = 0x32
    ComboBoxWindow = 0x33
    IconListItem = 0x34
    IconListItemSelected = 0x35
    ImageButton = 0x36
    Toolbar = 0x37
    ToolbarGraphic = 0x38
    ToolbarOptions = 0x39
    Rectangle = 0x3A
    TreeNodeBorder = 0x3B
    Background = 0x3C
    GroupTitle = 0x3D
    TextLabelSeparator = 0x3E
    AlignmentAnchor = 0x3F
    MinimiseHighlight = 0x40
    Table = 0x41
    TableBorder = 0x42
    TableFolderButton = 0x43
    TableAddEntryButton = 0x44
    TreeNode = 0x45
    CategoryCollapsed = 0x46
    CategoryExpanded = 0x47
    WindowTitleBarDragTarget = 0x48
    IconButtonSelected = 0x49
    Line = 0x4A
    LightLine = 0x4B
    TreeNodeBackground = 0x4C
    TreeNodeCategoryBackground = 0x4D
    SceneNodeBackground = 0x4E
    PinChildren = 0x4F
    UnpinChildren = 0x50
    DynamicPanel = 0x51
    DynamicPanelTitle = 0x52
    DynamicPanelCustomToolbar = 0x53
    Favourite = 0x54
    FavouriteSelected = 0x55
    FavouriteValue = 0x56
    FavouriteValueSelected = 0x57
    RevertButton = 0x58
    TreeNodeCustomPanel = 0x59
    IconButtonBordered = 0x5A
    IconButtonBorderedSelected = 0x5B
    Tooltip = 0x5C
    TooltipButton = 0x5D
    ContextMenuButton = 0x5E


class cTKNGuiEditorComponentSize(IntEnum):
    WindowResize = 0x0
    WindowButton = 0x1
    MinimumWindowHeight = 0x2
    MinimumWindowWidth = 0x3
    Indent = 0x4
    SeparatorHeight = 0x5
    SeparatorWidth = 0x6
    TreeNodeExpander = 0x7
    CheckBox = 0x8
    Adjuster = 0x9
    Cursor = 0xA
    TextEditSeparator = 0xB
    DefaultLineHeight = 0xC
    ColourEditHeight = 0xD
    ColourEditWidth = 0xE
    FileBrowser = 0xF
    EditorResize = 0x10
    EditorMove = 0x11
    IconButton = 0x12
    SliderKnob = 0x13
    SliderBarWidth = 0x14
    SliderBarHeight = 0x15
    CategoryHeight = 0x16
    WindowTitle = 0x17
    MinimumTabWidth = 0x18
    ScrollSpeed = 0x19
    ComboBox = 0x1A
    Taskbar = 0x1B
    IconListItem = 0x1C
    StartBarWindowButton = 0x1D
    StartBarWindowListItem = 0x1E
    StartBarWindowSeparatorWidth = 0x1F
    StartBarWindowChildOffset = 0x20
    Toolbar = 0x21
    ToolbarOptions = 0x22
    GlobalSearchBox = 0x23
    SearchBox = 0x24
    StartBarWindowWidth = 0x25
    StartBarHeight = 0x26
    StartBarWindowSearchWidth = 0x27
    GlobalsMenuWidth = 0x28
    TreeNodeSpacing = 0x29
    VectorSpacing = 0x2A
    SliderMinSpacing = 0x2B
    VectorMinSpacing = 0x2C
    ColourAlphaMinsize = 0x2D
    SpacingGap = 0x2E
    Scroll = 0x2F
    TextLabelSeparator = 0x30
    AlignmentAnchor = 0x31
    MinimiseHighlightHeight = 0x32
    TableButtonSpacing = 0x33
    TableHeaderHeight = 0x34
    TreeNodeHeight = 0x35
    ScrollMargin = 0x36
    ScrollIncrement = 0x37
    EditorPin = 0x38
    DynamicPanelTitle = 0x39
    FavouriteValueStar = 0x3A
    ShortcutBar = 0x3B
    RevertButton = 0x3C
    ToolbarItemPadding = 0x3D
    ContextMenuWidth = 0x3E
    TooltipButtonSize = 0x3F
    TooltipMaxWidth = 0x40


class cTkNGuiEditorIcons(IntEnum):
    none = 0x0
    _0 = 0x1
    _1 = 0x2
    _2 = 0x3
    _3 = 0x4
    _4 = 0x5
    _5 = 0x6
    _6 = 0x7
    _7 = 0x8
    _8 = 0x9
    _9 = 0xA
    a = 0xB
    address_book = 0xC
    address_book_outline = 0xD
    address_card = 0xE
    address_card_outline = 0xF
    align_center = 0x10
    align_justify = 0x11
    align_left = 0x12
    align_right = 0x13
    anchor = 0x14
    anchor_circle_check = 0x15
    anchor_circle_exclamation = 0x16
    anchor_circle_xmark = 0x17
    anchor_lock = 0x18
    angle_down = 0x19
    angle_left = 0x1A
    angle_right = 0x1B
    angle_up = 0x1C
    angles_down = 0x1D
    angles_left = 0x1E
    angles_right = 0x1F
    angles_up = 0x20
    ankh = 0x21
    apple_whole = 0x22
    archway = 0x23
    arrow_down = 0x24
    arrow_down_1_9 = 0x25
    arrow_down_9_1 = 0x26
    arrow_down_a_z = 0x27
    arrow_down_long = 0x28
    arrow_down_short_wide = 0x29
    arrow_down_up_across_line = 0x2A
    arrow_down_up_lock = 0x2B
    arrow_down_wide_short = 0x2C
    arrow_down_z_a = 0x2D
    arrow_left = 0x2E
    arrow_left_long = 0x2F
    arrow_pointer = 0x30
    arrow_right = 0x31
    arrow_right_arrow_left = 0x32
    arrow_right_from_bracket = 0x33
    arrow_right_long = 0x34
    arrow_right_to_bracket = 0x35
    arrow_right_to_city = 0x36
    arrow_rotate_left = 0x37
    arrow_rotate_right = 0x38
    arrow_trend_down = 0x39
    arrow_trend_up = 0x3A
    arrow_turn_down = 0x3B
    arrow_turn_up = 0x3C
    arrow_up = 0x3D
    arrow_up_1_9 = 0x3E
    arrow_up_9_1 = 0x3F
    arrow_up_a_z = 0x40
    arrow_up_from_bracket = 0x41
    arrow_up_from_ground_water = 0x42
    arrow_up_from_water_pump = 0x43
    arrow_up_long = 0x44
    arrow_up_right_dots = 0x45
    arrow_up_right_from_square = 0x46
    arrow_up_short_wide = 0x47
    arrow_up_wide_short = 0x48
    arrow_up_z_a = 0x49
    arrows_down_to_line = 0x4A
    arrows_down_to_people = 0x4B
    arrows_left_right = 0x4C
    arrows_left_right_to_line = 0x4D
    arrows_rotate = 0x4E
    arrows_spin = 0x4F
    arrows_split_up_and_left = 0x50
    arrows_to_circle = 0x51
    arrows_to_dot = 0x52
    arrows_to_eye = 0x53
    arrows_turn_right = 0x54
    arrows_turn_to_dots = 0x55
    arrows_up_down = 0x56
    arrows_up_down_left_right = 0x57
    arrows_up_to_line = 0x58
    asterisk = 0x59
    at = 0x5A
    atom = 0x5B
    audio_description = 0x5C
    austral_sign = 0x5D
    award = 0x5E
    b = 0x5F
    baby = 0x60
    baby_carriage = 0x61
    backward = 0x62
    backward_fast = 0x63
    backward_step = 0x64
    bacon = 0x65
    bacteria = 0x66
    bacterium = 0x67
    bag_shopping = 0x68
    bahai = 0x69
    baht_sign = 0x6A
    ban = 0x6B
    ban_smoking = 0x6C
    bandage = 0x6D
    bangladeshi_taka_sign = 0x6E
    barcode = 0x6F
    bars = 0x70
    bars_progress = 0x71
    bars_staggered = 0x72
    baseball = 0x73
    baseball_bat_ball = 0x74
    basket_shopping = 0x75
    basketball = 0x76
    bath = 0x77
    battery_empty = 0x78
    battery_full = 0x79
    battery_half = 0x7A
    battery_quarter = 0x7B
    battery_three_quarters = 0x7C
    bed = 0x7D
    bed_pulse = 0x7E
    beer_mug_empty = 0x7F
    bell = 0x80
    bell_outline = 0x81
    bell_concierge = 0x82
    bell_slash = 0x83
    bell_slash_outline = 0x84
    bezier_curve = 0x85
    bicycle = 0x86
    binoculars = 0x87
    biohazard = 0x88
    bitcoin_sign = 0x89
    blender = 0x8A
    blender_phone = 0x8B
    blog = 0x8C
    bold = 0x8D
    bolt = 0x8E
    bolt_lightning = 0x8F
    bomb = 0x90
    bone = 0x91
    bong = 0x92
    book = 0x93
    book_atlas = 0x94
    book_bible = 0x95
    book_bookmark = 0x96
    book_journal_whills = 0x97
    book_medical = 0x98
    book_open = 0x99
    book_open_reader = 0x9A
    book_quran = 0x9B
    book_skull = 0x9C
    book_tanakh = 0x9D
    bookmark = 0x9E
    bookmark_outline = 0x9F
    border_all = 0xA0
    border_none = 0xA1
    border_top_left = 0xA2
    bore_hole = 0xA3
    bottle_droplet = 0xA4
    bottle_water = 0xA5
    bowl_food = 0xA6
    bowl_rice = 0xA7
    bowling_ball = 0xA8
    box = 0xA9
    box_archive = 0xAA
    box_open = 0xAB
    box_tissue = 0xAC
    boxes_packing = 0xAD
    boxes_stacked = 0xAE
    braille = 0xAF
    brain = 0xB0
    brazilian_real_sign = 0xB1
    bread_slice = 0xB2
    bridge = 0xB3
    bridge_circle_check = 0xB4
    bridge_circle_exclamation = 0xB5
    bridge_circle_xmark = 0xB6
    bridge_lock = 0xB7
    bridge_water = 0xB8
    briefcase = 0xB9
    briefcase_medical = 0xBA
    broom = 0xBB
    broom_ball = 0xBC
    brush = 0xBD
    bucket = 0xBE
    bug = 0xBF
    bug_slash = 0xC0
    bugs = 0xC1
    building = 0xC2
    building_outline = 0xC3
    building_circle_arrow_right = 0xC4
    building_circle_check = 0xC5
    building_circle_exclamation = 0xC6
    building_circle_xmark = 0xC7
    building_columns = 0xC8
    building_flag = 0xC9
    building_lock = 0xCA
    building_ngo = 0xCB
    building_shield = 0xCC
    building_un = 0xCD
    building_user = 0xCE
    building_wheat = 0xCF
    bullhorn = 0xD0
    bullseye = 0xD1
    burger = 0xD2
    burst = 0xD3
    bus = 0xD4
    bus_simple = 0xD5
    business_time = 0xD6
    c = 0xD7
    cable_car = 0xD8
    cake_candles = 0xD9
    calculator = 0xDA
    calendar = 0xDB
    calendar_outline = 0xDC
    calendar_check = 0xDD
    calendar_check_outline = 0xDE
    calendar_day = 0xDF
    calendar_days = 0xE0
    calendar_days_outline = 0xE1
    calendar_minus = 0xE2
    calendar_minus_outline = 0xE3
    calendar_plus = 0xE4
    calendar_plus_outline = 0xE5
    calendar_week = 0xE6
    calendar_xmark = 0xE7
    calendar_xmark_outline = 0xE8
    camera = 0xE9
    camera_retro = 0xEA
    camera_rotate = 0xEB
    campground = 0xEC
    candy_cane = 0xED
    cannabis = 0xEE
    capsules = 0xEF
    car = 0xF0
    car_battery = 0xF1
    car_burst = 0xF2
    car_on = 0xF3
    car_rear = 0xF4
    car_side = 0xF5
    car_tunnel = 0xF6
    caravan = 0xF7
    caret_down = 0xF8
    caret_left = 0xF9
    caret_right = 0xFA
    caret_up = 0xFB
    carrot = 0xFC
    cart_arrow_down = 0xFD
    cart_flatbed = 0xFE
    cart_flatbed_suitcase = 0xFF
    cart_plus = 0x100
    cart_shopping = 0x101
    cash_register = 0x102
    cat = 0x103
    cedi_sign = 0x104
    cent_sign = 0x105
    certificate = 0x106
    chair = 0x107
    chalkboard = 0x108
    chalkboard_user = 0x109
    champagne_glasses = 0x10A
    charging_station = 0x10B
    chart_area = 0x10C
    chart_bar = 0x10D
    chart_bar_outline = 0x10E
    chart_column = 0x10F
    chart_gantt = 0x110
    chart_line = 0x111
    chart_pie = 0x112
    chart_simple = 0x113
    check = 0x114
    check_double = 0x115
    check_to_slot = 0x116
    cheese = 0x117
    chess = 0x118
    chess_bishop = 0x119
    chess_bishop_outline = 0x11A
    chess_board = 0x11B
    chess_king = 0x11C
    chess_king_outline = 0x11D
    chess_knight = 0x11E
    chess_knight_outline = 0x11F
    chess_pawn = 0x120
    chess_pawn_outline = 0x121
    chess_queen = 0x122
    chess_queen_outline = 0x123
    chess_rook = 0x124
    chess_rook_outline = 0x125
    chevron_down = 0x126
    chevron_left = 0x127
    chevron_right = 0x128
    chevron_up = 0x129
    child = 0x12A
    child_combatant = 0x12B
    child_dress = 0x12C
    child_reaching = 0x12D
    children = 0x12E
    church = 0x12F
    circle = 0x130
    circle_outline = 0x131
    circle_arrow_down = 0x132
    circle_arrow_left = 0x133
    circle_arrow_right = 0x134
    circle_arrow_up = 0x135
    circle_check = 0x136
    circle_check_outline = 0x137
    circle_chevron_down = 0x138
    circle_chevron_left = 0x139
    circle_chevron_right = 0x13A
    circle_chevron_up = 0x13B
    circle_dollar_to_slot = 0x13C
    circle_dot = 0x13D
    circle_dot_outline = 0x13E
    circle_down = 0x13F
    circle_down_outline = 0x140
    circle_exclamation = 0x141
    circle_h = 0x142
    circle_half_stroke = 0x143
    circle_info = 0x144
    circle_left = 0x145
    circle_left_outline = 0x146
    circle_minus = 0x147
    circle_nodes = 0x148
    circle_notch = 0x149
    circle_pause = 0x14A
    circle_pause_outline = 0x14B
    circle_play = 0x14C
    circle_play_outline = 0x14D
    circle_plus = 0x14E
    circle_question = 0x14F
    circle_question_outline = 0x150
    circle_radiation = 0x151
    circle_right = 0x152
    circle_right_outline = 0x153
    circle_stop = 0x154
    circle_stop_outline = 0x155
    circle_up = 0x156
    circle_up_outline = 0x157
    circle_user = 0x158
    circle_user_outline = 0x159
    circle_xmark = 0x15A
    circle_xmark_outline = 0x15B
    city = 0x15C
    clapperboard = 0x15D
    clipboard = 0x15E
    clipboard_outline = 0x15F
    clipboard_check = 0x160
    clipboard_list = 0x161
    clipboard_question = 0x162
    clipboard_user = 0x163
    clock = 0x164
    clock_outline = 0x165
    clock_rotate_left = 0x166
    clone = 0x167
    clone_outline = 0x168
    closed_captioning = 0x169
    closed_captioning_outline = 0x16A
    cloud = 0x16B
    cloud_arrow_down = 0x16C
    cloud_arrow_up = 0x16D
    cloud_bolt = 0x16E
    cloud_meatball = 0x16F
    cloud_moon = 0x170
    cloud_moon_rain = 0x171
    cloud_rain = 0x172
    cloud_showers_heavy = 0x173
    cloud_showers_water = 0x174
    cloud_sun = 0x175
    cloud_sun_rain = 0x176
    clover = 0x177
    code = 0x178
    code_branch = 0x179
    code_commit = 0x17A
    code_compare = 0x17B
    code_fork = 0x17C
    code_merge = 0x17D
    code_pull_request = 0x17E
    coins = 0x17F
    colon_sign = 0x180
    comment = 0x181
    comment_outline = 0x182
    comment_dollar = 0x183
    comment_dots = 0x184
    comment_dots_outline = 0x185
    comment_medical = 0x186
    comment_slash = 0x187
    comment_sms = 0x188
    comments = 0x189
    comments_outline = 0x18A
    comments_dollar = 0x18B
    compact_disc = 0x18C
    compass = 0x18D
    compass_outline = 0x18E
    compass_drafting = 0x18F
    compress = 0x190
    computer = 0x191
    computer_mouse = 0x192
    cookie = 0x193
    cookie_bite = 0x194
    copy = 0x195
    copy_outline = 0x196
    copyright = 0x197
    copyright_outline = 0x198
    couch = 0x199
    cow = 0x19A
    credit_card = 0x19B
    credit_card_outline = 0x19C
    crop = 0x19D
    crop_simple = 0x19E
    cross = 0x19F
    crosshairs = 0x1A0
    crow = 0x1A1
    crown = 0x1A2
    crutch = 0x1A3
    cruzeiro_sign = 0x1A4
    cube = 0x1A5
    cubes = 0x1A6
    cubes_stacked = 0x1A7
    d = 0x1A8
    database = 0x1A9
    delete_left = 0x1AA
    democrat = 0x1AB
    desktop = 0x1AC
    dharmachakra = 0x1AD
    diagram_next = 0x1AE
    diagram_predecessor = 0x1AF
    diagram_project = 0x1B0
    diagram_successor = 0x1B1
    diamond = 0x1B2
    diamond_turn_right = 0x1B3
    dice = 0x1B4
    dice_d20 = 0x1B5
    dice_d6 = 0x1B6
    dice_five = 0x1B7
    dice_four = 0x1B8
    dice_one = 0x1B9
    dice_six = 0x1BA
    dice_three = 0x1BB
    dice_two = 0x1BC
    disease = 0x1BD
    display = 0x1BE
    divide = 0x1BF
    dna = 0x1C0
    dog = 0x1C1
    dollar_sign = 0x1C2
    dolly = 0x1C3
    dong_sign = 0x1C4
    door_closed = 0x1C5
    door_open = 0x1C6
    dove = 0x1C7
    down_left_and_up_right_to_center = 0x1C8
    down_long = 0x1C9
    download = 0x1CA
    dragon = 0x1CB
    draw_polygon = 0x1CC
    droplet = 0x1CD
    droplet_slash = 0x1CE
    drum = 0x1CF
    drum_steelpan = 0x1D0
    drumstick_bite = 0x1D1
    dumbbell = 0x1D2
    dumpster = 0x1D3
    dumpster_fire = 0x1D4
    dungeon = 0x1D5
    e = 0x1D6
    ear_deaf = 0x1D7
    ear_listen = 0x1D8
    earth_africa = 0x1D9
    earth_americas = 0x1DA
    earth_asia = 0x1DB
    earth_europe = 0x1DC
    earth_oceania = 0x1DD
    egg = 0x1DE
    eject = 0x1DF
    elevator = 0x1E0
    ellipsis = 0x1E1
    ellipsis_vertical = 0x1E2
    envelope = 0x1E3
    envelope_outline = 0x1E4
    envelope_circle_check = 0x1E5
    envelope_open = 0x1E6
    envelope_open_outline = 0x1E7
    envelope_open_text = 0x1E8
    envelopes_bulk = 0x1E9
    equals = 0x1EA
    eraser = 0x1EB
    ethernet = 0x1EC
    euro_sign = 0x1ED
    exclamation = 0x1EE
    expand = 0x1EF
    explosion = 0x1F0
    eye = 0x1F1
    eye_outline = 0x1F2
    eye_dropper = 0x1F3
    eye_low_vision = 0x1F4
    eye_slash = 0x1F5
    eye_slash_outline = 0x1F6
    f = 0x1F7
    face_angry = 0x1F8
    face_angry_outline = 0x1F9
    face_dizzy = 0x1FA
    face_dizzy_outline = 0x1FB
    face_flushed = 0x1FC
    face_flushed_outline = 0x1FD
    face_frown = 0x1FE
    face_frown_outline = 0x1FF
    face_frown_open = 0x200
    face_frown_open_outline = 0x201
    face_grimace = 0x202
    face_grimace_outline = 0x203
    face_grin = 0x204
    face_grin_outline = 0x205
    face_grin_beam = 0x206
    face_grin_beam_outline = 0x207
    face_grin_beam_sweat = 0x208
    face_grin_beam_sweat_outline = 0x209
    face_grin_hearts = 0x20A
    face_grin_hearts_outline = 0x20B
    face_grin_squint = 0x20C
    face_grin_squint_outline = 0x20D
    face_grin_squint_tears = 0x20E
    face_grin_squint_tears_outline = 0x20F
    face_grin_stars = 0x210
    face_grin_stars_outline = 0x211
    face_grin_tears = 0x212
    face_grin_tears_outline = 0x213
    face_grin_tongue = 0x214
    face_grin_tongue_outline = 0x215
    face_grin_tongue_squint = 0x216
    face_grin_tongue_squint_outline = 0x217
    face_grin_tongue_wink = 0x218
    face_grin_tongue_wink_outline = 0x219
    face_grin_wide = 0x21A
    face_grin_wide_outline = 0x21B
    face_grin_wink = 0x21C
    face_grin_wink_outline = 0x21D
    face_kiss = 0x21E
    face_kiss_outline = 0x21F
    face_kiss_beam = 0x220
    face_kiss_beam_outline = 0x221
    face_kiss_wink_heart = 0x222
    face_kiss_wink_heart_outline = 0x223
    face_laugh = 0x224
    face_laugh_outline = 0x225
    face_laugh_beam = 0x226
    face_laugh_beam_outline = 0x227
    face_laugh_squint = 0x228
    face_laugh_squint_outline = 0x229
    face_laugh_wink = 0x22A
    face_laugh_wink_outline = 0x22B
    face_meh = 0x22C
    face_meh_outline = 0x22D
    face_meh_blank = 0x22E
    face_meh_blank_outline = 0x22F
    face_rolling_eyes = 0x230
    face_rolling_eyes_outline = 0x231
    face_sad_cry = 0x232
    face_sad_cry_outline = 0x233
    face_sad_tear = 0x234
    face_sad_tear_outline = 0x235
    face_smile = 0x236
    face_smile_outline = 0x237
    face_smile_beam = 0x238
    face_smile_beam_outline = 0x239
    face_smile_wink = 0x23A
    face_smile_wink_outline = 0x23B
    face_surprise = 0x23C
    face_surprise_outline = 0x23D
    face_tired = 0x23E
    face_tired_outline = 0x23F
    fan = 0x240
    faucet = 0x241
    faucet_drip = 0x242
    fax = 0x243
    feather = 0x244
    feather_pointed = 0x245
    ferry = 0x246
    file = 0x247
    file_outline = 0x248
    file_arrow_down = 0x249
    file_arrow_up = 0x24A
    file_audio = 0x24B
    file_audio_outline = 0x24C
    file_circle_check = 0x24D
    file_circle_exclamation = 0x24E
    file_circle_minus = 0x24F
    file_circle_plus = 0x250
    file_circle_question = 0x251
    file_circle_xmark = 0x252
    file_code = 0x253
    file_code_outline = 0x254
    file_contract = 0x255
    file_csv = 0x256
    file_excel = 0x257
    file_excel_outline = 0x258
    file_export = 0x259
    file_image = 0x25A
    file_image_outline = 0x25B
    file_import = 0x25C
    file_invoice = 0x25D
    file_invoice_dollar = 0x25E
    file_lines = 0x25F
    file_lines_outline = 0x260
    file_medical = 0x261
    file_pdf = 0x262
    file_pdf_outline = 0x263
    file_pen = 0x264
    file_powerpoint = 0x265
    file_powerpoint_outline = 0x266
    file_prescription = 0x267
    file_shield = 0x268
    file_signature = 0x269
    file_video = 0x26A
    file_video_outline = 0x26B
    file_waveform = 0x26C
    file_word = 0x26D
    file_word_outline = 0x26E
    file_zipper = 0x26F
    file_zipper_outline = 0x270
    fill = 0x271
    fill_drip = 0x272
    film = 0x273
    filter = 0x274
    filter_circle_dollar = 0x275
    filter_circle_xmark = 0x276
    fingerprint = 0x277
    fire = 0x278
    fire_burner = 0x279
    fire_extinguisher = 0x27A
    fire_flame_curved = 0x27B
    fire_flame_simple = 0x27C
    fish = 0x27D
    fish_fins = 0x27E
    flag = 0x27F
    flag_outline = 0x280
    flag_checkered = 0x281
    flag_usa = 0x282
    flask = 0x283
    flask_vial = 0x284
    floppy_disk = 0x285
    floppy_disk_outline = 0x286
    florin_sign = 0x287
    folder = 0x288
    folder_outline = 0x289
    folder_closed = 0x28A
    folder_closed_outline = 0x28B
    folder_minus = 0x28C
    folder_open = 0x28D
    folder_open_outline = 0x28E
    folder_plus = 0x28F
    folder_tree = 0x290
    font = 0x291
    font_awesome = 0x292
    font_awesome_outline = 0x293
    football = 0x294
    forward = 0x295
    forward_fast = 0x296
    forward_step = 0x297
    franc_sign = 0x298
    frog = 0x299
    futbol = 0x29A
    futbol_outline = 0x29B
    g = 0x29C
    gamepad = 0x29D
    gas_pump = 0x29E
    gauge = 0x29F
    gauge_high = 0x2A0
    gauge_simple = 0x2A1
    gauge_simple_high = 0x2A2
    gavel = 0x2A3
    gear = 0x2A4
    gears = 0x2A5
    gem = 0x2A6
    gem_outline = 0x2A7
    genderless = 0x2A8
    ghost = 0x2A9
    gift = 0x2AA
    gifts = 0x2AB
    glass_water = 0x2AC
    glass_water_droplet = 0x2AD
    glasses = 0x2AE
    globe = 0x2AF
    golf_ball_tee = 0x2B0
    gopuram = 0x2B1
    graduation_cap = 0x2B2
    greater_than = 0x2B3
    greater_than_equal = 0x2B4
    grip = 0x2B5
    grip_lines = 0x2B6
    grip_lines_vertical = 0x2B7
    grip_vertical = 0x2B8
    group_arrows_rotate = 0x2B9
    guarani_sign = 0x2BA
    guitar = 0x2BB
    gun = 0x2BC
    h = 0x2BD
    hammer = 0x2BE
    hamsa = 0x2BF
    hand = 0x2C0
    hand_outline = 0x2C1
    hand_back_fist = 0x2C2
    hand_back_fist_outline = 0x2C3
    hand_dots = 0x2C4
    hand_fist = 0x2C5
    hand_holding = 0x2C6
    hand_holding_dollar = 0x2C7
    hand_holding_droplet = 0x2C8
    hand_holding_hand = 0x2C9
    hand_holding_heart = 0x2CA
    hand_holding_medical = 0x2CB
    hand_lizard = 0x2CC
    hand_lizard_outline = 0x2CD
    hand_middle_finger = 0x2CE
    hand_peace = 0x2CF
    hand_peace_outline = 0x2D0
    hand_point_down = 0x2D1
    hand_point_down_outline = 0x2D2
    hand_point_left = 0x2D3
    hand_point_left_outline = 0x2D4
    hand_point_right = 0x2D5
    hand_point_right_outline = 0x2D6
    hand_point_up = 0x2D7
    hand_point_up_outline = 0x2D8
    hand_pointer = 0x2D9
    hand_pointer_outline = 0x2DA
    hand_scissors = 0x2DB
    hand_scissors_outline = 0x2DC
    hand_sparkles = 0x2DD
    hand_spock = 0x2DE
    hand_spock_outline = 0x2DF
    handcuffs = 0x2E0
    hands = 0x2E1
    hands_asl_interpreting = 0x2E2
    hands_bound = 0x2E3
    hands_bubbles = 0x2E4
    hands_clapping = 0x2E5
    hands_holding = 0x2E6
    hands_holding_child = 0x2E7
    hands_holding_circle = 0x2E8
    hands_praying = 0x2E9
    handshake = 0x2EA
    handshake_outline = 0x2EB
    handshake_angle = 0x2EC
    handshake_simple = 0x2ED
    handshake_simple_slash = 0x2EE
    handshake_slash = 0x2EF
    hanukiah = 0x2F0
    hard_drive = 0x2F1
    hard_drive_outline = 0x2F2
    hashtag = 0x2F3
    hat_cowboy = 0x2F4
    hat_cowboy_side = 0x2F5
    hat_wizard = 0x2F6
    head_side_cough = 0x2F7
    head_side_cough_slash = 0x2F8
    head_side_mask = 0x2F9
    head_side_virus = 0x2FA
    heading = 0x2FB
    headphones = 0x2FC
    headphones_simple = 0x2FD
    headset = 0x2FE
    heart = 0x2FF
    heart_outline = 0x300
    heart_circle_bolt = 0x301
    heart_circle_check = 0x302
    heart_circle_exclamation = 0x303
    heart_circle_minus = 0x304
    heart_circle_plus = 0x305
    heart_circle_xmark = 0x306
    heart_crack = 0x307
    heart_pulse = 0x308
    helicopter = 0x309
    helicopter_symbol = 0x30A
    helmet_safety = 0x30B
    helmet_un = 0x30C
    highlighter = 0x30D
    hill_avalanche = 0x30E
    hill_rockslide = 0x30F
    hippo = 0x310
    hockey_puck = 0x311
    holly_berry = 0x312
    horse = 0x313
    horse_head = 0x314
    hospital = 0x315
    hospital_outline = 0x316
    hospital_user = 0x317
    hot_tub_person = 0x318
    hotdog = 0x319
    hotel = 0x31A
    hourglass = 0x31B
    hourglass_outline = 0x31C
    hourglass_end = 0x31D
    hourglass_half = 0x31E
    hourglass_half_outline = 0x31F
    hourglass_start = 0x320
    house = 0x321
    house_chimney = 0x322
    house_chimney_crack = 0x323
    house_chimney_medical = 0x324
    house_chimney_user = 0x325
    house_chimney_window = 0x326
    house_circle_check = 0x327
    house_circle_exclamation = 0x328
    house_circle_xmark = 0x329
    house_crack = 0x32A
    house_fire = 0x32B
    house_flag = 0x32C
    house_flood_water = 0x32D
    house_flood_water_circle_arrow_right = 0x32E
    house_laptop = 0x32F
    house_lock = 0x330
    house_medical = 0x331
    house_medical_circle_check = 0x332
    house_medical_circle_exclamation = 0x333
    house_medical_circle_xmark = 0x334
    house_medical_flag = 0x335
    house_signal = 0x336
    house_tsunami = 0x337
    house_user = 0x338
    hryvnia_sign = 0x339
    hurricane = 0x33A
    i = 0x33B
    i_cursor = 0x33C
    ice_cream = 0x33D
    icicles = 0x33E
    icons = 0x33F
    id_badge = 0x340
    id_badge_outline = 0x341
    id_card = 0x342
    id_card_outline = 0x343
    id_card_clip = 0x344
    igloo = 0x345
    image = 0x346
    image_outline = 0x347
    image_portrait = 0x348
    images = 0x349
    images_outline = 0x34A
    inbox = 0x34B
    indent = 0x34C
    indian_rupee_sign = 0x34D
    industry = 0x34E
    infinity = 0x34F
    info = 0x350
    italic = 0x351
    j = 0x352
    jar = 0x353
    jar_wheat = 0x354
    jedi = 0x355
    jet_fighter = 0x356
    jet_fighter_up = 0x357
    joint = 0x358
    jug_detergent = 0x359
    k = 0x35A
    kaaba = 0x35B
    key = 0x35C
    keyboard = 0x35D
    keyboard_outline = 0x35E
    khanda = 0x35F
    kip_sign = 0x360
    kit_medical = 0x361
    kitchen_set = 0x362
    kiwi_bird = 0x363
    l = 0x364
    land_mine_on = 0x365
    landmark = 0x366
    landmark_dome = 0x367
    landmark_flag = 0x368
    language = 0x369
    laptop = 0x36A
    laptop_code = 0x36B
    laptop_file = 0x36C
    laptop_medical = 0x36D
    lari_sign = 0x36E
    layer_group = 0x36F
    leaf = 0x370
    left_long = 0x371
    left_right = 0x372
    lemon = 0x373
    lemon_outline = 0x374
    less_than = 0x375
    less_than_equal = 0x376
    life_ring = 0x377
    life_ring_outline = 0x378
    lightbulb = 0x379
    lightbulb_outline = 0x37A
    lines_leaning = 0x37B
    link = 0x37C
    link_slash = 0x37D
    lira_sign = 0x37E
    list = 0x37F
    list_check = 0x380
    list_ol = 0x381
    list_ul = 0x382
    litecoin_sign = 0x383
    location_arrow = 0x384
    location_crosshairs = 0x385
    location_dot = 0x386
    location_pin = 0x387
    location_pin_lock = 0x388
    lock = 0x389
    lock_open = 0x38A
    locust = 0x38B
    lungs = 0x38C
    lungs_virus = 0x38D
    m = 0x38E
    magnet = 0x38F
    magnifying_glass = 0x390
    magnifying_glass_arrow_right = 0x391
    magnifying_glass_chart = 0x392
    magnifying_glass_dollar = 0x393
    magnifying_glass_location = 0x394
    magnifying_glass_minus = 0x395
    magnifying_glass_plus = 0x396
    manat_sign = 0x397
    map = 0x398
    map_outline = 0x399
    map_location = 0x39A
    map_location_dot = 0x39B
    map_pin = 0x39C
    marker = 0x39D
    mars = 0x39E
    mars_and_venus = 0x39F
    mars_and_venus_burst = 0x3A0
    mars_double = 0x3A1
    mars_stroke = 0x3A2
    mars_stroke_right = 0x3A3
    mars_stroke_up = 0x3A4
    martini_glass = 0x3A5
    martini_glass_citrus = 0x3A6
    martini_glass_empty = 0x3A7
    mask = 0x3A8
    mask_face = 0x3A9
    mask_ventilator = 0x3AA
    masks_theater = 0x3AB
    mattress_pillow = 0x3AC
    maximize = 0x3AD
    medal = 0x3AE
    memory = 0x3AF
    menorah = 0x3B0
    mercury = 0x3B1
    message = 0x3B2
    message_outline = 0x3B3
    meteor = 0x3B4
    microchip = 0x3B5
    microphone = 0x3B6
    microphone_lines = 0x3B7
    microphone_lines_slash = 0x3B8
    microphone_slash = 0x3B9
    microscope = 0x3BA
    mill_sign = 0x3BB
    minimize = 0x3BC
    minus = 0x3BD
    mitten = 0x3BE
    mobile = 0x3BF
    mobile_button = 0x3C0
    mobile_retro = 0x3C1
    mobile_screen = 0x3C2
    mobile_screen_button = 0x3C3
    money_bill = 0x3C4
    money_bill_1 = 0x3C5
    money_bill_1_outline = 0x3C6
    money_bill_1_wave = 0x3C7
    money_bill_transfer = 0x3C8
    money_bill_trend_up = 0x3C9
    money_bill_wave = 0x3CA
    money_bill_wheat = 0x3CB
    money_bills = 0x3CC
    money_check = 0x3CD
    money_check_dollar = 0x3CE
    monument = 0x3CF
    moon = 0x3D0
    moon_outline = 0x3D1
    mortar_pestle = 0x3D2
    mosque = 0x3D3
    mosquito = 0x3D4
    mosquito_net = 0x3D5
    motorcycle = 0x3D6
    mound = 0x3D7
    mountain = 0x3D8
    mountain_city = 0x3D9
    mountain_sun = 0x3DA
    mug_hot = 0x3DB
    mug_saucer = 0x3DC
    music = 0x3DD
    n = 0x3DE
    naira_sign = 0x3DF
    network_wired = 0x3E0
    neuter = 0x3E1
    newspaper = 0x3E2
    newspaper_outline = 0x3E3
    not_equal = 0x3E4
    notdef = 0x3E5
    note_sticky = 0x3E6
    note_sticky_outline = 0x3E7
    notes_medical = 0x3E8
    o = 0x3E9
    object_group = 0x3EA
    object_group_outline = 0x3EB
    object_ungroup = 0x3EC
    object_ungroup_outline = 0x3ED
    oil_can = 0x3EE
    oil_well = 0x3EF
    om = 0x3F0
    otter = 0x3F1
    outdent = 0x3F2
    p = 0x3F3
    pager = 0x3F4
    paint_roller = 0x3F5
    paintbrush = 0x3F6
    palette = 0x3F7
    pallet = 0x3F8
    panorama = 0x3F9
    paper_plane = 0x3FA
    paper_plane_outline = 0x3FB
    paperclip = 0x3FC
    parachute_box = 0x3FD
    paragraph = 0x3FE
    passport = 0x3FF
    paste = 0x400
    paste_outline = 0x401
    pause = 0x402
    paw = 0x403
    peace = 0x404
    pen = 0x405
    pen_clip = 0x406
    pen_fancy = 0x407
    pen_nib = 0x408
    pen_ruler = 0x409
    pen_to_square = 0x40A
    pen_to_square_outline = 0x40B
    pencil = 0x40C
    people_arrows = 0x40D
    people_carry_box = 0x40E
    people_group = 0x40F
    people_line = 0x410
    people_pulling = 0x411
    people_robbery = 0x412
    people_roof = 0x413
    pepper_hot = 0x414
    percent = 0x415
    person = 0x416
    person_arrow_down_to_line = 0x417
    person_arrow_up_from_line = 0x418
    person_biking = 0x419
    person_booth = 0x41A
    person_breastfeeding = 0x41B
    person_burst = 0x41C
    person_cane = 0x41D
    person_chalkboard = 0x41E
    person_circle_check = 0x41F
    person_circle_exclamation = 0x420
    person_circle_minus = 0x421
    person_circle_plus = 0x422
    person_circle_question = 0x423
    person_circle_xmark = 0x424
    person_digging = 0x425
    person_dots_from_line = 0x426
    person_dress = 0x427
    person_dress_burst = 0x428
    person_drowning = 0x429
    person_falling = 0x42A
    person_falling_burst = 0x42B
    person_half_dress = 0x42C
    person_harassing = 0x42D
    person_hiking = 0x42E
    person_military_pointing = 0x42F
    person_military_rifle = 0x430
    person_military_to_person = 0x431
    person_praying = 0x432
    person_pregnant = 0x433
    person_rays = 0x434
    person_rifle = 0x435
    person_running = 0x436
    person_shelter = 0x437
    person_skating = 0x438
    person_skiing = 0x439
    person_skiing_nordic = 0x43A
    person_snowboarding = 0x43B
    person_swimming = 0x43C
    person_through_window = 0x43D
    person_walking = 0x43E
    person_walking_arrow_loop_left = 0x43F
    person_walking_arrow_right = 0x440
    person_walking_dashed_line_arrow_right = 0x441
    person_walking_luggage = 0x442
    person_walking_with_cane = 0x443
    peseta_sign = 0x444
    peso_sign = 0x445
    phone = 0x446
    phone_flip = 0x447
    phone_slash = 0x448
    phone_volume = 0x449
    photo_film = 0x44A
    piggy_bank = 0x44B
    pills = 0x44C
    pizza_slice = 0x44D
    place_of_worship = 0x44E
    plane = 0x44F
    plane_arrival = 0x450
    plane_circle_check = 0x451
    plane_circle_exclamation = 0x452
    plane_circle_xmark = 0x453
    plane_departure = 0x454
    plane_lock = 0x455
    plane_slash = 0x456
    plane_up = 0x457
    plant_wilt = 0x458
    plate_wheat = 0x459
    play = 0x45A
    plug = 0x45B
    plug_circle_bolt = 0x45C
    plug_circle_check = 0x45D
    plug_circle_exclamation = 0x45E
    plug_circle_minus = 0x45F
    plug_circle_plus = 0x460
    plug_circle_xmark = 0x461
    plus = 0x462
    plus_minus = 0x463
    podcast = 0x464
    poo = 0x465
    poo_storm = 0x466
    poop = 0x467
    power_off = 0x468
    prescription = 0x469
    prescription_bottle = 0x46A
    prescription_bottle_medical = 0x46B
    print = 0x46C
    pump_medical = 0x46D
    pump_soap = 0x46E
    puzzle_piece = 0x46F
    q = 0x470
    qrcode = 0x471
    question = 0x472
    quote_left = 0x473
    quote_right = 0x474
    r = 0x475
    radiation = 0x476
    radio = 0x477
    rainbow = 0x478
    ranking_star = 0x479
    receipt = 0x47A
    record_vinyl = 0x47B
    rectangle_ad = 0x47C
    rectangle_list = 0x47D
    rectangle_list_outline = 0x47E
    rectangle_xmark = 0x47F
    rectangle_xmark_outline = 0x480
    recycle = 0x481
    registered = 0x482
    registered_outline = 0x483
    repeat = 0x484
    reply = 0x485
    reply_all = 0x486
    republican = 0x487
    restroom = 0x488
    retweet = 0x489
    ribbon = 0x48A
    right_from_bracket = 0x48B
    right_left = 0x48C
    right_long = 0x48D
    right_to_bracket = 0x48E
    ring = 0x48F
    road = 0x490
    road_barrier = 0x491
    road_bridge = 0x492
    road_circle_check = 0x493
    road_circle_exclamation = 0x494
    road_circle_xmark = 0x495
    road_lock = 0x496
    road_spikes = 0x497
    robot = 0x498
    rocket = 0x499
    rotate = 0x49A
    rotate_left = 0x49B
    rotate_right = 0x49C
    route = 0x49D
    rss = 0x49E
    ruble_sign = 0x49F
    rug = 0x4A0
    ruler = 0x4A1
    ruler_combined = 0x4A2
    ruler_horizontal = 0x4A3
    ruler_vertical = 0x4A4
    rupee_sign = 0x4A5
    rupiah_sign = 0x4A6
    s = 0x4A7
    sack_dollar = 0x4A8
    sack_xmark = 0x4A9
    sailboat = 0x4AA
    satellite = 0x4AB
    satellite_dish = 0x4AC
    scale_balanced = 0x4AD
    scale_unbalanced = 0x4AE
    scale_unbalanced_flip = 0x4AF
    school = 0x4B0
    school_circle_check = 0x4B1
    school_circle_exclamation = 0x4B2
    school_circle_xmark = 0x4B3
    school_flag = 0x4B4
    school_lock = 0x4B5
    scissors = 0x4B6
    screwdriver = 0x4B7
    screwdriver_wrench = 0x4B8
    scroll = 0x4B9
    scroll_torah = 0x4BA
    sd_card = 0x4BB
    section = 0x4BC
    seedling = 0x4BD
    server = 0x4BE
    shapes = 0x4BF
    share = 0x4C0
    share_from_square = 0x4C1
    share_from_square_outline = 0x4C2
    share_nodes = 0x4C3
    sheet_plastic = 0x4C4
    shekel_sign = 0x4C5
    shield = 0x4C6
    shield_cat = 0x4C7
    shield_dog = 0x4C8
    shield_halved = 0x4C9
    shield_heart = 0x4CA
    shield_virus = 0x4CB
    ship = 0x4CC
    shirt = 0x4CD
    shoe_prints = 0x4CE
    shop = 0x4CF
    shop_lock = 0x4D0
    shop_slash = 0x4D1
    shower = 0x4D2
    shrimp = 0x4D3
    shuffle = 0x4D4
    shuttle_space = 0x4D5
    sign_hanging = 0x4D6
    signal = 0x4D7
    signature = 0x4D8
    signs_post = 0x4D9
    sim_card = 0x4DA
    sink = 0x4DB
    sitemap = 0x4DC
    skull = 0x4DD
    skull_crossbones = 0x4DE
    slash = 0x4DF
    sleigh = 0x4E0
    sliders = 0x4E1
    smog = 0x4E2
    smoking = 0x4E3
    snowflake = 0x4E4
    snowflake_outline = 0x4E5
    snowman = 0x4E6
    snowplow = 0x4E7
    soap = 0x4E8
    socks = 0x4E9
    solar_panel = 0x4EA
    sort = 0x4EB
    sort_down = 0x4EC
    sort_up = 0x4ED
    spa = 0x4EE
    spaghetti_monster_flying = 0x4EF
    spell_check = 0x4F0
    spider = 0x4F1
    spinner = 0x4F2
    splotch = 0x4F3
    spoon = 0x4F4
    spray_can = 0x4F5
    spray_can_sparkles = 0x4F6
    square = 0x4F7
    square_outline = 0x4F8
    square_arrow_up_right = 0x4F9
    square_caret_down = 0x4FA
    square_caret_down_outline = 0x4FB
    square_caret_left = 0x4FC
    square_caret_left_outline = 0x4FD
    square_caret_right = 0x4FE
    square_caret_right_outline = 0x4FF
    square_caret_up = 0x500
    square_caret_up_outline = 0x501
    square_check = 0x502
    square_check_outline = 0x503
    square_envelope = 0x504
    square_full = 0x505
    square_full_outline = 0x506
    square_h = 0x507
    square_minus = 0x508
    square_minus_outline = 0x509
    square_nfi = 0x50A
    square_parking = 0x50B
    square_pen = 0x50C
    square_person_confined = 0x50D
    square_phone = 0x50E
    square_phone_flip = 0x50F
    square_plus = 0x510
    square_plus_outline = 0x511
    square_poll_horizontal = 0x512
    square_poll_vertical = 0x513
    square_root_variable = 0x514
    square_rss = 0x515
    square_share_nodes = 0x516
    square_up_right = 0x517
    square_virus = 0x518
    square_xmark = 0x519
    staff_snake = 0x51A
    stairs = 0x51B
    stamp = 0x51C
    stapler = 0x51D
    star = 0x51E
    star_outline = 0x51F
    star_and_crescent = 0x520
    star_half = 0x521
    star_half_outline = 0x522
    star_half_stroke = 0x523
    star_half_stroke_outline = 0x524
    star_of_david = 0x525
    star_of_life = 0x526
    sterling_sign = 0x527
    stethoscope = 0x528
    stop = 0x529
    stopwatch = 0x52A
    stopwatch_20 = 0x52B
    store = 0x52C
    store_slash = 0x52D
    street_view = 0x52E
    strikethrough = 0x52F
    stroopwafel = 0x530
    subscript = 0x531
    suitcase = 0x532
    suitcase_medical = 0x533
    suitcase_rolling = 0x534
    sun = 0x535
    sun_outline = 0x536
    sun_plant_wilt = 0x537
    superscript = 0x538
    swatchbook = 0x539
    synagogue = 0x53A
    syringe = 0x53B
    t = 0x53C
    table = 0x53D
    table_cells = 0x53E
    table_cells_large = 0x53F
    table_columns = 0x540
    table_list = 0x541
    table_tennis_paddle_ball = 0x542
    tablet = 0x543
    tablet_button = 0x544
    tablet_screen_button = 0x545
    tablets = 0x546
    tachograph_digital = 0x547
    tag = 0x548
    tags = 0x549
    tape = 0x54A
    tarp = 0x54B
    tarp_droplet = 0x54C
    taxi = 0x54D
    teeth = 0x54E
    teeth_open = 0x54F
    temperature_arrow_down = 0x550
    temperature_arrow_up = 0x551
    temperature_empty = 0x552
    temperature_full = 0x553
    temperature_half = 0x554
    temperature_high = 0x555
    temperature_low = 0x556
    temperature_quarter = 0x557
    temperature_three_quarters = 0x558
    tenge_sign = 0x559
    tent = 0x55A
    tent_arrow_down_to_line = 0x55B
    tent_arrow_left_right = 0x55C
    tent_arrow_turn_left = 0x55D
    tent_arrows_down = 0x55E
    tents = 0x55F
    terminal = 0x560
    text_height = 0x561
    text_slash = 0x562
    text_width = 0x563
    thermometer = 0x564
    thumbs_down = 0x565
    thumbs_down_outline = 0x566
    thumbs_up = 0x567
    thumbs_up_outline = 0x568
    thumbtack = 0x569
    ticket = 0x56A
    ticket_simple = 0x56B
    timeline = 0x56C
    toggle_off = 0x56D
    toggle_on = 0x56E
    toilet = 0x56F
    toilet_paper = 0x570
    toilet_paper_slash = 0x571
    toilet_portable = 0x572
    toilets_portable = 0x573
    toolbox = 0x574
    tooth = 0x575
    torii_gate = 0x576
    tornado = 0x577
    tower_broadcast = 0x578
    tower_cell = 0x579
    tower_observation = 0x57A
    tractor = 0x57B
    trademark = 0x57C
    traffic_light = 0x57D
    trailer = 0x57E
    train = 0x57F
    train_subway = 0x580
    train_tram = 0x581
    transgender = 0x582
    trash = 0x583
    trash_arrow_up = 0x584
    trash_can = 0x585
    trash_can_outline = 0x586
    trash_can_arrow_up = 0x587
    tree = 0x588
    tree_city = 0x589
    triangle_exclamation = 0x58A
    trophy = 0x58B
    trowel = 0x58C
    trowel_bricks = 0x58D
    truck = 0x58E
    truck_arrow_right = 0x58F
    truck_droplet = 0x590
    truck_fast = 0x591
    truck_field = 0x592
    truck_field_un = 0x593
    truck_front = 0x594
    truck_medical = 0x595
    truck_monster = 0x596
    truck_moving = 0x597
    truck_pickup = 0x598
    truck_plane = 0x599
    truck_ramp_box = 0x59A
    tty = 0x59B
    turkish_lira_sign = 0x59C
    turn_down = 0x59D
    turn_up = 0x59E
    tv = 0x59F
    u = 0x5A0
    umbrella = 0x5A1
    umbrella_beach = 0x5A2
    underline = 0x5A3
    universal_access = 0x5A4
    unlock = 0x5A5
    unlock_keyhole = 0x5A6
    up_down = 0x5A7
    up_down_left_right = 0x5A8
    up_long = 0x5A9
    up_right_and_down_left_from_center = 0x5AA
    up_right_from_square = 0x5AB
    upload = 0x5AC
    user = 0x5AD
    user_outline = 0x5AE
    user_astronaut = 0x5AF
    user_check = 0x5B0
    user_clock = 0x5B1
    user_doctor = 0x5B2
    user_gear = 0x5B3
    user_graduate = 0x5B4
    user_group = 0x5B5
    user_injured = 0x5B6
    user_large = 0x5B7
    user_large_slash = 0x5B8
    user_lock = 0x5B9
    user_minus = 0x5BA
    user_ninja = 0x5BB
    user_nurse = 0x5BC
    user_pen = 0x5BD
    user_plus = 0x5BE
    user_secret = 0x5BF
    user_shield = 0x5C0
    user_slash = 0x5C1
    user_tag = 0x5C2
    user_tie = 0x5C3
    user_xmark = 0x5C4
    users = 0x5C5
    users_between_lines = 0x5C6
    users_gear = 0x5C7
    users_line = 0x5C8
    users_rays = 0x5C9
    users_rectangle = 0x5CA
    users_slash = 0x5CB
    users_viewfinder = 0x5CC
    utensils = 0x5CD
    v = 0x5CE
    van_shuttle = 0x5CF
    vault = 0x5D0
    vector_square = 0x5D1
    venus = 0x5D2
    venus_double = 0x5D3
    venus_mars = 0x5D4
    vest = 0x5D5
    vest_patches = 0x5D6
    vial = 0x5D7
    vial_circle_check = 0x5D8
    vial_virus = 0x5D9
    vials = 0x5DA
    video = 0x5DB
    video_slash = 0x5DC
    vihara = 0x5DD
    virus = 0x5DE
    virus_covid = 0x5DF
    virus_covid_slash = 0x5E0
    virus_slash = 0x5E1
    viruses = 0x5E2
    voicemail = 0x5E3
    volcano = 0x5E4
    volleyball = 0x5E5
    volume_high = 0x5E6
    volume_low = 0x5E7
    volume_off = 0x5E8
    volume_xmark = 0x5E9
    vr_cardboard = 0x5EA
    w = 0x5EB
    walkie_talkie = 0x5EC
    wallet = 0x5ED
    wand_magic = 0x5EE
    wand_magic_sparkles = 0x5EF
    wand_sparkles = 0x5F0
    warehouse = 0x5F1
    water = 0x5F2
    water_ladder = 0x5F3
    wave_square = 0x5F4
    weight_hanging = 0x5F5
    weight_scale = 0x5F6
    wheat_awn = 0x5F7
    wheat_awn_circle_exclamation = 0x5F8
    wheelchair = 0x5F9
    wheelchair_move = 0x5FA
    whiskey_glass = 0x5FB
    wifi = 0x5FC
    wind = 0x5FD
    window_maximize = 0x5FE
    window_maximize_outline = 0x5FF
    window_minimize = 0x600
    window_minimize_outline = 0x601
    window_restore = 0x602
    window_restore_outline = 0x603
    wine_bottle = 0x604
    wine_glass = 0x605
    wine_glass_empty = 0x606
    won_sign = 0x607
    worm = 0x608
    wrench = 0x609
    x = 0x60A
    x_ray = 0x60B
    xmark = 0x60C
    xmarks_lines = 0x60D
    y = 0x60E
    yen_sign = 0x60F
    yin_yang = 0x610
    z = 0x611


class cTkGraphicsDetailTypes(IntEnum):
    Low = 0x0
    Medium = 0x1
    High = 0x2
    Ultra = 0x3


class cTkEngineSettingTypes(IntEnum):
    FullScreen = 0x0
    Borderless = 0x1
    ResolutionWidth = 0x2
    ResolutionHeight = 0x3
    ResolutionScale = 0x4
    RetinaScaleIOS = 0x5
    Monitor = 0x6
    FoVOnFoot = 0x7
    FoVInShip = 0x8
    VSync = 0x9
    TextureQuality = 0xA
    AnimationQuality = 0xB
    ShadowQuality = 0xC
    ReflectionProbesMultiplier = 0xD
    ReflectionProbes = 0xE
    ScreenSpaceReflections = 0xF
    ReflectionsQuality = 0x10
    PostProcessingEffects = 0x11
    VolumetricsQuality = 0x12
    TerrainTessellation = 0x13
    PlanetQuality = 0x14
    WaterQuality = 0x15
    BaseQuality = 0x16
    UIQuality = 0x17
    DLSSQuality = 0x18
    FFXSRQuality = 0x19
    FFXSR2Quality = 0x1A
    XESSQuality = 0x1B
    DynamicResScaling = 0x1C
    EnableTessellation = 0x1D
    AntiAliasing = 0x1E
    AnisotropyLevel = 0x1F
    Brightness = 0x20
    VignetteAndScanlines = 0x21
    AvailableMonitors = 0x22
    MaxFrameRate = 0x23
    NumLowThreads = 0x24
    NumHighThreads = 0x25
    NumGraphicsThreads = 0x26
    TextureStreaming = 0x27
    TexturePageSizeKb = 0x28
    MotionBlurStrength = 0x29
    ShowRequirementsWarnings = 0x2A
    AmbientOcclusion = 0x2B
    MaxTextureMemoryMb = 0x2C
    FixedTextureMemory = 0x2D
    UseArbSparseTexture = 0x2E
    UseTerrainTextureCache = 0x2F
    AdapterIndex = 0x30
    UseHDR = 0x31
    MinGPUMode = 0x32
    MetalFXQuality = 0x33
    DLSSFrameGeneration = 0x34
    NVIDIAReflexLowLatency = 0x35


class cTkVolumeTriggerType(IntEnum):
    Open = 0x0
    GenericInterior = 0x1
    GenericGlassInterior = 0x2
    Corridor = 0x3
    SmallRoom = 0x4
    LargeRoom = 0x5
    OpenCovered = 0x6
    HazardProtection = 0x7
    Dungeon = 0x8
    FieldBoundary = 0x9
    Custom_Biodome = 0xA
    Portal = 0xB
    VehicleBoost = 0xC
    NexusPlaza = 0xD
    NexusCommunityHub = 0xE
    NexusHangar = 0xF
    RaceObstacle = 0x10
    HazardProtectionCold = 0x11
    SpaceStorm = 0x12
    HazardProtectionNoRecharge = 0x13
    HazardProtectionSpook = 0x14
    ForceJetpackIgnition = 0x15


class cTkCurveType(IntEnum):
    Linear = 0x0
    SmoothInOut = 0x1
    FastInSlowOut = 0x2
    BellSquared = 0x3
    Squared = 0x4
    Cubed = 0x5
    Logarithmic = 0x6
    SlowIn = 0x7
    SlowOut = 0x8
    ReallySlowOut = 0x9
    SmootherStep = 0xA
    SmoothFastInSlowOut = 0xB
    SmoothSlowInFastOut = 0xC
    EaseInSine = 0xD
    EaseOutSine = 0xE
    EaseInOutSine = 0xF
    EaseInQuad = 0x10
    EaseOutQuad = 0x11
    EaseInOutQuad = 0x12
    EaseInQuart = 0x13
    EaseOutQuart = 0x14
    EaseInOutQuart = 0x15
    EaseInQuint = 0x16
    EaseOutQuint = 0x17
    EaseInOutQuint = 0x18
    EaseInExpo = 0x19
    EaseOutExpo = 0x1A
    EaseInOutExpo = 0x1B
    EaseInCirc = 0x1C
    EaseOutCirc = 0x1D
    EaseInOutCirc = 0x1E
    EaseInBack = 0x1F
    EaseOutBack = 0x20
    EaseInOutBack = 0x21
    EaseInElastic = 0x22
    EaseOutElastic = 0x23
    EaseInOutElastic = 0x24
    EaseInBounce = 0x25
    EaseOutBounce = 0x26
    EaseInOutBounce = 0x27


class cTkAnimStateMachineBlendTimeMode(IntEnum):
    Normalised = 0x0
    Seconds = 0x1


class cTkAnimBlendType(IntEnum):
    Normal = 0x0
    MatchTimes = 0x1
    MatchTimesAndPhase = 0x2
    OffsetByBlendTime = 0x3


class cGcWonderType(IntEnum):
    Treasure = 0x0
    WeirdBasePart = 0x1
    Planet = 0x2
    Creature = 0x3
    Flora = 0x4
    Mineral = 0x5
    Custom = 0x6


class cGcWonderTreasureCategory(IntEnum):
    Loot = 0x0
    Document = 0x1
    BioSample = 0x2
    Fossil = 0x3
    Plant = 0x4
    Tool = 0x5
    Farm = 0x6
    SeaLoot = 0x7
    SeaHorror = 0x8
    Salvage = 0x9
    Bones = 0xA
    SpaceHorror = 0xB
    SpaceBones = 0xC


class cGcWonderWeirdBasePartCategory(IntEnum):
    EngineOrb = 0x0
    BeamStone = 0x1
    BubbleCluster = 0x2
    MedGeometric = 0x3
    Shard = 0x4
    StarJoint = 0x5
    BoneGarden = 0x6
    ContourPod = 0x7
    HydroPod = 0x8
    ShellWhite = 0x9
    WeirdCube = 0xA


class cGcWonderCreatureCategory(IntEnum):
    HerbivoreSizeMax = 0x0
    HerbivoreSizeMin = 0x1
    CarnivoreSizeMax = 0x2
    CarnivoreSizeMin = 0x3
    IntelligenceMax = 0x4
    ViciousnessMax = 0x5
    Hot = 0x6
    Cold = 0x7
    Tox = 0x8
    Rad = 0x9
    Weird = 0xA
    Water = 0xB
    Robot = 0xC
    Flyer = 0xD
    Cave = 0xE


class cGcWonderCustomCategory(IntEnum):
    Custom01 = 0x0
    Custom02 = 0x1
    Custom03 = 0x2
    Custom04 = 0x3
    Custom05 = 0x4
    Custom06 = 0x5
    Custom07 = 0x6
    Custom08 = 0x7
    Custom09 = 0x8
    Custom10 = 0x9
    Custom11 = 0xA
    Custom12 = 0xB


class cGcWonderFloraCategory(IntEnum):
    GeneralFact0 = 0x0
    GeneralFact1 = 0x1
    GeneralFact2 = 0x2
    GeneralFact3 = 0x3
    ColdFact = 0x4
    HotFact = 0x5
    RadFact = 0x6
    ToxFact = 0x7


class cGcWonderMineralCategory(IntEnum):
    GeneralFact0 = 0x0
    GeneralFact1 = 0x1
    GeneralFact2 = 0x2
    MetalFact = 0x3
    ColdFact = 0x4
    HotFact = 0x5
    RadFact = 0x6
    ToxFact = 0x7


class cGcWonderPlanetCategory(IntEnum):
    TemperatureMax = 0x0
    TemperatureMin = 0x1
    ToxicityMax = 0x2
    RadiationMax = 0x3
    AnomalyMax = 0x4
    RadiusMax = 0x5
    RadiusMin = 0x6
    AltitudeReachedMax = 0x7
    AltitudeReachedMin = 0x8
    PerfectionMax = 0x9
    PerfectionMin = 0xA


class cGcWikiTopicType(IntEnum):
    Substances = 0x0
    CustomSubstanceList = 0x1
    Products = 0x2
    CustomProductList = 0x3
    CustomItemList = 0x4
    Technologies = 0x5
    CustomTechnologyList = 0x6
    BuildableTech = 0x7
    Construction = 0x8
    TradeCommodities = 0x9
    Curiosities = 0xA
    Cooking = 0xB
    Fish = 0xC
    StoneRunes = 0xD
    Words = 0xE
    RecipesAll = 0xF
    RecipesCooker = 0x10
    RecipesRefiner1 = 0x11
    RecipesRefiner2 = 0x12
    RecipesRefiner3 = 0x13
    Guide = 0x14
    Stories = 0x15
    TreasureWonders = 0x16
    WeirdBasePartWonders = 0x17
    PlanetWonders = 0x18
    CreatureWonders = 0x19
    FloraWonders = 0x1A
    MineralWonders = 0x1B
    CustomWonders = 0x1C
    ExhibitBones = 0x1D
    DebugSweep = 0x1E


class cGcLaunchFuelCostDifficultyOption(IntEnum):
    Free = 0x0
    Low = 0x1
    Normal = 0x2
    High = 0x3


class cGcNPCPopulationDifficultyOption(IntEnum):
    Full = 0x0
    Abandoned = 0x1


class cGcOptionsUIHeaderIcons(IntEnum):
    General = 0x0
    Ship = 0x1
    Cog = 0x2
    Scanner = 0x3
    Advanced = 0x4
    Cloud = 0x5


class cGcReputationGainDifficultyOption(IntEnum):
    VeryFast = 0x0
    Fast = 0x1
    Normal = 0x2
    Slow = 0x3


class cGcScannerRechargeDifficultyOption(IntEnum):
    VeryFast = 0x0
    Fast = 0x1
    Normal = 0x2
    Slow = 0x3


class cGcSprintingCostDifficultyOption(IntEnum):
    Free = 0x0
    Low = 0x1
    Full = 0x2


class cGcSubstanceCollectionDifficultyOption(IntEnum):
    High = 0x0
    Normal = 0x1
    Low = 0x2


class cGcHazardDrainDifficultyOption(IntEnum):
    Slow = 0x0
    Normal = 0x1
    Fast = 0x2


class cGcInventoryStackLimitsDifficultyOption(IntEnum):
    High = 0x0
    Normal = 0x1
    Low = 0x2


class cGcItemShopAvailabilityDifficultyOption(IntEnum):
    High = 0x0
    Normal = 0x1
    Low = 0x2


class cGcDifficultyOptionGroups(IntEnum):
    Survival = 0x0
    Crafting = 0x1
    Combat = 0x2
    Ease = 0x3


class cGcDifficultySettingEnum(IntEnum):
    SettingsLocked = 0x0
    InventoriesAlwaysInRange = 0x1
    AllSlotsUnlocked = 0x2
    WarpDriveRequirements = 0x3
    CraftingIsFree = 0x4
    TutorialEnabled = 0x5
    StartWithAllItemsKnown = 0x6
    BaseAutoPower = 0x7
    DeathConsequences = 0x8
    DamageReceived = 0x9
    DamageGiven = 0xA
    ActiveSurvivalBars = 0xB
    HazardDrain = 0xC
    EnergyDrain = 0xD
    SubstanceCollection = 0xE
    InventoryStackLimits = 0xF
    ChargingRequirements = 0x10
    FuelUse = 0x11
    LaunchFuelCost = 0x12
    CurrencyCost = 0x13
    ScannerRecharge = 0x14
    ReputationGain = 0x15
    CreatureHostility = 0x16
    SpaceCombat = 0x17
    GroundCombat = 0x18
    ItemShopAvailablity = 0x19
    SprintingCost = 0x1A
    BreakTechOnDamage = 0x1B
    Fishing = 0x1C
    NPCPopulation = 0x1D


class cGcDifficultyPresetType(IntEnum):
    Invalid = 0x0
    Custom = 0x1
    Normal = 0x2
    Creative = 0x3
    Relaxed = 0x4
    Survival = 0x5
    Permadeath = 0x6


class cGcDifficultySettingType(IntEnum):
    Toggle = 0x0
    OptionList = 0x1


class cGcDifficultySettingEditability(IntEnum):
    FullyEditable = 0x0
    IncreaseOnly = 0x1
    DecreaseOnly = 0x2
    LockedVisible = 0x3
    LockedHidden = 0x4


class cGcEnergyDrainDifficultyOption(IntEnum):
    Slow = 0x0
    Normal = 0x1
    Fast = 0x2


class cGcFuelUseDifficultyOption(IntEnum):
    Free = 0x0
    Cheap = 0x1
    Normal = 0x2
    Expensive = 0x3


class cGcFishingDifficultyOption(IntEnum):
    AutoCatch = 0x0
    LongCatchWindow = 0x1
    NormalCatchWindow = 0x2
    ShortCatchWindow = 0x3


class cGcQuickMenuActions(IntEnum):
    None_ = 0x0
    CallFreighter = 0x1
    DismissFreighter = 0x2
    SummonNexus = 0x3
    CallShip = 0x4
    CallRecoveryShip = 0x5
    CallSquadron = 0x6
    SummonVehicleSubMenu = 0x7
    SummonBuggy = 0x8
    SummonBike = 0x9
    SummonTruck = 0xA
    SummonWheeledBike = 0xB
    SummonHovercraft = 0xC
    SummonSubmarine = 0xD
    SummonMech = 0xE
    VehicleAIToggle = 0xF
    VehicleScan = 0x10
    VehicleScanSelect = 0x11
    VehicleRestartRace = 0x12
    Torch = 0x13
    GalaxyMap = 0x14
    PhotoMode = 0x15
    ChargeMenu = 0x16
    Charge = 0x17
    ChargeSubMenu = 0x18
    Repair = 0x19
    BuildMenu = 0x1A
    CommunicatorReceive = 0x1B
    CommunicatorInitiate = 0x1C
    ThirdPersonCharacter = 0x1D
    ThirdPersonShip = 0x1E
    ThirdPersonVehicle = 0x1F
    EconomyScan = 0x20
    EmoteMenu = 0x21
    Emote = 0x22
    UtilitySubMenu = 0x23
    SummonSubMenu = 0x24
    SummonShipSubMenu = 0x25
    ChangeSecondaryWeaponMenu = 0x26
    ChangeSecondaryWeapon = 0x27
    ChooseCreatureFoodMenu = 0x28
    ChooseCreatureFood = 0x29
    EmergencyWarp = 0x2A
    SwapMultitool = 0x2B
    SwapMultitoolSubMenu = 0x2C
    CreatureSubMenu = 0x2D
    SummonPet = 0x2E
    SummonPetSubMenu = 0x2F
    WarpToNexus = 0x30
    PetUI = 0x31
    ByteBeatSubMenu = 0x32
    ByteBeatPlay = 0x33
    ByteBeatStop = 0x34
    ByteBeatLibrary = 0x35
    ReportBase = 0x36
    CargoShield = 0x37
    CallRocket = 0x38
    SummonSkiff = 0x39
    FishBaitBox = 0x3A
    FoodUnit = 0x3B
    SettlementOverview = 0x3C
    CorvetteEject = 0x3D
    CorvetteAutoPilotMenu = 0x3E
    CorvetteAutoPilot = 0x3F
    Invalid = 0x40


class cGcHotActionMenuTypes(IntEnum):
    OnFoot = 0x0
    InShip = 0x1
    InExocraft = 0x2


class cGcActiveSurvivalBarsDifficultyOption(IntEnum):
    None_ = 0x0
    HealthOnly = 0x1
    HealthAndHazard = 0x2
    All = 0x3


class cGcBreakTechOnDamageDifficultyOption(IntEnum):
    None_ = 0x0
    Low = 0x1
    High = 0x2


class cGcChargingRequirementsDifficultyOption(IntEnum):
    None_ = 0x0
    Low = 0x1
    Normal = 0x2
    High = 0x3


class cGcShipWeapons(IntEnum):
    Laser = 0x0
    Projectile = 0x1
    Shotgun = 0x2
    Minigun = 0x3
    Plasma = 0x4
    Missile = 0x5
    Rocket = 0x6


class cGcCombatTimerDifficultyOption(IntEnum):
    Off = 0x0
    Slow = 0x1
    Normal = 0x2
    Fast = 0x3


class cGcCreatureHostilityDifficultyOption(IntEnum):
    NeverAttack = 0x0
    AttackIfProvoked = 0x1
    FullEcosystem = 0x2


class cGcCurrencyCostDifficultyOption(IntEnum):
    Free = 0x0
    Cheap = 0x1
    Normal = 0x2
    Expensive = 0x3


class cGcDamageGivenDifficultyOption(IntEnum):
    High = 0x0
    Normal = 0x1
    Low = 0x2


class cGcDamageReceivedDifficultyOption(IntEnum):
    None_ = 0x0
    Low = 0x1
    Normal = 0x2
    High = 0x3


class cGcDeathConsequencesDifficultyOption(IntEnum):
    None_ = 0x0
    ItemGrave = 0x1
    DestroyItems = 0x2
    DestroySave = 0x3


class cGcAIShipWeapons(IntEnum):
    Projectile = 0x0
    Laser = 0x1
    MiningLaser = 0x2


class cGcVehicleWeaponMode(IntEnum):
    Laser = 0x0
    Gun = 0x1
    TerrainEdit = 0x2
    StunGun = 0x3
    Flamethrower = 0x4


class cGcPlayerWeaponClass(IntEnum):
    None_ = 0x0
    Projectile = 0x1
    ChargedProjectile = 0x2
    Laser = 0x3
    Grenade = 0x4
    Utility = 0x5
    TerrainEditor = 0x6
    Spawner = 0x7
    SpawnerAlt = 0x8
    Fishing = 0x9


class cGcVehicleType(IntEnum):
    Buggy = 0x0
    Bike = 0x1
    Truck = 0x2
    WheeledBike = 0x3
    Hovercraft = 0x4
    Submarine = 0x5
    Mech = 0x6


class cGcRemoteWeapons(IntEnum):
    Laser = 0x0
    VehicleLaser = 0x1
    AIMechLaser = 0x2
    ShipLaser = 0x3
    ShipLaser2 = 0x4
    RailLaser = 0x5
    NumLasers = 0x6
    BoltCaster = 0x7
    Shotgun = 0x8
    Cannon = 0x9
    Burst = 0xA
    Flamethrower = 0xB
    MineGrenade = 0xC
    BounceGrenade = 0xD
    StunGrenade = 0xE
    VehicleCanon = 0xF
    AIMechCanon = 0x10
    ShipPhoton = 0x11
    ShipShotgun = 0x12
    ShipMinigun = 0x13
    ShipPlasma = 0x14
    ShipRocket = 0x15
    None_ = 0x16


class cGcPlayerWeapons(IntEnum):
    Bolt = 0x0
    Shotgun = 0x1
    Burst = 0x2
    Rail = 0x3
    Cannon = 0x4
    Laser = 0x5
    Grenade = 0x6
    MineGrenade = 0x7
    Scope = 0x8
    FrontShield = 0x9
    Melee = 0xA
    TerrainEdit = 0xB
    SunLaser = 0xC
    Spawner = 0xD
    SpawnerAlt = 0xE
    SoulLaser = 0xF
    Flamethrower = 0x10
    StunGrenade = 0x11
    Stealth = 0x12
    FishLaser = 0x13


class cGcMechMeshPart(IntEnum):
    Scanner = 0x0
    Body = 0x1
    Legs = 0x2
    LeftArm = 0x3
    RightArm = 0x4


class cGcMechMeshType(IntEnum):
    Exocraft = 0x0
    Sentinel = 0x1
    BugHunter = 0x2
    Stone = 0x3


class cGcMechWeaponLocation(IntEnum):
    TurretExocraft = 0x0
    TurretSentinel = 0x1
    ArmLeft = 0x2
    ArmRight = 0x3
    FlameThrower = 0x4


class cGcShipMessage(IntEnum):
    Leave = 0x0
    Fight = 0x1


class cGcShipDialogueTreeEnum(IntEnum):
    Bribe = 0x0
    Beg = 0x1
    Ambush = 0x2
    Trade = 0x3
    Help = 0x4
    Goods = 0x5
    Hostile = 0x6


class cGcAISpaceshipRoles(IntEnum):
    Standard = 0x0
    PlayerSquadron = 0x1
    Freighter = 0x2
    CapitalFreighter = 0x3
    SmallFreighter = 0x4
    TinyFreighter = 0x5
    Frigate = 0x6
    Biggs = 0x7


class cGcAISpaceshipTypes(IntEnum):
    None_ = 0x0
    Pirate = 0x1
    Police = 0x2
    Trader = 0x3
    Freighter = 0x4
    PlayerSquadron = 0x5
    DefenceForce = 0x6


class cGcWaterEmissionBehaviourType(IntEnum):
    None_ = 0x0
    Constant = 0x1
    Pulse = 0x2
    NightOnly = 0x3


class cGcWealthClass(IntEnum):
    Poor = 0x0
    Average = 0x1
    Wealthy = 0x2
    Pirate = 0x3


class cGcTradingClass(IntEnum):
    Mining = 0x0
    HighTech = 0x1
    Trading = 0x2
    Manufacturing = 0x3
    Fusion = 0x4
    Scientific = 0x5
    PowerGeneration = 0x6


class cGcRainbowType(IntEnum):
    Always = 0x0
    Occasional = 0x1
    Storm = 0x2
    None_ = 0x3


class cGcPlayerConflictData(IntEnum):
    Low = 0x0
    Default = 0x1
    High = 0x2
    Pirate = 0x3


class cGcSolarSystemClass(IntEnum):
    Default = 0x0
    Initial = 0x1
    Anomaly = 0x2
    GameStart = 0x3


class cGcPlanetSize(IntEnum):
    Large = 0x0
    Medium = 0x1
    Small = 0x2
    Moon = 0x3
    Giant = 0x4


class cGcPlanetClass(IntEnum):
    Default = 0x0
    Initial = 0x1
    InInitialSystem = 0x2


class cGcPlanetSentinelLevel(IntEnum):
    Low = 0x0
    Default = 0x1
    Aggressive = 0x2
    Corrupt = 0x3


class cGcBiomeType(IntEnum):
    Lush = 0x0
    Toxic = 0x1
    Scorched = 0x2
    Radioactive = 0x3
    Frozen = 0x4
    Barren = 0x5
    Dead = 0x6
    Weird = 0x7
    Red = 0x8
    Green = 0x9
    Blue = 0xA
    Test = 0xB
    Swamp = 0xC
    Lava = 0xD
    Waterworld = 0xE
    GasGiant = 0xF
    All = 0x10


class cGcBiomeSubType(IntEnum):
    None_ = 0x0
    Standard = 0x1
    HighQuality = 0x2
    Structure = 0x3
    Beam = 0x4
    Hexagon = 0x5
    FractCube = 0x6
    Bubble = 0x7
    Shards = 0x8
    Contour = 0x9
    Shell = 0xA
    BoneSpire = 0xB
    WireCell = 0xC
    HydroGarden = 0xD
    HugePlant = 0xE
    HugeLush = 0xF
    HugeRing = 0x10
    HugeRock = 0x11
    HugeScorch = 0x12
    HugeToxic = 0x13
    Variant_A = 0x14
    Variant_B = 0x15
    Variant_C = 0x16
    Variant_D = 0x17
    Infested = 0x18
    Swamp = 0x19
    Lava = 0x1A
    Worlds = 0x1B
    Remix_A = 0x1C
    Remix_B = 0x1D
    Remix_C = 0x1E
    Remix_D = 0x1F


class cGcSolarSystemLocatorTypes(IntEnum):
    Generic1 = 0x0
    Generic2 = 0x1
    Generic3 = 0x2
    Generic4 = 0x3


class cGcSentinelQuadWeaponMode(IntEnum):
    Laser = 0x0
    MiniCannon = 0x1
    Grenades = 0x2
    Flamethrower = 0x3


class cGcSentinelTypes(IntEnum):
    PatrolDrone = 0x0
    CombatDrone = 0x1
    MedicDrone = 0x2
    SummonerDrone = 0x3
    CorruptedDrone = 0x4
    Quad = 0x5
    SpiderQuad = 0x6
    SpiderQuadMini = 0x7
    Mech = 0x8
    Walker = 0x9
    FriendlyDrone = 0xA
    StoneMech = 0xB
    StoneFloater = 0xC


class cGcDroneTypes(IntEnum):
    Patrol = 0x0
    Combat = 0x1
    Corrupted = 0x2


class cGcProjectileImpactType(IntEnum):
    Default = 0x0
    Terrain = 0x1
    Substance = 0x2
    Rock = 0x3
    Asteroid = 0x4
    Shield = 0x5
    Creature = 0x6
    Robot = 0x7
    Freighter = 0x8
    Cargo = 0x9
    Ship = 0xA
    Plant = 0xB
    NeedsTech = 0xC
    Player = 0xD
    OtherPlayer = 0xE
    SentinelShield = 0xF
    SpaceshipShield = 0x10
    FreighterShield = 0x11


class cGcPlayerSurvivalBarType(IntEnum):
    Health = 0x0
    Hazard = 0x1
    Energy = 0x2


class cGcScanType(IntEnum):
    Tool = 0x0
    Beacon = 0x1
    RadioTower = 0x2
    Observatory = 0x3
    DistressSignal = 0x4
    Waypoint = 0x5
    Ship = 0x6
    DebugPlanet = 0x7
    DebugSpace = 0x8
    VisualOnly = 0x9
    VisualOnlyAerial = 0xA


class cGcDamageType(IntEnum):
    Gun = 0x0
    Laser = 0x1
    Shotgun = 0x2
    Burst = 0x3
    Rail = 0x4
    Cannon = 0x5
    Explosion = 0x6
    Melee = 0x7
    ShipGun = 0x8
    ShipLaser = 0x9
    ShipShotgun = 0xA
    ShipMinigun = 0xB
    ShipRockets = 0xC
    ShipPlasma = 0xD
    VehicleGun = 0xE
    VehicleLaser = 0xF
    SentinelLaser = 0x10
    PlayerDamage = 0x11
    PlayerWeapons = 0x12
    ShipWeapons = 0x13
    VehicleWeapons = 0x14
    CombatEffects = 0x15
    Fiend = 0x16
    FreighterLaser = 0x17
    FreighterTorpedo = 0x18


class cGcPlayerHazardType(IntEnum):
    None_ = 0x0
    NoOxygen = 0x1
    ExtremeHeat = 0x2
    ExtremeCold = 0x3
    ToxicGas = 0x4
    Radiation = 0x5
    Spook = 0x6


class cGcPhotoShip(IntEnum):
    Freighter = 0x0
    Dropship = 0x1
    Fighter = 0x2
    Scientific = 0x3
    Shuttle = 0x4
    PlayerFreighter = 0x5
    Royal = 0x6
    Alien = 0x7
    Sail = 0x8
    Robot = 0x9
    Corvette = 0xA


class cGcHand(IntEnum):
    Right = 0x0
    Left = 0x1


class cGcHandType(IntEnum):
    Offhand = 0x0
    Dominant = 0x1


class cGcMovementDirection(IntEnum):
    WorldRelative = 0x0
    BodyRelative = 0x1
    HeadRelative = 0x2
    NotSet = 0x3


class cGcPlayerCharacterStateType(IntEnum):
    Idle = 0x0
    Jog = 0x1
    JogUphill = 0x2
    JogDownhill = 0x3
    SteepSlope = 0x4
    Sliding = 0x5
    Run = 0x6
    Airborne = 0x7
    JetpackBoost = 0x8
    RocketBoots = 0x9
    Riding = 0xA
    Swimming = 0xB
    SwimmingJetpack = 0xC
    Death = 0xD
    FullBodyOverride = 0xE
    Spacewalk = 0xF
    SpacewalkAtmosphere = 0x10
    LowGWalk = 0x11
    LowGRun = 0x12
    Fishing = 0x13


class cGcPhotoBuilding(IntEnum):
    Shelter = 0x0
    Abandoned = 0x1
    Shop = 0x2
    Outpost = 0x3
    RadioTower = 0x4
    Observatory = 0x5
    Depot = 0x6
    Monolith = 0x7
    Factory = 0x8
    Portal = 0x9
    Ruin = 0xA
    MissionTower = 0xB
    LargeBuilding = 0xC


class cGcPhotoCreature(IntEnum):
    Ground = 0x0
    Water = 0x1
    Air = 0x2


class cGcPhotoPlant(IntEnum):
    Sodium = 0x0
    Oxygen = 0x1
    BluePlant = 0x2


class cGcNPCSettlementBehaviourState(IntEnum):
    Generic = 0x0
    Sociable = 0x1
    Productive = 0x2
    Tired = 0x3
    Afraid = 0x4


class cGcNPCSettlementBehaviourAreaProperty(IntEnum):
    ContainsPlayer = 0x0
    ContainsNPCs = 0x1


class cGcNPCInteractiveObjectType(IntEnum):
    Idle = 0x0
    Generic = 0x1
    Chair = 0x2
    Conversation = 0x3
    WatchShip = 0x4
    Shop = 0x5
    Dance = 0x6
    None_ = 0x7


class cGcMissionCategory(IntEnum):
    Info = 0x0
    SelectableHint = 0x1
    Mission = 0x2
    Danger = 0x3
    Urgent = 0x4


class cGcMissionConditionTest(IntEnum):
    AnyFalse = 0x0
    AllFalse = 0x1
    AnyTrue = 0x2
    AllTrue = 0x3


class cGcMissionDifficulty(IntEnum):
    Easy = 0x0
    Normal = 0x1
    Hard = 0x2


class cGcMissionFaction(IntEnum):
    Gek = 0x0
    Korvax = 0x1
    Vykeen = 0x2
    TradeGuild = 0x3
    WarriorGuild = 0x4
    ExplorerGuild = 0x5
    Nexus = 0x6
    Pirates = 0x7
    Builders = 0x8
    None_ = 0x9


class cGcMissionGalacticFeature(IntEnum):
    Anomaly = 0x0
    Atlas = 0x1
    BlackHole = 0x2


class cGcMissionGalacticPoint(IntEnum):
    Atlas = 0x0
    BlackHole = 0x1


class cGcMissionPageHint(IntEnum):
    None_ = 0x0
    Suit = 0x1
    Ship = 0x2
    Weapon = 0x3
    Vehicle = 0x4
    Freighter = 0x5
    Wiki = 0x6
    Catalogue = 0x7
    MissionLog = 0x8
    Discovery = 0x9
    Journey = 0xA
    Expedition = 0xB
    Options = 0xC


class cGcMissionType(IntEnum):
    SpaceCombat = 0x0
    GroundCombat = 0x1
    Research = 0x2
    MissingPerson = 0x3
    Repair = 0x4
    Cargo = 0x5
    Piracy = 0x6
    Photo = 0x7
    Feeding = 0x8
    Planting = 0x9
    Construction = 0xA
    LocalCorrupted = 0xB
    LocalCorruptedCombat = 0xC
    LocalSalvage = 0xD
    LocalBiomePlants = 0xE
    LocalExtreme = 0xF
    LocalBones = 0x10
    LocalInfested = 0x11
    LocalPlanetaryPirates = 0x12
    LocalPredators = 0x13
    LocalSentinels = 0x14
    BuildersLanguage = 0x15
    Fishing = 0x16
    CorvetteRobots = 0x17
    CorvetteTreeScanning = 0x18
    CorvettePredators = 0x19
    CorvetteCollectItem = 0x1A
    CorvetteMultiWorld = 0x1B
    CorvetteTreasure = 0x1C
    CorvetteSalvage = 0x1D
    CorvetteFeeding = 0x1E
    CorvetteGroundCombat = 0x1F
    CorvetteFiendKill = 0x20


class cGcSaveContextQuery(IntEnum):
    DontCare = 0x0
    Season = 0x1
    Main = 0x2
    NoSeason = 0x3
    NoMain = 0x4


class cGcScanEventGPSHint(IntEnum):
    None_ = 0x0
    Accurate = 0x1
    OffsetNarrow = 0x2
    OffsetMid = 0x3
    OffsetWide = 0x4
    Obfuscated = 0x5
    PartObfuscated = 0x6
    BuilderCorruption = 0x7


class cGcMonth(IntEnum):
    January = 0x0
    February = 0x1
    March = 0x2
    April = 0x3
    May = 0x4
    June = 0x5
    July = 0x6
    August = 0x7
    September = 0x8
    October = 0x9
    November = 0xA
    December = 0xB


class cGcDay(IntEnum):
    Sunday = 0x0
    Monday = 0x1
    Tuesday = 0x2
    Wednesday = 0x3
    Thursday = 0x4
    Friday = 0x5
    Saturday = 0x6


class cGcInteractionMissionState(IntEnum):
    Unused = 0x0
    Unlocked = 0x1
    MonoCorrupted = 0x2
    GiftGiven = 0x3


class cGcLocalSubstanceType(IntEnum):
    AnyDeposit = 0x0
    Common = 0x1
    Uncommon = 0x2
    Rare = 0x3
    Plant = 0x4


class cGcDefaultMissionProductEnum(IntEnum):
    None_ = 0x0
    PrimaryProduct = 0x1
    SecondaryProduct = 0x2


class cGcDefaultMissionSubstanceEnum(IntEnum):
    None_ = 0x0
    PrimarySubstance = 0x1
    SecondarySubstance = 0x2


class cGcMissionConditionUsingPortal(IntEnum):
    Any = 0x0
    Story = 0x1
    NotStory = 0x2


class cGcMissionConditionUsingThirdPersonCamera(IntEnum):
    OnFoot = 0x0
    Ship = 0x1
    Vehicle = 0x2


class cGcMissionConditionSentinelLevel(IntEnum):
    None_ = 0x0
    Low = 0x1
    Default = 0x2
    Aggressive = 0x3
    Corrupt = 0x4


class cGcMissionConditionShipEngineStatus(IntEnum):
    Thrusting = 0x0
    Braking = 0x1
    Landing = 0x2
    Landed = 0x3
    Boosting = 0x4
    Pulsing = 0x5
    LowFlight = 0x6
    Inverted = 0x7
    EnginesRepaired = 0x8
    PulsingToPlanet = 0x9


class cGcMissionConditionPlatform(IntEnum):
    Undefined = 0x0
    NintendoSwitch = 0x1


class cGcMissionConditionLocation(IntEnum):
    OnPlanet = 0x0
    OnPlanetInVehicle = 0x1
    AnywhereInPlanetAtmos = 0x2
    InShipLanded = 0x3
    InShipInPlanetOrbit = 0x4
    InShipInSpace = 0x5
    OnFootInSpace = 0x6
    OnFootInAnyCorvette = 0x7
    OnFootInYourCorvette = 0x8
    OnFootInOtherPlayerCorvette = 0x9
    OnFootInOtherPlayerCorvetteNotLanded = 0xA
    InShipAnywhere = 0xB
    InSpaceStation = 0xC
    InFreighter = 0xD
    InYourFreighter = 0xE
    InOtherPlayerFreighter = 0xF
    Underground = 0x10
    InBuilding = 0x11
    Frigate = 0x12
    Underwater = 0x13
    UnderwaterSwimming = 0x14
    DeepUnderwater = 0x15
    InSubmarine = 0x16
    Frigate_Damaged = 0x17
    FreighterConstructionArea = 0x18
    FriendsPlanetBase = 0x19
    OnPlanetSurface = 0x1A
    InNexus = 0x1B
    InNexusOnFoot = 0x1C
    AbandonedFreighterExterior = 0x1D
    AbandonedFreighterInterior = 0x1E
    AbandonedFreighterAirlock = 0x1F
    AtlasStation = 0x20
    AtlasStationFinal = 0x21


class cGcMissionConditionIsAbandFreighterDoorOpen(IntEnum):
    DungeonNotReady = 0x0
    Locked = 0x1
    Opening = 0x2
    Open = 0x3


class cGcMissionConditionIsPlayerWeak(IntEnum):
    ShipOrWeapon = 0x0
    Ship = 0x1
    Weapon = 0x2


class cGcMissionConditionHasFreighter(IntEnum):
    DontCare = 0x0
    Yes = 0x1
    No = 0x2


class cGcMissionConditionAbandonedOrEmptySystem(IntEnum):
    Either = 0x0
    Empty = 0x1
    Abandoned = 0x2
    SeasonForcedAbandoned = 0x3


class cGcScanEventTableType(IntEnum):
    Space = 0x0
    Planet = 0x1
    Missions = 0x2
    Tutorial = 0x3
    MissionsCreative = 0x4
    Vehicle = 0x5
    NPCPlanetSite = 0x6
    Seasonal = 0x7


class cGcSpaceshipClasses(IntEnum):
    Freighter = 0x0
    Dropship = 0x1
    Fighter = 0x2
    Scientific = 0x3
    Shuttle = 0x4
    PlayerFreighter = 0x5
    Royal = 0x6
    Alien = 0x7
    Sail = 0x8
    Robot = 0x9
    Corvette = 0xA


class cGcSpaceshipSize(IntEnum):
    empty = 0x0
    Small = 0x1
    Large = 0x2


class cGcWeaponClasses(IntEnum):
    Pistol = 0x0
    Rifle = 0x1
    Pristine = 0x2
    Alien = 0x3
    Royal = 0x4
    Robot = 0x5
    Atlas = 0x6
    AtlasYellow = 0x7
    AtlasBlue = 0x8
    Staff = 0x9


class cGcRegionHotspotTypes(IntEnum):
    empty = 0x0
    Power = 0x1
    Mineral1 = 0x2
    Mineral2 = 0x4
    Mineral3 = 0x8
    Gas1 = 0x10
    Gas2 = 0x20


class cGcPhysicsCollisionGroups(IntEnum):
    Normal = 0x0
    Terrain = 0x1
    TerrainInstance = 0x2
    TerrainActivated = 0x3
    Water = 0x4
    Substance = 0x5
    Asteroid = 0x6
    Player = 0x7
    NetworkPlayer = 0x8
    NPC = 0x9
    Ragdoll = 0xA
    Vehicle = 0xB
    Vehicle_Piloted = 0xC
    Creature = 0xD
    Spaceship = 0xE
    Spaceship_Landing = 0xF
    Debris = 0x10
    Shield = 0x11
    Loot = 0x12
    Trigger = 0x13
    CollidesWithNothing = 0x14
    CollidesWithEverything = 0x15
    DefaultRaycast = 0x16
    Raycast = 0x17
    Raycast_Camera = 0x18
    Raycast_SampleCollisionWithCamera = 0x19
    Raycast_PlayerInteract = 0x1A
    Raycast_PlayerInteract_Shoot = 0x1B
    Raycast_Projectile = 0x1C
    Raycast_LaserBeam = 0x1D
    Raycast_WeaponOfPlayer = 0x1E
    Raycast_WeaponOfAgent = 0x1F
    Raycast_Binoculars = 0x20
    Raycast_TerrainEditingBeam = 0x21
    Raycast_TerrainEditing_OverlappingObjects = 0x22
    Raycast_PlayerClimb = 0x23
    Raycast_PlayerAim = 0x24
    Raycast_PlayerThrow = 0x25
    Raycast_PlayerSpawn = 0x26
    Raycast_ObjectPlacement = 0x27
    Raycast_DroneControl = 0x28
    Raycast_PlanetHeightTest = 0x29
    Raycast_PlanetHeightTestIncludingStructures = 0x2A
    Raycast_LineOfSight = 0x2B
    Raycast_VehicleCanDriveOn = 0x2C
    Raycast_SpaceshipAvoidance = 0x2D
    Raycast_SpaceshipAvoidanceOnLeaving = 0x2E
    Raycast_HudPing = 0x2F
    Raycast_HudPingNoTerrain = 0x30
    Raycast_ObstacleToAgentMovement = 0x31
    Raycast_DebugEditor = 0x32
    Raycast_PlayerIk = 0x33
    Raycast_MechIk = 0x34
    Raycast_CreatureIk = 0x35
    Raycast_CreatureIk_Indoors = 0x36
    Raycast_NavigationLink = 0x37
    Raycast_AiShipAtack = 0x38
    Raycast_AiShipTravel = 0x39
    Raycast_ObstructionQuery = 0x3A
    Raycast_GeometryProbe = 0x3B
    Raycast_DroneTargetSensing_Friendly = 0x3C
    Raycast_DroneTargetSensing_Unfriendly = 0x3D
    Raycast_DroneTargetSensing_Friendly_NoShield = 0x3E
    Raycast_DroneTargetSensing_Unfriendly_NoShield = 0x3F
    Raycast_ObjectPlacementAddObject = 0x40
    Raycast_CatchCreatures = 0x41
    Raycast_CatchNormal = 0x42
    Raycast_CatchTerrain = 0x43
    Raycast_CatchTerrainAndNormal = 0x44
    Raycast_CatchCreatureObstacles = 0x45
    Raycast_SpaceStationShipBuilderCamera = 0x46


class cGcFrigateFlybyType(IntEnum):
    SingleShip = 0x0
    AmbientGroup = 0x1
    ScriptedGroup = 0x2
    DeepSpace = 0x3
    DeepSpaceCommon = 0x4
    GhostShip = 0x5


class cGcItemQuality(IntEnum):
    Junk = 0x0
    Common = 0x1
    Rare = 0x2
    Epic = 0x3
    Legendary = 0x4


class cGcFishSize(IntEnum):
    Small = 0x0
    Medium = 0x1
    Large = 0x2
    ExtraLarge = 0x3


class cGcFishingTime(IntEnum):
    Day = 0x0
    Night = 0x1
    Both = 0x2


class cGcGalaxyWaypointTypes(IntEnum):
    User = 0x0
    Gameplay_AtlasStation = 0x1
    Gameplay_DistressBeacon = 0x2
    Gameplay_BlackHole = 0x3
    Gameplay_Mission = 0x4
    Gameplay_SeasonParty = 0x5


class cGcBuilderPadType(IntEnum):
    NoBuild = 0x0
    ExclusivelyBuild = 0x1
    Hybrid = 0x2


class cGcGalaxyStarAnomaly(IntEnum):
    None_ = 0x0
    AtlasStation = 0x1
    AtlasStationFinal = 0x2
    BlackHole = 0x3
    MiniStation = 0x4


class cGcGalaxyStarTypes(IntEnum):
    Yellow = 0x0
    Green = 0x1
    Blue = 0x2
    Red = 0x3
    Purple = 0x4


class cGcGalaxyMarkerTypes(IntEnum):
    StartingLocation = 0x0
    Home = 0x1
    Waypoint = 0x2
    Contact = 0x3
    Blackhole = 0x4
    AtlasStation = 0x5
    Selection = 0x6
    PlanetBase = 0x7
    Visited = 0x8
    ScanEvent = 0x9
    Expedition = 0xA
    NetworkPlayer = 0xB
    Freighter = 0xC
    PathIcon = 0xD
    SeasonParty = 0xE
    Settlement = 0xF


class cGcWFCDecorationTheme(IntEnum):
    Default = 0x0
    Construction = 0x1
    Upgrade1 = 0x2
    Upgrade2 = 0x3
    Upgrade3 = 0x4


class cGcWeatherOptions(IntEnum):
    Clear = 0x0
    Dust = 0x1
    Humid = 0x2
    Snow = 0x3
    Toxic = 0x4
    Scorched = 0x5
    Radioactive = 0x6
    RedWeather = 0x7
    GreenWeather = 0x8
    BlueWeather = 0x9
    Swamp = 0xA
    Lava = 0xB
    Bubble = 0xC
    Weird = 0xD
    Fire = 0xE
    ClearCold = 0xF
    GasGiant = 0x10


class cGcHazardModifiers(IntEnum):
    Temperature = 0x0
    Toxicity = 0x1
    Radiation = 0x2
    LifeSupportDrain = 0x3
    Gravity = 0x4
    SpookLevel = 0x5


class cGcHazardValueTypes(IntEnum):
    Ambient = 0x0
    Water = 0x1
    Cave = 0x2
    Storm = 0x3
    Night = 0x4
    DeepWater = 0x5


class cGcObjectPlacementCategory(IntEnum):
    None_ = 0x0
    ResourceSmall = 0x1
    ResourceMedium = 0x2
    ResourceLarge = 0x3
    ResourceDebris = 0x4


class cGcTerrainTileType(IntEnum):
    Air = 0x0
    Base = 0x1
    Rock = 0x2
    Mountain = 0x3
    Underwater = 0x4
    Cave = 0x5
    Dirt = 0x6
    Liquid = 0x7
    Substance = 0x8


class cGcPlanetLife(IntEnum):
    Dead = 0x0
    Low = 0x1
    Mid = 0x2
    Full = 0x3


class cGcResourceOrigin(IntEnum):
    Terrain = 0x0
    Crystal = 0x1
    Asteroid = 0x2
    Robot = 0x3
    Depot = 0x4


class cGcMarkerType(IntEnum):
    Default = 0x0
    PlanetPoleNorth = 0x1
    PlanetPoleSouth = 0x2
    PlanetPoleEast = 0x3
    PlanetPoleWest = 0x4
    BaseBuildingMarkerBeacon = 0x5
    TerrainResource = 0x6
    Object = 0x7
    Tagged = 0x8
    TaggedPlanet = 0x9
    Unknown = 0xA
    Ship = 0xB
    Corvette = 0xC
    Freighter = 0xD
    NetworkPlayerFireTeamFreighter = 0xE
    FreighterBase = 0xF
    PlayerFreighter = 0x10
    PlayerSettlement = 0x11
    DamagedFrigate = 0x12
    Bounty = 0x13
    PlanetRaid = 0x14
    Battle = 0x15
    SpaceSignal = 0x16
    BlackHole = 0x17
    SpaceAnomalySignal = 0x18
    SpaceAtlasSignal = 0x19
    GenericIcon = 0x1A
    NetworkPlayerFireTeam = 0x1B
    NetworkPlayerFireTeamShip = 0x1C
    NetworkPlayer = 0x1D
    NetworkPlayerShip = 0x1E
    NetworkPlayerVehicle = 0x1F
    Monument = 0x20
    PlayerBase = 0x21
    EditingBase = 0x22
    MessageBeacon = 0x23
    ExternalBase = 0x24
    PlanetBaseTerminal = 0x25
    Vehicle = 0x26
    VehicleCheckpoint = 0x27
    VehicleGarage = 0x28
    Pet = 0x29
    DeathPoint = 0x2A
    Signal = 0x2B
    Portal = 0x2C
    PurchasableFrigate = 0x2D
    Expedition = 0x2E
    Building = 0x2F
    ActiveNetworkMarker = 0x30
    CustomMarker = 0x31
    PlacedMarker = 0x32
    Nexus = 0x33
    PowerHotspot = 0x34
    MineralHotspot = 0x35
    GasHotspot = 0x36
    NPC = 0x37
    SettlementNPC = 0x38
    FishPot = 0x39
    CreatureCurious = 0x3A
    CreatureAction = 0x3B
    CreatureTame = 0x3C
    CreatureDanger = 0x3D
    CreatureFiend = 0x3E
    CreatureMilk = 0x3F
    FuelAsteroid = 0x40
    PulseEncounter = 0x41
    FrigateFlyby = 0x42
    ShipExperienceSpawn = 0x43
    FriendlyDrone = 0x44
    ImportantNPC = 0x45
    CorvetteAutopilotDestination = 0x46
    CorvetteDeployedTeleporter = 0x47
    CorvettePadLink = 0x48


class cGcBuildingDensityLevels(IntEnum):
    Dead = 0x0
    Low = 0x1
    Mid = 0x2
    Full = 0x3
    Weird = 0x4
    HalfWeird = 0x5
    Waterworld = 0x6
    GasGiant = 0x7


class cGcBuildingSystemTypeEnum(IntEnum):
    Normal = 0x0
    AbandonedSystem = 0x1


class cGcBuildingClassification(IntEnum):
    None_ = 0x0
    TerrainResource = 0x1
    Shelter = 0x2
    Abandoned = 0x3
    Terminal = 0x4
    Shop = 0x5
    Outpost = 0x6
    Waypoint = 0x7
    Beacon = 0x8
    RadioTower = 0x9
    Observatory = 0xA
    Depot = 0xB
    Factory = 0xC
    Harvester = 0xD
    Plaque = 0xE
    Monolith = 0xF
    Portal = 0x10
    Ruin = 0x11
    Debris = 0x12
    DamagedMachine = 0x13
    DistressSignal = 0x14
    LandingPad = 0x15
    Base = 0x16
    MissionTower = 0x17
    CrashedFreighter = 0x18
    GraveInCave = 0x19
    StoryGlitch = 0x1A
    TreasureRuins = 0x1B
    GameStartSpawn = 0x1C
    WaterCrashedFreighter = 0x1D
    WaterTreasureRuins = 0x1E
    WaterAbandoned = 0x1F
    WaterDistressSignal = 0x20
    NPCDistressSignal = 0x21
    NPCDebris = 0x22
    LargeBuilding = 0x23
    Settlement_Hub = 0x24
    Settlement_LandingZone = 0x25
    Settlement_Bar = 0x26
    Settlement_Tower = 0x27
    Settlement_Market = 0x28
    Settlement_Small = 0x29
    Settlement_SmallIndustrial = 0x2A
    Settlement_Medium = 0x2B
    Settlement_Large = 0x2C
    Settlement_Monument = 0x2D
    Settlement_SheriffsOffice = 0x2E
    Settlement_Double = 0x2F
    Settlement_Farm = 0x30
    Settlement_Factory = 0x31
    Settlement_Clump = 0x32
    DroneHive = 0x33
    SentinelDistressSignal = 0x34
    AbandonedRobotCamp = 0x35
    RobotHead = 0x36
    DigSite = 0x37
    AncientGuardian = 0x38
    Settlement_Hub_Builders = 0x39
    Settlement_FishPond = 0x3A
    Settlement_Builders_RoboArm = 0x3B


class cGcNPCSeatedPosture(IntEnum):
    Sofa = 0x0
    Sit = 0x1


class cGcPetAccessoryType(IntEnum):
    None_ = 0x0
    CargoCylinder = 0x1
    Containers = 0x2
    ShieldArmour = 0x3
    SolarBattery = 0x4
    Tank = 0x5
    WingPanel = 0x6
    TravelPack = 0x7
    SpacePack = 0x8
    CargoLong = 0x9
    Antennae = 0xA
    Computer = 0xB
    Toolbelt = 0xC
    LeftCanisters = 0xD
    LeftEnergyCoil = 0xE
    LeftFrigateTurret = 0xF
    LeftHeadLights = 0x10
    LeftArmourPlate = 0x11
    LeftTurret = 0x12
    LeftSupportSystem = 0x13
    RightCanisters = 0x14
    RightEnergyCoil = 0x15
    RightFrigateTurret = 0x16
    RightHeadLights = 0x17
    RightArmourPlate = 0x18
    RightTurret = 0x19
    RightSupportSystem = 0x1A
    RightMechanicalPaw = 0x1B
    LeftMechanicalPaw = 0x1C
    MechanicalPaw = 0x1D


class cGcNPCTriggerTypes(IntEnum):
    None_ = 0x0
    Idle = 0x1
    Greet = 0x2
    Mood = 0x3
    StartDead = 0x4
    Talk_Start = 0x5
    Talk_Stop = 0x6
    Interact_Start = 0x7
    Interact_Stop = 0x8
    Interact_BeginHold = 0x9
    Interact_CancelHold = 0xA
    LookAt_Player_Start = 0xB
    LookAt_Player_Stop = 0xC
    SetProp = 0xD
    Interact_StartFromRemote = 0xE
    StartBusy = 0xF
    OneShotMoodResponse = 0x10


class cGcCreatureSpawnEnum(IntEnum):
    None_ = 0x0
    Resource = 0x1
    ResourceAway = 0x2
    HeavyAir = 0x3
    Drone = 0x4
    Deer = 0x5
    DeerScan = 0x6
    DeerWords = 0x7
    DeerWordsAway = 0x8
    Diplo = 0x9
    DiploScan = 0xA
    DiploWords = 0xB
    DiploWordsAway = 0xC
    Flyby = 0xD
    Beast = 0xE
    Wingmen = 0xF
    Scouts = 0x10
    Fleet = 0x11
    Attackers = 0x12
    AttackersFromBehind = 0x13
    Flee = 0x14
    RemoveFleet = 0x15
    Fighters = 0x16
    PostFighters = 0x17
    Escape = 0x18
    Warp = 0x19


class cGcNPCPropType(IntEnum):
    None_ = 0x0
    Default = 0x1
    DontCare = 0x2
    IPad = 0x3
    RandomHologram = 0x4
    HoloBlob = 0x5
    HoloFrigate = 0x6
    HoloShip = 0x7
    HoloMultitool = 0x8
    HoloSolarSystem = 0x9
    HoloDrone = 0xA
    Container = 0xB
    Box = 0xC
    Cup = 0xD
    Staff = 0xE


class cGcCreatureGroups(IntEnum):
    Solo = 0x0
    Couple = 0x1
    Group = 0x2
    Herd = 0x3


class cGcCreatureHemiSphere(IntEnum):
    Any = 0x0
    Northern = 0x1
    Southern = 0x2


class cGcCreatureRoles(IntEnum):
    None_ = 0x0
    Predator = 0x1
    PlayerPredator = 0x2
    Prey = 0x3
    Passive = 0x4
    Bird = 0x5
    FishPrey = 0x6
    FishPredator = 0x7
    Butterfly = 0x8
    Robot = 0x9
    Pet = 0xA


class cGcCreatureDiet(IntEnum):
    Carnivore = 0x0
    Omnivore = 0x1
    Herbivore = 0x2
    Robot = 0x3


class cGcCreatureGenerationDensity(IntEnum):
    Sparse = 0x0
    Normal = 0x1
    Dense = 0x2
    VeryDense = 0x3


class cGcCreatureActiveTime(IntEnum):
    OnlyDay = 0x0
    MostlyDay = 0x1
    AnyTime = 0x2
    MostlyNight = 0x3
    OnlyNight = 0x4


class cGcPetBehaviours(IntEnum):
    None_ = 0x0
    Idle = 0x1
    Eat = 0x2
    Poop = 0x3
    LayEgg = 0x4
    FollowPlayer = 0x5
    AdoptedFollowPlayer = 0x6
    ScanForResource = 0x7
    FindResource = 0x8
    FindHazards = 0x9
    AttackHazard = 0xA
    FindBuilding = 0xB
    Fetch = 0xC
    Explore = 0xD
    Emote = 0xE
    GestureReact = 0xF
    OrderedToPos = 0x10
    ComeHere = 0x11
    Mine = 0x12
    Summoned = 0x13
    Adopted = 0x14
    Hatched = 0x15
    PostInteract = 0x16
    Rest = 0x17
    Attack = 0x18
    Watch = 0x19
    Greet = 0x1A
    TeleportToPlayer = 0x1B


class cGcCreatureTypes(IntEnum):
    None_ = 0x0
    Bird = 0x1
    FlyingLizard = 0x2
    FlyingSnake = 0x3
    Butterfly = 0x4
    FlyingBeetle = 0x5
    Beetle = 0x6
    Fish = 0x7
    Shark = 0x8
    Crab = 0x9
    Snake = 0xA
    Dino = 0xB
    Antelope = 0xC
    Rodent = 0xD
    Cat = 0xE
    Fiend = 0xF
    BugQueen = 0x10
    BugFiend = 0x11
    Drone = 0x12
    Quad = 0x13
    SpiderQuad = 0x14
    SpiderQuadMini = 0x15
    Walker = 0x16
    Predator = 0x17
    PlayerPredator = 0x18
    Prey = 0x19
    Passive = 0x1A
    FishPredator = 0x1B
    FishPrey = 0x1C
    FiendFishSmall = 0x1D
    FiendFishBig = 0x1E
    Jellyfish = 0x1F
    LandJellyfish = 0x20
    RockCreature = 0x21
    MiniFiend = 0x22
    Floater = 0x23
    Scuttler = 0x24
    Slug = 0x25
    MiniDrone = 0x26
    MiniRobo = 0x27
    SpaceFloater = 0x28
    JellyBoss = 0x29
    JellyBossBrood = 0x2A
    LandSquid = 0x2B
    Weird = 0x2C
    SeaSnake = 0x2D
    SandWorm = 0x2E
    ProtoRoller = 0x2F
    ProtoFlyer = 0x30
    ProtoDigger = 0x31
    Plough = 0x32
    Digger = 0x33
    Drill = 0x34
    Brainless = 0x35
    Pet = 0x36


class cGcCreatureSizeClasses(IntEnum):
    Small = 0x0
    Medium = 0x1
    Large = 0x2
    Huge = 0x3


class cGcCreatureRoleFrequencyModifier(IntEnum):
    Never = 0x0
    Low = 0x1
    Normal = 0x2
    High = 0x3


class cGcCreaturePetMood(IntEnum):
    Hungry = 0x0
    Lonely = 0x1


class cGcCreaturePetRewardActions(IntEnum):
    Tickle = 0x0
    Treat = 0x1
    Ride = 0x2
    Customise = 0x3
    Abandon = 0x4
    LayEgg = 0x5
    Adopt = 0x6
    Milk = 0x7
    HarvestSpecial = 0x8


class cGcCreaturePetTraits(IntEnum):
    Helpfulness = 0x0
    Aggression = 0x1
    Independence = 0x2


class cGcCreatureParticleEffectTrigger(IntEnum):
    empty = 0x0
    Spawn = 0x1
    Despawn = 0x2
    Death = 0x4
    Ragdoll = 0x8
    Appear = 0x10
    Disappear = 0x20


class cGcCreatureIkType(IntEnum):
    Foot = 0x0
    Hinge_X = 0x1
    Hinge_Y = 0x2
    Hinge_Z = 0x3
    Locked = 0x4
    Head = 0x5
    Toe = 0x6
    SpaceshipFoot = 0x7
    SpaceshipToe = 0x8


class cGcPrimaryAxis(IntEnum):
    Z = 0x0
    ZNeg = 0x1
    X = 0x2
    XNeg = 0x3
    Y = 0x4
    YNeg = 0x5


class cGcBehaviourLegacyData(IntEnum):
    Riding = 0x0
    Interaction = 0x1
    Attracted = 0x2
    Flee = 0x3
    Defend = 0x4
    FollowPlayer = 0x5
    AvoidPlayer = 0x6
    NoticePlayer = 0x7
    FollowRoutine = 0x8


class cGcWarpAction(IntEnum):
    BlackHole = 0x0
    SpacePOI = 0x1


class cGcMultitoolPoolType(IntEnum):
    Standard = 0x0
    Exotic = 0x1
    Sentinel = 0x2
    Atlas = 0x3
    SettlementRotational = 0x4


class cGcBaseDefenceStatusType(IntEnum):
    AttackingTarget = 0x0
    Alert = 0x1
    SearchingForTarget = 0x2
    Disabled = 0x3
    Security = 0x4


class cGcBroadcastLevel(IntEnum):
    Scene = 0x0
    LocalModel = 0x1
    Local = 0x2


class cGcInteractionType(IntEnum):
    None_ = 0x0
    Shop = 0x1
    NPC = 0x2
    NPC_Secondary = 0x3
    NPC_Anomaly = 0x4
    NPC_Anomaly_Secondary = 0x5
    Ship = 0x6
    Outpost = 0x7
    SpaceStation = 0x8
    RadioTower = 0x9
    Monolith = 0xA
    Factory = 0xB
    AbandonedShip = 0xC
    Harvester = 0xD
    Observatory = 0xE
    TradingPost = 0xF
    DistressBeacon = 0x10
    Portal = 0x11
    Plaque = 0x12
    AtlasStation = 0x13
    AbandonedBuildings = 0x14
    WeaponTerminal = 0x15
    SuitTerminal = 0x16
    SignalScanner = 0x17
    Teleporter_Base = 0x18
    Teleporter_Station = 0x19
    ClaimBase = 0x1A
    NPC_Freighter_Captain = 0x1B
    NPC_HIRE_Weapons = 0x1C
    NPC_HIRE_Weapons_Wait = 0x1D
    NPC_HIRE_Farmer = 0x1E
    NPC_HIRE_Farmer_Wait = 0x1F
    NPC_HIRE_Builder = 0x20
    NPC_HIRE_Builder_Wait = 0x21
    NPC_HIRE_Vehicles = 0x22
    NPC_HIRE_Vehicles_Wait = 0x23
    MessageBeacon = 0x24
    NPC_HIRE_Scientist = 0x25
    NPC_HIRE_Scientist_Wait = 0x26
    NPC_Recruit = 0x27
    NPC_Freighter_Captain_Secondary = 0x28
    NPC_Recruit_Secondary = 0x29
    Vehicle = 0x2A
    MessageModule = 0x2B
    TechShop = 0x2C
    VehicleRaceStart = 0x2D
    BuildingShop = 0x2E
    MissionGiver = 0x2F
    HoloHub = 0x30
    HoloExplorer = 0x31
    HoloSceptic = 0x32
    HoloNoone = 0x33
    PortalRuneEntry = 0x34
    PortalActivate = 0x35
    CrashedFreighter = 0x36
    GraveInCave = 0x37
    GlitchyStoryBox = 0x38
    NetworkPlayer = 0x39
    NetworkMonument = 0x3A
    AnomalyComputer = 0x3B
    AtlasPlinth = 0x3C
    Epilogue = 0x3D
    GuildEnvoy = 0x3E
    ManageFleet = 0x3F
    ManageExpeditions = 0x40
    Frigate = 0x41
    CustomiseCharacter = 0x42
    CustomiseShip = 0x43
    CustomiseWeapon = 0x44
    CustomiseVehicle = 0x45
    ClaimBaseAnywhere = 0x46
    FleetNavigator = 0x47
    FleetCommandPost = 0x48
    StoryUtility = 0x49
    MPMissionGiver = 0x4A
    SpecialsShop = 0x4B
    WaterRuin = 0x4C
    LocationScanner = 0x4D
    ByteBeat = 0x4E
    NPC_CrashSite = 0x4F
    NPC_Scavenger = 0x50
    BaseGridPart = 0x51
    NPC_Freighter_Crew = 0x52
    NPC_Freighter_Crew_Owned = 0x53
    AbandonedShip_With_NPC = 0x54
    ShipPilot = 0x55
    NexusMilestones = 0x56
    NexusDailyMission = 0x57
    CreatureFeeder = 0x58
    ExoticExtra1 = 0x59
    ExoticExtra2 = 0x5A
    ExoticExtra3 = 0x5B
    ExoticExtra4 = 0x5C
    ExoticExtra5 = 0x5D
    ExoticExtra6 = 0x5E
    MapShop = 0x5F
    NPC_Closure = 0x60
    StorageContainer = 0x61
    Teleporter_Nexus = 0x62
    ShipSalvage = 0x63
    ByteBeatSwitch = 0x64
    AbandonedFreighterIntro = 0x65
    AbandonedFreighterEnd = 0x66
    AbandonedFreighterProcText = 0x67
    AbandonedFreighterCaptLog = 0x68
    AbandonedFreighterCrewLog = 0x69
    AbandonedFreighterShop = 0x6A
    CustomiseFreighter = 0x6B
    LibraryVault = 0x6C
    LibraryMainTerminal = 0x6D
    LibraryMap = 0x6E
    WeaponUpgrade = 0x6F
    Pet = 0x70
    Creature = 0x71
    FreighterGalacticMap = 0x72
    RecipeStation = 0x73
    StationCore = 0x74
    NPC_Settlement_SpecialWorker = 0x75
    NPC_Settlement_Secondary = 0x76
    SettlementHub = 0x77
    SettlementBuildingSite = 0x78
    SettlementAdminTerminal = 0x79
    FriendlyDrone = 0x7A
    DroneHive = 0x7B
    RocketLocker = 0x7C
    FrigateCaptain = 0x7D
    PirateShop = 0x7E
    NPC_PirateSecondary = 0x7F
    NPC_FreighterBase_SquadronPilot = 0x80
    NPC_FreighterBase_FrigateCaptain = 0x81
    NPC_FreighterBase_Worker = 0x82
    RobotHead = 0x83
    RobotCampTerminal = 0x84
    MonolithNub = 0x85
    NexusSpiderman = 0x86
    WeaponSalvage = 0x87
    DiscoverySelector = 0x88
    RobotShop = 0x89
    SeasonTerminal = 0x8A
    NPC_Freighter_Captain_Pirate = 0x8B
    SkiffLocker = 0x8C
    CustomiseSkiff = 0x8D
    ExhibitAssembly = 0x8E
    ArchiveMultitool = 0x8F
    BoneShop = 0x90
    SettlementBuildingDetail = 0x91
    ByteBeatJukebox = 0x92
    NPC_Settlement_SquadronPilot = 0x93
    Settlement_TowerTerminal = 0x94
    EditShip = 0x95
    CorvetteTeleport = 0x96
    CorvetteTeleportReturn = 0x97


class cGcHologramState(IntEnum):
    Hologram = 0x0
    Attract = 0x1
    Explode = 0x2
    Disabled = 0x3


class cGcHologramType(IntEnum):
    Mesh = 0x0
    PlayerCharacter = 0x1
    PlayerShip = 0x2
    PlayerMultiTool = 0x3


class cGcHologramPivotType(IntEnum):
    Origin = 0x0
    CentreBounds = 0x1


class cGcCharacterControlInputValidity(IntEnum):
    Always = 0x0
    PadOnly = 0x1
    KeyboardAnMouseOnly = 0x2


class cGcCharacterControlOutputSpace(IntEnum):
    CameraRelative = 0x0
    CameraRelativeTopDown = 0x1
    Raw = 0x2


class cGcStatsTypes(IntEnum):
    Unspecified = 0x0
    Weapon_Laser = 0x1
    Weapon_Laser_Damage = 0x2
    Weapon_Laser_Mining_Speed = 0x3
    Weapon_Laser_HeatTime = 0x4
    Weapon_Laser_Bounce = 0x5
    Weapon_Laser_ReloadTime = 0x6
    Weapon_Laser_Recoil = 0x7
    Weapon_Laser_Drain = 0x8
    Weapon_Laser_StrongLaser = 0x9
    Weapon_Laser_ChargeTime = 0xA
    Weapon_Laser_MiningBonus = 0xB
    Weapon_Projectile = 0xC
    Weapon_Projectile_Damage = 0xD
    Weapon_Projectile_Range = 0xE
    Weapon_Projectile_Rate = 0xF
    Weapon_Projectile_ClipSize = 0x10
    Weapon_Projectile_ReloadTime = 0x11
    Weapon_Projectile_Recoil = 0x12
    Weapon_Projectile_Bounce = 0x13
    Weapon_Projectile_Homing = 0x14
    Weapon_Projectile_Dispersion = 0x15
    Weapon_Projectile_BulletsPerShot = 0x16
    Weapon_Projectile_MinimumCharge = 0x17
    Weapon_Projectile_MaximumCharge = 0x18
    Weapon_Projectile_BurstCap = 0x19
    Weapon_Projectile_BurstCooldown = 0x1A
    Weapon_ChargedProjectile = 0x1B
    Weapon_ChargedProjectile_ChargeTime = 0x1C
    Weapon_ChargedProjectile_CooldownDuration = 0x1D
    Weapon_ChargedProjectile_Drain = 0x1E
    Weapon_ChargedProjectile_ExtraSpeed = 0x1F
    Weapon_Rail = 0x20
    Weapon_Shotgun = 0x21
    Weapon_Burst = 0x22
    Weapon_Flame = 0x23
    Weapon_Cannon = 0x24
    Weapon_Grenade = 0x25
    Weapon_Grenade_Damage = 0x26
    Weapon_Grenade_Radius = 0x27
    Weapon_Grenade_Speed = 0x28
    Weapon_Grenade_Bounce = 0x29
    Weapon_Grenade_Homing = 0x2A
    Weapon_Grenade_Clusterbomb = 0x2B
    Weapon_TerrainEdit = 0x2C
    Weapon_SunLaser = 0x2D
    Weapon_SoulLaser = 0x2E
    Weapon_MineGrenade = 0x2F
    Weapon_FrontShield = 0x30
    Weapon_Scope = 0x31
    Weapon_Spawner = 0x32
    Weapon_SpawnerAlt = 0x33
    Weapon_Melee = 0x34
    Weapon_StunGrenade = 0x35
    Weapon_Stealth = 0x36
    Weapon_Scan = 0x37
    Weapon_Scan_Radius = 0x38
    Weapon_Scan_Recharge_Time = 0x39
    Weapon_Scan_Types = 0x3A
    Weapon_Scan_Binoculars = 0x3B
    Weapon_Scan_Discovery_Creature = 0x3C
    Weapon_Scan_Discovery_Flora = 0x3D
    Weapon_Scan_Discovery_Mineral = 0x3E
    Weapon_Scan_Secondary = 0x3F
    Weapon_Scan_Terrain_Resource = 0x40
    Weapon_Scan_Surveying = 0x41
    Weapon_Scan_BuilderReveal = 0x42
    Weapon_Fish = 0x43
    Weapon_Stun = 0x44
    Weapon_Stun_Duration = 0x45
    Weapon_Stun_Damage_Multiplier = 0x46
    Weapon_FireDOT = 0x47
    Weapon_FireDOT_Duration = 0x48
    Weapon_FireDOT_DPS = 0x49
    Weapon_FireDOT_Damage_Multiplier = 0x4A
    Suit_Armour_Health = 0x4B
    Suit_Armour_Shield = 0x4C
    Suit_Armour_Shield_Strength = 0x4D
    Suit_Energy = 0x4E
    Suit_Energy_Regen = 0x4F
    Suit_Protection = 0x50
    Suit_Protection_Cold = 0x51
    Suit_Protection_Heat = 0x52
    Suit_Protection_Toxic = 0x53
    Suit_Protection_Radiation = 0x54
    Suit_Protection_Spook = 0x55
    Suit_Protection_Pressure = 0x56
    Suit_Underwater = 0x57
    Suit_UnderwaterLifeSupport = 0x58
    Suit_DamageReduce_Cold = 0x59
    Suit_DamageReduce_Heat = 0x5A
    Suit_DamageReduce_Toxic = 0x5B
    Suit_DamageReduce_Radiation = 0x5C
    Suit_Protection_HeatDrain = 0x5D
    Suit_Protection_ColdDrain = 0x5E
    Suit_Protection_ToxDrain = 0x5F
    Suit_Protection_RadDrain = 0x60
    Suit_Protection_WaterDrain = 0x61
    Suit_Protection_SpookDrain = 0x62
    Suit_Stamina_Strength = 0x63
    Suit_Stamina_Speed = 0x64
    Suit_Stamina_Recovery = 0x65
    Suit_Jetpack = 0x66
    Suit_Jetpack_Tank = 0x67
    Suit_Jetpack_Drain = 0x68
    Suit_Jetpack_Refill = 0x69
    Suit_Jetpack_Ignition = 0x6A
    Suit_Jetpack_DoubleJump = 0x6B
    Suit_Jetpack_WaterEfficiency = 0x6C
    Suit_Jetpack_MidairRefill = 0x6D
    Suit_Refiner = 0x6E
    Suit_AutoTranslator = 0x6F
    Suit_Utility = 0x70
    Suit_RocketLocker = 0x71
    Suit_FishPlatform = 0x72
    Suit_FoodUnit = 0x73
    Suit_Denier = 0x74
    Suit_Vehicle_Summon = 0x75
    Ship_Weapons_Guns = 0x76
    Ship_Weapons_Guns_Damage = 0x77
    Ship_Weapons_Guns_Rate = 0x78
    Ship_Weapons_Guns_HeatTime = 0x79
    Ship_Weapons_Guns_CoolTime = 0x7A
    Ship_Weapons_Guns_Scale = 0x7B
    Ship_Weapons_Guns_BulletsPerShot = 0x7C
    Ship_Weapons_Guns_Dispersion = 0x7D
    Ship_Weapons_Guns_Range = 0x7E
    Ship_Weapons_Guns_Damage_Radius = 0x7F
    Ship_Weapons_Lasers = 0x80
    Ship_Weapons_Lasers_Damage = 0x81
    Ship_Weapons_Lasers_HeatTime = 0x82
    Ship_Weapons_Missiles = 0x83
    Ship_Weapons_Missiles_NumPerShot = 0x84
    Ship_Weapons_Missiles_Speed = 0x85
    Ship_Weapons_Missiles_Damage = 0x86
    Ship_Weapons_Missiles_Size = 0x87
    Ship_Weapons_Shotgun = 0x88
    Ship_Weapons_MiniGun = 0x89
    Ship_Weapons_Plasma = 0x8A
    Ship_Weapons_Rockets = 0x8B
    Ship_Weapons_ShieldLeech = 0x8C
    Ship_Armour_Shield = 0x8D
    Ship_Armour_Shield_Strength = 0x8E
    Ship_Armour_Health = 0x8F
    Ship_Scan = 0x90
    Ship_Scan_EconomyFilter = 0x91
    Ship_Scan_ConflictFilter = 0x92
    Ship_Hyperdrive = 0x93
    Ship_Hyperdrive_JumpDistance = 0x94
    Ship_Hyperdrive_JumpsPerCell = 0x95
    Ship_Hyperdrive_QuickWarp = 0x96
    Ship_Launcher = 0x97
    Ship_Launcher_TakeOffCost = 0x98
    Ship_Launcher_AutoCharge = 0x99
    Ship_PulseDrive = 0x9A
    Ship_PulseDrive_MiniJumpFuelSpending = 0x9B
    Ship_PulseDrive_MiniJumpSpeed = 0x9C
    Ship_Boost = 0x9D
    Ship_Maneuverability = 0x9E
    Ship_BoostManeuverability = 0x9F
    Ship_LifeSupport = 0xA0
    Ship_Drift = 0xA1
    Ship_Inventory = 0xA2
    Ship_Tech_Slots = 0xA3
    Ship_Cargo_Slots = 0xA4
    Ship_Teleport = 0xA5
    Ship_CargoShield = 0xA6
    Ship_WaterLandingJet = 0xA7
    Freighter_Hyperdrive = 0xA8
    Freighter_Hyperdrive_JumpDistance = 0xA9
    Freighter_Hyperdrive_JumpsPerCell = 0xAA
    Freighter_MegaWarp = 0xAB
    Freighter_Teleport = 0xAC
    Freighter_Fleet_Boost = 0xAD
    Freighter_Fleet_Speed = 0xAE
    Freighter_Fleet_Fuel = 0xAF
    Freighter_Fleet_Combat = 0xB0
    Freighter_Fleet_Trade = 0xB1
    Freighter_Fleet_Explore = 0xB2
    Freighter_Fleet_Mine = 0xB3
    Vehicle_Boost = 0xB4
    Vehicle_Engine = 0xB5
    Vehicle_Scan = 0xB6
    Vehicle_EngineFuelUse = 0xB7
    Vehicle_EngineTopSpeed = 0xB8
    Vehicle_BoostSpeed = 0xB9
    Vehicle_BoostTanks = 0xBA
    Vehicle_Grip = 0xBB
    Vehicle_SkidGrip = 0xBC
    Vehicle_SubBoostSpeed = 0xBD
    Vehicle_Laser = 0xBE
    Vehicle_LaserDamage = 0xBF
    Vehicle_LaserHeatTime = 0xC0
    Vehicle_LaserStrongLaser = 0xC1
    Vehicle_Gun = 0xC2
    Vehicle_GunDamage = 0xC3
    Vehicle_GunHeatTime = 0xC4
    Vehicle_GunRate = 0xC5
    Vehicle_StunGun = 0xC6
    Vehicle_TerrainEdit = 0xC7
    Vehicle_FuelRegen = 0xC8
    Vehicle_AutoPilot = 0xC9
    Vehicle_Flame = 0xCA
    Vehicle_FlameDamage = 0xCB
    Vehicle_FlameHeatTime = 0xCC
    Vehicle_Refiner = 0xCD


class cGcWordCategoryTableEnum(IntEnum):
    MISC = 0x0
    DIRECTIONS = 0x1
    HELP = 0x2
    TRADE = 0x3
    LORE = 0x4
    TECH = 0x5
    THREAT = 0x6


class cGcItemFilterMatchIDType(IntEnum):
    Exact = 0x0
    Prefix = 0x1
    Postfix = 0x2


class cGcUnlockableItemTreeGroups(IntEnum):
    Test = 0x0
    BasicBaseParts = 0x1
    BasicTechParts = 0x2
    BaseParts = 0x3
    SpecialBaseParts = 0x4
    SuitTech = 0x5
    ShipTech = 0x6
    WeapTech = 0x7
    ExocraftTech = 0x8
    CraftProducts = 0x9
    FreighterTech = 0xA
    S9BaseParts = 0xB
    S9ExoTech = 0xC
    S9ShipTech = 0xD
    CorvetteParts = 0xE


class cGcWeightingCurve(IntEnum):
    NoWeighting = 0x0
    MaxIsUncommon = 0x1
    MaxIsRare = 0x2
    MaxIsSuperRare = 0x3
    MinIsUncommon = 0x4
    MinIsRare = 0x5
    MinIsSuperRare = 0x6


class cGcTechnologyCategory(IntEnum):
    Ship = 0x0
    Weapon = 0x1
    Suit = 0x2
    Personal = 0x3
    All = 0x4
    None_ = 0x5
    Freighter = 0x6
    Maintenance = 0x7
    Exocraft = 0x8
    Colossus = 0x9
    Submarine = 0xA
    Mech = 0xB
    AllVehicles = 0xC
    AlienShip = 0xD
    AllShips = 0xE
    RobotShip = 0xF
    AllShipsExceptAlien = 0x10
    Corvette = 0x11


class cGcTechnologyRarity(IntEnum):
    Normal = 0x0
    VeryCommon = 0x1
    Common = 0x2
    Rare = 0x3
    VeryRare = 0x4
    Impossible = 0x5
    Always = 0x6


class cGcTradeCategory(IntEnum):
    Mineral = 0x0
    Tech = 0x1
    Commodity = 0x2
    Component = 0x3
    Alloy = 0x4
    Exotic = 0x5
    Energy = 0x6
    None_ = 0x7
    SpecialShop = 0x8


class cGcStatsEnum(IntEnum):
    None_ = 0x0
    DEPOTS_BROKEN = 0x1
    FPODS_BROKEN = 0x2
    PLANTS_PLANTED = 0x3
    SALVAGE_LOOTED = 0x4
    TREASURE_FOUND = 0x5
    QUADS_KILLED = 0x6
    WALKERS_KILLED = 0x7
    FLORA_KILLED = 0x8
    PLANTS_GATHERED = 0x9
    BONES_FOUND = 0xA
    C_SENT_KILLS = 0xB
    STORM_CRYSTALS = 0xC
    BURIED_PROPS = 0xD
    MINIWORM_KILL = 0xE
    POOP_COLLECTED = 0xF
    GRAVBALLS = 0x10
    EGG_PODS = 0x11
    CORRUPT_PILLAR = 0x12
    DRONE_SHARDS = 0x13
    MECHS_KILLED = 0x14
    SPIDERS_KILLED = 0x15
    SM_SPIDER_KILLS = 0x16
    SEAGLASS = 0x17
    RUINS_LOOTED = 0x18
    STONE_KILLS = 0x19


class cGcSettlementStatStrength(IntEnum):
    PositiveWide = 0x0
    PositiveLarge = 0x1
    PositiveMedium = 0x2
    PositiveSmall = 0x3
    NegativeSmall = 0x4
    NegativeMedium = 0x5
    NegativeLarge = 0x6


class cGcSizeIndicator(IntEnum):
    Small = 0x0
    Medium = 0x1
    Large = 0x2


class cGcRewardTeleport(IntEnum):
    None_ = 0x0
    ToBase = 0x1
    Station = 0x2
    Atlas = 0x3


class cGcRewardStartShipBuildMode(IntEnum):
    CreateFromDefault = 0x0
    CreateFromDockedShip = 0x1
    ResumeBuild = 0x2
    ResumeBuildFromPurchaseScreen = 0x3


class cGcRewardSignalScan(IntEnum):
    None_ = 0x0
    DropPod = 0x1
    Shelter = 0x2
    Search = 0x3
    Relic = 0x4
    Industrial = 0x5
    Alien = 0x6
    CrashedFreighter = 0x7


class cGcRewardScanEventOutcome(IntEnum):
    Success = 0x0
    Interstellar = 0x1
    BadData = 0x2
    FailedToFindBase = 0x3
    Duplicate = 0x4
    NoBuilding = 0x5
    NoSystem = 0x6


class cGcRewardRepairWholeInventory(IntEnum):
    Personal = 0x0
    PersonalTech = 0x1
    Ship = 0x2
    ShipTech = 0x3
    Freighter = 0x4
    Vehicle = 0x5
    AttachedAbandonedShip = 0x6
    Weapon = 0x7


class cGcRewardFrigateDamageResponse(IntEnum):
    StayOut = 0x0
    ReturnHome = 0x1
    CheckForMoreDamage = 0x2
    ShowDamagedCaptain = 0x3
    ShowExpeditionCaptain = 0x4
    AbortExpedition = 0x5


class cGcRewardJourneyThroughCentre(IntEnum):
    Next = 0x0
    Abandoned = 0x1
    Vicious = 0x2
    Lush = 0x3
    Balanced = 0x4


class cGcRewardEndSettlementExpedition(IntEnum):
    Debrief = 0x0
    Shutdown = 0x1


class cGcRealitySubstanceCategory(IntEnum):
    Fuel = 0x0
    Metal = 0x1
    Catalyst = 0x2
    Stellar = 0x3
    Flora = 0x4
    Earth = 0x5
    Exotic = 0x6
    Special = 0x7
    BuildingPart = 0x8


class cGcRewardAtlasPathProgress(IntEnum):
    IncrementPathProgress = 0x0
    FinalStoryAtlas = 0x1
    StoreLoopingCompleteStations = 0x2


class cGcRealityCommonFactions(IntEnum):
    Player = 0x0
    Civilian = 0x1
    Pirate = 0x2
    Police = 0x3
    Creature = 0x4


class cGcProductTableType(IntEnum):
    Main = 0x0
    BaseParts = 0x1
    ModularCustomisation = 0x2


class cGcRealityGameIcons(IntEnum):
    Stamina = 0x0
    NoStamina = 0x1
    EnergyCharge = 0x2
    Scanner = 0x3
    NoScanner = 0x4
    Grave = 0x5
    Resources = 0x6
    Inventory = 0x7
    InventoryFull = 0x8
    RareItems = 0x9
    Pirates = 0xA
    PirateScan = 0xB
    Drone = 0xC
    Quad = 0xD
    Mech = 0xE
    Walker = 0xF
    Spider = 0x10
    DroneOff = 0x11
    Police = 0x12
    PoliceFreighter = 0x13
    AtlasStation = 0x14
    BlackHole = 0x15
    SaveGame = 0x16
    SaveInventory = 0x17
    Jetpack = 0x18
    JetpackEmpty = 0x19
    VehicleBoost = 0x1A
    VehicleBoostRecharge = 0x1B
    Fuel = 0x1C
    FuelEmpty = 0x1D
    GekStanding = 0x1E
    VykeenStanding = 0x1F
    KorvaxStanding = 0x20
    GekDiamondStanding = 0x21
    VykeenDiamondStanding = 0x22
    KorvaxDiamondStanding = 0x23
    TradeGuildStanding = 0x24
    WarGuildStanding = 0x25
    ExplorationGuildStanding = 0x26
    TradeGuildDiamondStanding = 0x27
    WarGuildDiamondStanding = 0x28
    ExplorationGuildDiamondStanding = 0x29
    GMPathToCentre = 0x2A
    GMAtlas = 0x2B
    GMBlackHole = 0x2C
    GMUserWaypoint = 0x2D
    GMUserMission = 0x2E
    GMSeasonal = 0x2F
    TransferPersonal = 0x30
    TransferPersonalCargo = 0x31
    TransferShip = 0x32
    TransferBike = 0x33
    TransferBuggy = 0x34
    TransferTruck = 0x35
    TransferWheeledBike = 0x36
    TransferHovercraft = 0x37
    TransferSubmarine = 0x38
    TransferMech = 0x39
    TransferFreighter = 0x3A
    TransferBase = 0x3B
    TransferCooker = 0x3C
    TransferSkiff = 0x3D
    TransferCorvette = 0x3E
    HazardIndicatorHot = 0x3F
    HazardIndicatorCold = 0x40
    HazardIndicatorRadiation = 0x41
    HazardIndicatorToxic = 0x42
    TerrainAdd = 0x43
    TerrainRemove = 0x44
    TerrainFlatten = 0x45
    TerrainUndo = 0x46
    SpacePhone = 0x47
    GarageMarkerBuggy = 0x48
    GarageMarkerBike = 0x49
    GarageMarkerTruck = 0x4A
    GarageMarkerWheeledBike = 0x4B
    GarageMarkerHovercraft = 0x4C
    CorruptedDrone = 0x4D
    AncientGuardian = 0x4E
    HandHold = 0x4F
    ShipThumbnailBG = 0x50
    CClass = 0x51
    BClass = 0x52
    AClass = 0x53
    SClass = 0x54
    NoSaveWarning = 0x55
    ExploreMissionPlanetIcon = 0x56
    ExploreMissionSystemIcon = 0x57
    PetThumbnailBG = 0x58
    SettlementOSD = 0x59
    SettlementUpgradeOSD = 0x5A
    Stealth = 0x5B
    StealthEmpty = 0x5C
    DefenceForce = 0x5D
    SummonSquadron = 0x5E
    CookShop = 0x5F
    HazardIndicatorSpook = 0x60
    BioShip = 0x61
    CargoShip = 0x62
    ExoticShip = 0x63
    FighterShip = 0x64
    ScienceShip = 0x65
    SentinelShip = 0x66
    ShuttleShip = 0x67
    SailShip = 0x68
    PistolWeapon = 0x69
    RifleWeapon = 0x6A
    PristineWeapon = 0x6B
    AlienWeapon = 0x6C
    RoyalWeapon = 0x6D
    RobotWeapon = 0x6E
    AtlasWeapon = 0x6F
    StaffWeapon = 0x70
    CorvetteShip = 0x71
    InvalidShipBuild = 0x72


class cGcRarity(IntEnum):
    Common = 0x0
    Uncommon = 0x1
    Rare = 0x2


class cGcProceduralProductCategory(IntEnum):
    Loot = 0x0
    Document = 0x1
    BioSample = 0x2
    Fossil = 0x3
    Plant = 0x4
    Tool = 0x5
    Farm = 0x6
    SeaLoot = 0x7
    SeaHorror = 0x8
    Salvage = 0x9
    Bones = 0xA
    SpaceHorror = 0xB
    SpaceBones = 0xC
    FreighterPassword = 0xD
    FreighterCaptLog = 0xE
    FreighterCrewList = 0xF
    FreighterTechHyp = 0x10
    FreighterTechSpeed = 0x11
    FreighterTechFuel = 0x12
    FreighterTechTrade = 0x13
    FreighterTechCombat = 0x14
    FreighterTechMine = 0x15
    FreighterTechExp = 0x16
    DismantleBio = 0x17
    DismantleTech = 0x18
    DismantleData = 0x19
    MessageInBottle = 0x1A
    ExhibitFossil = 0x1B


class cGcProductCategory(IntEnum):
    Component = 0x0
    Consumable = 0x1
    Tradeable = 0x2
    Curiosity = 0x3
    BuildingPart = 0x4
    Procedural = 0x5
    Emote = 0x6
    CustomisationPart = 0x7
    CreatureEgg = 0x8
    Fish = 0x9
    ExhibitBone = 0xA


class cGcNameGeneratorTypes(IntEnum):
    Generic = 0x0
    Mineral = 0x1
    Region_NO = 0x2
    Region_RU = 0x3
    Region_CH = 0x4
    Region_JP = 0x5
    Region_LT = 0x6
    Region_FL = 0x7


class cGcProceduralTechnologyCategory(IntEnum):
    None_ = 0x0
    Combat = 0x1
    Mining = 0x2
    Scanning = 0x3
    Protection = 0x4


class cGcModularCustomisationResourceType(IntEnum):
    MultiToolStaff = 0x0
    Fighter = 0x1
    Dropship = 0x2
    Scientific = 0x3
    Shuttle = 0x4
    Sail = 0x5
    ExhibitTRex = 0x6
    ExhibitWorm = 0x7
    ExhibitGrunt = 0x8
    ExhibitQuadruped = 0x9
    ExhibitBird = 0xA


class cGcMaintenanceElementGroups(IntEnum):
    Custom = 0x0
    Farming = 0x1
    Fuelling = 0x2
    Repairing = 0x3
    EasyRepairing = 0x4
    Cleaning = 0x5
    Frigate = 0x6
    Sentinels = 0x7
    Runes = 0x8
    RobotHeads = 0x9


class cGcNameGeneratorSectorTypes(IntEnum):
    Generic = 0x0
    Elevated = 0x1
    Low = 0x2
    Trees = 0x3
    LushTrees = 0x4
    Lush = 0x5
    Wet = 0x6
    Cave = 0x7
    Dead = 0x8
    Buildings = 0x9
    Water = 0xA
    Ice = 0xB


class cGcInventoryType(IntEnum):
    Substance = 0x0
    Technology = 0x1
    Product = 0x2


class cGcInventoryLayoutSizeType(IntEnum):
    SciSmall = 0x0
    SciMedium = 0x1
    SciLarge = 0x2
    FgtSmall = 0x3
    FgtMedium = 0x4
    FgtLarge = 0x5
    ShuSmall = 0x6
    ShtMedium = 0x7
    ShtLarge = 0x8
    DrpSmall = 0x9
    DrpMedium = 0xA
    DrpLarge = 0xB
    RoySmall = 0xC
    RoyMedium = 0xD
    RoyLarge = 0xE
    AlienSmall = 0xF
    AlienMedium = 0x10
    AlienLarge = 0x11
    SailSmall = 0x12
    SailMedium = 0x13
    SailLarge = 0x14
    RobotSmall = 0x15
    RobotMedium = 0x16
    RobotLarge = 0x17
    WeaponSmall = 0x18
    WeaponMedium = 0x19
    WeaponLarge = 0x1A
    FreighterSmall = 0x1B
    FreighterMedium = 0x1C
    FreighterLarge = 0x1D
    VehicleSmall = 0x1E
    VehicleMedium = 0x1F
    VehicleLarge = 0x20
    ChestSmall = 0x21
    ChestMedium = 0x22
    ChestLarge = 0x23
    ChestCapsule = 0x24
    Suit = 0x25
    MaintObject = 0x26
    RocketLocker = 0x27
    FishBaitBox = 0x28
    FishingPlatform = 0x29
    FoodUnit = 0x2A
    Corvette = 0x2B
    CorvetteStorage = 0x2C


class cGcItemNeedPurpose(IntEnum):
    None_ = 0x0
    Crafting = 0x1
    Building = 0x2
    Repairing = 0x3
    Charging = 0x4
    Paying = 0x5


class cGcInventorySpecialSlotType(IntEnum):
    Broken = 0x0
    TechOnly = 0x1
    Cargo = 0x2
    BlockedByBrokenTech = 0x3
    TechBonus = 0x4


class cGcLegality(IntEnum):
    Legal = 0x0
    Illegal = 0x1


class cGcInventoryStackSizeGroup(IntEnum):
    Default = 0x0
    Personal = 0x1
    PersonalCargo = 0x2
    Ship = 0x3
    ShipCargo = 0x4
    Freighter = 0x5
    FreighterCargo = 0x6
    Vehicle = 0x7
    Chest = 0x8
    BaseCapsule = 0x9
    MaintenanceObject = 0xA
    UIPopup = 0xB
    SeasonTransfer = 0xC


class cGcFrigateClass(IntEnum):
    Combat = 0x0
    Exploration = 0x1
    Mining = 0x2
    Diplomacy = 0x3
    Support = 0x4
    Normandy = 0x5
    DeepSpace = 0x6
    DeepSpaceCommon = 0x7
    Pirate = 0x8
    GhostShip = 0x9


class cGcDiscoveryTrimGroup(IntEnum):
    System = 0x0
    Planet = 0x1
    Interesting = 0x2
    Boring = 0x3


class cGcDiscoveryTrimScoringCategory(IntEnum):
    IsNamedSystem = 0x0
    RecentlyVisitedSystem = 0x1
    RecentDiscoveryInSystem = 0x2
    NumDiscoveredPlanetsInSystem = 0x3
    IsNamedPlanet = 0x4
    NumBasesOnPlanet = 0x5
    NumWondersOnPlanet = 0x6
    NumNamedDiscoveries = 0x7


class cGcFrigateTraitStrength(IntEnum):
    NegativeLarge = 0x0
    NegativeMedium = 0x1
    NegativeSmall = 0x2
    TertiarySmall = 0x3
    TertiaryMedium = 0x4
    TertiaryLarge = 0x5
    SecondarySmall = 0x6
    SecondaryMedium = 0x7
    SecondaryLarge = 0x8
    Primary = 0x9


class cGcDiscoveryType(IntEnum):
    Unknown = 0x0
    SolarSystem = 0x1
    Planet = 0x2
    Animal = 0x3
    Flora = 0x4
    Mineral = 0x5
    Sector = 0x6
    Building = 0x7
    Interactable = 0x8
    Sentinel = 0x9
    Starship = 0xA
    Artifact = 0xB
    Mystery = 0xC
    Treasure = 0xD
    Control = 0xE
    HarvestPlant = 0xF
    FriendlyDrone = 0x10


class cGcInventoryClass(IntEnum):
    C = 0x0
    B = 0x1
    A = 0x2
    S = 0x3


class cGcExpeditionCategory(IntEnum):
    Combat = 0x0
    Exploration = 0x1
    Mining = 0x2
    Diplomacy = 0x3
    Balanced = 0x4


class cGcExpeditionDuration(IntEnum):
    VeryShort = 0x0
    Short = 0x1
    Medium = 0x2
    Long = 0x3
    VeryLong = 0x4


class cGcFrigateStatType(IntEnum):
    Combat = 0x0
    Exploration = 0x1
    Mining = 0x2
    Diplomatic = 0x3
    FuelBurnRate = 0x4
    FuelCapacity = 0x5
    Speed = 0x6
    ExtraLoot = 0x7
    Repair = 0x8
    Invulnerable = 0x9
    Stealth = 0xA


class cGcFossilCategory(IntEnum):
    None_ = 0x0
    Head = 0x1
    Body = 0x2
    Limb = 0x3
    Tail = 0x4


class cGcCurrency(IntEnum):
    Units = 0x0
    Nanites = 0x1
    Specials = 0x2


class cGcCreatureRarity(IntEnum):
    Common = 0x0
    Uncommon = 0x1
    Rare = 0x2
    SuperRare = 0x3


class cGcCorvettePartCategory(IntEnum):
    empty = 0x0
    Cockpit = 0x1
    Hab = 0x2
    Gear = 0x4
    Gun = 0x8
    Shield = 0x10
    Hull = 0x20
    Access = 0x40
    Wing = 0x80
    Engine = 0x100
    Reactor = 0x200
    Connector = 0x400
    Decor = 0x800


class cGcCatalogueGroups(IntEnum):
    MaterialsAndItems = 0x0
    CraftingAndTechnology = 0x1
    Buildables = 0x2
    Recipes = 0x3
    Wonders = 0x4


class cGcAlienRace(IntEnum):
    Traders = 0x0
    Warriors = 0x1
    Explorers = 0x2
    Robots = 0x3
    Atlas = 0x4
    Diplomats = 0x5
    Exotics = 0x6
    None_ = 0x7
    Builders = 0x8


class cGcAlienMood(IntEnum):
    Neutral = 0x0
    Positive = 0x1
    VeryPositive = 0x2
    Negative = 0x3
    VeryNegative = 0x4
    Pity = 0x5
    Sad = 0x6
    Dead = 0x7
    Confused = 0x8
    Busy = 0x9


class cGcAlienPuzzleTableIndex(IntEnum):
    Regular = 0x0
    Seeded = 0x1
    Random = 0x2


class cGcAlienPuzzleCategory(IntEnum):
    Default = 0x0
    GuildTraderNone = 0x1
    GuildTraderLow = 0x2
    GuildTraderMed = 0x3
    GuildTraderHigh = 0x4
    GuildTraderBest = 0x5
    GuildWarriorNone = 0x6
    GuildWarriorLow = 0x7
    GuildWarriorMed = 0x8
    GuildWarriorHigh = 0x9
    GuildWarriorBest = 0xA
    GuildExplorerNone = 0xB
    GuildExplorerLow = 0xC
    GuildExplorerMed = 0xD
    GuildExplorerHigh = 0xE
    GuildExplorerBest = 0xF
    BiomeHot = 0x10
    BiomeCold = 0x11
    BiomeLush = 0x12
    BiomeDusty = 0x13
    BiomeTox = 0x14
    BiomeRad = 0x15
    BiomeWeird = 0x16
    LocationSpaceStation = 0x17
    LocationShop = 0x18
    LocationOutpost = 0x19
    LocationObservatory = 0x1A
    Walking = 0x1B
    ExtremeWeather = 0x1C
    ExtremeSentinels = 0x1D
    WaterPlanet = 0x1E
    FreighterCrew = 0x1F
    FreighterCrewOwned = 0x20
    ShipShop = 0x21
    SuitShop = 0x22
    WeapShop = 0x23
    VehicleShop = 0x24
    MoodVeryPositive = 0x25
    MoodPositive = 0x26
    MoodNeutral = 0x27
    MoodNegative = 0x28
    MoodVeryNegative = 0x29
    Proc = 0x2A
    FirstAbandonedFreighter = 0x2B
    StandardAbandonedFreighter = 0x2C
    BiomeSwamp = 0x2D
    BiomeLava = 0x2E
    AbandonedSystem = 0x2F
    InhabitedSystem = 0x30
    SettlementOwned = 0x31
    SettlementNotOwned = 0x32
    PirateStation = 0x33
    StandardPilot = 0x34
    Unlocked = 0x35
    AllUnlocked = 0x36
    NotUnlocked = 0x37
    SpiderA = 0x38
    SpiderB = 0x39
    SpiderRenewed = 0x3A


class cTkUniqueContextTypes(IntEnum):
    Debug = 0x0
    Generic = 0x1
    Environment = 0x2
    Building = 0x3
    Event = 0x4
    BaseObject = 0x5
    Dungeon = 0x6


class cGcExperienceDebugTriggerActionTypes(IntEnum):
    None_ = 0x0
    Drones = 0x1
    FlyBy = 0x2
    FrigateFlyByBegin = 0x3
    FrigateFlyByEnd = 0x4
    PirateCargoAttack = 0x5
    PirateRaid = 0x6
    FreighterAttack = 0x7
    SpawnShips = 0x8
    LaunchShips = 0x9
    Mechs = 0xA
    SpaceBattle = 0xB
    PirateSpaceBattle = 0xC
    ClearPirateSpaceBattle = 0xD
    RespawnInShip = 0xE
    DebugWalker = 0xF
    DebugWalkerTitanFall = 0x10
    SpawnNexus = 0x11
    Freighters = 0x12
    NPCs = 0x13
    Sandworm = 0x14
    SpacePOI = 0x15
    BackgroundSpaceEncounter = 0x16
    Creatures = 0x17
    CameraPath = 0x18
    SummonFleet = 0x19
    SummonSquadron = 0x1A
    ResetScene = 0x1B
    ResetPlayerPos = 0x1C
    CameraSpin = 0x1D
    SpawnEnemyShips = 0x1E
    PetHappy = 0x1F
    PetSad = 0x20
    PetFollow = 0x21
    PetFollowClose = 0x22
    PetRest = 0x23
    PetNatural = 0x24
    PetMine = 0x25
    PetMineAndDeposit = 0x26
    RidePet = 0x27
    GhostShip = 0x28
    Normandy = 0x29
    LivingFrigate = 0x2A
    UpgradeSettlement = 0x2B
    SentinelFreighter = 0x2C
    ClearSpacePolice = 0x2D
    SpawnQuad = 0x2E
    SpawnSpiderQuad = 0x2F
    SpawnSpiderQuadMini = 0x30
    SpawnDockedShips = 0x31
    LaunchDockedShips = 0x32
    StartStorm = 0x33
    EndStorm = 0x34
    SpawnBugQueen = 0x35
    RemoveAllFiendsAndBugs = 0x36
    WaterTransition = 0x37


class cTkPlatformGroup(IntEnum):
    empty = 0x0
    Playfab = 0x1
    Steam = 0x2
    Playstation = 0x4
    XBox = 0x8
    Nintendo = 0x10


class cGcJourneyMedalType(IntEnum):
    Standings = 0x0
    Missions = 0x1
    Words = 0x2
    Systems = 0x3
    Sentinels = 0x4
    Pirates = 0x5
    Plants = 0x6
    Units = 0x7
    RaceCreatures = 0x8
    DistanceWarped = 0x9


class cGcJourneyCategoryType(IntEnum):
    Journey = 0x0
    SeasonHistory = 0x1
    Race = 0x2
    Guild = 0x3


class cGcMessageSummonAndDismiss(IntEnum):
    Summon = 0x0
    Dismiss = 0x1


class cTkImposterActivation(IntEnum):
    Default = 0x0
    ForceHaveImposter = 0x1
    ForceNoImposter = 0x2


class cTkImposterType(IntEnum):
    Hemispherical = 0x0
    Spherical = 0x1


class cGcActionSetType(IntEnum):
    None_ = 0x0
    FRONTEND = 0x1
    Frontend_Right = 0x2
    Frontend_Left = 0x3
    OnFootControls = 0x4
    OnFootControls_Right = 0x5
    OnFootControls_Left = 0x6
    OnFootQuickMenu = 0x7
    OnFootQuickMenu_Right = 0x8
    OnFootQuickMenu_Left = 0x9
    ShipControls = 0xA
    ShipControls_Right = 0xB
    ShipControls_Left = 0xC
    ShipQuickMenu = 0xD
    ShipQuickMenu_Right = 0xE
    ShipQuickMenu_Left = 0xF
    VehicleMode = 0x10
    VehicleMode_Right = 0x11
    VehicleMode_Left = 0x12
    VehicleQuickMenu = 0x13
    VehicleQuickMenu_Right = 0x14
    VehicleQuickMenu_Left = 0x15
    GalacticMap = 0x16
    GalacticMap_Right = 0x17
    GalacticMap_Left = 0x18
    PhotoModeMenu = 0x19
    PhotoModeMenu_Right = 0x1A
    PhotoModeMenu_Left = 0x1B
    PhotoModeMvCam = 0x1C
    PhotoModeMvCam_Right = 0x1D
    PhotoModeMvCam_Left = 0x1E
    AmbientMode = 0x1F
    DebugMode = 0x20
    TextChat = 0x21
    BuildMenuSelectionMode = 0x22
    BuildMenuSelectionMode_Right = 0x23
    BuildMenuSelectionMode_Left = 0x24
    BuildMenuPlacementMode = 0x25
    BuildMenuPlacementMode_Right = 0x26
    BuildMenuPlacementMode_Left = 0x27
    BuildMenuBiggsSelection = 0x28
    BuildMenuBiggsSelection_Right = 0x29
    BuildMenuBiggsSelection_Left = 0x2A
    BuildMenuBiggsPlacement = 0x2B
    BuildMenuBiggsPlacement_Right = 0x2C
    BuildMenuBiggsPlacement_Left = 0x2D


class cGcActionUseType(IntEnum):
    Active = 0x0
    ActiveVR = 0x1
    ActiveNonVR = 0x2
    ActiveXbox = 0x3
    ActivePS4 = 0x4
    Hidden = 0x5
    Debug = 0x6
    Obsolete = 0x7


class cGcNGuiEditorVisibility(IntEnum):
    UseData = 0x0
    Visible = 0x1
    Hidden = 0x2


class cGcScannerIconTypes(IntEnum):
    None_ = 0x0
    Health = 0x1
    Shield = 0x2
    Hazard = 0x3
    LifeSupport = 0x4
    Tech = 0x5
    BluePlant = 0x6
    CaveSubstance = 0x7
    LaunchCrystals = 0x8
    Power = 0x9
    Carbon = 0xA
    CarbonPlus = 0xB
    Oxygen = 0xC
    Mineral = 0xD
    Sodium = 0xE
    SodiumPlus = 0xF
    Crate = 0x10
    Artifact = 0x11
    Plant = 0x12
    HazardPlant = 0x13
    ArtifactCrate = 0x14
    BuriedTech = 0x15
    BuriedRare = 0x16
    Drone = 0x17
    CustomMarker = 0x18
    SignalBooster = 0x19
    Refiner = 0x1A
    Grave = 0x1B
    Rare1 = 0x1C
    Rare2 = 0x1D
    Rare3 = 0x1E
    Pearl = 0x1F
    RareEgg = 0x20
    HazardEgg = 0x21
    FishFiend = 0x22
    Clam = 0x23
    CaveStone = 0x24
    StormCrystal = 0x25
    BiomeTrophy = 0x26
    PowerHotspot = 0x27
    MineralHotspot = 0x28
    GasHotspot = 0x29
    HarvestPlant = 0x2A
    Cooker = 0x2B
    CreaturePoop = 0x2C
    FreighterTeleporter = 0x2D
    FreighterDoor = 0x2E
    FreighterTerminal = 0x2F
    FreighterHeater = 0x30
    FreighterDataPad = 0x31
    LandedPilot = 0x32
    PetEgg = 0x33
    Sandworm = 0x34
    FriendlyDrone = 0x35
    CorruptedCrystal = 0x36
    CorruptedMachine = 0x37
    RobotHead = 0x38
    HiddenCrystal = 0x39
    SpaceDestrutibleSmall = 0x3A
    SpaceDestrutibleLarge = 0x3B
    ShieldGenerator = 0x3C
    FreighterEngine = 0x3D
    FreighterWeakPoint = 0x3E
    FreighterTrenchEntrance = 0x3F
    Terrain = 0x40
    FuelAsteroid = 0x41
    Grub = 0x42
    FishPlatform = 0x43
    FishPot = 0x44
    RuinBeacon = 0x45
    SeaGlass = 0x46
    LocalWeatherHazard = 0x47
    StoneEnemy = 0x48
    BuriedFossil = 0x49
    BuriedFossilHazard = 0x4A


class cGcGenericIconTypes(IntEnum):
    None_ = 0x0
    Interaction = 0x1
    SpaceStation = 0x2
    SpaceAnomaly = 0x3
    SpaceAtlas = 0x4
    Nexus = 0x5


class cGcInventorySortOptions(IntEnum):
    None_ = 0x0
    Value = 0x1
    Type = 0x2
    Name = 0x3
    Colour = 0x4


class cGcModelViews(IntEnum):
    Suit = 0x0
    SplitSuit = 0x1
    SuitWithCape = 0x2
    Weapon = 0x3
    Ship = 0x4
    Corvette = 0x5
    SpookShip = 0x6
    Vehicle = 0x7
    DiscoveryMain = 0x8
    DiscoveryThumbnail = 0x9
    WonderThumbnail = 0xA
    WonderThumbnailCreatureSmall = 0xB
    WonderThumbnailCreatureMed = 0xC
    WonderThumbnailCreatureLarge = 0xD
    WonderThumbnailFloraSmall = 0xE
    WonderThumbnailFloraLarge = 0xF
    WonderThumbnailMineralSmall = 0x10
    WonderThumbnailMineralLarge = 0x11
    ToolboxMain = 0x12
    ToolboxThumbnail = 0x13
    TradeSuit = 0x14
    TradeShip = 0x15
    TradeCompareShips = 0x16
    TradeCompareWeapons = 0x17
    HUDThumbnail = 0x18
    Interaction = 0x19
    Freighter = 0x1A
    TradeFreighter = 0x1B
    TradeChest = 0x1C
    TradeCapsule = 0x1D
    TradeFrigate = 0x1E
    TerrainBall = 0x1F
    FreighterChest = 0x20
    Submarine = 0x21
    TradeCooker = 0x22
    SuitRefiner = 0x23
    SuitRefinerWithCape = 0x24
    FreighterRepair = 0x25
    DiscoveryPlanetaryMapping = 0x26
    Mech = 0x27
    PetThumbnail = 0x28
    PetThumbnailUI = 0x29
    PetLarge = 0x2A
    SquadronPilotLarge = 0x2B
    SquadronPilotThumbnail = 0x2C
    SquadronSpaceshipThumbnail = 0x2D
    VehicleRefiner = 0x2E
    FishingFloat = 0x2F
    ModelViewer = 0x30
    None_ = 0x31


class cGcScannerBuildingIconTypes(IntEnum):
    None_ = 0x0
    Generic = 0x1
    Shelter = 0x2
    Relic = 0x3
    Factory = 0x4
    Unknown = 0x5
    Distress = 0x6
    Beacon = 0x7
    Waypoint = 0x8
    SpaceStation = 0x9
    TechResource = 0xA
    FuelResource = 0xB
    MineralResource = 0xC
    SpaceAnomaly = 0xD
    SpaceAtlas = 0xE
    ExternalBase = 0xF
    PlanetBaseTerminal = 0x10
    Nexus = 0x11
    AbandonedFreighter = 0x12
    Telescope = 0x13
    Outpost = 0x14
    UpgradePod = 0x15
    Cog = 0x16
    Ruins = 0x17
    Portal = 0x18
    Library = 0x19
    Abandoned = 0x1A
    SmallBuilding = 0x1B
    StoryGlitch = 0x1C
    GraveInCave = 0x1D
    HoloHub = 0x1E
    Settlement = 0x1F
    DroneHive = 0x20
    SentinelDistress = 0x21
    AbandonedRobotCamp = 0x22


class cGcScannerIconHighlightTypes(IntEnum):
    Diamond = 0x0
    Hexagon = 0x1
    Tag = 0x2
    Octagon = 0x3
    Circle = 0x4


class cGcInventoryFilterOptions(IntEnum):
    All = 0x0
    Substance = 0x1
    HighValue = 0x2
    Consumable = 0x3
    Deployable = 0x4


class cGcFontTypesEnum(IntEnum):
    Impact = 0x0
    Bebas = 0x1
    GeosansLightWide = 0x2
    GeosansLight = 0x3
    GeosansLightMedium = 0x4
    GeosansLightSmall = 0x5
    Segoeuib = 0x6
    Segoeui32 = 0x7


class cGcScreenFilters(IntEnum):
    Default = 0x0
    DefaultStorm = 0x1
    Frozen = 0x2
    FrozenStorm = 0x3
    Toxic = 0x4
    ToxicStorm = 0x5
    Radioactive = 0x6
    RadioactiveStorm = 0x7
    Scorched = 0x8
    ScorchedStorm = 0x9
    Barren = 0xA
    BarrenStorm = 0xB
    Weird1 = 0xC
    Weird2 = 0xD
    Weird3 = 0xE
    Weird4 = 0xF
    Weird5 = 0x10
    Weird6 = 0x11
    Weird7 = 0x12
    Weird8 = 0x13
    Vintage = 0x14
    HyperReal = 0x15
    Desaturated = 0x16
    Amber = 0x17
    GBGreen = 0x18
    Apocalypse = 0x19
    Diffusion = 0x1A
    Green = 0x1B
    BlackAndWhite = 0x1C
    Isolation = 0x1D
    Sepia = 0x1E
    Filmic = 0x1F
    GBGrey = 0x20
    Binoculars = 0x21
    Surveying = 0x22
    Nexus = 0x23
    SpaceStation = 0x24
    Freighter = 0x25
    FreighterAbandoned = 0x26
    Frigate = 0x27
    MissionSurvey = 0x28
    NewVibrant = 0x29
    NewVibrantBright = 0x2A
    NewVibrantWarm = 0x2B
    NewVintageBright = 0x2C
    NewVintageWash = 0x2D
    Drama = 0x2E
    MemoryBold = 0x2F
    Memory = 0x30
    MemoryWash = 0x31
    Autumn = 0x32
    AutumnFade = 0x33
    ClassicBright = 0x34
    Classic = 0x35
    ClassicWash = 0x36
    BlackAndWhiteDream = 0x37
    ColourTouchB = 0x38
    ColourTouchC = 0x39
    NegativePrint = 0x3A
    SepiaExtreme = 0x3B
    Solarise = 0x3C
    TwoToneStrong = 0x3D
    TwoTone = 0x3E
    Dramatic = 0x3F
    Fuchsia = 0x40
    Violet = 0x41
    Cyan = 0x42
    GreenNew = 0x43
    AmberNew = 0x44
    Red = 0x45
    HueShiftA = 0x46
    HueShiftB = 0x47
    HueShiftC = 0x48
    HueShiftD = 0x49
    WarmStripe = 0x4A
    NMSRetroA = 0x4B
    NMSRetroB = 0x4C
    NMSRetroC = 0x4D
    NMSRetroD = 0x4E
    NMSRetroE = 0x4F
    NMSRetroF = 0x50
    NMSRetroG = 0x51
    CorruptSentinels = 0x52
    DeepWater = 0x53


class cGcStatsAchievements(IntEnum):
    FirstWarp = 0x0
    FirstDiscovery = 0x1


class cGcStatsOneShotTypes(IntEnum):
    ShipLanded = 0x0
    ShipLaunched = 0x1
    ShipWarped = 0x2
    WeaponFired = 0x3


class cGcStatsValueTypes(IntEnum):
    DistanceJetpacked = 0x0
    DistanceWalked = 0x1
    DistanceWarped = 0x2
    DamageSustained = 0x3


class cGcStatTrackType(IntEnum):
    Set = 0x0
    Add = 0x1
    Max = 0x2
    Min = 0x3


class cGcStatType(IntEnum):
    Int = 0x0
    Float = 0x1
    AvgRate = 0x2


class cGcStatModifyType(IntEnum):
    Set = 0x0
    Add = 0x1
    Subtract = 0x2


class cGcPetVocabularyWords(IntEnum):
    Attack = 0x0
    Dislike = 0x1
    Cute = 0x2
    Good = 0x3
    Happy = 0x4
    Hostile = 0x5
    Like = 0x6
    Lonely = 0x7
    Loved = 0x8
    Noise = 0x9
    OwnerLove = 0xA
    SummonedTrait = 0xB
    Hungry = 0xC
    Tickles = 0xD
    Yummy = 0xE


class cGcSpecialPetChatType(IntEnum):
    Monster = 0x0
    Quad = 0x1
    MiniRobo = 0x2


class cGcStatusMessageMissionMarkup(IntEnum):
    KillFiend = 0x0
    KillPirate = 0x1
    KillSentinel = 0x2
    KillHazardousPlants = 0x3
    KillTraders = 0x4
    KillCreatures = 0x5
    KillPredators = 0x6
    KillDepot = 0x7
    KillWorms = 0x8
    KillSpookSquids = 0x9
    FeedCreature = 0xA
    CollectBones = 0xB
    CollectScrap = 0xC
    Discover = 0xD
    CollectSubstanceProduct = 0xE
    Build = 0xF
    Always = 0x10
    None_ = 0x11


class cGcStatDisplayType(IntEnum):
    None_ = 0x0
    Sols = 0x1
    Distance = 0x2


class cGcFriendlyDroneChatType(IntEnum):
    Summoned = 0x0
    Unsummoned = 0x1
    BecomeWanted = 0x2
    LoseWanted = 0x3
    Idle = 0x4


class cGcPetChatType(IntEnum):
    Adopted = 0x0
    Hatched = 0x1
    Summoned = 0x2
    Greeting = 0x3
    Hazard = 0x4
    Scanning = 0x5
    PositiveEmote = 0x6
    HungryEmote = 0x7
    LonelyEmote = 0x8
    Go_There = 0x9
    Come_Here = 0xA
    Planet = 0xB
    Mine = 0xC
    Attack = 0xD
    Chase = 0xE
    ReceivedTreat = 0xF
    Tickled = 0x10
    Ride = 0x11
    Egg_Laid = 0x12
    Customise = 0x13
    Unsummoned = 0x14


class cGcInteractionBufferType(IntEnum):
    Distress_Signal = 0x0
    Crate = 0x1
    Destructable = 0x2
    Terrain = 0x3
    Cost = 0x4
    Building = 0x5
    Creature = 0x6
    Maintenance = 0x7
    Personal = 0x8
    Personal_Maintenance = 0x9
    FireteamSync = 0xA


class cGcSynchronisedBufferType(IntEnum):
    Refiner = 0x0
    Example1 = 0x1
    Example2 = 0x2
    Example3 = 0x3


class cGcTeleporterType(IntEnum):
    Base = 0x0
    Spacestation = 0x1
    Atlas = 0x2
    PlanetAwayFromShip = 0x3
    ExternalBase = 0x4
    EmergencyGalaxyFix = 0x5
    OnNexus = 0x6
    SpacestationFixPosition = 0x7
    Settlement = 0x8
    Freighter = 0x9


class cGcSeasonEndRewardsRedemptionState(IntEnum):
    None_ = 0x0
    Available = 0x1
    PendingRedemption = 0x2
    Redeemed = 0x3


class cGcSeasonSaveStateOnDeath(IntEnum):
    Standard = 0x0
    ResetAndQuit = 0x1
    ResetPosSaveAndQuit = 0x2
    SaveAndQuit = 0x3


class cGcSettlementTowerPower(IntEnum):
    EarnNavigationData = 0x0
    ScanForBuildings = 0x1
    ScanForAnomalies = 0x2
    ScanForCrashedShips = 0x3


class cGcPlayerMissionParticipantType(IntEnum):
    None_ = 0x0
    MissionGiver = 0x1
    MissionGiverReference = 0x2
    Primary = 0x3
    Secondary1 = 0x4
    Secondary2 = 0x5
    Secondary3 = 0x6
    Secondary4 = 0x7
    Secondary5 = 0x8
    Secondary6 = 0x9
    Secondary7 = 0xA
    Secondary8 = 0xB
    Secondary9 = 0xC


class cGcGameMode(IntEnum):
    Unspecified = 0x0
    Normal = 0x1
    Creative = 0x2
    Survival = 0x3
    Ambient = 0x4
    Permadeath = 0x5
    Seasonal = 0x6


class cGcFreighterNPCType(IntEnum):
    SquadronPilot = 0x0
    FrigateCaptain = 0x1
    WorkerBio = 0x2
    WorkerTech = 0x3
    WorkerIndustry = 0x4


class cGcNPCNavSubgraphNodeType(IntEnum):
    Path = 0x0
    Connection = 0x1
    PointOfInterest = 0x2


class cGcPersistentBaseTypes(IntEnum):
    HomePlanetBase = 0x0
    FreighterBase = 0x1
    ExternalPlanetBase = 0x2
    CivilianFreighterBase = 0x3
    FriendsPlanetBase = 0x4
    FriendsFreighterBase = 0x5
    SpaceBase = 0x6
    GeneratedPlanetBase = 0x7
    GeneratedPlanetBaseEdits = 0x8
    PlayerShipBase = 0x9
    FriendsShipBase = 0xA
    UITempShipBase = 0xB
    ShipBaseScratch = 0xC


class cGcBuildMenuOption(IntEnum):
    Place = 0x0
    ChangeColour = 0x1
    FreeRotate = 0x2
    Scale = 0x3
    SnapRotate = 0x4
    Move = 0x5
    Duplicate = 0x6
    Delete = 0x7
    ToggleBuildCam = 0x8
    ToggleSnappingAndCollision = 0x9
    ToggleSelectionMode = 0xA
    ToggleWiringMode = 0xB
    ViewRelatives = 0xC
    CyclePart = 0xD
    PlaceWire = 0xE
    CycleRotateMode = 0xF
    Flip = 0x10
    ToggleCatalogue = 0x11
    Purchase = 0x12
    FamiliesRotate = 0x13
    YFlip = 0x14


class cGcLinkNetworkTypes(IntEnum):
    Power = 0x0
    Resources = 0x1
    Fuel = 0x2
    Portals = 0x3
    PlantGrowth = 0x4
    ByteBeat = 0x5


class cGcNPCHabitationType(IntEnum):
    WeaponsExpert = 0x0
    Farmer = 0x1
    Builder = 0x2
    Vehicles = 0x3
    Scientist = 0x4


class cGcBuildingPlacementErrorTypes(IntEnum):
    Offline = 0x0
    InvalidBiome = 0x1
    InvalidAboveWater = 0x2
    InvalidUnderwater = 0x3
    PlanetLimitReached = 0x4
    BaseLimitReached = 0x5
    RegionLimitReached = 0x6
    InvalidMaxBasesReached = 0x7
    InvalidOverlappingAnyBase = 0x8
    InvalidOverlappingSettlement = 0x9
    InvalidOverlappingBase = 0xA
    OutOfBaseRange = 0xB
    OutOfConnectionRange = 0xC
    LinkGridMismatch = 0xD
    InsufficientResources = 0xE
    ComplexityLimitReached = 0xF
    SubstanceOnly = 0x10
    InvalidPosition = 0x11
    InvalidSnap = 0x12
    MustPlaceOnTerrain = 0x13
    MustPlaceWithSnap = 0x14
    Collision = 0x15
    ShipInside = 0x16
    PlayerInside = 0x17
    InvalidCorvettePosition = 0x18


class cGcBaseBuildingSecondaryMode(IntEnum):
    ShipStructural = 0x0


class cGcBaseSnapState(IntEnum):
    IsSnapped = 0x0
    NotSnapped = 0x1


class cGcBaseBuildingPartStyle(IntEnum):
    None_ = 0x0
    Wood = 0x1
    Metal = 0x2
    Concrete = 0x3
    Stone = 0x4
    Timber = 0x5
    Fibreglass = 0x6
    Builders = 0x7
    BIGGS_A = 0x8
    BIGGS_B = 0x9
    BIGGS_C = 0xA
    BIGGS_D = 0xB
    BIGGS_Empty0 = 0xC
    BIGGS_Toilet0 = 0xD
    BIGGS_Kitchen0 = 0xE
    BIGGS_Bunk0 = 0xF
    BIGGS_Cargo0 = 0x10
    BIGGS_Cargo1 = 0x11
    BIGGS_Cargo2 = 0x12
    BIGGS_Cargo3 = 0x13
    BIGGS_Cargo4 = 0x14
    BIGGS_Cargo5 = 0x15
    BIGGS_Cargo6 = 0x16
    BIGGS_Cargo7 = 0x17
    BIGGS_Cargo8 = 0x18
    BIGGS_Cargo9 = 0x19
    BIGGS_Med0 = 0x1A
    BIGGS_Tech0 = 0x1B
    BIGGS_Tech1 = 0x1C
    BIGGS_Window0 = 0x1D
    BIGGS_Window1 = 0x1E
    BIGGS_Window2 = 0x1F
    BIGGS_Planter0 = 0x20
    BIGGS_STR_A = 0x21
    BIGGS_STR_B = 0x22
    BIGGS_STR_C = 0x23
    BIGGS_STR_D = 0x24
    BIGGS_STR_E = 0x25
    BIGGS_STR_F = 0x26
    BIGGS_STR_G = 0x27
    BIGGS_STR_H = 0x28
    BIGGS_STR_I = 0x29
    BIGGS_STR_J = 0x2A
    BIGGS_STR_K = 0x2B
    BIGGS_STR_L = 0x2C
    BIGGS_STR_M = 0x2D
    BIGGS_STR_N = 0x2E
    BIGGS_STR_O = 0x2F
    BIGGS_STR_P = 0x30
    BIGGS_STR_Q = 0x31
    BIGGS_STR_R = 0x32
    BIGGS_STR_S = 0x33


class cGcBaseBuildingMode(IntEnum):
    Inactive = 0x0
    Selection = 0x1
    Placement = 0x2
    Browse = 0x3
    Relatives = 0x4


class cGcBaseAutoPowerSetting(IntEnum):
    UseDefault = 0x0
    ForceDisabled = 0x1
    ForceEnabled = 0x2


class cGcBaseBuildingCameraMode(IntEnum):
    Inactive = 0x0
    FreeCam = 0x1
    FocusCam = 0x2
    OrbitCam = 0x3


class cGcBaseBuildingObjectDecorationTypes(IntEnum):
    Normal = 0x0
    SurfaceNormal = 0x1
    Ceiling = 0x2
    Terrain = 0x3
    Substance = 0x4
    Plant = 0x5
    BuildingSurfaceNormal = 0x6
    WaterSurface = 0x7


class cGcSettlementConstructionLevel(IntEnum):
    Start = 0x0
    GroundStorey = 0x1
    RegularStorey = 0x2
    Roof = 0x3
    Decoration = 0x4
    Upgrade1 = 0x5
    Upgrade2 = 0x6
    Upgrade3 = 0x7
    Other = 0x8


class cGcSettlementJudgementType(IntEnum):
    None_ = 0x0
    StrangerVisit = 0x1
    Policy = 0x2
    NewBuilding = 0x3
    BuildingChoice = 0x4
    Conflict = 0x5
    Request = 0x6
    BlessingPerkRelated = 0x7
    JobPerkRelated = 0x8
    ProcPerkRelated = 0x9
    UpgradeBuilding = 0xA
    UpgradeBuildingChoice = 0xB


class cGcSettlementStatType(IntEnum):
    MaxPopulation = 0x0
    Happiness = 0x1
    Production = 0x2
    Upkeep = 0x3
    Sentinels = 0x4
    Debt = 0x5
    Alert = 0x6
    BugAttack = 0x7


class cGcSentinelCoverState(IntEnum):
    Deploying = 0x0
    Deployed = 0x1
    ShuttingDown = 0x2
    ShutDown = 0x3


class cGcEncounterType(IntEnum):
    FactoryGuards = 0x0
    HarvesterGuards = 0x1
    ScrapHeap = 0x2
    Reward = 0x3
    CorruptedDroneInteract = 0x4
    GroundWorms = 0x5
    DroneHiveGuards = 0x6
    CorruptDronePillar = 0x7
    Fossil = 0x8


class cGcFiendCrime(IntEnum):
    None_ = 0x0
    EggDamaged = 0x1
    EggDestroyed = 0x2
    EggCollected = 0x3
    UnderwaterPropDamaged = 0x4
    UnderwaterPropCollected = 0x5
    RockTransform = 0x6
    GroundPropDamage = 0x7
    ShotWorm = 0x8
    Carnage = 0x9
    FishCarnage = 0xA
    Bugs = 0xB
    JellyBoss = 0xC


class cGcAntagonistGroup(IntEnum):
    Player = 0x0
    Fiends = 0x1
    Creatures = 0x2
    Sentinels = 0x3
    Turrets = 0x4
    Walls = 0x5


class cGcCombatEffectType(IntEnum):
    None_ = 0x0
    Fire = 0x1
    Stun = 0x2
    Slow = 0x3
    ElectricDOT = 0x4
    SpookyLight = 0x5


class cGcTrackedPosition(IntEnum):
    GameCamera = 0x0
    ActiveCamera = 0x1
    DebugCamera = 0x2
    Frozen = 0x3


class cGcFonts(IntEnum):
    Body = 0x0
    Title = 0x1
    Console1 = 0x2
    Console2 = 0x3


class cGcByteBeatToken(IntEnum):
    T = 0x0
    AND = 0x1
    OR = 0x2
    XOR = 0x3
    Plus = 0x4
    Minus = 0x5
    Multiply = 0x6
    Divide = 0x7
    Modulo = 0x8
    ShiftLeft = 0x9
    ShiftRight = 0xA
    Greater = 0xB
    GreaterEqual = 0xC
    Less = 0xD
    LessEqual = 0xE
    Number = 0xF
    OpenParenthesis = 0x10
    CloseParenthesis = 0x11


class cGcAudioWwiseRTPCs(IntEnum):
    INVALID_RTPC = 0x0
    BASE_BATTERY_CHARGING = 0x7C13B3BA
    BASE_SPHERE_ROLLSPEED = 0xB7D53D81
    BINOCULARS_EFFECT = 0x65306505
    BURN_INTENSITY = 0x8B1E9F48
    BYTEBEAT_FX = 0xDC013338
    BYTEBEAT_RMS = 0xA3155F70
    COMMS_CHATTER_DISTANCE = 0x7A371A94
    COMMS_CHATTER_FREIGHTERATTACKED = 0x46A238DC
    COMMS_CHATTER_PIRATES = 0x54E82B11
    COMMS_CHATTER_POLICE = 0xD547E7BB
    CREATURE_EXISTENCE = 0xBBAE19A3
    CREATURES_STEP_SIZE = 0xE1067D02
    DOPPLER_DROID_SMALL = 0x1F092F38
    GAMEOBJECT_DISTANCE = 0x8EB54518
    GLOBAL_HAZARD_LEVEL = 0xFDD1B808
    GLOBAL_HEALTH_LEVEL = 0x2A61033E
    GLOBAL_SHIELD_LEVEL = 0xEA9FE763
    HG_VA_EMOTE = 0x181937FF
    HG_VA_GAMEOBJECTS = 0x8904C9A1
    HG_VA_HEADBODYRATIO = 0xF6293C64
    HG_VA_SEED = 0x232F7C0E
    HG_VA_SIZE = 0x2E25003A
    INTERACT_TIMER = 0x1EE7B825
    JETPACK_HEIGHT = 0x70B5E6C1
    MAP_STAR_WOOSH = 0xBC7AB0AD
    MASTER_CHAT_LEVEL = 0x5B8E4667
    MASTER_MUSIC_LEVEL = 0xF8F6ACB4
    MASTER_SFX_LEVEL = 0xC9C3F2F8
    MASTER_VOICE_LEVEL = 0xDCB64A17
    MECH_IDLE = 0xBB021D37
    METEORITE_INCOMING = 0xCFBF792E
    MOTION_DRIVER_A = 0x732F78BC
    MOTION_DRIVER_B = 0x732F78BF
    MUS_FISHING = 0x6999BC45
    NPC_SHIP_DISTANCE = 0x810FD033
    NPC_SHIP_DOPPLER = 0xD8BAE8F6
    NPC_SHIP_SPEED = 0x925EFD57
    PL_AMB_HEIGHT = 0x12F4388A
    PL_ATLASGUN = 0xF17B2015
    PL_CAVE_ENCLOSED = 0x99475573
    PL_EXERTION = 0x9C64F46C
    PL_FALL_SPEED = 0x76233CFB
    PL_FOLEY_CLOTHING_LOCO_SPEED = 0x8B826A1A
    PL_HAZARD_PROTECTION = 0x7EF62492
    PL_SHIP_HEIGHT = 0xFEF18CB4
    PL_SHIP_LANDINGDISTANCE = 0xC99A4E93
    PL_SHIP_SPEED = 0xD26BA1DA
    PL_SHIP_SPEED_REV = 0x9407EEA4
    PL_SHIP_SURFACE_WATER = 0xC99CF8A6
    PL_SHIP_THRUST = 0xE61896C3
    PL_SHIP_VR_EXIT = 0x88814C78
    PL_SHIP_YAW = 0x9142CD7A
    PL_UNDERWATER_DEPTH = 0x72C84A65
    PL_WALK_SPEED = 0x5BF0E7CB
    PL_WPN_LASER_RESOURCEGATHER = 0x767BB3A5
    PL_WPN_LASERPOWER = 0x9918F44C
    PL_WPN_NUMBEROFBULLETS = 0x3CF9013F
    PL_WPN_OVERHEAT = 0x96D534DC
    PLANET_TIME = 0x4C034D71
    PLAYER_VR_FOLEY_ARMS = 0xBA619E61
    POD_SQUISH = 0x47DC0016
    PROTOROLLER = 0x98F8B9B1
    PS5_HEADPHONES = 0x6B9EA36F
    PULSE_BUS01_MASTER_VOLUME = 0x42E24B14
    PULSE_EVENT_PANFR = 0xF714E8C1
    PULSE_EVENT_PANLR = 0x114F803
    PULSE_EVENT_PITCH = 0x70C3F202
    PULSE_EVENT_SENDBUS_00 = 0xB0196737
    PULSE_EVENT_SENDBUS_01 = 0xB0196736
    PULSE_EVENT_SENDBUS_02 = 0xB0196735
    PULSE_EVENT_SENDBUS_03 = 0xB0196734
    PULSE_EVENT_VOLUME = 0xCE889A56
    QUAD_LASERBUILDUP = 0x84FF38B3
    RAIN_INTENSITY = 0x9637D55D
    RAIN_INTENSITY_BUILDING = 0x83ACB2F0
    RAIN_ROOF = 0xFAC73584
    RAIN_SHIP_EXTERIOR = 0xCB736AFD
    RUMBLE_INTENSITY = 0x81780120
    SENTINEL_DETECTOR = 0x8157313E
    SETTLEMENT_DISTANCE = 0x4B8316B2
    SETTLEMENT_INTENSITY = 0x11CAF8FA
    SHIP_BUILDABLE_SIZE = 0x74118A72
    SHIP_WATER_LANDING = 0x1315AFAF
    SHORELINE = 0x1A1A962
    SHUTTLE_THRUST = 0x51D5A621
    SQUADRON_SHIPS = 0x199ACEC2
    STORM = 0x648999E0
    SUITVOICE_RMS = 0x8843E23
    THEREMIN_PITCH = 0xD774D3B8
    THEREMIN_VOLUME = 0x26294964
    UI_VR_MENU = 0x2C7EDD8C
    VEHICLE_EXIT = 0xF4378552
    VEHICLE_IMPACTS = 0x855298E7
    VEHICLE_JUMP = 0x1E1DDD32
    VEHICLE_SKID = 0xA1303CF3
    VEHICLE_SPEED = 0x5979CECB
    VEHICLE_SUSPENSION = 0x3016F2FD
    VEHICLE_TORQUE = 0x480D482C
    WALKER_MOOD = 0xFB1B461B
    WAVE_INTENSITY = 0xC532D3F8
    WPN_PL_JAVELIN_CHARGE = 0xF04467B0
    WPN_PL_NEUTRON_CANNON_CHARGE = 0x60C92E72


class cGcBasePartAudioLocation(IntEnum):
    None_ = 0x0
    Freighter_SpaceWalk = 0x1
    Freighter_BioRoom = 0x2
    Freighter_TechRoom = 0x3
    Freighter_IndustrialRoom = 0x4


class cGcByteBeatEnvelope(IntEnum):
    Short = 0x0
    Med = 0x1
    Long = 0x2


class cGcByteBeatWave(IntEnum):
    SawTooth = 0x0
    Sine = 0x1
    Square = 0x2
    Triangle = 0x3


class cGcAudioWwiseEvents(IntEnum):
    INVALID_EVENT = 0x0
    ABANDONED_DOOR_UNLOCK = 0x264BED2D
    ABANDONED_FIEND_IDLE = 0x187DE821
    ABANDONED_FIEND_ROAR = 0xD6403FEF
    ABANDONED_FIEND_RUN = 0xF4780FEE
    ABANDONED_FIEND_SPIT = 0x81754059
    ABANDONED_FIEND_WALK = 0xC8910DD0
    ABANDONED_JELLYFISH_DEATH = 0x439E085F
    ABANDONED_JELLYFISH_SWIM = 0x4DD7469F
    AF_CAPSULE = 0x4CDD3358
    AF_DOOR_PRESSURISING = 0x24E7DF92
    AF_DOOR_PRESSURISING1 = 0xAB04F2E7
    AF_DOOR_PRESSURISING2 = 0xAB04F2E4
    AF_DOOR_PRESSURISING3 = 0xAB04F2E5
    AF_EXPLODINGCAPSULE = 0x5F8A1444
    AF_FAN = 0xA5F03712
    AF_ROTATINGDEVICE = 0x9BBD3FD5
    AMB_ABANDONEDBUILDING = 0x4C987896
    AMB_ABANDONEDBUILDING_STOP = 0xA891AC5
    AMB_ANCIENTGUARDIAN = 0xAED37253
    AMB_BLACKHOLE = 0x7A8710CD
    AMB_BUILDING_START = 0x143EDD47
    AMB_BUILDING_STOP = 0x5CE58FED
    AMB_FREIGHTER_INTERNAL = 0x5F322152
    AMB_FRIGATE = 0xC397F586
    AMB_NEBULA_STORM = 0x9B1672B5
    AMB_NEXUS = 0xB15F1A93
    AMB_PLANET_ALL = 0xB0FEDFC0
    AMB_PLANET_ALL_STOP = 0x870A61EF
    AMB_RAIN_SURFACE = 0xD5115048
    AMB_RAIN_SURFACE_STOP = 0x31243A67
    AMB_SETTLEMENT_HUB = 0x297F17E3
    AMB_SPACESTATION_HANGER = 0xEC3F2892
    AMB_WEATHER_THUNDER = 0xEA8B35F9
    AMB_WEATHER_THUNDER_STOP = 0x7A68768C
    AMBIENT_EMPHASISER = 0x62B568C5
    ANIMATEDDOOR_CLOSE = 0xD135F2D3
    ANIMATEDDOOR_OPEN = 0x93B90D65
    ANOMALY_CORE = 0x95FDDC1A
    ANOMALY_DOOR_CLOSE = 0xE7C7565A
    ANOMALY_DOOR_OPEN = 0xF376E95E
    ANOMALY_MAINAIRLOCK_CLOSE = 0x97933C38
    ANOMALY_MAINAIRLOCK_OPEN = 0x7A31D97C
    ANOMALY_SIMULATION_CONSOLE_END = 0xC89FD926
    ANOMALY_SIMULATION_CONSOLE_FLASH = 0x4D525F5B
    ANOMALY_SIMULATION_CONSOLE_START = 0x226E710D
    ANOMALY_SIMULATION_LIGHTSOFF = 0x5C36AC25
    ANOMALY_SIMULATION_LIGHTSON = 0x32B01899
    ANOMALY_SIMULATION_REVEAL_OPEN = 0xAF06F8C5
    ANOMALY_SIMULATION_TERMINAL_DIE = 0xD6AD5022
    ANOMALY_WEAPONCRATE_CLOSE = 0xE35624E5
    ANOMALY_WEAPONCRATE_OPEN = 0x8A1736EF
    ANTATTACK2 = 0x5BCBDC96
    ANTELOPE2LEGPOUNCE1 = 0x26DF7660
    ANTELOPEATTACK3 = 0xD81B03CA
    ANTELOPEROAR = 0xCB03FA5B
    ANTELOPESHAKE = 0x60DF35B
    ANTELOPETWOLEGATTACK = 0xF74CC245
    ANTELOPETWOLEGATTACK2 = 0x92D5D2AD
    ANTELOPETWOLEGATTACK3 = 0x92D5D2AC
    ANTELOPETWOLEGPOUNCE2 = 0x633AFD2F
    ANTELOPETWOLEGPOUNCE3 = 0x633AFD2E
    ANTELOPETWOLEGROAR = 0xA2B4EF51
    ANTELOPETWOPERFORM = 0x1627CCF6
    ANTPOUNCE1 = 0x2DD423DB
    ANTPOUNCE02 = 0xFEF4701C
    ANTPOUNCE03 = 0xFEF4701D
    ARTHROPOD_ATTACK01 = 0xBEEF8EA0
    ARTHROPOD_EAT = 0x84FB32FD
    ARTHROPOD_POUNCE = 0x6CC98D93
    ARTHROPOD_QUEEN_ATTACK01 = 0xD1C4F58D
    ARTHROPOD_QUEEN_BIRTHING = 0x8FF2DCC5
    ARTHROPOD_QUEEN_BOUNCE = 0x5094F4D0
    ARTHROPOD_QUEEN_EAT = 0x891AA586
    ARTHROPOD_QUEEN_GROUNDAPPEAR = 0xFFAAAEDA
    ARTHROPOD_QUEEN_POUNCE01 = 0xACDB5EDF
    ARTHROPOD_QUEEN_ROAR = 0x32B5FCF4
    ARTHROPOD_QUEEN_SPIT = 0xC97180DA
    ASTEROID_EXPLODE = 0xF91DD0FC
    ASTEROID_HIT = 0xFE51061C
    ATLAS_ARCH = 0xA4494F25
    ATLAS_BALLOFLIGHT = 0x9E3D0CB
    ATLAS_CORE = 0xBC1CE2F8
    ATLAS_CORE_ACTIVATE = 0x916A8160
    ATLAS_CORE_INTERACT = 0x4734CC65
    ATLAS_GALAXY_SPIN_LP = 0x68977FD7
    ATLAS_GALAXYBEAM = 0xC5B56B54
    ATLAS_GALAXYSTART_MULTIPLE = 0xA3DFC892
    ATLAS_GALAXYSTART_SINGLE = 0x1D6B1966
    ATLAS_INTERFACE_GALAXY_SPIN = 0xC1D86B30
    ATLAS_INTERFACE_TRIGGER = 0xFCA6F003
    ATLAS_ORB_FLARE = 0xA3217125
    ATLAS_ORB_ILLUMINATE = 0x1736FCDD
    ATLAS_PLINTH_RISE = 0x8464FB10
    ATLAS_SEED_01 = 0x82B25AB8
    ATLAS_SEED_02 = 0x82B25ABB
    ATLAS_SEED_03 = 0x82B25ABA
    ATLAS_SEED_04 = 0x82B25ABD
    ATLAS_SEED_05 = 0x82B25ABC
    ATLAS_SPHERE_PULSE = 0x6F545734
    ATLAS_SPHERE_SPARK = 0xC0F94248
    ATLAS_SPHERE_WIND = 0x59F53DC7
    ATLAS_VANISH = 0x1DBBF4C
    ATLASCORRUPTED_LP = 0x41327075
    ATLASCORRUPTED_LP_STOP = 0x276E5E18
    ATLASCORRUPTED_START = 0xEBCD5933
    ATLASINTERACT_CLOSE = 0xFAED1D89
    ATLASINTERACT_OPEN = 0xFFC5D75B
    ATLASSTARTSCENEORB_ACTIVATE = 0x3F60B597
    ATLASSTARTSCENEORB_ACTIVATEIDLE = 0x10DCFBD1
    ATLASSTARTSCENEORB_DISMISS = 0x3F5AD170
    ATLASSTARTSCENEORB_END = 0x4855A843
    ATLASSTARTSCENEORB_IDLE = 0x4123CCDA
    BASE_AQUARIUM = 0x4A30FB0
    BASE_BATTERY_CHARGING = 0x7C13B3BA
    BASE_BATTERY_DISCHARGING = 0x230E6054
    BASE_BATTERY_FULLYCHARGED = 0x36F5BDDF
    BASE_BATTERY_FULLYDISCHARGED = 0xC50227AD
    BASE_BIOFUELCHARGED = 0xE43B51CF
    BASE_BIOFUELDISCHARGED = 0xDF54E5D
    BASE_BIOFUELRUNNING = 0xBE89F34E
    BASE_CALCISHROOM = 0xDFC60F7F
    BASE_CUBEGADGET = 0x35F1697A
    BASE_CYCLONIC_LATHE = 0xEC4E25A8
    BASE_DOOR_CLOSE = 0xF5C07B4C
    BASE_DOOR_OPEN = 0xAB8E00D8
    BASE_ELECTRICALWIRING_DELETE = 0x94811EC9
    BASE_ELECTRICALWIRING_PLACE = 0x1D81BC71
    BASE_ELECTRICCUBE = 0x78527FE3
    BASE_FORCEFIELD_DOOR = 0xCEB18629
    BASE_GARAGE_DOOR_CLOSE = 0x3935565C
    BASE_GARAGE_DOOR_OPEN = 0x1B8E3148
    BASE_GASEXTRACTOR = 0x6F563648
    BASE_GASEXTRACTOR_OFF = 0x6270A7CE
    BASE_LARGEMONITORSTATION = 0x1B3F5918
    BASE_LIGHTBOX = 0xDA4C4B9A
    BASE_MINERALEXTRACTOR = 0x44AD4073
    BASE_MINERALEXTRACTOR_OFF = 0x1CB23CA5
    BASE_MONITORSTATION = 0x703BBA57
    BASE_OSCILLOSCOPE = 0x8603C216
    BASE_PIPE_DELETE = 0x987092CD
    BASE_PIPE_PLACE = 0x280CACAD
    BASE_POCKETREALITYGENERATOR = 0x95D9B358
    BASE_POWER_CONNECT = 0xA8DC0783
    BASE_POWER_OFF = 0x9E862FCE
    BASE_POWER_ON = 0x72477AB0
    BASE_POWER_POWERDOWN = 0xB0EC3B5A
    BASE_POWER_POWERUP = 0x6627C5F9
    BASE_POWER_SWITCH_OFF = 0x6BD0C41D
    BASE_POWER_SWITCH_ON = 0xED8BA271
    BASE_POWERFLOW_OFF = 0xB0E54966
    BASE_POWERFLOW_ON = 0x7E373308
    BASE_SERVER = 0x6DD9D114
    BASE_SOL_CLOSE = 0x9AA926CC
    BASE_SOL_OPEN = 0x53FBD758
    BASE_SOLARPANEL_CLOSE = 0xCF003B2B
    BASE_SOLARPANEL_OPEN = 0xF241066D
    BASE_SPHERECREATE = 0x304F20F2
    BASE_SPHEREROLL = 0x5D2DB27F
    BASEBEACON = 0xA2D231B2
    BASEBUILD_ITEM_BEACON = 0xE011D583
    BASEBUILD_ITEM_COMMUNICATIONSSTATION = 0x91C32F14
    BASEBUILD_ITEM_COMMUNICATIONSSTATION_ACCEPT = 0xFF644EEF
    BASEBUILD_ITEM_COMMUNICATIONSSTATION_CANCEL = 0x1855CDED
    BASEBUILD_ITEM_CONSTRUCTIONTERMINAL = 0x5FF59BA4
    BASEBUILD_ITEM_PLANTINCUBATOR = 0xED58F63F
    BASEBUILD_ITEM_SCIENCETERMINAL = 0x99231F73
    BASEBUILD_ITEM_SIGNALBOOSTER_LOOP = 0xF746FF22
    BASEBUILD_ITEM_SIGNALBOOSTER_START = 0xDD70498C
    BASEBUILD_ITEM_TERMINALGENERIC = 0xC8E2F31A
    BASEBUILD_ITEM_WEAPONTERMINAL = 0xB15A99B7
    BASESHOP_OPEN = 0xC0D6FE45
    BASETERMINAL = 0x71FD32FE
    BEACON_TRIGGER_START = 0x9B8CB96D
    BEACON_TRIGGER_STOP = 0x819AACAF
    BEAMSTONE = 0x8EC94FFF
    BEETLE_FLY = 0xB990B31A
    BEETLE_WALK = 0x8AD063BC
    BINOCULARS_ENTER = 0x9FD4BC6C
    BINOCULARS_EXIT = 0x3EEB7CAE
    BINOCULARS_ZOOM01 = 0xBCD75A
    BINOCULARS_ZOOM02 = 0xBCD759
    BINOCULARS_ZOOM03 = 0xBCD758
    BLACKHOLE_WARP = 0x4F9D6EE1
    BLD_ALARM_LP = 0x2CC0151E
    BLD_ALARM_LP_STOP = 0x42B994FD
    BLD_AMB_ATM = 0x16C1B9A5
    BLD_AMB_DEBRISLARGE = 0xFC66BDC7
    BLD_AMB_DEPOTS = 0x793F92E
    BLD_AMB_DEPOTS_STOP = 0x6A9C012D
    BLD_BLACKBOX_OPEN = 0x3BBECA3F
    BLD_DAMAGEDMACH_BEAM = 0xE5821724
    BLD_DEBRISLARGE_OPEN = 0x6829FAA1
    BLD_DMG_MACH_POD_LP = 0x5035727B
    BLD_DOOR_EXPLODE = 0x801AE19A
    BLD_HOLOGRAM_APPEAR = 0x62AE0EA3
    BLD_LIGHTS = 0x1892FE37
    BLD_POD_DOOR_CLOSE = 0xA2DC6005
    BLD_POD_DOOR_OPEN = 0x4C4F68F
    BLD_POD_SHUTDOWN = 0x6FD14262
    BLD_POD_STARTUP = 0x5C4B561F
    BLD_RUIN_MONOLITH = 0x1EDC03C1
    BLD_RUIN_PLAQUE = 0x5D206C15
    BLD_SC_FACT_INT = 0xBB08AD3D
    BLD_SC_OBS_IN = 0xB504D119
    BLD_SCIENTIFIC_DOOR_CLOSE = 0x40961F37
    BLD_SCIENTIFIC_DOOR_OPEN = 0xE8572281
    BLD_SCIENTIFIC_FACTORY_ROOF = 0x47BC05
    BLD_SCIENTIFIC_PISTON = 0x2FEB96E5
    BLD_SCIENTIFIC_WINDOW_CLOSE = 0x1DEC7157
    BLD_SCIENTIFIC_WINDOW_OPEN = 0x1B615F21
    BLD_SERVER = 0x933C9559
    BLD_TONEINT_GENERIC_01 = 0x207AA53D
    BLD_TONEINT_GENERIC_02 = 0x207AA53E
    BLD_TONEINT_GENERIC_03 = 0x207AA53F
    BLD_TONEINT_GENERIC_04 = 0x207AA538
    BLD_TONEINT_GENERIC_05 = 0x207AA539
    BLD_TONEINT_GENERIC_06 = 0x207AA53A
    BLD_TONEINT_GENERIC_07 = 0x207AA53B
    BLD_TONEINT_GENERIC_08 = 0x207AA534
    BLD_TONEINT_GENERIC_09 = 0x207AA535
    BLD_TONEINT_GENERIC_10 = 0x217AA6AF
    BLD_TONEINT_GENERIC_11 = 0x217AA6AE
    BLD_TONEINT_GENERIC_12 = 0x217AA6AD
    BLD_TONEINT_GENERIC_13 = 0x217AA6AC
    BLD_TONEINT_GENERIC_14 = 0x217AA6AB
    BLD_TONEINT_GENERIC_15 = 0x217AA6AA
    BLD_TONEINT_GENERIC_16 = 0x217AA6A9
    BLD_TONEINT_GENERIC_17 = 0x217AA6A8
    BLD_TONEINT_GENERIC_18 = 0x217AA6A7
    BLD_TONEINT_HANGER_START_01 = 0xCF108C8
    BLD_TONEINT_HANGER_STOP_01 = 0x74461F80
    BLD_TR_HAR_INT = 0x3C3CB2A0
    BLD_TRADER_DOOR_CLOSE = 0xE74FE36
    BLD_TRADER_DOOR_OPEN = 0xA876DCE2
    BLD_TRADER_FACTORY_ROOF = 0xDD99760
    BLD_TRADER_RADIOTOWEREFFECT = 0xDA81C2AC
    BLD_WARRIOR_DOOR_CLOSE = 0x42737C4C
    BLD_WARRIOR_DOOR_OPEN = 0x44339BD8
    BLD_WARRIOR_FACTORY_ROOF = 0x33B9723E
    BLD_WARRIOR_ROOF_OBS = 0x79E2A24
    BLD_WARRIOR_SATELLITE = 0x9D2AD184
    BLD_WARRIOR_WALLEX_CAP = 0x2F73E8B3
    BLD_WORDSTATION = 0x5EADD344
    BLOB_TERRARIUM = 0x836231DE
    BLOBATTACK = 0xF73A93BC
    BLOBATTACK2 = 0xED3690C6
    BLOBATTACK3 = 0xED3690C7
    BLOBROAR = 0x743C03A4
    BRIDGETERMINAL_CLOSE = 0xC3D36AE3
    BRIDGETERMINAL_OPEN = 0xA26E57D5
    BRIDGETERMINALSCREEN = 0xB7549556
    BUGFIEND_ATTACK01 = 0x531CBC05
    BUGFIEND_EAT = 0x933FE89E
    BUGFIEND_GROUNDAPPEAR = 0x950EAFA2
    BUGFIEND_PAIN01 = 0x932BD321
    BUGFIEND_POUNCE01 = 0x7573DD67
    BUGFIEND_SPIT = 0xA79F6A92
    BUGFIEND_STUNNED = 0x47D1F241
    BUGGY_BOOST_START = 0xA8AD0530
    BUGGY_BOOST_STOP = 0x5998369C
    BUGGY_HORN_START = 0xF277A3F6
    BUGGY_HORN_STOP = 0x19167876
    BUGGY_IDLE_EXTERIOR = 0x6F5E01BB
    BUGGY_IMPACTS = 0x7A3FF7D1
    BUGGY_JUMP = 0x40AED174
    BUGGY_START = 0x574EA9C4
    BUGGY_STOP = 0x9AF38178
    BUGGY_SUSPENSION = 0x9979BE53
    BURNING_BARREL = 0xF24D4A35
    BUTTERFLY = 0xD410A32
    BYTEBEAT = 0x3DB63CCF
    BYTEBEAT_BAR = 0x8EEE3065
    BYTEBEAT_BAR_STOP = 0x4B3267A8
    BYTEBEAT_PLAYER = 0x1DF2F9B5
    BYTEBEAT_STOP = 0x932527FA
    CAPSULE_COLLECT = 0xBC55E8B1
    CAPSULE_PANEL_OPEN = 0xE95C7888
    CATALTATTACK = 0x9AD42B64
    CATALTATTACK2 = 0x20004E5E
    CATALTATTACK3 = 0x20004E5F
    CATALTHAPPY = 0x6179CA9A
    CATALTPERFORM01 = 0x2FF4EBE6
    CATALTROAR = 0x93C693EC
    CATATTACK1 = 0x49AFA08
    CATATTACK2 = 0x49AFA0B
    CATATTACK3 = 0x49AFA0A
    CATLARGEATTACK = 0xAC68C044
    CATPERFORM01 = 0x74F5CCB3
    CATPOUNCE = 0x23978AD9
    CATROAR = 0x8D40571B
    CHARACTEREDITOR_SELECT = 0xE22A1DC0
    CHARACTEREDITOR_WOOSH = 0x1B532920
    CHAT = 0xF6C8069B
    CLAMCLOSE = 0x9E33F27A
    CLAMOPEN = 0x9D20C9FE
    CLAMSHELL_IDLE = 0x896C2B0D
    CLAMSHELL_OPEN = 0x3F0E2BF
    COLLECTABLE_RECEIVED = 0xC266F931
    COMMS_CHATTER_FREIGHTER = 0xDFEA2C37
    COMMS_CHATTER_PIRATES_AMBIENT = 0x48838B34
    COMMS_CHATTER_PIRATES_HIT = 0x81CCB593
    COMMS_CHATTER_POLICE = 0xD547E7BB
    COMMS_CHATTER_POLICE_HIT = 0x40407039
    COMMS_CHATTER_STOP_ALL = 0x50409A1D
    COMMUNICATOR_CLOSE = 0x2D2D0DB1
    COMMUNICATOR_HAIL = 0x7B52749D
    COMMUNICATOR_OPEN = 0x41B5F833
    COMPUTER_TEXT = 0x2F2F62DC
    COMPUTER_TEXT_STOP = 0xFE197CAB
    COMPUTER_TEXT_TYPE = 0x28D3F683
    COMPUTER_TEXT_TYPE_STOP = 0xE271EAEE
    COOKER_CLOSE = 0xDE567DC9
    COOKER_COOKING = 0x1409D575
    COOKER_END = 0xF9F58DD6
    COOKER_OPEN = 0xC703639B
    CORETERMINAL_COLLECTDATA = 0x5A8D1FF
    CORRUPTED_PILLAR = 0xF8AD68FE
    CORRUPTED_PILLAR_FR0 = 0x230ADD5B
    CORRUPTED_PILLAR_FR226 = 0x8BA349BD
    CORRUPTEDQUAD_AMBIENT_TONE = 0x4736C7DE
    CORRUPTEDQUAD_DIE = 0xA7E3590D
    CORRUPTEDQUAD_EMOTE_LP = 0xB11C2646
    CORRUPTEDQUAD_EMOTE_LP_STOP = 0x9E7EA915
    CORRUPTEDQUAD_EVADE = 0xC54605A8
    CORRUPTEDQUAD_POUNCE = 0x760FEF17
    CORRUPTEDQUAD_POUNCEBACK = 0xA18C6526
    CORRUPTEDQUAD_STUNNED = 0x71BCF6C2
    CORRUPTMONOLITH_BASE = 0xEE3CFFE4
    CORRUPTMONOLITH_BURST = 0xE30F0A57
    CORRUPTMONOLITH_CLOSE = 0x62AB0D15
    CORRUPTMONOLITH_SPARK = 0x5B7D7DAA
    COWATTACK1 = 0xF26FF8FF
    COWATTACK2 = 0xF26FF8FC
    COWATTACK2HIND = 0xFED92B2F
    COWATTACK3 = 0xF26FF8FD
    COWATTACK3HIND = 0x9C8C20B2
    COWATTACKHIND = 0x2E946A79
    COWFLOATHAPPY = 0xBE89AD0A
    COWFLOATSAD = 0x31FB447C
    COWHAPPYHIND = 0xD48DDDFF
    COWHINDPERFORM01 = 0xD64E7029
    COWHINDROAR01 = 0x2197E780
    COWPERFORM01 = 0xA1E54730
    COWPOUNCE1 = 0x31C0A479
    COWROAR = 0xE2F1E4D6
    CRASHED_FREIGHTER = 0xA672C68C
    CRATE_WEAPON = 0x144B7049
    CRATE_WEAPON_CLOSE = 0x7ACC6D60
    CRATELOCKOPEN = 0xF7DED48F
    CRATEM_OPEN = 0xB602DA46
    CREATURE_BITE = 0xA83D7AAB
    CREATURE_JUMPSWIPE = 0xC4B64355
    CREATURE_POOP = 0x57FC4B17
    CREATURE_ROAR = 0x58EB908D
    CREATURE_STEP_BLOB = 0x8A27FDBB
    CREATURE_STEP_BLOB_WALK = 0x707CF181
    CREATURE_STEPS = 0x2A6F6752
    CREATURE_SWIPE = 0x64797DF9
    CREATURE_VOCALS_SQUAWK_AGGRESSION = 0x75F5A46D
    CREATURE_VOCALS_SQUAWK_ATTACK = 0x23D5A471
    CREATURE_VOCALS_SQUAWK_DIE = 0x395F9689
    CREATURE_VOCALS_SQUAWK_FLEE = 0xEF169B9
    CREATURE_VOCALS_SQUAWK_IDLE = 0x6DCF4D8B
    CREATURE_VOCALS_SQUAWK_PAIN = 0x6C8842D5
    CREATURE_VOCALS_SQUAWK_ROAR = 0x80D02225
    CREATURE_VOCALS_SQUAWK_ROAR_ANGRY = 0x4FF9BF6F
    CREATURE_VOCALS_SQUAWK_ROAR_HAPPY = 0x925E724A
    CREATURE_VOCALS_SQUAWK_ROAR_NEUTRAL = 0xA8E86F75
    CREATURE_VOCALS_SQUAWK_SNORE = 0x8DFE9A1A
    CRT_BIRD_FLAP = 0x361B8FB6
    CRT_COW_WINGFLAP = 0x6B97E021
    CRT_GRUNT_WINGFLAPRUN = 0x7B6E923
    CRT_GRUNT_WINGFLAPWALK = 0x1E4355FF
    CRYOCHAMBER = 0xCDD3E924
    CRYOCHAMBER_CLOSE = 0x2ADCB15D
    CRYSTAL_RARE_EXPLODE = 0xA0786AA6
    CRYSTAL_RARE_LP = 0x86DDA9C7
    CRYSTALALTAR_COLLECT = 0x441AEFA0
    CRYSTALALTAR_LOOP = 0xE2EAC53C
    CUSTOMISE_ACTIVATE = 0xE1CCDB77
    CUSTOMISE_END = 0x734712A3
    CUSTOMISE_IDLE = 0x38B3D8BA
    DEATH_DAMAGE = 0x617076E7
    DEATH_DAMAGE_REBUILD = 0x30258C33
    DEATHMARKER_PULSE = 0x57F9C699
    DEATHMARKER_TRANSFORM = 0x651ED76
    DEATHSHOUT = 0xEBA2C6C4
    DISCOVER_PLANET = 0x721715FD
    DISCOVERY_UPLOADED = 0xF8D5FE88
    DOOR_BROKEN_SPARKS = 0xA5397178
    DRAGONFLY = 0xB48AC47B
    DRAGONFLY_BOOST_START = 0xC7ADCCAE
    DRAGONFLY_BOOST_STOP = 0xD7CF88E
    DRAGONFLY_HORN_START = 0xC06C8F4
    DRAGONFLY_HORN_STOP = 0xC55D6968
    DRAGONFLY_IDLE_EXTERIOR = 0x81E3589D
    DRAGONFLY_IMPACTS = 0xA58ADC43
    DRAGONFLY_JUMP = 0xD07A3EA6
    DRAGONFLY_START = 0xED4829D6
    DRAGONFLY_STOP = 0xB4782DD6
    DRAGONFLY_SUSPENSION = 0x6F051BC9
    DRILL_IN = 0x87E6EB8A
    DRILL_LP = 0x84E6E75B
    DRILL_LP_STOP = 0x5A24BEF6
    DRILL_OUT = 0x958077E5
    DRONE_ALERT = 0x7A84D746
    DRONE_ARMOURED_BRACE = 0x5A7DE16F
    DRONE_ARMOURED_UNBRACE = 0xD65D31C4
    DRONE_ATTACK = 0x234F1F00
    DRONE_ATTACK_STOP = 0xA6B07F2F
    DRONE_DEBRIS = 0x3CCD53D1
    DRONE_DIE = 0x772B483E
    DRONE_EMOTE_LP = 0xD5FDCCDF
    DRONE_EMOTE_LP_STOP = 0xBC9CA56A
    DRONE_EMOTE_ONESHOT = 0x6890081
    DRONE_ENGINE = 0x7F0625AA
    DRONE_ENGINE_CORRUPTED = 0xA1D3CD87
    DRONE_FRIENDLY_COMBAT = 0xE1F7777C
    DRONE_FRIENDLY_COMBAT_STOP = 0x7A6EDC0B
    DRONE_FRIENDLY_DEVICE_OFF = 0xEE5687A8
    DRONE_FRIENDLY_DEVICE_ON = 0xB1FEF1B2
    DRONE_FRIENDLY_SUMMONED = 0x3FFEDE7A
    DRONE_FRIENDLY_UNSUMMONED = 0xC39240FB
    DRONE_FRIENDLY_WANTED = 0x30684DA9
    DRONE_FRIENDLY_WANTED_END = 0xA3274B4B
    DRONE_INVESTIGATING = 0x1B83BC48
    DRONE_LASER = 0x9DF60645
    DRONE_MEDIC_ATTACK = 0xF6B0A69
    DRONE_MEDIC_DISENGAGE = 0x45F4D79A
    DRONE_MEDIC_ENGAGE = 0x28DE13F8
    DRONE_MEDIC_FIX = 0xB63AAB4A
    DRONE_MEDIC_IDLE = 0x5D87B953
    DRONE_RECHARGE = 0xACC011B
    DRONE_SCAN_START = 0xD4DA690A
    DRONE_SCAN_STOP = 0x410B5462
    DRONE_SEARCHING = 0x6EC52C40
    DRONE_SHIELD_ACTIVATE = 0x3530F375
    DRONE_SHIELD_DEACTIVATE = 0xAABD2664
    DRONE_SHIELD_GLITCH = 0x8FE1B631
    DRONE_SUMMONER_ALARM = 0xF1CE63E2
    DRONE_SUMMONER_SIGNAL = 0xE67CDB17
    DRONE_SUMMONER_UNSIGNAL = 0x58AEE782
    DRONE_SUSPICIOUS = 0xB6CE0AD5
    E3_ZOOMIN = 0xBE030510
    E3_ZOOMOUT = 0x15C6E177
    EGG_MACHINE_AMBIENT_LP = 0x7BE7B7BA
    EGG_MACHINE_CLOSE = 0x6B395F97
    EGG_MACHINE_COOK = 0xBAB81BD1
    EGG_MACHINE_FINISH = 0xD5B01638
    EGG_MACHINE_OPEN = 0x955F5B61
    EGG_MACHINE_START = 0x97160567
    EGGOPENS = 0x9058C8F7
    EGGRESOURCE_COLLECT = 0x5D44C34B
    ENGINEREACTOR_OFF_IDLE = 0xF322160A
    EQUIP_DAMAGED = 0xF56C53BB
    EXOCRAFT_SUMMONING_STATION = 0x29EF00E2
    EXPL_DEPOT = 0x14D13D39
    EXPL_ELECTRICAL_STUN = 0xCEDE2742
    EXPL_ELECTRICAL_STUN_STOP = 0x50AC08C1
    EXPL_FIREWORK = 0xC78B45E
    EXPL_FIREWORK_LAUNCH = 0x203840E0
    EXPL_FIREWORK_LAUNCH_SLIME = 0x37F4611
    EXPL_FIREWORK_SLIME = 0xD86955AF
    EXPL_FIREWORK_TAIL = 0xAF543557
    EXPL_FIREWORK_TAIL_SLIME = 0x6665BA8A
    EXPL_FREIGHTER = 0x38C32017
    EXPL_FREIGHTER_BUILDUP = 0xCD0A69F9
    EXPL_FREIGHTER_CONTAINER_LARGE = 0x98E3FACB
    EXPL_FREIGHTER_CONTAINER_SMALL = 0x8ED7A637
    EXPL_FREIGHTER_ONE_SHOTS = 0x39897238
    EXPL_FREIGHTER_ROD = 0xFE15D955
    EXPL_NEWSTARSYSTEM = 0xD468363A
    EXPL_ROCK = 0xB5CC968E
    EXPL_SHIELD_GENERATOR = 0xA6A5B3D4
    EXPL_SHIP_SMALL = 0x2D0884BB
    EXPL_SHIPS_LARGE = 0xBB5CA45A
    EXPL_SHIPS_MED = 0x618DEA29
    EXPL_SHIPS_SMALL = 0xB8D9B746
    EXPL_SMALL_SPACE_GENERIC = 0xC7DD7E03
    EXPL_SPACE_MEMORYBOAT = 0xC7026C2B
    EXPL_TORPEDO = 0x75651EF2
    EXPLODINGBARREL = 0xA7AE41A9
    EXPLORERANGRYIPAD = 0xB1BD172B
    EXPLORERCHATTER = 0xE1C4E07B
    EXPLORERHAPPYIPAD = 0xC786698E
    EXPLORERHAPPYIPAD2 = 0xA6982AB8
    EXPLORERHAPPYIPAD3 = 0xA6982AB9
    EXPLORERIPADGREET = 0xC03F5D47
    EXPLORERIPADGREET2 = 0xEABFD6F7
    EXPLORERIPADGREET3 = 0xEABFD6F6
    EXPLORERIPADGREET4 = 0xEABFD6F1
    EXPLORERNEUTRALIPAD = 0x87AE24B1
    EXPLOSION_RESOURCE_GATHER = 0x42613325
    EYESTALK = 0x33AF58C1
    FEEDERDISPENSE = 0x722708E9
    FIBREGLASS_DOOR1_SETTLEMENT_CLOSE = 0x1A13F00
    FIBREGLASS_DOOR1_SETTLEMENT_OPEN = 0x4ADAF334
    FIBREGLASS_DOOR2_SETTLEMENT_CLOSE = 0x9004F65D
    FIBREGLASS_DOOR2_SETTLEMENT_OPEN = 0x4E200377
    FIEND_ATTACK = 0x4EBD3690
    FIEND_BURY = 0xA732976C
    FIEND_DIE = 0x57FEA6E
    FIEND_GROUNDAPPEAR = 0x9A41A76E
    FIEND_GROUNDEFFECT = 0xE816A4C6
    FIEND_IDLE = 0x9393197A
    FIEND_POUNCE = 0x74BB47B2
    FIEND_ROAR = 0x859699D0
    FIEND_SPIT = 0xFA3ABC76
    FIREPLACE_LP = 0x499F8DC1
    FIRESTORM = 0x2841CE64
    FIRESTORM_STOP = 0x37098E83
    FISHCAUGHT = 0x511DD5F7
    FISHFIEND_DIE = 0x6E831730
    FISHFIEND_EAT = 0x5A853604
    FISHFIEND_SPAWN = 0x1C3DC95F
    FISHING_PLATFORM_LP = 0xB3D3B34
    FISHING_PLATFORM_OPEN = 0xF81A3B8
    FISHSPARKLE = 0x2AF797E7
    FISHSTRUGGLE = 0x99B4CCB6
    FLOATING_GASBAG_EXPLODE = 0x5D91DBB7
    FLOATINGFERN = 0x23132724
    FLOATNIBBLE = 0x36776BB
    FLOATRIPPLE = 0xB201D5BB
    FLOATSPLASH = 0xE24550E4
    FOLEY_STOP_ALL = 0xAEA67841
    FOOT_LOCKER_OPEN = 0xAF12AD4F
    FOOTSTEP = 0x6F394B77
    FOOTSTEP_FALLLAND = 0xFFA89F82
    FORFANGRY01 = 0x419C389A
    FORFCHATTER01 = 0xE497504E
    FORFGREET01 = 0x9934D7C6
    FORFHAPPY01 = 0x40C85F
    FOSSIL_COLLECT = 0xC13BB166
    FOURTHRACE_APOLLO_ANGRY00 = 0xAC2665AE
    FOURTHRACE_APOLLO_CHATTER00 = 0x73545F86
    FOURTHRACE_APOLLO_GREET00 = 0xEE5A2A22
    FOURTHRACE_APOLLO_GREET01 = 0xEE5A2A23
    FOURTHRACE_APOLLO_GREET02 = 0xEE5A2A20
    FOURTHRACE_APOLLO_GREET03 = 0xEE5A2A21
    FOURTHRACE_APOLLO_GREET04 = 0xEE5A2A26
    FOURTHRACE_APOLLO_HAPPY00 = 0xD14ED307
    FOURTHRACE_APOLLO_HAPPY01 = 0xD14ED306
    FOURTHRACE_APOLLO_HAPPY02 = 0xD14ED305
    FOURTHRACE_APOLLO_IDLE00 = 0x747677FD
    FOURTHRACE_ARTEMIS_ANGRY00 = 0x1EA5A71C
    FOURTHRACE_ARTEMIS_CHATTER00 = 0x1E577730
    FOURTHRACE_ARTEMIS_GREET00 = 0x15AA44F4
    FOURTHRACE_ARTEMIS_GREET01 = 0x15AA44F5
    FOURTHRACE_ARTEMIS_GREET02 = 0x15AA44F6
    FOURTHRACE_ARTEMIS_GREET03 = 0x15AA44F7
    FOURTHRACE_ARTEMIS_GREET04 = 0x15AA44F0
    FOURTHRACE_ARTEMIS_HAPPY00 = 0x738920B9
    FOURTHRACE_ARTEMIS_HAPPY01 = 0x738920B8
    FOURTHRACE_ARTEMIS_HAPPY02 = 0x738920BB
    FOURTHRACE_ARTEMIS_IDLE00 = 0x946BA2B3
    FOURTHRACE_NULL_ANGRY00 = 0xAD16E1B0
    FOURTHRACE_NULL_CHATTER00 = 0xD4C3C08C
    FOURTHRACE_NULL_GREET00 = 0x960B9B68
    FOURTHRACE_NULL_GREET01 = 0x960B9B69
    FOURTHRACE_NULL_GREET02 = 0x960B9B6A
    FOURTHRACE_NULL_GREET03 = 0x960B9B6B
    FOURTHRACE_NULL_GREET04 = 0x960B9B6C
    FOURTHRACE_NULL_HAPPY00 = 0xBD9D7CAD
    FOURTHRACE_NULL_HAPPY01 = 0xBD9D7CAC
    FOURTHRACE_NULL_HAPPY02 = 0xBD9D7CAF
    FOURTHRACE_NULL_IDLE00 = 0xC5B3E657
    FOURTHRACE_PROC_ANGRY00 = 0xA69C07BF
    FOURTHRACE_PROC_CHATTER00 = 0x5FB0BF2B
    FOURTHRACE_PROC_GREET00 = 0x4A1A67CB
    FOURTHRACE_PROC_GREET01 = 0x4A1A67CA
    FOURTHRACE_PROC_GREET02 = 0x4A1A67C9
    FOURTHRACE_PROC_GREET03 = 0x4A1A67C8
    FOURTHRACE_PROC_GREET04 = 0x4A1A67CF
    FOURTHRACE_PROC_HAPPY00 = 0x7402CDD2
    FOURTHRACE_PROC_HAPPY01 = 0x7402CDD3
    FOURTHRACE_PROC_HAPPY02 = 0x7402CDD0
    FOURTHRACE_PROC_IDLE00 = 0x1593DBFE
    FRACTALCUBE = 0xB6F17CBB
    FREIGHTER_ALARM = 0x10F2436D
    FREIGHTER_ALARM_START = 0x2B11860C
    FREIGHTER_BRIDGE = 0x8DDFA449
    FREIGHTER_CALL = 0xBA2BE15A
    FREIGHTER_CORRIDOR = 0x7D0215EC
    FREIGHTER_DOOR_INTERNAL_CLOSE = 0xFA499897
    FREIGHTER_DOOR_INTERNAL_OPEN = 0x3F55DE61
    FREIGHTER_DOOR_REINFORCED_CLOSE = 0x4DE5D229
    FREIGHTER_DOOR_REINFORCED_OPEN = 0x16C6217B
    FREIGHTER_DRONE = 0xA4898134
    FREIGHTER_ELEVATOR = 0x1D26E750
    FREIGHTER_HANGAR = 0xC3642BEB
    FREIGHTER_HANGARDOOR_CLOSE = 0xA9AF6976
    FREIGHTER_HANGARDOOR_OPEN = 0xF6307F22
    FREIGHTER_LOWSHIELD_ALARM = 0xEF3758E5
    FREIGHTER_REFINER_ROOM = 0x82217F99
    FREIGHTER_REFINER_RUNNING = 0x22D0D8CD
    FREIGHTER_SHIELD_LP = 0x10C0C14C
    FREIGHTER_SHIELD_LP_STOP = 0x8DF13AFB
    FREIGHTER_SHIELD_ONESHOT = 0x316F204
    FREIGHTER_STELLAREXTRACTOR = 0x5806FFF
    FREIGHTER_STORAGE_TERMINAL = 0x511D7268
    FREIGHTER_TELEPORT = 0xDCD9243F
    FREIGHTER_TELEPORTER = 0xCDD40E2A
    FRIGATE_LIVING_DEVOUR = 0x1E1153E9
    FRIGATE_LIVING_REVEAL = 0x4045C9B3
    FRIGATE_LIVING_TALK = 0x1E4E7B6
    FRIGATE_LIVING_WARPIN = 0x195615B7
    GAS_BASTARD_POP = 0x3EA92568
    GEMCRYSTAL_COLLECT = 0xAC4DFF83
    GLITCHY_MONITOR = 0x1E04A85C
    GRABBYPLANT_ATTACK_END = 0x684EBBB8
    GRABBYPLANT_ATTACK_LP = 0x10A22325
    GRABBYPLANT_DIE = 0xD7FAF53C
    GRAV_BALLS = 0xC72A3468
    GRAV_BALLS_STOP = 0xAE129547
    GROUND_SIZZLE = 0x577DF00A
    GROUND_SIZZLE_STOP = 0x1BAC5A39
    GROUNDWORM_CLOSE = 0x6D6FB800
    GROUNDWORM_KILL = 0xCA498284
    GROUNDWORM_OPEN = 0x25023634
    GRUNTATTACK2 = 0xDE8A7D61
    GRUNTATTACK3 = 0xDE8A7D60
    GRUNTFLOATHAPPY = 0xFFBDD045
    GRUNTFLOATSLEEP = 0x9ED114F6
    GRUNTPOUNCE = 0xB66812B
    GRUNTROAR = 0x8C8B6075
    HARRYTEST = 0xD13E408D
    HAZ_CRIT_COLD = 0x4C14E836
    HAZ_CRIT_HEAT = 0xAA7866FE
    HAZ_CRIT_O2 = 0xBDA886E7
    HAZ_CRIT_RAD = 0x582BD949
    HAZ_CRIT_RAD_FALLING = 0x6F3906B1
    HAZ_CRIT_RAD_STABLE = 0xAD62460D
    HAZ_CRIT_SHIELD = 0x4643A77B
    HAZ_CRIT_SHIELD_FALLING = 0x10651173
    HAZ_CRIT_SHIELD_STABLE = 0x274BF05F
    HAZ_CRIT_THERM_FALLING = 0xF60D19A6
    HAZ_CRIT_TOXIC = 0xA2EE4605
    HAZ_CRIT_TOXIC_FALLING = 0xC71CDD4D
    HAZ_CRIT_TOXIC_STABLE = 0x55AB8951
    HAZARDPLANT_CLOSE = 0x8C136AB5
    HAZARDPLANT_IDLE = 0xA9E70AAD
    HAZARDPLANT_OPEN = 0x246D555F
    HAZARDPLANT_OPENIDLE = 0x9308BAF9
    HEATER_OFF = 0xD57B9408
    HEATER_ON = 0x4E481692
    HEXAGON = 0x66DC42F
    HOLOHUB_END = 0xCF84178C
    HOLOHUB_LADDER_END = 0x372BBD97
    HOLOHUB_LADDER_START = 0xEF70C184
    HOLOHUB_START = 0xD60EC7EF
    HOVERCRAFT_BOOST_START = 0xF116021C
    HOVERCRAFT_BOOST_STOP = 0xC256FEF0
    HOVERCRAFT_HORN_START = 0xA5828922
    HOVERCRAFT_HORN_STOP = 0x6EEC151A
    HOVERCRAFT_IDLE_EXTERIOR = 0x293C4C27
    HOVERCRAFT_IMPACTS = 0xF638247D
    HOVERCRAFT_JUMP = 0x611F8178
    HOVERCRAFT_START = 0x18B0E3B0
    HOVERCRAFT_STOP = 0x4909EE1C
    HOVERCRAFT_SUSPENSION = 0x26A065CF
    HUD_JUMP_ENGAGE = 0x3AC8D717
    HUD_JUMPING = 0x4238C05
    IDENTIFY_SCAN_OFF = 0x8E533775
    IDENTIFY_SCAN_ON = 0xC5976489
    IMPACT_CREATURE_SQUISH = 0xAD1494AB
    IMPACTS_GROUND_GENERIC_SMALL = 0x785AA13A
    INTERACT_COLLECT = 0x2DB05350
    INTERACTION_CARGOBAY = 0x2153E9AE
    INTERACTION_CARGOBAYSTUCK = 0x8374264A
    INTERACTION_CARGOCONTLOAD = 0xEF521ED6
    INTERACTION_ENGINEREACTOR = 0x1255F34E
    INTERACTION_MAINTPOINT = 0xFE58FBEF
    INTERACTION_TURRETSHELLS = 0xA8F90361
    INTERACTION_TURRETTURN = 0xDB15CA55
    INTERACTIVECASE_OPEN = 0xE81E1242
    JELLYFISH_DIE = 0x8D0341AE
    JELLYFISH_SPAWN = 0x4CF735B9
    JELLYFISH_SWIM = 0x6DF627F0
    JELLYFISHBOSS_APPEAR = 0x4B30A1CE
    JELLYFISHBOSS_ORBATTACK = 0x252C9E10
    JELLYFISHBOSS_SWIM = 0xF1258E95
    JETPACK_BOOST_PICKUP = 0x1662D4A8
    JETPACK_BOOST_START = 0x59EEB4F8
    JETPACK_BOOST_STOP = 0xE6CC9004
    JETPACK_BOOST_TIMEOUT = 0x3D3E8565
    JETPACK_DEPLETED = 0x4392405
    JETPACK_PARTICLES_JETSPACEFX = 0x4C30345B
    JETPACK_PARTICLES_JETSPACEFX_END = 0x968B943D
    JETPACK_START = 0xBF36A0FC
    JETPACK_STOP = 0x35973C50
    JETPACK_WATER_TRANSITION_INTO_ATMOS = 0x3EBFB6F9
    JETPACK_WATER_TRANSITION_INTO_WATER = 0x20BEC596
    KEYCONTAINER = 0xF4218B47
    LANDING_PLATFORM_CLOSE = 0x854717ED
    LANDING_PLATFORM_OPEN = 0x78991C27
    LANDINGBAY_ACTIVATE = 0x3816AA16
    LANDINGBAY_DEACTIVATE = 0x853967B7
    LANDSQUID_APPEAR = 0x3C4D6560
    LANDSQUID_DISAPPEAR = 0x2B93DE02
    LANDSQUID_KAMIKAZE = 0xFEDCC316
    LANDSQUID_KAMIKAZE_STOP = 0x5EB75A45
    LANDSQUID_KILL = 0x327DB8CF
    LANDSQUID_SPIT = 0x65F318DD
    LANDSQUID_SWIM = 0x65E64CDB
    LANTERNCLOSE = 0x808EAE35
    LANTERNOPEN = 0x8AFD33DF
    LAVA_VOLCANO_AMBIENT = 0x4D0F2CED
    LAVA_VOLCANO_ERUPT = 0xE111872B
    LAVA_VOLCANO_EXPLODE = 0x82B62E7E
    LIGHTNING = 0xC6BFE289
    LOCKER_OPEN = 0x305CA008
    LOWERORDERANGRYIPAD = 0xA7B5482F
    LOWERORDERCHATTERIPAD = 0x3E606FBB
    LOWERORDERGREET1IPAD = 0x18A08D70
    LOWERORDERGREET2IPAD = 0xB00B7183
    LOWERORDERGREET3IPAD = 0xD559CDA2
    LOWERORDERGREET4IPAD = 0x4F012E65
    LOWERORDERGREET5IPAD = 0x39664C44
    LOWERORDERHAPPY2IPAD = 0x324DAE34
    LOWERORDERHAPPY3IPAD = 0xCCFEEDD5
    LOWERORDERHAPPY4IPAD = 0x93565F52
    LOWERORDERHAPPYIPAD = 0x8547CFD2
    MAINTENANCE_BROKEN = 0xEEE46E
    MANTARAY_ATTACK = 0x74EEDFC1
    MANTARAY_FASTSWIM = 0xF5F12B8F
    MANTARAY_SWIM = 0xF8F768E1
    MAP_STAR_WOOSH = 0xBC7AB0AD
    MAP_WAYPOINT_TONE_LP = 0xCD4C651B
    MECH_EXIT = 0xBCC570FD
    MECH_IDLE = 0xBB021D37
    MECH_JETPACK_LANDING = 0x520C6999
    MECH_JETPACK_LANDING_INTRO = 0xB183200A
    MECH_JETPACK_LANDING_SKID = 0x180A89A5
    MECH_JETPACK_LP = 0xDE5305B4
    MECH_JETPACK_LP_END = 0xA6FCEB2A
    MECH_JETPACK_RETRIGGER = 0x76E0CB75
    MECH_JETPACK_STARTUP = 0x16C249B
    MECH_JETPACK_TRIGGER = 0xCF7D714
    MECH_MOVE_RUN = 0xD7C5239C
    MECH_MOVE_WALK = 0x936BCEAA
    MECH_SENTINEL_STEP_RUN = 0x85D18C
    MECH_SENTINEL_STEP_WALK = 0xA892E81A
    MECH_STEP_RUN = 0xE008E6CD
    MECH_STEP_WALK = 0x5569365D
    MECH_STONE_STEP_RUN = 0xBA0B131B
    MECH_STONE_STEP_WALK = 0xAE485EF7
    MESSAGEMODULE_IDLE = 0x74347F1F
    MESSAGEMODULE_START = 0x96AB9597
    METALFORMATION_COLLECT = 0x2F24E23C
    METEORITE_EXPLODE = 0xD846F01D
    METEORITE_INCOMING = 0xCFBF792E
    MILK_BOTTLING = 0x4511C1AE
    MILK_PUMPING = 0x87C5888F
    MINIDRONE_ACTIVE = 0x9F140B13
    MINIDRONE_IDLE = 0xA651E327
    MINIDRONE_SHOOT = 0xE1A418B6
    MINIWORM_BURSTOUT = 0x105FB33A
    MINIWORM_DEATH = 0x2996DB4A
    MINIWORM_IDLE = 0x8C3BC9E2
    MINIWORM_LUNGE = 0xB1195BC9
    MINIWORM_LURKING = 0x72AF95EC
    MINIWORM_RETRACT = 0x97EB3C43
    MINIWORM_ROAR = 0xA0EA53E8
    MOLE = 0xBD7B65F0
    MONOLITH_BEAM_START = 0x22177738
    MONOLITH_INTERACTIONPLATFORM_START = 0x31D40DBC
    MONUMENT = 0x9AB78CBA
    MOTION_PS5_01 = 0x139A94EC
    MOTION_PS5_STOP = 0xECE193FD
    MSTRUCTURE = 0x2E46515
    MUS_AMBIENT_MODE = 0xEB3C1A97
    MUS_AMBIENT_MODE_STOP = 0xB0299432
    MUS_ATLASSTATION = 0xD2C903D2
    MUS_COMMUNITYRESEARCH = 0xC44ABF93
    MUS_CORRUPTED_LP = 0x9CF981B6
    MUS_CORRUPTED_LP_STOP_FAST = 0x26307F5A
    MUS_CORRUPTED_LP_STOP_SLOW = 0xB9DB6827
    MUS_CORRUPTED_MUSICCUE = 0xA1CA2E10
    MUS_CORRUPTED_STING_LONG = 0x89859902
    MUS_ENCLAVE_DISCOVER = 0xFC4C03AD
    MUS_ENDING = 0x3414FF98
    MUS_EXPEDITION_START = 0x68E79865
    MUS_FIRSTTIMESPACESTATION = 0x1C477914
    MUS_FIRSTTIMEWARP = 0x21015BC
    MUS_FISHING = 0x6999BC45
    MUS_FISHING_STOP = 0x7F346DC8
    MUS_GAMESTART = 0x6E416461
    MUS_GAMESTART_LUSHWALK = 0xE4582A4F
    MUS_GAMESTART_LUSHWALK_STOP = 0x57DB907A
    MUS_GAMESTART_STOP = 0x2BE88C64
    MUS_LEVEL_UP = 0xDBB97803
    MUS_LOADING01 = 0x58A3185E
    MUS_LOADING02 = 0x58A3185D
    MUS_LOADING03 = 0x58A3185C
    MUS_LOADING04 = 0x58A3185B
    MUS_LOADING05 = 0x58A3185A
    MUS_LOADING06 = 0x58A31859
    MUS_LOADING07 = 0x58A31858
    MUS_LOADING08 = 0x58A31857
    MUS_LOADING09 = 0x58A31856
    MUS_LOADING10 = 0x57A316EC
    MUS_LOADING11 = 0x57A316ED
    MUS_LOADING12 = 0x57A316EE
    MUS_LOADING13 = 0x57A316EF
    MUS_LOADING14 = 0x57A316E8
    MUS_LOADING15 = 0x57A316E9
    MUS_LOADING16 = 0x57A316EA
    MUS_LOADING17 = 0x57A316EB
    MUS_LOADING18 = 0x57A316E4
    MUS_LOADING19 = 0x57A316E5
    MUS_LOADING20 = 0x5AA31BA5
    MUS_LOADING21 = 0x5AA31BA4
    MUS_LOADING22 = 0x5AA31BA7
    MUS_LOADING23 = 0x5AA31BA6
    MUS_LOADING24 = 0x5AA31BA1
    MUS_LOADING25 = 0x5AA31BA0
    MUS_LOADING26 = 0x5AA31BA3
    MUS_LOADING27 = 0x5AA31BA2
    MUS_LOADING28 = 0x5AA31BAD
    MUS_LOADING29 = 0x5AA31BAC
    MUS_LOADING30 = 0x59A31A32
    MUS_LOADING31 = 0x59A31A33
    MUS_LOADING32 = 0x59A31A30
    MUS_LOADING33 = 0x59A31A31
    MUS_LOADING34 = 0x59A31A36
    MUS_LOADING35 = 0x59A31A37
    MUS_LOADING36 = 0x59A31A34
    MUS_LOADING37 = 0x59A31A35
    MUS_LOADING38 = 0x59A31A3A
    MUS_LOADING39 = 0x59A31A3B
    MUS_LOADING40 = 0x54A31213
    MUS_LOADING41 = 0x54A31212
    MUS_LOADING42 = 0x54A31211
    MUS_LOADING43 = 0x54A31210
    MUS_LOADING44 = 0x54A31217
    MUS_LOADING45 = 0x54A31216
    MUS_LOADING46 = 0x54A31215
    MUS_LOADING47 = 0x54A31214
    MUS_LOADING48 = 0x54A3121B
    MUS_LOADING49 = 0x54A3121A
    MUS_LOADING50 = 0x53A310A0
    MUS_LOADING51 = 0x53A310A1
    MUS_LOADING52 = 0x53A310A2
    MUS_LOADING_STOP = 0x1E870702
    MUS_MILESTONE_COMPLETE = 0xD15B7779
    MUS_MILESTONE_REWARDS = 0x72C807B0
    MUS_MONOLITH = 0x18D5A84D
    MUS_MONOLITH_STOP = 0x120E6A40
    MUS_ONE_SINGLE_STAR = 0x77BEEC59
    MUS_RECURSIVE_SIMULATION = 0xE5C1825B
    MUS_SPACEVIRGIN = 0x2E518E96
    MUS_STATUS_UPDATE = 0x9E8F516D
    MUS_STORYMODE_MUSICCUE_01 = 0xC12BE1FC
    MUS_STORYMODE_MUSICCUE_02 = 0xC12BE1FF
    MUS_STORYMODE_MUSICCUE_03 = 0xC12BE1FE
    MUS_STORYMODE_MUSICCUE_04 = 0xC12BE1F9
    MUS_STORYMODE_MUSICCUE_05 = 0xC12BE1F8
    MUS_STORYMODE_MUSICCUE_06_LP = 0xC345F572
    MUS_STORYMODE_MUSICCUE_06_LP_STOP = 0x37EA3DD1
    MUS_STORYMODE_MUSICCUE_07 = 0xC12BE1FA
    MUS_STORYMODE_MUSICCUE_08_LP = 0x31987684
    MUS_STORYMODE_MUSICCUE_08_LP_STOP = 0x4F40ADE3
    MUS_STORYMODE_MUSICCUE_09 = 0xC12BE1F4
    MUS_STORYMODE_MUSICCUE_10_LP = 0xDD4A2FD
    MUS_STORYMODE_MUSICCUE_10_LP_STOP = 0x21A4CB50
    MUS_STORYMODE_MUSICCUE_11_LP = 0x57BEDBE2
    MUS_STORYMODE_MUSICCUE_11_LP_STOP = 0x22CA1
    MUS_STORYMODE_MUSICCUE_12_LP = 0x102487FB
    MUS_STORYMODE_MUSICCUE_12_LP_STOP = 0xA8509856
    MUS_STORYMODE_MUSICCUE_13_LP = 0x9B4C59A0
    MUS_STORYMODE_MUSICCUE_13_LP_STOP = 0xB5CCBF8F
    MUS_STORYMODE_MUSICCUE_14 = 0xC02BE00E
    MUS_STORYMODE_MUSICCUE_15 = 0xC02BE00F
    MUS_STORYMODE_MUSICCUE_16 = 0xC02BE00C
    MUS_STORYMODE_MUSICCUE_17 = 0xC02BE00D
    MUS_STORYMODE_MUSICCUE_18 = 0xC02BE002
    MUS_STORYMODE_MUSICCUE_19 = 0xC02BE003
    MUS_STORYMODE_MUSICCUE_20 = 0xBF2BDE97
    MUS_STORYMODE_MUSICCUE_21 = 0xBF2BDE96
    MUS_STORYMODE_MUSICCUE_22_LP = 0x10FAF564
    MUS_STORYMODE_MUSICCUE_22_LP_STOP = 0x46E34383
    MUS_STORYMODE_MUSICCUE_23 = 0xBF2BDE94
    MUS_STORYMODE_MUSICCUE_24 = 0xBF2BDE93
    MUS_STORYMODE_MUSICCUE_25 = 0xBF2BDE92
    MUS_STORYMODE_MUSICCUE_26 = 0xBF2BDE91
    MUS_STORYMODE_MUSICCUE_27 = 0xBF2BDE90
    MUS_STORYMODE_MUSICCUE_28 = 0xBF2BDE9F
    MUS_STORYMODE_MUSICCUE_29 = 0xBF2BDE9E
    MUS_STORYMODE_MUSICCUE_30 = 0xBE2BDD24
    MUS_STORYMODE_MUSICCUE_31 = 0xBE2BDD25
    MUS_STORYMODE_MUSICCUE_32 = 0xBE2BDD26
    MUS_STORYMODE_MUSICCUE_33 = 0xBE2BDD27
    MUS_STORYMODE_STOPALL = 0x5519D8C5
    MUS_THE_APPEARANCE_OF_A_STAR_SYSTEM = 0x5EC79C9C
    MUS_UNKNOWN_SYSTEM_X349866 = 0x637CCD8
    MUS_XBOX_SPLASHSCREEN = 0x99AFDCA0
    MUS_XBOX_SPLASHSCREEN_STOP = 0x89EE888F
    NADA_CHATTER_11 = 0xF7BB5BF6
    NADA_CHATTER_12 = 0xF7BB5BF5
    NADA_CHATTER_13 = 0xF7BB5BF4
    NADA_GREET_08 = 0x7D9C920C
    NADA_GREET_09 = 0x7D9C920D
    NEW_TECH = 0xCAC84920
    NEW_WEAPON = 0xE3FA979C
    NEXUS_BRIDGEENGINE_IDLE = 0xB01A5461
    NEXUS_BUBBLINGTUBE_SMALL = 0x495F0A84
    NEXUS_CONTROLROOM_CENTRE = 0xD9E873E9
    NEXUS_CONTROLROOM_HOLOGRAM = 0xB1F10DCD
    NEXUS_COOKINGFOOD = 0x6A2D035F
    NEXUS_EXTERIORLEG = 0xA2F9E64D
    NEXUS_FUELPUMP = 0xC949845F
    NEXUS_LANDING_RINGS = 0x725742B2
    NEXUS_MARKETDOOR_CLOSE = 0x99262904
    NEXUS_MARKETDOOR_OPEN = 0x81306600
    NEXUS_MIDDLEDRONE_IDLE = 0x2FA246D9
    NEXUS_PLANTGROWBOX = 0x7490B24
    NEXUS_ROBOARM_MOVE1 = 0x229C720C
    NEXUS_ROBOARM_MOVE1_REV = 0x21CFF112
    NEXUS_ROTATINGSIGN = 0x7D5A7B6A
    NEXUS_SMALLDRONE_FRAME0 = 0x2F28D10A
    NEXUS_SMALLDRONE_FRAME192 = 0x26731F8A
    NEXUS_SMALLDRONE_FRAME289 = 0xA56B98D9
    NEXUS_SMALLDRONE_FRAME512 = 0xB67CFCF6
    NEXUS_SMALLDRONE_FRAME640 = 0x21755640
    NEXUS_SMALLDRONE_FRAME879 = 0xA45C8CFA
    NEXUS_SMALLDRONE_LP = 0x6CC12C6F
    NEXUS_TELEPORTER = 0xADAB0AF1
    NEXUS_VENT = 0x2440A0FC
    NEXUS_WALLFAN = 0x1FA26F80
    NORMANDY_BEACON = 0xCC905DCE
    NOTIFY_ADDITIONALRESOURCES = 0xF4860355
    NOTIFY_AREANOTCLEAR = 0x129A400
    NOTIFY_ASSISTANT = 0x44073D5F
    NOTIFY_ATTACKSHIPSENGAGED = 0x97E57481
    NOTIFY_BASEOUTRANGE = 0xC25586D1
    NOTIFY_BASEOUTRANGE_RETURN = 0x9D895AAE
    NOTIFY_BUILDLIMIT = 0x85C9120C
    NOTIFY_CIVILIANFREIGHTER_DESTROYED = 0x75D6D35A
    NOTIFY_CRITIAL_ENERGY = 0xAF6B907C
    NOTIFY_CRITIAL_HIT = 0xB4DC4AF7
    NOTIFY_CRITICAL_COLD = 0x3534E9B7
    NOTIFY_CRITICAL_HEAT = 0xEE9FF4E3
    NOTIFY_CRITICAL_NOOXYGEN = 0xF718BE58
    NOTIFY_CRITICAL_RAD = 0x6694BE72
    NOTIFY_CRITICAL_TOXIC = 0xE80C3762
    NOTIFY_DAMAGESUSTAINED = 0x70C2A03A
    NOTIFY_DAMAGEVEHICLE = 0x8D4D1E66
    NOTIFY_DAMAGEVEHICLESUSTAINED = 0x1A9FD076
    NOTIFY_ENERGY_PERCENT = 0xE4CE6907
    NOTIFY_EXTERNALVIEW = 0xB03C84EF
    NOTIFY_EXTREMEHAZARDPLANET = 0xF43765ED
    NOTIFY_EXTREMESENTINELPLANET = 0x83C94F75
    NOTIFY_FREIGHTERACQUIRED = 0x5FC34813
    NOTIFY_FREIGHTERWARP = 0x82FD0FD1
    NOTIFY_FUELDEPLETED = 0xEF3000F4
    NOTIFY_FUELREQUIRED = 0xE89842EA
    NOTIFY_GAS_PLANT = 0x3A05F2D6
    NOTIFY_HAZ_CAVE_COLD = 0xF31B087B
    NOTIFY_HAZ_CAVE_HEAT = 0xC4AD486F
    NOTIFY_HAZ_CAVE_RADIATION = 0xF18F48E6
    NOTIFY_HAZ_CAVE_TOXIC = 0xC6F1B1A6
    NOTIFY_HAZ_CRIT_COLD = 0xBDE32DB6
    NOTIFY_HAZ_CRIT_HEAT = 0x1C46AC7E
    NOTIFY_HAZ_CRIT_RADIATION = 0x1CDFE22D
    NOTIFY_HAZ_CRIT_TOXIC = 0x4AA5AE85
    NOTIFY_HAZ_NIGHT_COLD = 0xD9846BCE
    NOTIFY_HAZ_NIGHT_HEAT = 0xF7B71686
    NOTIFY_HAZ_NIGHT_RADIATION = 0x90E58735
    NOTIFY_HAZ_NIGHT_TOXIC = 0x714CA8DD
    NOTIFY_HAZ_TEMP_STABLE = 0xB56C8D2F
    NOTIFY_HAZ_WATER_COLD = 0x81DE761F
    NOTIFY_HAZ_WATER_HEAT = 0x5BC840DB
    NOTIFY_HAZ_WATER_TOXIC = 0x6E79BAEA
    NOTIFY_HIT_COLD = 0xD38A3CED
    NOTIFY_HIT_ENERGY = 0x869CE84F
    NOTIFY_HIT_HEAT = 0xE92FA0E9
    NOTIFY_HIT_RAD = 0x176C6800
    NOTIFY_HIT_TOXIC = 0x9B632C5C
    NOTIFY_HOMEPLANET = 0xA44B6BB2
    NOTIFY_HOMEPLANETESTABLISHED = 0x648ABCEC
    NOTIFY_HOSTILES = 0x19F50A20
    NOTIFY_HOSTILES_DEFEATED = 0x5886A77D
    NOTIFY_HOSTILESYSTEM = 0xE60E20FE
    NOTIFY_HOSTILESYSTEMENGAGE = 0x4161E437
    NOTIFY_HOSTILESYSTEMWEAPONS = 0xE3138F29
    NOTIFY_HOT_ROCK = 0x2022A12E
    NOTIFY_INSUFFICIENTRESOURCES = 0x87CD5C9B
    NOTIFY_INTERNALVIEW = 0xE5A5363D
    NOTIFY_INV_TRANSFERRED = 0xF5199CCD
    NOTIFY_INVENTORY_SHIP_FULL = 0x7FEAB5CC
    NOTIFY_INVENTORY_SUIT_FULL = 0x57A8357F
    NOTIFY_ITEM_RECEIVED = 0x64B8C086
    NOTIFY_LANDING = 0x244555A
    NOTIFY_LANDINGSEQUENCE = 0xF8167905
    NOTIFY_LIFESUPPORTFALLING = 0xB1A96BA5
    NOTIFY_LOW_ENERGY = 0x916DB99C
    NOTIFY_MISSILEDESTROYED = 0xBE9C28A0
    NOTIFY_MISSILEENEMY = 0xC0A031A5
    NOTIFY_MISSILEENEMYINBOUND = 0xCFCA9E0C
    NOTIFY_MISSILEINBOUND = 0x8A853C06
    NOTIFY_MISSILEINCOMING = 0x117B54CF
    NOTIFY_MISSILEINCOMINGDESTROYED = 0xD9BC2ADC
    NOTIFY_MISSILEINCOMINGNEUTRALISED = 0x900B6253
    NOTIFY_MISSILELOCKED = 0xB2B6FCF5
    NOTIFY_MISSILENEUTRALISED = 0xB1E6896F
    NOTIFY_MISSILEREADY = 0x2704818
    NOTIFY_MISSILESDESTROYED = 0xFEA1EB33
    NOTIFY_MISSILESINCOMINGDESTROYED = 0x7844BE83
    NOTIFY_MISSILESINCOMINGNEUTRALISED = 0x305C90C8
    NOTIFY_MISSILESNEUTRALISED = 0x27D01838
    NOTIFY_NEW_SHIP = 0x4E3FD7DE
    NOTIFY_NEW_SLOT = 0x5048D544
    NOTIFY_NEW_SYSTEM = 0xEB09F91B
    NOTIFY_NEW_WEAPON = 0xF9D4781C
    NOTIFY_NEWASSISTANT = 0xA87F871F
    NOTIFY_NEWASSISTANTACQUIRED = 0xE4B6193F
    NOTIFY_NEWBOUNTY = 0x2ED364C4
    NOTIFY_NEWFREIGHTERACQUIRED = 0x8943C7D3
    NOTIFY_OBJECTIVE_COMPLETE = 0xBB7E1EA4
    NOTIFY_PIRATEENGINES = 0xF1E2BFBF
    NOTIFY_PIRATESLARGE = 0x8D320F36
    NOTIFY_PIRATESSPOTTED = 0x19003798
    NOTIFY_PRO_OFFLINE = 0x5DEDA806
    NOTIFY_PRO_PERCENT = 0x19661DC8
    NOTIFY_PRODUCT_RECEIVED = 0x36B5EED4
    NOTIFY_PULSE = 0xFDA5D118
    NOTIFY_PULSEOFFATMOS = 0x2A8B274B
    NOTIFY_PULSEOFFFUEL = 0xAFCB0F67
    NOTIFY_PULSEOFFLARGESHIP = 0x62E50DE2
    NOTIFY_PULSEOFFLOCAL = 0xC42AB9F0
    NOTIFY_PULSEOFFPLANET = 0x24FCA7F9
    NOTIFY_PULSEOFFSTATION = 0xCFF19999
    NOTIFY_RADLEAK_DAMAGE = 0x3A928F91
    NOTIFY_RADPRO_OFFLINE = 0x66C488F
    NOTIFY_REFUELVEHICLE = 0x7A00F4CE
    NOTIFY_SENTINELSARRIVED = 0x5807CBC3
    NOTIFY_SENTINELSDEACTIVATED = 0xBE2FA622
    NOTIFY_SENTINELSTARSHIPS = 0xD6463F36
    NOTIFY_SENTINELSTARSHIPSCOMBAT = 0x965E55FA
    NOTIFY_SHIELD_DOWN = 0x4619ABB5
    NOTIFY_TARGETACQUIRED = 0x4734B5E6
    NOTIFY_TARGETLOCKED = 0x22D490DC
    NOTIFY_TECHNOLOGYCRITICALLYDAMAGED = 0x8D9A8992
    NOTIFY_THRUSTERSOFFATMOS = 0x7AD9AE32
    NOTIFY_THRUSTERSOFFLARGESHIP = 0xD1B3E833
    NOTIFY_THRUSTERSOFFLOCAL = 0x206BDF55
    NOTIFY_THRUSTERSOFFSTATION = 0xFFAE5BB8
    NOTIFY_TOXICPRO_OFFLINE = 0x52C65D7
    NOTIFY_TRANSFERRED = 0xB1FB7B81
    NOTIFY_TRANSFERRED_ELEMENT = 0x92F3EE84
    NOTIFY_TRANSFERRED_PRODUCT = 0x1BBA22D9
    NOTIFY_UNITS_DEPLETED = 0x1B43FD00
    NOTIFY_UNITS_INSUFFICIENT = 0x77EA828C
    NOTIFY_UNITS_RECEIVED = 0xE2A736C0
    NOTIFY_VEHICLE = 0xE31EB0A7
    NOTIFY_VEHICLEACQUIRED = 0x79BFA8D7
    NOTIFY_VEHICLEDEPOLYED = 0x55CB1197
    NOTIFY_VEHICLEMOBILISED = 0x22ACF15B
    NOTIFY_VEHICLESUMMONED = 0xE0F39F69
    NOTIFY_WARNING = 0xEC145583
    NOTIFY_WARP = 0x261F5C3B
    NOTIFY_WARPING = 0x66D34BA5
    NPC_CLOTHING_1H_INTERACT_IPAD01 = 0x5AA4948A
    NPC_CLOTHING_1H_INTERACT_IPAD02 = 0x5AA49489
    NPC_CLOTHING_1H_SITTING_INTERACT_IPAD01 = 0xF18063B3
    NPC_CLOTHING_1H_SITTING_INTERACT_IPAD02 = 0xF18063B0
    NPC_CONSTRUCTION_TERMINAL = 0x1433F1D1
    NPC_FOLEY_CLOTHING_0H_IDLE_BASIC01 = 0xD646765B
    NPC_FOLEY_CLOTHING_0H_IDLE_BASIC02 = 0xD6467658
    NPC_FOLEY_CLOTHING_0H_IDLE_BASIC03 = 0xD6467659
    NPC_FOLEY_CLOTHING_0H_IDLE_BASIC04 = 0xD646765E
    NPC_FOLEY_CLOTHING_0H_IDLE_BASIC05 = 0xD646765F
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKDOWN01 = 0x5D508CC4
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKLEFT01 = 0x93461FF7
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKLEFT02 = 0x93461FF4
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKLEFT03 = 0x93461FF5
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKRIGHT01 = 0x7A2CAEC
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKRIGHT02 = 0x7A2CAEF
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKRIGHT03 = 0x7A2CAEE
    NPC_FOLEY_CLOTHING_0H_IDLE_LOOKUP01 = 0xDC60245B
    NPC_FOLEY_CLOTHING_0H_INT_CNSL_IN = 0x6D1BD65F
    NPC_FOLEY_CLOTHING_0H_INT_CNSL_LP = 0x701BDA9A
    NPC_FOLEY_CLOTHING_0H_INT_CNSL_OUT = 0xAD6D0F2
    NPC_FOLEY_CLOTHING_0H_INT_RT_01_IN = 0xA9983603
    NPC_FOLEY_CLOTHING_0H_INT_RT_01_LP = 0xA4982EFE
    NPC_FOLEY_CLOTHING_0H_INT_RT_01_OUT = 0x168E23FE
    NPC_FOLEY_CLOTHING_0H_INT_RT_02_IN = 0x558369C6
    NPC_FOLEY_CLOTHING_0H_INT_RT_02_LP = 0x5A8371F7
    NPC_FOLEY_CLOTHING_0H_INT_RT_02_OUT = 0x7EEEB7C9
    NPC_FOLEY_CLOTHING_0H_INT_RT_03 = 0xF65FDE5D
    NPC_FOLEY_CLOTHING_0H_INT_RT_04 = 0xF65FDE5A
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_01 = 0xF6916F77
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_02 = 0xF6916F74
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_03 = 0xF6916F75
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_04 = 0xF6916F72
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_05 = 0xF6916F73
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_06 = 0xF6916F70
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_07 = 0xF6916F71
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_08 = 0xF6916F7E
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_09 = 0xF6916F7F
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_10 = 0xF79170E9
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_11 = 0xF79170E8
    NPC_FOLEY_CLOTHING_0H_INTER_LISTEN_12 = 0xF79170EB
    NPC_FOLEY_CLOTHING_0H_SHUTDWN_IN = 0xB237B602
    NPC_FOLEY_CLOTHING_0H_SHUTDWN_OUT = 0x9AAF193D
    NPC_FOLEY_CLOTHING_0H_SIT_ANGRY01 = 0x7502B292
    NPC_FOLEY_CLOTHING_0H_SIT_ANGRY02 = 0x7502B291
    NPC_FOLEY_CLOTHING_0H_SIT_CHATTER01 = 0x7DE81D76
    NPC_FOLEY_CLOTHING_0H_SIT_CHATTER02 = 0x7DE81D75
    NPC_FOLEY_CLOTHING_0H_SIT_GREET01 = 0xC4F0B05E
    NPC_FOLEY_CLOTHING_0H_SIT_GREET02 = 0xC4F0B05D
    NPC_FOLEY_CLOTHING_0H_SIT_HAPPY01 = 0xDA2DA237
    NPC_FOLEY_CLOTHING_0H_SIT_HAPPY02 = 0xDA2DA234
    NPC_FOLEY_CLOTHING_0H_SIT_LOOK_L01 = 0xB11AD035
    NPC_FOLEY_CLOTHING_0H_SIT_LOOK_L02 = 0xB11AD036
    NPC_FOLEY_CLOTHING_0H_SIT_LOOK_R01 = 0x350207DB
    NPC_FOLEY_CLOTHING_0H_SIT_LOOK_R02 = 0x350207D8
    NPC_FOLEY_CLOTHING_0H_SIT_LOOKARND = 0x8BC36BE
    NPC_FOLEY_CLOTHING_0H_SIT_NEUTRAL01 = 0xFDD53340
    NPC_FOLEY_CLOTHING_0H_SIT_NEUTRAL02 = 0xFDD53343
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_IDLE01 = 0x1826E27B
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_IDLE02 = 0x1826E278
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_IDLE03 = 0x1826E279
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_IDLE04 = 0x1826E27E
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_IDLE05 = 0x1826E27F
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_IDLE06 = 0x1826E27C
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_IDLE07 = 0x1826E27D
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_INTO = 0x4BB40382
    NPC_FOLEY_CLOTHING_0H_SIT_SOFA_OUTOF = 0xCE067C73
    NPC_FOLEY_CLOTHING_0H_SIT_STRETCH = 0x6C12BE63
    NPC_FOLEY_CLOTHING_0H_STAND_ANGRY01 = 0x44CB2FE6
    NPC_FOLEY_CLOTHING_0H_STAND_ANGRY02 = 0x44CB2FE5
    NPC_FOLEY_CLOTHING_0H_STAND_ANGRY05 = 0x44CB2FE2
    NPC_FOLEY_CLOTHING_0H_STAND_ANGRY_LP01 = 0xD00508BF
    NPC_FOLEY_CLOTHING_0H_STAND_ANGRY_LP02 = 0xD00508BC
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER01 = 0x9C9C8A22
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER02 = 0x9C9C8A21
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER03 = 0x9C9C8A20
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER04 = 0x9C9C8A27
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER05 = 0x9C9C8A26
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER06 = 0x9C9C8A25
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER07 = 0x9C9C8A24
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER08 = 0x9C9C8A2B
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER09 = 0x9C9C8A2A
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER10 = 0x9B9C88B0
    NPC_FOLEY_CLOTHING_0H_STAND_CHATTER14 = 0x9B9C88B4
    NPC_FOLEY_CLOTHING_0H_STAND_GREET01 = 0x4BCB4C32
    NPC_FOLEY_CLOTHING_0H_STAND_GREET02 = 0x4BCB4C31
    NPC_FOLEY_CLOTHING_0H_STAND_GREET03 = 0x4BCB4C30
    NPC_FOLEY_CLOTHING_0H_STAND_GREET04 = 0x4BCB4C37
    NPC_FOLEY_CLOTHING_0H_STAND_GREET05 = 0x4BCB4C36
    NPC_FOLEY_CLOTHING_0H_STAND_GREET06 = 0x4BCB4C35
    NPC_FOLEY_CLOTHING_0H_STAND_GREET07 = 0x4BCB4C34
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY01 = 0xAD11189B
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY02 = 0xAD111898
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY03 = 0xAD111899
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY04 = 0xAD11189E
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY05 = 0xAD11189F
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY06 = 0xAD11189C
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY07 = 0xAD11189D
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY08 = 0xAD111892
    NPC_FOLEY_CLOTHING_0H_STAND_HAPPY09 = 0xAD111893
    NPC_FOLEY_CLOTHING_0H_STAND_NEUTRAL01 = 0x6A7ED79C
    NPC_FOLEY_CLOTHING_0H_STAND_NEUTRAL02 = 0x6A7ED79F
    NPC_FOLEY_CLOTHING_0H_TURN_L_120 = 0x61557725
    NPC_FOLEY_CLOTHING_0H_TURN_R_120 = 0x799CCD57
    NPC_FOLEY_CLOTHING_1H_INTERACT_IPAD03 = 0x9E246668
    NPC_FOLEY_CLOTHING_1H_INTERACT_IPAD04 = 0x9E24666F
    NPC_FOLEY_CLOTHING_1H_INTERACT_IPAD05 = 0x9E24666E
    NPC_FOLEY_CLOTHING_1H_SAD_LP01 = 0x1B899810
    NPC_FOLEY_CLOTHING_1H_STAND_ANGRY03 = 0x62053463
    NPC_FOLEY_CLOTHING_1H_STAND_ANGRY04 = 0x62053464
    NPC_FOLEY_CLOTHING_1H_STAND_NEUTRAL03 = 0xB895DC69
    NPC_FOLEY_CLOTHING_1H_STAND_NEUTRAL04 = 0xB895DC6E
    NPC_FOLEY_CLOTHING_1H_UNSHEATH_IPAD = 0xEEA97
    NPC_FOOTSTEPS_GENERIC = 0xEBEBBF24
    NPC_HANDHOLOGRAM = 0x826D3313
    NPC_ROBOT_FOOTSTEP = 0x72AB250
    NPC_SCIENCE_WORKSTATION_ARMS = 0x2AE4A2D5
    NPC_SHIP_ENGINE_FREIGHTER_FRONT = 0xA84C5D19
    NPC_SHIP_ENGINES = 0xB264012B
    NPC_SHIP_IDLE = 0x24526C1C
    NPC_SHIP_LAND = 0x87C20BE9
    NPC_SHIP_LAND_IMPACT = 0xD3FDB23A
    NPC_SHIP_LAND_ROTATE = 0xFA6D3689
    NPC_SHIP_LAND_ROTATE_STOP = 0xB736C13C
    NPC_SHIP_LASER = 0x922FB54B
    NPC_SHIP_LASERS01 = 0x71E894F3
    NPC_SHIP_LASERS02 = 0x71E894F0
    NPC_SHIP_LASERS03 = 0x71E894F1
    NPC_SHIP_LASERS04 = 0x71E894F6
    NPC_SHIP_POLICE_SIREN = 0xCEA4E032
    NPC_SHIP_POLICE_SIREN_STOP = 0xFB949B91
    NPC_SHIP_SCAN_PULSE = 0xD80B1123
    NPC_SHIP_SPACESTATION_FLYIN = 0xF746B237
    NPC_SHIP_TAKEOFF = 0xAA8DD0FA
    NPC_SHIPS_WARPIN = 0xA3176202
    NPC_SHIPS_WARPOUT = 0xCACADD3D
    NPC_SHIPSMALL_WARPIN = 0xC0106C54
    NPC_SHIPSMALL_WARPOUT = 0xA4CB6FF3
    NPC_SPEECH_CHATTER = 0xE46F6261
    NPC_TALK_STOP = 0xE4A1A5E6
    NPC_VOCAL_1H_ANGRY_STAND_03 = 0x9F5CFFE9
    NPC_VOCAL_1H_ANGRY_STAND_04 = 0x9F5CFFEE
    NPC_VOCAL_1H_NEUTRAL_STAND_03 = 0x5519FD7
    NPC_VOCAL_ANGRY_STAND01 = 0x36FAD9EA
    NPC_VOCAL_ANGRY_STAND02 = 0x36FAD9E9
    NPC_VOCAL_CHATTER_STAND_01 = 0x8C317B1F
    NPC_VOCAL_CHATTER_STAND_02 = 0x8C317B1C
    NPC_VOCAL_CHATTER_STAND_03 = 0x8C317B1D
    NPC_VOCAL_CHATTER_STAND_04 = 0x8C317B1A
    NPC_VOCAL_GREET_STAND_01 = 0x3547199B
    NPC_VOCAL_GREET_STAND_02 = 0x35471998
    NPC_VOCAL_GREET_STAND_03 = 0x35471999
    NPC_VOCAL_GREET_STAND_04 = 0x3547199E
    NPC_VOCAL_GREET_STAND_06 = 0x3547199C
    NPC_VOCAL_GREET_STAND_07 = 0x3547199D
    NPC_VOCAL_HAPPY_STAND_01 = 0xEBF7787C
    NPC_VOCAL_HAPPY_STAND_02 = 0xEBF7787F
    NPC_VOCAL_HAPPY_STAND_03 = 0xEBF7787E
    NPC_VOCAL_HAPPY_STAND_04 = 0xEBF77879
    NPC_VOCAL_HAPPY_STAND_05 = 0xEBF77878
    NPC_VOCAL_HAPPY_STAND_06 = 0xEBF7787B
    NPC_VOCAL_HAPPY_STAND_07 = 0xEBF7787A
    NPC_VOCAL_HAPPY_STAND_08 = 0xEBF77875
    NPC_VOCAL_IDLE_BASIC01 = 0x7EB4B73
    NPC_VOCAL_NEUTRAL_STAND_01 = 0xE4463E89
    NPC_VOCAL_NEUTRAL_STAND_02 = 0xE4463E8A
    NPC_VOCAL_SIT_ANGRY_01 = 0x1BC6EB37
    NPC_VOCAL_SIT_ANGRY_02 = 0x1BC6EB34
    NPC_VOCAL_SIT_CHATTER_01 = 0xBA70E1BB
    NPC_VOCAL_SIT_CHATTER_02 = 0xBA70E1B8
    NPC_VOCAL_SIT_GREET_01 = 0x3CF60EF3
    NPC_VOCAL_SIT_GREET_02 = 0x3CF60EF0
    NPC_VOCAL_SIT_HAPPY_01 = 0x8FD013FC
    NPC_VOCAL_SIT_HAPPY_02 = 0x8FD013FF
    NPC_WPN_FREIGHTER_GUN = 0xDBF6ADA4
    NPC_WPN_FREIGHTER_LASER = 0x87E7FDC7
    NPC_WPN_FREIGHTER_LASER_END = 0x965A42C9
    NPC_WPN_FREIGHTER_TURRET_FIRE = 0x2A924483
    NPC_WPN_FREIGHTER_TURRET_ROTATE = 0xE146872E
    NPC_WPN_FREIGHTER_TURRET_ROTATE_STOP = 0x65002B2D
    NPC_WPN_SMALLSHIP_LASER = 0xDD05AA14
    NPC_WPN_SMALLSHIP_LASER_STOP = 0xFAA48C13
    NPC_WPN_TORPEDO_LAUNCH = 0x3B44D26C
    NPC_WPN_TORPEDO_LP_STOP = 0xA8D00D38
    NPC_WPN_TURRET_START = 0x6AB593D2
    NPC_WPN_TURRET_STOP = 0x3C50938A
    OBJ_ATMOSPHERE_HARVESTER = 0x71246308
    OBJ_BARREL_MED = 0xC9953608
    OBJ_CRATE_LARGE = 0x613B2D40
    OBJ_CRATE_MED = 0xC5E4BAC7
    OBJ_CRATE_SMALLA = 0x6B9851E9
    OBJ_CRATE_SMALLB = 0x6B9851EA
    OBJ_CRUISER_WORKSHOP_LP = 0xC31DF9E3
    OBJ_FLAG = 0x4D907B09
    OBJ_HARVESTER = 0x4099D393
    OBJ_HEALTHSTATION_OFF = 0x777473D5
    OBJ_HEALTHSTATION_ON = 0xD2519969
    OBJ_MINING_AMU = 0x5F04D3FD
    OBJ_MINING_GAS_HARVESTER = 0xD278D30E
    OBJ_MONOLITH = 0xAFF212EB
    OBJ_PLAQUE = 0x6E4AAD8B
    OBJ_PORTABLEREFINERY_START = 0x318F8A43
    OBJ_PORTABLEREFINERY_STOP = 0xC52354C1
    OBJ_REFINERYLARGE_IDLE = 0x344C4FB9
    OBJ_REFINERYLARGE_START = 0xA7C2D6AD
    OBJ_REFINERYLARGE_STOP = 0x2745AFEF
    OBJ_REFINERYMEDIUM_IDLE = 0xF037F80F
    OBJ_REFINERYMEDIUM_START = 0xC27FE2E7
    OBJ_REFINERYMEDIUM_STOP = 0x4A31510D
    OBJ_ROBOTHEAD = 0x91611EAB
    OBJ_ROBOTHEAD_HAND = 0xBB49D295
    OBJ_RUINS_RESOURCE_LP = 0x57539186
    OBJ_SHIELD_REPAIRER_OFF = 0x2D439567
    OBJ_SHIELD_REPAIRER_ON = 0x5D1B7B93
    OBJ_SPINNINGCHAIR = 0x31D21E68
    OBJ_SPINNINGGLOBE = 0x2E2F03EC
    OBJ_SPINNINGSHAPE = 0x6BD9CA70
    OBJ_STANDINGSTONE_ACTIVATE = 0x994C77D2
    OBJ_STANDINGSTONE_RARE = 0xA4603971
    OBJ_STANDINGSTONES = 0x5CEA7805
    OBJ_WAYPOINT = 0xEB0C2542
    OBJECT_ANALYSING = 0x18EF30C7
    OBJECT_OF_INTEREST = 0x7C61D8C5
    OBSERVATORY_HOLOGRAM = 0x4587B823
    OCTO_IDLE_FR1 = 0x4982E72D
    OCTO_IDLE_FR145 = 0x1136566C
    OCTO_IDLE_FR353 = 0x1C3AE4EB
    OCTO_IDLE_FR575 = 0x9E2CA6C1
    OCTO_IDLE_FR780 = 0x91310F9B
    OCTO_SPRINGWALK_FR1 = 0x3FA36967
    OCTO_SPRINGWALK_FR161 = 0x50F34D8
    OCTO_WALK_FR1 = 0xD7EC18B8
    OCTO_WALK_FR145 = 0x890DC0A1
    OCTO_WALK_FR353 = 0xE130F12
    OCTO_WALK_FR575 = 0xFC176FCC
    OCTO_WALK_FR780 = 0x811CBEB6
    OILSTREAM = 0x607B82D7
    ORBIDLE = 0xE0625692
    ORBIDLE_LOOP = 0xAAD2AC93
    PARTICLES_DUSTDEVIL = 0x73BA60C9
    PARTICLES_DUSTDEVIL_STOP = 0x88C0177C
    PARTICLES_ELECTRICAL_SPARKS = 0xFC91F6C0
    PARTICLES_ELECTRICAL_SPARKS_STOP = 0xE475E6EF
    PARTICLES_ELECTRICALANOMALY = 0x94FDA5E6
    PARTICLES_ELECTRICALANOMALY_STOP = 0x4736D7F5
    PARTICLES_GEOTHERMAL = 0x3AC18629
    PARTICLES_GEOTHERMAL_EXPLODE = 0x2C5CFB0B
    PARTICLES_GEOTHERMAL_STOP = 0x509A891C
    PARTICLES_GRAVITYINVERSION = 0xCC383C04
    PARTICLES_GRAVITYINVERSION_STOP = 0x3D3A9E63
    PARTICLES_LAVAVENT = 0xD8080D82
    PARTICLES_LAVAVENT_EXPLODE = 0xF72E024
    PARTICLES_LAVAVENT_STOP = 0xC2360C01
    PARTICLES_RADIOANOMALY = 0x72F46861
    PARTICLES_RADIOANOMALY_STOP = 0x2609864
    PARTICLES_SPARKS_COMMON = 0x89739B49
    PARTICLES_SPARKS_COMMON_STOP = 0x9D9126FC
    PARTICLES_TOXICCLOUD = 0x1278E4D9
    PARTICLES_TOXICCLOUD_STOP = 0xB205BCAC
    PET_EGG_INDUCE = 0x979DE509
    PET_EGGSPLOSION = 0x874B2413
    PET_UI_ADOPT = 0xBA4E41AE
    PET_UI_CALLPET = 0x507485B
    PET_UI_COLLECT_EGGS = 0x23B82F2F
    PET_UI_CUSTOM_FLANK = 0xBB6990AA
    PET_UI_CUSTOM_SELECT = 0x7F84507C
    PET_UI_DISMISS = 0x6797B7FC
    PET_UI_EGG_HATCH = 0x92C0559C
    PET_UI_FOOD_PELLET = 0x60B750C1
    PET_UI_MENU_HOVER = 0x64BD01EE
    PET_UI_PAT = 0xFEAFB237
    PET_UI_SUMMON = 0x716F5B99
    PET_UI_TREAT = 0x28CCAA60
    PILGRIM_BOOST_START = 0x5D72659C
    PILGRIM_BOOST_STOP = 0xAB53D70
    PILGRIM_HORN_START = 0xEDE0C7A2
    PILGRIM_HORN_STOP = 0xDE95EC9A
    PILGRIM_IDLE_EXTERIOR = 0x698C1BA7
    PILGRIM_IMPACTS = 0x7D8D4FFD
    PILGRIM_JUMP = 0xE6D853F8
    PILGRIM_START = 0x1AA44330
    PILGRIM_STOP = 0xCEC2C09C
    PILGRIM_SUSPENSION = 0x6EFEA44F
    PIPE_SMOKE = 0xD9CB4AF
    PIPE_SMOKE_STOP = 0xC85D689A
    PIRATE_SALVAGE_CHAIR_SPIN = 0x839C9669
    PIRATE_STATION_GENERATOR = 0xC421C6D5
    PIRATE_STATIONCORE = 0xED62DD76
    PL_BREATHING_START = 0x8D7EFCF7
    PL_BREATHING_STOP = 0x73C9C55D
    PL_CAMOUFLAGE_IN = 0x4E6C24EA
    PL_CAMOUFLAGE_OUT = 0x793836C5
    PL_DAMAGE_WARNING_LOW_HEALTH_LP = 0x9AE9352D
    PL_DAMAGE_WARNING_LOW_HEALTH_LP_STOP = 0x1AD6B960
    PL_DAMAGE_WARNING_SHIELD_LOSS = 0x5BE3084
    PL_FISHING_LINE_PULL = 0x4148A197
    PL_FISHING_LINE_PULL_STOP = 0xC6256932
    PL_FOLEY_BODYHITS = 0x915FF2EE
    PL_FOLEY_CLOTHING_0H_SWIM_BACK = 0x3DEA4F58
    PL_FOLEY_CLOTHING_0H_SWIM_FORWARD = 0xFABD31D4
    PL_FOLEY_CLOTHING_0H_SWIM_IDLE = 0x50A7E0CF
    PL_FOLEY_CLOTHING_0H_SWIM_LEFT_RIGHT = 0xBA7587F5
    PL_FOLEY_CLOTHING_1H_MULTITOOL_MELEE = 0x9D96CD91
    PL_FOLEY_CLOTHING_1H_OVERHEAT = 0x10B47D33
    PL_FOLEY_CLOTHING_1H_RELOAD = 0xD9219578
    PL_FOLEY_CLOTHING_2H_MULTITOOL_MELEE = 0xD63657DC
    PL_FOLEY_CLOTHING_2H_MULTITOOLRELOAD = 0x3036188A
    PL_FOLEY_CLOTHING_DEATH_KNEES = 0xC5403F26
    PL_FOLEY_CLOTHING_DEATH_SWIM = 0x5FC94D6
    PL_FOLEY_CLOTHING_EMOTE_CALLPET = 0x7F9262A7
    PL_FOLEY_CLOTHING_EMOTE_DANCEINTO = 0x843BC963
    PL_FOLEY_CLOTHING_EMOTE_FALLKNEESINTO = 0x9E81C443
    PL_FOLEY_CLOTHING_EMOTE_FALLKNEESLP = 0x846370D
    PL_FOLEY_CLOTHING_EMOTE_FEED = 0x16F3DD78
    PL_FOLEY_CLOTHING_EMOTE_GREET_WAVE = 0x451D518D
    PL_FOLEY_CLOTHING_EMOTE_HEROICINTO = 0x6C7928E2
    PL_FOLEY_CLOTHING_EMOTE_LOOKDISTANCEINTO = 0xEC9B5CE
    PL_FOLEY_CLOTHING_EMOTE_MINDBLOWN = 0x8CC7D7CE
    PL_FOLEY_CLOTHING_EMOTE_NEG_FINGERWAG = 0xC74E5AF9
    PL_FOLEY_CLOTHING_EMOTE_POINT = 0x8685F006
    PL_FOLEY_CLOTHING_EMOTE_RELAXINTO = 0xAA4B1AAC
    PL_FOLEY_CLOTHING_EMOTE_SITINTO = 0x71A2E776
    PL_FOLEY_CLOTHING_EMOTE_STROKE = 0x2056D3D0
    PL_FOLEY_CLOTHING_EMOTE_THUMBSUP = 0x1B2E5FE8
    PL_FOLEY_CLOTHING_EMOTE_WONDER = 0x90D499C5
    PL_FOLEY_CLOTHING_FALL_CONTROL = 0xAA776AEA
    PL_FOLEY_CLOTHING_FALL_PANIC = 0xE28BA57C
    PL_FOLEY_CLOTHING_IDLE_WEIGHT_SHIFT = 0x48554711
    PL_FOLEY_CLOTHING_JOG_TO_IDLE = 0x31229EF8
    PL_FOLEY_CLOTHING_LADDER_CYCLE_DOWN = 0xA5310BB
    PL_FOLEY_CLOTHING_LADDER_CYCLE_UP = 0x3D3DDF5C
    PL_FOLEY_CLOTHING_LADDER_DISMOUNT_BOTTOM = 0x8FF84B91
    PL_FOLEY_CLOTHING_LADDER_DISMOUNT_TOP = 0xB5A5F559
    PL_FOLEY_CLOTHING_LADDER_MOUNT_BOTTOM = 0xF4ED6D9D
    PL_FOLEY_CLOTHING_LADDER_MOUNT_TOP = 0xFE176015
    PL_FOLEY_CLOTHING_LOCO = 0xB79EA60A
    PL_FOLEY_CLOTHING_MULTITOOL_DRAW = 0x9B2BB175
    PL_FOLEY_CLOTHING_MULTITOOL_HOLSTER = 0xAA65F0D4
    PL_FOLEY_CLOTHING_MULTITOOL_OVERHEAT = 0x1BD229F3
    PL_FOLEY_CLOTHING_MULTITOOL_RELOAD = 0x5C1C938
    PL_FOLEY_CLOTHING_RUN_TO_IDLE = 0x73450387
    PL_FOLEY_CLOTHING_SWIM_STOPALL = 0x7F90AA67
    PL_FOLEY_COCKPIT_SIT_IN = 0x4A716F50
    PL_FOLEY_COCKPIT_SIT_OUT = 0x679690B7
    PL_FOLEY_COCKPIT_SIT_TO_STAND = 0x2568E81F
    PL_FOLEY_EMOTE_DANCELOOP = 0xD832CAD2
    PL_FOLEY_EMOTE_HELP = 0x3EAC0F72
    PL_FOLEY_EMOTE_JOY = 0xB65D913
    PL_FOLEY_EMOTE_LAUGH = 0x953BF62E
    PL_FOLEY_EMOTE_NEEDRESOURCE = 0xF62E41F3
    PL_FOLEY_EMOTE_OVERHERE = 0x7B06DE1F
    PL_FOLEY_EMOTE_UNDERWATER_OK = 0xC10135E9
    PL_FOLEY_EMOTE_UNDERWATER_THUMBSDOWN = 0x920C1178
    PL_FOLEY_EMOTE_UNDERWATER_THUMBSUP = 0xC732E21B
    PL_FOLEY_FISHING_CASTOFF = 0x889F330F
    PL_FOLEY_FISHING_FLICK = 0x34157F46
    PL_FOLEY_FISHING_LAND_FISH = 0x21FA9047
    PL_FOLEY_FISHING_LINE_STOP = 0x80D9F8E2
    PL_FOLEY_FISHING_REEL_IN = 0x36BDB29D
    PL_FOLEY_FISHING_STOP = 0x6581AFD5
    PL_FOLEY_SLOPE_SLIDE_START = 0xD922A3D6
    PL_FOLEY_SLOPE_SLIDE_STOP = 0xE2280BD6
    PL_HAZARD_CRITICAL_HIT = 0x95BC4F32
    PL_HAZARD_RECOVERY = 0x9A6776
    PL_HAZARD_WARNING = 0xD0D988E1
    PL_HEALTH = 0xB050FA76
    PL_OUTOFBREATH = 0x2AC9FF29
    PL_PROTECTION_CHARGE = 0xE20B8CE4
    PL_PROTECTION_END = 0x38657B27
    PL_PROTECTION_LP = 0x1D037974
    PL_RUN_FAIL = 0xD51DCF4E
    PL_SHIELD_CHARGE = 0x969598CA
    PL_SHIELD_HIT = 0x17D34A45
    PL_SHIELD_LOWSWEEP = 0xCBBD44C4
    PL_SHIELD_SHIP_HIT_BIG = 0x74EB2D51
    PL_SHIELD_SHIP_HIT_SMALL = 0x768B8A3E
    PL_SHIP_BOOST_FAIL = 0x9A4E27BD
    PL_SHIP_BOOST_POWERUP = 0x62CDCDDB
    PL_SHIP_BOOST_START = 0xCDB230F3
    PL_SHIP_BOOST_STOP = 0x6B0B4731
    PL_SHIP_BUILDABLE_ENTER_COCKPIT = 0x3C18D292
    PL_SHIP_BUILDABLE_EXIT_COCKPIT = 0x417C1C10
    PL_SHIP_BUILDABLE_GEARVENT = 0x38C3F982
    PL_SHIP_BUILDABLE_GEARVENT_END = 0x31A861D8
    PL_SHIP_BUILDABLE_LANDINGGEAR_END = 0xC2FDDC8
    PL_SHIP_BUILDABLE_LANDINGGEAR_START = 0xDF71E0F3
    PL_SHIP_BUILDABLE_LANDINGTHRUSTERS_END = 0xF92A8BDD
    PL_SHIP_BUILDABLE_LANDINGTHRUSTERS_START = 0x7B10416
    PL_SHIP_BUILDABLE_LIFT_RAMPDOWN = 0xAA976ED8
    PL_SHIP_BUILDABLE_LIFT_RAMPUP = 0xB5D8867B
    PL_SHIP_BUILDABLE_PROP_KITCHENA = 0x831C3D55
    PL_SHIP_BUILDABLE_PROP_LIVINGWALL = 0x6C4E6063
    PL_SHIP_BUILDABLE_PROP_RADAR = 0x1452DE58
    PL_SHIP_BUILDABLE_PROP_RADARC = 0x567404EB
    PL_SHIP_BUILDABLE_PROP_REFINER = 0x37CDA337
    PL_SHIP_BUILDABLE_PROP_REFINERA = 0xFB7EFF4
    PL_SHIP_BUILDABLE_PROP_REFINERC = 0xFB7EFF6
    PL_SHIP_BUILDABLE_RAMPA_CLOSEHALF = 0x651B9BF5
    PL_SHIP_BUILDABLE_RAMPA_DOWN = 0x692ADD5A
    PL_SHIP_BUILDABLE_RAMPA_OPENHALF = 0xEA18CF21
    PL_SHIP_BUILDABLE_RAMPA_UP = 0xAFC917F9
    PL_SHIP_BUILDABLE_RAMPB_CLOSEHALF = 0xB6DFB606
    PL_SHIP_BUILDABLE_RAMPB_DOWN = 0xAE432E2B
    PL_SHIP_BUILDABLE_RAMPB_OPENHALF = 0x31FF10A4
    PL_SHIP_BUILDABLE_RAMPB_UP = 0x6590EFEC
    PL_SHIP_BUILDABLE_RAMPDOWNLANDA = 0x2EFD9516
    PL_SHIP_BUILDABLE_RAMPDOWNLANDB = 0x2EFD9515
    PL_SHIP_BUILDABLE_VENT = 0xAE59D7FB
    PL_SHIP_BUILDABLE_VENT_END = 0x2CCE781D
    PL_SHIP_BURN = 0xB0660BE
    PL_SHIP_BURN_STOP = 0x958071DD
    PL_SHIP_COCKPIT_RAIN = 0x2380A5E5
    PL_SHIP_COCKPIT_RAIN_STOP = 0xBBD86828
    PL_SHIP_ENGINES_START = 0x7FBDB4F7
    PL_SHIP_ENGINES_START_REMOTE = 0x38FAB124
    PL_SHIP_ENGINES_STOP = 0xE8A32D5D
    PL_SHIP_ENGINES_STOP_REMOTE = 0x46E00B8A
    PL_SHIP_ENTER = 0x17D409FD
    PL_SHIP_EXIT = 0x2F3259B1
    PL_SHIP_GROUND_IMPACT = 0x2CE59259
    PL_SHIP_HASLANDED = 0xB585E053
    PL_SHIP_HASLANDED_RACER = 0xEDFA38D
    PL_SHIP_HYPERSPACE_END = 0xC1AE6E4B
    PL_SHIP_HYPERSPACE_START = 0x4AA4CB30
    PL_SHIP_IDLE = 0xFC4A8773
    PL_SHIP_LANDING = 0xB35579F6
    PL_SHIP_MINIWARP_COUNTDOWN = 0x5064D24A
    PL_SHIP_MINIWARP_END = 0x53B4B6F4
    PL_SHIP_MINIWARP_JUMP = 0xA54A1259
    PL_SHIP_RACER_LANDING = 0x23B40F78
    PL_SHIP_RACER_TAKEOFF = 0xB52D6DE5
    PL_SHIP_ROBOT_CARRIAGELOCK_LANDING = 0xECF68579
    PL_SHIP_ROBOT_CARRIAGELOCK_TAKEOFF = 0x19B453B0
    PL_SHIP_ROBOT_CHUNKYLEGS_LANDING = 0xECF46219
    PL_SHIP_ROBOT_CHUNKYLEGS_TAKEOFF = 0x19B23150
    PL_SHIP_ROBOT_FLIPWINGS_LANDING = 0x461EB821
    PL_SHIP_ROBOT_FLIPWINGS_TAKEOFF = 0xEC758F8
    PL_SHIP_ROBOT_HUGGINGWALLWINGS_LANDING = 0x1D6C0DD1
    PL_SHIP_ROBOT_HUGGINGWALLWINGS_TAKEOFF = 0xDE705488
    PL_SHIP_ROBOT_LANDINGGEAR_LANDING = 0x97B8DB7E
    PL_SHIP_ROBOT_LANDINGGEAR_TAKEOFF = 0xB9990F
    PL_SHIP_ROBOT_NEEDLEWINGS_LANDING = 0x30C68E35
    PL_SHIP_ROBOT_NEEDLEWINGS_TAKEOFF = 0x1D1BD23C
    PL_SHIP_ROBOT_SKIRTWINGS_LANDING = 0xBF6FFECD
    PL_SHIP_ROBOT_SKIRTWINGS_TAKEOFF = 0x4F094A34
    PL_SHIP_ROBOT_TOPWINGS_LANDING = 0x3E9FD09D
    PL_SHIP_ROBOT_TOPWINGS_TAKEOFF = 0x491445A4
    PL_SHIP_ROBOT_WALLWINGS_LANDING = 0xC04C033E
    PL_SHIP_ROBOT_WALLWINGS_TAKEOFF = 0x26D258CF
    PL_SHIP_SCANNED = 0xE2A36147
    PL_SHIP_SHIELD_DOWN = 0x7DC5CDE9
    PL_SHIP_SPACESTATION_LAUNCH_END = 0x824C1ACD
    PL_SHIP_SPARKS = 0x3A41BA4B
    PL_SHIP_SPARKS_STOP = 0x5E131FC6
    PL_SHIP_START_ACTIVE = 0x53F54244
    PL_SHIP_TAKEOFF = 0x1EA46787
    PL_SHIP_TAKEOFF_WHENREMAININSHIP = 0x67C6E21D
    PL_SHIP_THRUST_ONESHOTS = 0xDA41B521
    PL_SHIP_THRUST_REVERSE_ONESHOTS = 0xB71468B0
    PL_SHIP_TRANSITION_TO_PLANET_END = 0x102A0FD3
    PL_SHIP_TRANSITION_TO_PLANET_START = 0x6693D868
    PL_SHIP_TRANSITION_TO_SPACE_END = 0xF8BCF39
    PL_SHIP_TRANSITION_TO_SPACE_START = 0xB630765A
    PL_SHIP_VR_EXIT = 0x88814C78
    PL_SHIP_VR_EXIT_STOP = 0xFB5202B7
    PL_SHIP_WARP = 0x8D21AECF
    PL_SUIT_START = 0xA22F68E2
    PL_SUIT_STARTUP = 0x68319AB9
    PL_SUIT_STARTUP_CONFIRM = 0xCB37B9FC
    PL_SUIT_STARTUP_INTERACT_TIMER = 0x3C572AD4
    PL_SUIT_STARTUP_INTERACT_TIMER_STOP = 0xD1B12CD3
    PL_SUIT_STOP = 0xA1E440DA
    PL_SURVEYING = 0x64B2EA2A
    PL_SURVEYING_C = 0xC44E4630
    PL_SURVEYING_DISCOVER = 0x5CFC7900
    PL_SURVEYING_HIGHLIGHT = 0x5D0CC4E3
    PL_SURVEYING_L = 0xC44E463F
    PL_SURVEYING_R = 0xC44E4621
    PL_SURVEYING_SWITCHTO = 0x12FAB8BA
    PL_TELEPORT_WARP_END = 0xCAD30640
    PL_TELEPORT_WARP_START = 0xC5955A1B
    PL_VEHICLE_REMOTE_BOOST = 0xC188029
    PL_VEHICLE_REMOTE_DESTRUCTIBLE = 0xF466485A
    PL_VEHICLE_REMOTE_ENGINE = 0xABFB7216
    PL_VEHICLE_REMOTE_HORN = 0xC8F8145B
    PL_VEHICLE_REMOTE_IDLE = 0x27EBC5B6
    PL_VEHICLE_REMOTE_IMPACTS = 0xF9B16951
    PL_VEHICLE_REMOTE_JUMP = 0x934AB5F4
    PL_VEHICLE_REMOTE_START = 0xE2B75F44
    PL_VEHICLE_REMOTE_STOP = 0xED8F65F8
    PL_VEHICLE_REMOTE_SURFACE = 0x3B76DFB9
    PL_VEHICLE_REMOTE_SUSPENSION = 0x3B127ED3
    PL_WOUND = 0x82AA4045
    PL_WPN_SHIP_MISSILE_SHOOT = 0x404C8523
    PLACEMARKER_FLARE = 0xA539AE71
    PLACEMARKER_IMPACT = 0x5FC8A561
    PLACEMARKER_LP = 0x36097177
    PLACEMARKER_LP_STOP = 0xEDF59752
    PLACEMARKER_WOOSH = 0xCA202279
    PLANT_ATTACK = 0x4D6B4503
    PLANT_CLOSE = 0x7E3854F5
    PLANT_GASGIANT_STEAMER = 0x299D71F5
    PLANT_GATHER_ALOEFLESH = 0x755AFF3C
    PLANT_GATHER_FIREBERRY = 0x8716FE03
    PLANT_GATHER_FROZENTUBERS = 0xCFD83A4
    PLANT_GATHER_GRAHFRUIT = 0x20134DA1
    PLANT_GATHER_HEPTAWHEAT = 0x153FCA3A
    PLANT_GATHER_IMPULSEBEANS = 0x9063D3AF
    PLANT_GATHER_JADEPEAS = 0x4ED86D0A
    PLANT_GATHER_PULPYROOTS = 0xCEF5472C
    PLANT_GATHER_SWEETROOT = 0x682532C3
    PLANT_ILLUMINATED = 0x426CF1E7
    PLANT_ILLUMINATED_STOP = 0x914B3AA2
    PLANT_RADIOACTIVE_STEAMER = 0xB02F895A
    PLANTCAT_ATTACK01 = 0x383D5896
    PLANTCAT_ATTACK02 = 0x383D5895
    PLANTCAT_ATTACK03 = 0x383D5894
    PLANTCAT_DEATH = 0x43C5BD2F
    PLANTCAT_DETBARK01 = 0x663EDCA9
    PLANTCAT_EAT_FR1 = 0xB52848FF
    PLANTCAT_EAT_FR160 = 0xDA4D5A71
    PLANTCAT_HAPPY01_FR1 = 0x188B5BAE
    PLANTCAT_HAPPY01_FR111 = 0xF7356EF0
    PLANTCAT_PAIN = 0x86694E27
    PLANTCAT_PERFORM02 = 0xC37D5314
    PLANTCAT_PERFORM03 = 0xC37D5315
    PLANTCAT_PERFORM04 = 0xC37D5312
    PLANTCAT_PERFORMATK = 0x1F12F18C
    PLANTCAT_POUNCE = 0x6E38D3C5
    PLANTCAT_ROAR = 0x6F09349F
    PLANTCAT_SAD01 = 0xE7CCA134
    PLANTCAT_SLEEPEND = 0x76AF1AEF
    PLANTCAT_SLEEPSTART = 0x91D5C44C
    PLAQUE_END = 0xA28CC67
    PLAQUE_LOOP = 0x841DC68A
    PLAQUE_START = 0x12497354
    PLAY_BASE_POWER_CONNECT = 0x12E999E4
    PLAY_MAP_CENTRECHORD_01_INDEX_01_MAP_CENTRECHORD_01 = 0xD6A75CD2
    PLAY_MAP_CENTRECHORD_02_INDEX_01_MAP_CENTRECHORD_02 = 0x124A4FFA
    PLAY_MAP_DRONENOISE_01_INDEX_01_MAP_SPACE_NOISE_DRONE = 0xF270DBF0
    PLAY_MAP_DRONENOISE_02_INDEX_01_MAP_SPACE_NOISE_DRONE_RR = 0x57C811D0
    PLAY_MAP_DRONETONE_01_INDEX_01_MUS_MAP1_DRONE_E = 0x2E489D33
    PLAY_MAP_PIANO_INDEX_01_MUS_MAP01_PIANO_01 = 0xB99E1F47
    PLAY_MAP_SINGLES_01_INDEX_01_MUS_MAP01_SINGLES1_04 = 0x614FBC55
    PLAY_MAP_SINGLES_02_INDEX_01_MUS_MAP01_SINGLES2_09 = 0x7F6217FC
    PLAY_MAP_ZONE01_INDEX_01_MAP_ZONE01 = 0x5908A1EE
    PLAY_MAP_ZONE02_INDEX_01_MAP_ZONE02 = 0x827E6B9A
    PLAY_MAP_ZONE02_SINGLES_INDEX_01_ZONE02_SINGLES02 = 0x7B91D5E9
    PLAY_PL_BASS_INDEX_01_MONOLITH_BOWEDBASSGTR_GMIN_6 = 0x67E0BFCD
    PLAY_PL_BASS_INDEX_07_MONOLITH_BOWEDBASSGTR_GMIN_1 = 0x7E462BF8
    PLAY_PL_BASS_INDEX_26_MELB_PLANETBASS_8 = 0x5659A098
    PLAY_PL_CELLO_INDEX_07_EOTWS_CELLO_1 = 0xC0A831E6
    PLAY_PL_DRONE_01_INDEX_01_EQUINOXSOFT_EMIN_2 = 0x400244DF
    PLAY_PL_DRONE_01_INDEX_03_SM_VOX_GRANULAR_DMIN_1 = 0xDE1DF727
    PLAY_PL_DRONE_01_INDEX_08_ASCENSION_SPACE_6 = 0x7BD641CF
    PLAY_PL_DRONE_01_INDEX_10_TETSUO_VOXTEXTURE_1 = 0xC156BA58
    PLAY_PL_DRONE_01_INDEX_13_BEYOND_PLANETDRONE_9 = 0x4FF2963A
    PLAY_PL_DRONE_01_INDEX_14_EOTWSALT_STRINGHOLD_7 = 0x69C8FFA1
    PLAY_PL_DRONE_01_INDEX_16_BOREALIS_GTRDELAY_AMIN_7 = 0x133D7B99
    PLAY_PL_DRONE_01_INDEX_18_NMS2017_MIDS_52 = 0x828A5D91
    PLAY_PL_DRONE_01_INDEX_20_TUNG_PLANET_TEXTURE_2 = 0xEC21FBBE
    PLAY_PL_DRONE_01_INDEX_21_OCT_TEXTURE_39 = 0xF466613E
    PLAY_PL_DRONE_01_INDEX_23_ECHO_PLANETLOWEND_15 = 0xC995CA0F
    PLAY_PL_DRONE_01_INDEX_24_DOMO_PLANETIRIS_2 = 0x5652655A
    PLAY_PL_DRONE_01_INDEX_25_SCRAPER_PLANETROOTS_6 = 0x6C589FF4
    PLAY_PL_DRONE_01_INDEX_27_OVERSEER_PLANETACOUSTICBED_5 = 0xDBCF152F
    PLAY_PL_DRONE_01_INDEX_28_SCRAPER_PLANETROOTS_11 = 0x9DE016C7
    PLAY_PL_DRONE_02_INDEX_01_TOMORROW_FM_1 = 0x57C9311D
    PLAY_PL_DRONE_02_INDEX_08_TOMORROW_FM_CHOPPED_1 = 0x1087A406
    PLAY_PL_DRONE_02_INDEX_14_EOTWSALT_STRINGLOOP_3 = 0xED13C371
    PLAY_PL_DRONE_02_INDEX_18_NMS2017_POLYHIGH_1 = 0x4753E199
    PLAY_PL_DRONE_02_INDEX_25_SCRAPER_PLANETWEIRDARP_1 = 0xC2C438B5
    PLAY_PL_DRONE_02_INDEX_28_SCRAPER_PLANETGTRTEXTURE_8 = 0xACFC51A7
    PLAY_PL_FX_01_INDEX_01_BOWEDCYMBAL_CLEAN_6 = 0x588F99C5
    PLAY_PL_FX_01_INDEX_03_SM_ATMOS_DMIN_4 = 0x4635AF44
    PLAY_PL_FX_01_INDEX_06_EV_PLANETNOISE_9 = 0x5C56712E
    PLAY_PL_FX_01_INDEX_14_EOTWSALT_CRACKLE_2 = 0x2519853
    PLAY_PL_FX_01_INDEX_15_HAUNTED_ARCTIC_EMIN_3 = 0x68DFC6E
    PLAY_PL_FX_01_INDEX_17_APORIA_PLANET_ROBOT_14 = 0xE0D1741E
    PLAY_PL_FX_01_INDEX_18_NMS2017_IMPACTS_3 = 0x9BF2BB69
    PLAY_PL_FX_01_INDEX_19_TUES_PLANETTREMOR_17 = 0x8D44671A
    PLAY_PL_FX_01_INDEX_25_DASKA_PLANETTHUD = 0xF8EB165F
    PLAY_PL_FX_01_INDEX_27_OVERSEER_PLANETTHUMPS_9 = 0x1311F2DC
    PLAY_PL_FX_02_INDEX_03_BOWEDCYMBAL_CHOPDISTORT_22 = 0x8F5FF60A
    PLAY_PL_FX_03_INDEX_03_SM_HHPATTER_6 = 0x2C589B01
    PLAY_PL_GUITAR_01_INDEX_01_MONOLITH_PLANET_GTRSOUNDSCAPE_5 = 0xCF8CADD5
    PLAY_PL_GUITAR_01_INDEX_02_ASIM_PLANET_PAULGTR_5 = 0x6FBE88C7
    PLAY_PL_GUITAR_01_INDEX_03_SM_PLANET_ATMOSGTR_DMIN_3 = 0x8732317B
    PLAY_PL_GUITAR_01_INDEX_04_BLUEPRINT_BOWEDGTR_EMIN_31 = 0x8831B83
    PLAY_PL_GUITAR_01_INDEX_06_EV_PLANETGTR_5 = 0xF7207851
    PLAY_PL_GUITAR_01_INDEX_12_ATWOOD_GTRVERB_7 = 0xADA95082
    PLAY_PL_GUITAR_01_INDEX_13_LULL_GTR_16 = 0xD0ACF4C1
    PLAY_PL_GUITAR_01_INDEX_15_HAUNTED_GTRSHARK_EMIN_4 = 0x4E2457C5
    PLAY_PL_GUITAR_01_INDEX_16_MONOALT_PLANETMALLETFX_6 = 0x255A1F5C
    PLAY_PL_GUITAR_01_INDEX_19_TUES_PLANETGTR_3 = 0x4D7ACD5F
    PLAY_PL_GUITAR_01_INDEX_22_VOSTOK_BOWEDGTR_1 = 0xE45DFE19
    PLAY_PL_GUITAR_01_INDEX_23_ECHO_PLANETGTRBED_9 = 0xBC265BCF
    PLAY_PL_GUITAR_01_INDEX_25_DASHKA_JOEGTR_5 = 0x9165FEF
    PLAY_PL_GUITAR_01_INDEX_26_MELB_PLANETGTR_3 = 0x7A3F4310
    PLAY_PL_GUITAR_02_INDEX_02_ASIM_PLANET_MALLETGTR_BMIN_4 = 0xA9F582C1
    PLAY_PL_GUITAR_02_INDEX_04_BLUEPRINT_GTRTEXTURE_EMIN_5 = 0xF7BDE53
    PLAY_PL_GUITAR_02_INDEX_22_VOSTOK_BOWEDGTRREV_18 = 0x49DDA12D
    PLAY_PL_GUITAR_03_INDEX_02_ASIM_PLANET_MALLETGTRTWO_BMIN_2 = 0x6C2FABF8
    PLAY_PL_GUITAR_04_INDEX_02_ASIM_PLANET_JOEGTRWASHSOFT_BMIN_4 = 0x6730E015
    PLAY_PL_GUITARDRONE_INDEX_01_DEPARTURE_GTR_EMIN_1 = 0xE4ED3E1B
    PLAY_PL_GUITARDRONE_INDEX_08_DEPARTURE_GTR_EMIN_1 = 0x823E3728
    PLAY_PL_GUITARFAST_INDEX_01_CELESTIAL_GTRLOOP_2 = 0x30097230
    PLAY_PL_GUITARFAST_INDEX_08_CELESTIAL_GTRLOOP_3 = 0x3D1FC51C
    PLAY_PL_HIGHCELLO_INDEX_09_RIPLEY_CELLOHIGHER_1 = 0x851502B6
    PLAY_PL_HIGHSYNTH_INDEX_08_CELESTIAL_HIGH_2 = 0xB4547CC4
    PLAY_PL_HIGHSYNTH_INDEX_19_TUES_PLANETHIGH_2 = 0xF7E7F471
    PLAY_PL_HIGHSYNTH_INDEX_20_TUNG_PLANET_PIANOHIGHINT_21 = 0xEA6A0F56
    PLAY_PL_HIGHSYNTH_INDEX_24_DOMO_PLANETHIGHINTEREST_2 = 0x11BE54A5
    PLAY_PL_HIGHSYNTH_INDEX_25_SCRAPER_PLANETGTRMELS_4 = 0x67648F5
    PLAY_PL_HIGHSYNTH_INDEX_27_OVERSEER_PLANETHIGHINTEREST_5 = 0xEF9D0195
    PLAY_PL_MELODY_HI_INDEX_01_MONLITH_PLANET_PIANOMELVERB_1 = 0xD3074360
    PLAY_PL_MELODY_HI_INDEX_02_ASIM_PLANETJUNO_BMIN_7 = 0xA6CE8694
    PLAY_PL_MELODY_HI_INDEX_03_SM_PIANOHIGH_DMIN_5 = 0xA92BA318
    PLAY_PL_MELODY_HI_INDEX_05_REDPARA_CELESTA_9 = 0x7EC0D2BC
    PLAY_PL_MELODY_HI_INDEX_06_EV_HIGHINTEREST_1 = 0x22EB2562
    PLAY_PL_MELODY_HI_INDEX_10_TETSUO_PLANETHI_1 = 0xB4503E43
    PLAY_PL_MELODY_HI_INDEX_11_AKIRA_PLANETPIANO_1 = 0xCDB93632
    PLAY_PL_MELODY_HI_INDEX_13_LULL_PIANO_8 = 0xF678F5FC
    PLAY_PL_MELODY_HI_INDEX_14_EOTWS_PIANOLOOP_4 = 0xBF265D1A
    PLAY_PL_MELODY_HI_INDEX_15_HAUNTED_SHARKUPCLOSE_EMIN_7 = 0xDAB6CF40
    PLAY_PL_MELODY_HI_INDEX_16_MONOALT_REVPIANO_11 = 0x7E23BA9F
    PLAY_PL_MELODY_HI_INDEX_18_NMS2017_MODMELS_2 = 0xD0BF75D2
    PLAY_PL_MELODY_HI_INDEX_21_OCT_HIGHMEL_11 = 0x7D9658D5
    PLAY_PL_MELODY_HI_INDEX_22_VOSTOK_PLANETHIGH_7 = 0xE059651B
    PLAY_PL_MELODY_HI_INDEX_25_DASKA_PLANETHIGHINTEREST_12 = 0xFC6719FE
    PLAY_PL_MELODY_HI_INDEX_27_OVERSEER_PLANETACOUSTIC_13 = 0x39F704ED
    PLAY_PL_MELODY_HI_INDEX_28_SCRAPER_PLANETGTRMELS_7 = 0x6123AC43
    PLAY_PL_MELODY_INDEX_25_DASHKA_PLANETLOOPS_6 = 0x9161064A
    PLAY_PL_MELODY_INDEX_28_SCRAPER_PLANETWEIRDARP_2 = 0x114B8E0E
    PLAY_PL_MUSICBOX_INDEX_01_MUSICBOXLONG_EMIN = 0x5CCD8909
    PLAY_PL_MUSICBOX_INDEX_08_MUSICBOXLONG_EMIN = 0x9F8539B4
    PLAY_PL_PIANO_INDEX_09_RIPLEY_PIANOHI_1 = 0x57B0FC0A
    PLAY_PL_PIANO_INDEX_11_AKIRA_PLANETPIANOREV_18 = 0xF72C407C
    PLAY_PL_PIANO_INDEX_12_ATWOOD_PIANO_5 = 0x6E236852
    PLAY_PL_PIANO_INDEX_17_APORIA_PLANETSINEKEYS_2 = 0x83E153A2
    PLAY_PL_PIANO_INDEX_20_TUNG_PLANET_PIANO_2 = 0x1E867B77
    PLAY_PL_PIANO_INDEX_22_VOSTOK_PLANETKEYS_19 = 0xF34CEC83
    PLAY_PL_PIANO_INDEX_23_ECHO_PIANOHIGH_2 = 0x280B0EAA
    PLAY_PL_PIANO_INDEX_24_DOMO_PLANETBURN_3 = 0xE874446A
    PLAY_PL_STRINGS_INDEX_09_RIPLEY_CELLO_1 = 0x61AF6512
    PLAY_PL_STRINGS_INDEX_17_APORIA_PLANETSOFTBED_2 = 0x975FE591
    PLAY_PL_SYNTH_INDEX_01_CELESTIAL_MOD_1 = 0xC1740844
    PLAY_PL_SYNTH_INDEX_05_REDPARA_SPACEFROST_AMIN_1 = 0x8B892521
    PLAY_PL_SYNTH_INDEX_08_CELESTIAL_MOD_8 = 0x70304420
    PLAY_PL_SYNTH_INDEX_13_BEYOND_SLOWSYNTH_6 = 0xB7D8EC9E
    PLAY_PL_SYNTH_INDEX_15_HAUNTED_DIGITALSHARK_EMIN_2 = 0x480E9420
    PLAY_PL_SYNTH_INDEX_17_APORIA_PLANETREAMPTEXTURE_22 = 0x85937240
    PLAY_PL_SYNTH_INDEX_21_OCT_SLOWMEL_25 = 0xB30EE13F
    PLAY_PL_SYNTH_INDEX_25_DASHKA_PLANETCOUNTER_314 = 0x5E16C9DD
    PLAY_PL_SYNTH_INDEX_26_MELB_PLANETBURNT_4 = 0x11362C7D
    PLAY_PL_VOCAL_INDEX_10_TETSUO_VOXSOFT_1 = 0x19D7608A
    PLAY_PL_VOX_INDEX_03_SM_VOX_DMIN_3 = 0xD6ACAB19
    PLAY_PL_VOX_INDEX_13_LULL_VOX_16 = 0x8B3A1916
    PLAY_SP_ARP_HI_INDEX_01_MONOLITH_SPACE_ARP_GMIN_11 = 0xC22E661B
    PLAY_SP_ARP_HI_INDEX_02_ASIMOVARP_A1 = 0xF21C52D1
    PLAY_SP_ARP_HI_INDEX_03_SUPERMOON_17 = 0x4EDC8A96
    PLAY_SP_ARP_HI_INDEX_04_BLUEPRINT_ARPEMIN_128BPM_3 = 0x3397A0BD
    PLAY_SP_ARP_HI_INDEX_05_REDPARA_SPACEARP_AMIN_7 = 0x73AC58C
    PLAY_SP_ARP_HI_INDEX_07_ARPEOTWS_A11 = 0x3D5692D2
    PLAY_SP_ARP_HI_INDEX_08_HUSK_7 = 0xA6145F83
    PLAY_SP_ARP_HI_INDEX_09_RIPLEY_12 = 0xAA2EFA26
    PLAY_SP_ARP_HI_INDEX_10_ARPTETSUO_B9 = 0x350D57DC
    PLAY_SP_ARP_HI_INDEX_12_ATWOOD_10 = 0xBF34FC67
    PLAY_SP_ARP_HI_INDEX_13_ARPBEYOND_A9 = 0x3F9FF61
    PLAY_SP_ARP_HI_INDEX_14_EOTWSALT_11 = 0x42BAC2B1
    PLAY_SP_ARP_HI_INDEX_15_MACREADY_4 = 0x165044CF
    PLAY_SP_ARP_HI_INDEX_16_MONOALT_7 = 0x228B67A7
    PLAY_SP_ARP_HI_INDEX_21_OCT_ARPS_10 = 0x13035ED0
    PLAY_SP_ARP_HI_INDEX_25_DASHKA_SPACEGTR_8 = 0x7ED77A28
    PLAY_SP_BASS_INDEX_01_SPARKGROWLER_EMIN_4 = 0xDF4601B1
    PLAY_SP_BASS_INDEX_02_SKANNERLOW_EMIN_4 = 0xD6FCD897
    PLAY_SP_BASS_INDEX_07_EOTWS_REAMP_1 = 0x67A6502B
    PLAY_SP_BASS_INDEX_09_RIPLEY_SPACEBASS_EMIN_1 = 0xCD3A288
    PLAY_SP_BASS_INDEX_17_APORIA_SPACEBASS_6 = 0xB4F25703
    PLAY_SP_BASS_INDEX_18_NMS2017_SPACEBASS_7 = 0x6A2EFC7F
    PLAY_SP_BASS_INDEX_20_TUNG_SPACEBASS2 = 0xEEDCEB62
    PLAY_SP_BASS_INDEX_25_DASHKA_SPACEBASS_3 = 0xD4FA04F5
    PLAY_SP_BASS_INDEX_26_MELB_SPACELOWS_5 = 0x6410B4E6
    PLAY_SP_BASS_INDEX_28_SCRAPER_SPACEROOTS_7 = 0xB966DBA0
    PLAY_SP_CHORDS_INDEX_03_SM_CLUSTERKEYS_DMIN_2 = 0x416181A
    PLAY_SP_CHORDS_INDEX_17_APORIA_SPACECHORDS_16 = 0x22601B2
    PLAY_SP_CHORDS_INDEX_18_NMS2017_SPACECHORDSYNTH_10 = 0xF4FCC08
    PLAY_SP_DRONE_01_INDEX_01_MONOLITH_WANTEDGTRDRONES_GMIN_3 = 0x60EAFF30
    PLAY_SP_DRONE_01_INDEX_02_ASIM_KORGSPACESYNTH_BMIN_9 = 0x37AD4C1C
    PLAY_SP_DRONE_01_INDEX_04_BLUEPRINT_MOPHODRONE_EMIN_4 = 0xE91F0CFF
    PLAY_SP_DRONE_01_INDEX_05_REDPARA_SPACEPULSE_AMIN_7 = 0xA5A09195
    PLAY_SP_DRONE_01_INDEX_06_EV_SPACEDRONEONE_ENEUTRAL_2 = 0xA8735D7
    PLAY_SP_DRONE_01_INDEX_12_ATWOOD_DRONESUB_1 = 0xDCAB9F9
    PLAY_SP_DRONE_01_INDEX_13_BEYOND_SPACEKORG_13 = 0x9C46D223
    PLAY_SP_DRONE_01_INDEX_16_MONOALT_SPACEDRONE_5 = 0xAAA6DF83
    PLAY_SP_DRONE_01_INDEX_20_TUNG_SPACEMODAL_14 = 0x1B3D3175
    PLAY_SP_DRONE_01_INDEX_22_VOSTOK_SPACETEXTURE_33 = 0xB4D09396
    PLAY_SP_DRONE_01_INDEX_24_DOMO_SPACEDRONE_15 = 0xB0ECE2C0
    PLAY_SP_DRONE_01_INDEX_25_DASHKA_SPACEAMBIENCE_7 = 0xC4CE4289
    PLAY_SP_DRONE_02_INDEX_06_EV_SPACEDRONETWO_ENEUTRAL_4 = 0x75705BDA
    PLAY_SP_DRONE_02_INDEX_22_VOSTOK_SPACEGRAIN_6 = 0x27F67AEF
    PLAY_SP_DRONE_03_INDEX_22_VOSTOK_LOW_2 = 0x11579679
    PLAY_SP_FX_01_INDEX_02_BOWEDCYMBAL_CLEAN_22 = 0xBCD640CD
    PLAY_SP_FX_01_INDEX_14_EOTWS2_SPACECHIME_1 = 0xF0244729
    PLAY_SP_FX_01_INDEX_22_VOSTOK_ECHO_6 = 0x2EDF484E
    PLAY_SP_FX_01_INDEX_28_SCRAPER_VERBAMBIENCE_7 = 0x6D70AB77
    PLAY_SP_GUITAR_INDEX_07_EOTWS_GTRCLEANNOTES_16 = 0xAAE231EC
    PLAY_SP_GUITAR_INDEX_09_RIPLEY_SPACEGTRHI_1 = 0xE8C36DF6
    PLAY_SP_GUITAR_INDEX_21_OCT_SPACEGTR_31 = 0x9DA8B57
    PLAY_SP_HARP_INDEX_01_ASCENSION_HARP_3 = 0xA45C3554
    PLAY_SP_HARP_INDEX_08_ASCENSION_HARP_4 = 0xF145DEC0
    PLAY_SP_LOWATMOS_INDEX_01_ASCENSION_LONGRISE_2 = 0xB66CB2AC
    PLAY_SP_LOWATMOS_INDEX_08_ASCENSION_LONGRISE_2 = 0x69291BF7
    PLAY_SP_MELODY_HI_INDEX_02_ASIM_SPACEDUDE_9 = 0x92E2D7C0
    PLAY_SP_MELODY_HI_INDEX_06_EV_SPACEPIANO_3_REV = 0xFCE3BF92
    PLAY_SP_MELODY_HI_INDEX_11_AKIRA_DULCECLUSTER_7 = 0x478AC911
    PLAY_SP_MELODY_HI_INDEX_12_ATWOOD_SPACEHIGHINTEREST_2 = 0xF7DCC916
    PLAY_SP_MELODY_HI_INDEX_13_BEYOND_HIGHMELODY_12 = 0xD9F7F0CD
    PLAY_SP_MELODY_HI_INDEX_16_MONOALT_VIOLIN_2 = 0x42820E95
    PLAY_SP_MELODY_HI_INDEX_19_TUES_SPACEHIGHONESHOTS_11 = 0x69573671
    PLAY_SP_MELODY_HI_INDEX_23_ECHO_SPACEHIGHINTERESTREV_1 = 0x8C39509
    PLAY_SP_MELODY_HI_INDEX_27_OVERSEER_SPACEHIGHINTEREST_10 = 0x9ADFD246
    PLAY_SP_MELODY_INDEX_01_ASCENSION_ELEKTRIK_EMIN_1 = 0x55ADB9E1
    PLAY_SP_MELODY_INDEX_03_SM_JUNOCHORDS_DMIN_18 = 0x2D887AF5
    PLAY_SP_MELODY_INDEX_04_BLUEPRINT_ORGANSCATTER_EMIN_10 = 0x2FC2C04A
    PLAY_SP_MELODY_INDEX_08_ASCENSION_ELEKTRIK_EMIN_1 = 0xC089EA38
    PLAY_SP_MELODY_INDEX_11_AKIRA_SPACEORGAN_15 = 0x956D3D20
    PLAY_SP_MELODY_INDEX_15_MAC_SPACEPADS_4 = 0x44EA076C
    PLAY_SP_MELODY_INDEX_19_TUES_MUSICBOX_12 = 0xDED04AC9
    PLAY_SP_MELODY_INDEX_23_ECHO_SPACETHUD_19 = 0xDA845B1A
    PLAY_SP_MELODY_INDEX_26_MELB_SPACEMELS_3 = 0xC71C04F9
    PLAY_SP_MISC_HI_INDEX_01_MONOLITH_MISC_GMIN_1 = 0x5D2FCB47
    PLAY_SP_MISC_HI_INDEX_20_TUNG_SPACEHIGHINTEREST_13 = 0x93AE2D3
    PLAY_SP_MISC_HI_INDEX_22_VOSTOK_SPACEHIGHINT_60 = 0x814B3BC2
    PLAY_SP_MISC_HI_INDEX_23_ECHO_WANTEDCELESTA_3 = 0xFF89DCAA
    PLAY_SP_MISC_HI_INDEX_24_DOMO_SPACEHIGHINTEREST_9 = 0x29AB4507
    PLAY_SP_SYNTH_INDEX_01_ASCENSION_SYNTHSTAB_6 = 0xE8943E79
    PLAY_SP_SYNTH_INDEX_08_ASCENSION_SYNTHSTAB_9 = 0xD6A9E64B
    PLAY_SP_SYNTH_INDEX_11_AKIRA_SPACESYNTH_9 = 0xD0A18574
    PLAY_SP_SYNTH_INDEX_13_BEYOND_SLOWSYNTH_6 = 0x1D942713
    PLAY_SP_SYNTH_INDEX_14_EOTWS2_SPACESTABS_5 = 0xA781CF68
    PLAY_SP_SYNTH_INDEX_19_TUES_JUNO_6 = 0xFA97E7FE
    PLAY_SP_SYNTH_INDEX_21_OCT_SPACEKEYS_14 = 0xFE626DB9
    PLAY_SP_SYNTH_INDEX_22_VOSTOK_ECHOREV_7 = 0xD4D22C6C
    PLAY_SP_SYNTH_INDEX_23_ECHO_SPACEPOLY_7 = 0xFAB5FB24
    PLAY_SP_SYNTH_INDEX_24_DOMO_SPACEARP_22 = 0xA28F7AB7
    PLAY_SP_SYNTH_INDEX_27_OVERSEER_SPACESYNTH_6 = 0x5B9A5C75
    PLAY_SP_SYNTHHIGH_INDEX_10_TETSUO_MOPHOHIGHINTEREST_1 = 0xADF95C78
    PLAY_SP_SYNTHHIGH_INDEX_13_BEYOND_HIGHMELODY_14 = 0xA8B7067F
    PLAY_SP_SYNTHHIGH_INDEX_17_APORIA_SPACE_HIGHINTEREST_3 = 0x39C50559
    PLAY_SP_SYNTHHIGH_INDEX_26_MELB_SPACEHIGHINTEREST6 = 0x9B772B4C
    PLAY_SP_SYNTHHIGH_INDEX_28_SCRAPER_SPACEARPS_5 = 0x725D9C8
    PLAY_SP_SYNTHINTERFERENCE_INDEX_10_TETSUO_SPACEHIGHINTEREST_1 = 0x70929769
    PLAY_SP_SYNTHPADS_INDEX_10_TETSUO_SPACEPADS_17 = 0x32F3C5E
    PLAY_SP_SYNTHPADS_INDEX_14_EOTWS2_SPACEPADS_3 = 0x64FBB0CF
    PLAY_SP_SYNTHPADS_INDEX_27_OVERSEER_SPACEDRIFTS_10 = 0x415027FE
    PLAY_VO_WARNINGDRONE_ACTIVATED = 0xB16E06F0
    PLAY_VO_WARNINGDRONE_COMBAT = 0xA7DEA5CF
    PLAY_VO_WARNINGDRONE_ENGAGED = 0xCCDF400E
    PLAY_VO_WARNINGSENTINELELITE = 0x302ED34F
    PLAY_VO_WARNINGSENTINELINCOMING = 0x57798EBA
    PLAY_VO_WARNINGWALKER = 0x7334AE90
    PLAY_WT_ARP_INDEX_05_REDPARA_SPACEARP_AMIN_3 = 0xE8ABFEA4
    PLAY_WT_ARP_INDEX_06_EV_WANTEDARPS_4 = 0x29011642
    PLAY_WT_ARP_INDEX_08_MONOLITH_SPACE_ARP_GMIN_4 = 0x79BDCBD2
    PLAY_WT_ARP_INDEX_17_APORIA_WANTEDARPS_1 = 0x816AC8F4
    PLAY_WT_ARP_INDEX_19_TUES_WANTEDARP_2 = 0x309679DF
    PLAY_WT_ARP_INDEX_23_ECHO_WANTEDCELESTA_3 = 0xDA34E957
    PLAY_WT_BASS_INDEX_02_SKANNERLOW_EMIN_1 = 0xCE67C6FA
    PLAY_WT_BASS_INDEX_03_SM_WANTED_BASSSEQ_118BPM_DMIN_2 = 0xF54EDD74
    PLAY_WT_BASS_INDEX_08_MONOLITH_WANTED_SYNTHLOW_1 = 0x16BE8EB1
    PLAY_WT_BASS_INDEX_20_TUNG_PLANET_PIANOLOWINT2 = 0xE893B9AA
    PLAY_WT_BASS_INDEX_22_VOSTOK_WANTEDSTABS_3 = 0x819C2011
    PLAY_WT_BASS_INDEX_25_DASHKA_WANTEDBASSSYNTH_5 = 0x52D2E4AE
    PLAY_WT_BASS_INDEX_26_MELB_PLANETBASS_2 = 0x3D53BDE3
    PLAY_WT_BASS_INDEX_27_OVERSEER_WANTEDBASS_2 = 0x1FEA96F4
    PLAY_WT_DRONE_02_INDEX_08_DEPARTURE_NOISE_EMIN_1 = 0x7D3F9967
    PLAY_WT_DRONE_02_INDEX_09_RIPLEY_GRAIN__1 = 0x2D7961A7
    PLAY_WT_DRONE_INDEX_03_DEPARTURE_GTR_EMIN_9 = 0x6D1E8BF2
    PLAY_WT_DRONE_INDEX_04_DEPARTURE_NOISE_EMIN_5 = 0xD33A4CFA
    PLAY_WT_DRONE_INDEX_07_EOTWS_GRAINSPACE_1 = 0xD8E07776
    PLAY_WT_DRONE_INDEX_08_BOREALIS_GTRFEEDBACK_AMIN_1 = 0x7D546579
    PLAY_WT_DRONE_INDEX_09_SM_ATMOS_DMIN_1 = 0xE9CDD90E
    PLAY_WT_DRONE_INDEX_10_TETSUO_GRAINSPACE_1 = 0xADA17A3A
    PLAY_WT_DRONE_INDEX_11_AKIRA_PLANETGRAIN_17 = 0x6AAB05BA
    PLAY_WT_DRONE_INDEX_12_ATWOOD_DRONEGTR_16 = 0x92198342
    PLAY_WT_DRONE_INDEX_14_DEPARTURE_GTR_EMIN_1 = 0xC2FC8B7E
    PLAY_WT_DRONE_INDEX_15_MAC_MAINPADSFULL_CSHARP_MIN_2 = 0xEC4E0A5
    PLAY_WT_DRONE_INDEX_16_MONOALT_GRAIN_10 = 0x37317CEA
    PLAY_WT_DRONE_INDEX_22_VOSTOK_ECHOREV_7 = 0x65358E7C
    PLAY_WT_DRONE_INDEX_24_DOMO_WANTEDBACKGROUND_2 = 0xEDA0C79F
    PLAY_WT_DRUMS_INDEX_01_MONOLITH_WANTED_DRUMLOOPS_20 = 0x976BCC42
    PLAY_WT_DRUMS_INDEX_02_ASIM_DRUMSDIRTY_128BPM_6 = 0xD1FD662A
    PLAY_WT_DRUMS_INDEX_03_SM_WANTED_DRUMLOOPS_15 = 0xA6B6A988
    PLAY_WT_DRUMS_INDEX_04_BLUEPRINT_DRMSGLITCHYBEATS_128BPM_5 = 0xD5CC957C
    PLAY_WT_DRUMS_INDEX_05_REDPARA_WANTEDDRUMLOOPS_1 = 0x88B928BF
    PLAY_WT_DRUMS_INDEX_06_EV_DRUMLOOPS_138BPM_9 = 0x105917
    PLAY_WT_DRUMS_INDEX_07_EOTWS_WANTEDBEATS_1 = 0xD4BB78E
    PLAY_WT_DRUMS_INDEX_08_HUSKWANTEDBEATS11 = 0xB5A776F9
    PLAY_WT_DRUMS_INDEX_09_RIPLEY_DRUMLOOPS_120BPM_1 = 0xFFA06FAD
    PLAY_WT_DRUMS_INDEX_10_TETSUO_DRUMLOOPS_1 = 0xC919BA1D
    PLAY_WT_DRUMS_INDEX_11_AKIRAWANTEDBEATS3 = 0xB31FEE49
    PLAY_WT_DRUMS_INDEX_12_ATWOOD_WANTEDARPBEATS_24 = 0xB4B96ABC
    PLAY_WT_DRUMS_INDEX_13_BEYONDTOMORROW1 = 0x5188A113
    PLAY_WT_DRUMS_INDEX_14_EOTWS_WANTEDDRUMS_2 = 0x9ACE2CC5
    PLAY_WT_DRUMS_INDEX_15_MAC_DRUMLOOP_5 = 0x63BD3B06
    PLAY_WT_DRUMS_INDEX_16_MONOALT_WANTEDLOOPS_8 = 0xC300036F
    PLAY_WT_DRUMS_INDEX_17_APORIA_WANTEDBEATS_2 = 0x1E5E0C9A
    PLAY_WT_DRUMS_INDEX_18_NMS2017_WANTEDSYNTHBEATS_1 = 0x99B4CD28
    PLAY_WT_DRUMS_INDEX_19_TUES_WANTEDBEATS4 = 0xAC12AE00
    PLAY_WT_DRUMS_INDEX_20_TUNG_WANTEDBEATS_3 = 0xED622083
    PLAY_WT_DRUMS_INDEX_21_OCT_WANTEDBEATS_1 = 0x738B234E
    PLAY_WT_DRUMS_INDEX_22_VOSTOK_WANTEDDRUMS_2 = 0x67E42272
    PLAY_WT_DRUMS_INDEX_23_ECHO_WANTEDLOOPS_2 = 0x6F73905E
    PLAY_WT_DRUMS_INDEX_24_DOMO_WANTEDDRUMS_3 = 0xC03ABC3C
    PLAY_WT_DRUMS_INDEX_25_DASHKA_WANTEDBEATS_3 = 0x310645C0
    PLAY_WT_DRUMS_INDEX_26_MELB_WANTEDBEATS_6 = 0x90D1B150
    PLAY_WT_DRUMS_INDEX_27_OVERSEER_WANTEDDRUMS_6 = 0x13D2BB3C
    PLAY_WT_DRUMS_INDEX_28_SCRAPER_WANTEDBEATS_8 = 0xF5818A
    PLAY_WT_FX_01_INDEX_03_SM_ATMOS_DMIN_5 = 0xB37E574E
    PLAY_WT_FX_01_INDEX_04_BLUEPRINT_MOPHOSTUTTER_EMIN_4 = 0x6B45AE08
    PLAY_WT_FX_01_INDEX_17_APORIA_SPACEBOWS_49 = 0x9461CB1B
    PLAY_WT_FX_01_INDEX_19_TUES_SONIC_2 = 0x958C95B8
    PLAY_WT_FX_01_INDEX_25_DASHKA_WANTEDNOISE_5 = 0x2A8CCF98
    PLAY_WT_GUITAR_INDEX_02_ASIM_JOEGTRLOUD_BMIN_18 = 0x315EC7A
    PLAY_WT_GUITAR_INDEX_04_BLUEPRINT_GTRBUILD_EMIN_9 = 0xFE2DAC64
    PLAY_WT_GUITAR_INDEX_05_REDPARA_GTRTREM_9 = 0xF30ED157
    PLAY_WT_GUITAR_INDEX_10_TETSUO_GTR1 = 0x3E3A0819
    PLAY_WT_GUITAR_INDEX_15_MAC_GTRMEL_2 = 0xBC898CEF
    PLAY_WT_GUITAR_INDEX_17_APORIA_WANTEDSTABS_1 = 0x2D251D20
    PLAY_WT_GUITAR_INDEX_18_NMS2017_EBOWGTR_5 = 0xFB8B7983
    PLAY_WT_GUITAR_INDEX_19_TUES_WANTEDGTR_3 = 0xB56B6CBD
    PLAY_WT_GUITAR_INDEX_20_TUNG_WANTEDGTRS_5 = 0xBA1CBEC9
    PLAY_WT_GUITAR_INDEX_21_OCT_WANTEDGTR_32 = 0x8421736D
    PLAY_WT_GUITAR_INDEX_23_ECHO_WANTEDGTRS_1 = 0x1BB1747F
    PLAY_WT_GUITAR_INDEX_26_MELB_PLANETGTR_2 = 0xAEFE5FBA
    PLAY_WT_GUITAR_INDEX_27_OVERSEER_WANTEDGTR_7 = 0x7730B6E
    PLAY_WT_GUITARS_02_INDEX_04_BLUEPRINT_GTREND_EMIN_6 = 0x387EC3EA
    PLAY_WT_GUITARS_02_INDEX_05_REDPARA_EBOWDRONE_5 = 0x25B9F145
    PLAY_WT_GUITARS_02_INDEX_17_APORIA_WANTEDGTRS_1 = 0xBD78E4D
    PLAY_WT_GUITARS_02_INDEX_20_TUNG_WANTEDBASS_3 = 0x7C61FF9A
    PLAY_WT_GUITARS_02_INDEX_26_MELB_DIST_2 = 0x9C2E6721
    PLAY_WT_MELODY_INDEX_03_SM_JOEGTRBURTS_DMIN_19 = 0x42473AD4
    PLAY_WT_MELODY_INDEX_04_KOAECAX_SLOWSYNTH_2 = 0x5B6A46
    PLAY_WT_MELODY_INDEX_06_EV_PIANOWANTED_AMIN_12 = 0x162A4ED3
    PLAY_WT_MELODY_INDEX_07_EOTWS_PLANETHIINTEREST_1 = 0x35FF80B0
    PLAY_WT_MELODY_INDEX_12_ATWOOD_CRACKLE_5 = 0xCD321398
    PLAY_WT_MELODY_INDEX_18_NMS2017_WANTEDLOOPS_3 = 0x16A15695
    PLAY_WT_MELODY_INDEX_21_OCT_WANTEDMELS_4 = 0xB93D3088
    PLAY_WT_MELODY_INDEX_23_ECHO_SPACEHIGHINTEREST_1 = 0x1C772C4
    PLAY_WT_MELODY_INDEX_24_DOMO_WANTEDMELS_1 = 0xF6EADAF3
    PLAY_WT_MELODY_INDEX_25_DASHKA_SPACEPIANO_6 = 0xB88F3749
    PLAY_WT_MELODY_INDEX_27_OVERSEER_WANTEDMELS_4 = 0x84FB5085
    PLAY_WT_MELODY_INDEX_28_SCRAPER_WANTEDMELS_10 = 0x41FA07E6
    PLAY_WT_NOISE_INDEX_01_MONOLITH_WANTED_NOISEONESHOTS_2 = 0x7EBF2A9
    PLAY_WT_ONESHOTS_INDEX_01_MONOLITH_WANTED_FASTONESHOTS_13 = 0x2634FD60
    PLAY_WT_ONESHOTS_INDEX_03_TOMORROW_FM_CHOPPED_5 = 0x76EACDAC
    PLAY_WT_ONESHOTS_INDEX_04_BLUEPRINT_JOESTUTTER_EMIN_11 = 0xB0C277CA
    PLAY_WT_ONESHOTS_INDEX_05_REDPARA_WANTEDSONGONESHOT_2 = 0x80B04A24
    PLAY_WT_ONESHOTS_INDEX_11_BLUEPRINT_GTREND_EMIN_5 = 0x70AADAA4
    PLAY_WT_ONESHOTS_INDEX_14_EOTWS_WANTEDBURN_4 = 0x733E0945
    PLAY_WT_ONESHOTS_INDEX_17_APORIA_PLANETSTABS_37 = 0x50D748A5
    PLAY_WT_ONESHOTS_INDEX_20_TUNG_SPACEHIGHINTEREST_16 = 0xF42D762D
    PLAY_WT_ORGAN_INDEX_06_EV_ORGANWANTED_AMIN_4 = 0xD8EA60FF
    PLAY_WT_PADS_INDEX_04_BLUEPRINT_INTROPADS_EMIN_48 = 0x9011770E
    PLAY_WT_PADS_INDEX_13_BEYOND_WANTEDPADS_6 = 0xC4907E3D
    PLAY_WT_SYNTH_INDEX_17_APORIA_SPACECHORDS_1 = 0x79F49AA7
    PLAY_WT_SYNTH_INDEX_20_TUNG_SPACEMODAL_2 = 0xF17FFB5A
    PLAY_WT_SYNTH_INDEX_26_MELB_WANTEDKEYS_5 = 0x85C4424B
    PLAYER_DIE = 0x5BEE16D1
    PLAYER_DIE_SURFACE = 0x3E80F715
    PLAYER_ORB = 0x44F92B10
    PLAYER_SHIP_TRANSITION = 0x4C30CFEB
    PLAYER_WATER_TRANSITION_INTO_ATMOS = 0xD2A5E6C2
    PLAYER_WATER_TRANSITION_INTO_WATER = 0x10DA6251
    PLOUGH = 0x73DFF4A4
    POD_BEAT = 0x5BD80B25
    POD_BURST = 0x9731DC65
    POD_SHAKE = 0xD1F704ED
    POI_ASTEROID_BEACON = 0x5E085E18
    POI_ATLAS_BEACON_01 = 0x20E5FCAC
    POI_ATLAS_BEACON_02 = 0x20E5FCAF
    POI_BONES = 0xD43CA593
    POI_CRYSTALS = 0x333E286B
    POI_CUBE_STATION = 0xC09FF838
    POI_DERELICT_01 = 0x25A14BD2
    POI_DERELICT_02 = 0x25A14BD1
    POI_DERELICT_03 = 0x25A14BD0
    POI_EYE = 0xC5038395
    POI_EYE_BEAM_END = 0x8593A2D7
    POI_EYE_BEAM_LP = 0x52AF1964
    POI_GAS_BRAIN = 0xA158AFF4
    POI_GEKHEAD = 0xBCAA303B
    POI_GYRO_BALL = 0x8FAB3C89
    POI_HORROR = 0xF3D9CFF2
    POI_JELLYFISH = 0x74BD0818
    POI_JELLYFISH_SPACE_SWIM = 0xABDB3F66
    POI_LINE_GEO = 0x1F696682
    POI_MEMORYLIFEBOAT_FLARE = 0x6C22D0CE
    POI_MEMORYLIFEBOAT_IDLE = 0x55D58134
    POI_NEURON = 0x3B4DCF27
    POI_RADIO_PILLAR = 0x64CC1342
    POI_RELAYBEACON = 0x1B7DE839
    POI_RELICGATE = 0x63E4FEA6
    POI_SPACE_EGG = 0x983E577A
    POI_SPACECLOCK = 0x38EF2B82
    POI_SPINNER = 0xF1CA2105
    POI_WEIRD_METAL = 0xFF2F4C51
    POLICE_CHATTER_START = 0x22042BF0
    POLICE_CHATTER_STOP = 0x86855F5C
    POLICE_INCOMING = 0xE2FDAA5A
    PORTAL_ACTIVATE_NORMAL = 0xC84F6011
    PORTAL_CAMERA_TOTERMINAL = 0x4CF219CD
    PORTAL_CORRUPTED_AMBIENT_LP = 0xCE45018E
    PORTAL_CORRUPTED_AWAKEN = 0xEB4E8710
    PORTAL_CORRUPTED_RUMBLE_BUILD = 0xB732E347
    PORTAL_CORRUPTED_RUMBLE_LP = 0xA30105C9
    PORTAL_CORRUPTED_STOP = 0x52B28E11
    PORTAL_DIAL_SPIN_START = 0x9AA1C4A6
    PORTAL_DIAL_SPIN_STOP = 0xF831E3E6
    PORTAL_EXPLOSION = 0xB8CAC8DB
    PORTAL_JUMP_NORMAL_END = 0x20AA1BB2
    PORTAL_JUMP_NORMAL_END_AMBIENCES = 0x6713C8E4
    PORTAL_JUMP_NORMAL_START = 0xE3B61E91
    PORTAL_JUMP_STORY_END = 0x1F67ACB6
    PORTAL_JUMP_STORY_START = 0xA0AB3F9D
    PORTAL_PILLARSATTACH = 0x77EE9DE6
    PORTAL_PILLARSDETACH = 0x2BF21928
    PORTAL_PILLARSLOCK = 0x4B8CCC60
    PORTAL_PILLARSUNLOCK = 0x8060BB55
    PORTAL_RUNE_SELECT = 0x42F26699
    PORTAL_RUNE_UNAVAILABLE = 0x3E81D195
    PORTAL_RUNES_APPEAR = 0x2926B953
    PORTAL_STOP_ALL = 0x4CAFE42A
    PORTAL_TERMINAL_CLOSE = 0xACE8E6E3
    PORTAL_TERMINAL_OPEN = 0x7606BD5
    PORTAL_WEIRD_BUILDUP = 0xD11EC5BF
    POWER_SWITCH_AUTOSWITCH_OFF = 0x31E73B95
    POWER_SWITCH_AUTOSWITCH_ON = 0x7A01D829
    POWER_SWITCH_BUTTON_OFF = 0xE959674
    POWER_SWITCH_BUTTON_ON = 0xBD66A4EE
    POWER_SWITCH_FLOOR_OFF = 0x882DA65A
    POWER_SWITCH_FLOOR_ON = 0x4C5B965C
    POWER_SWITCH_PROXIMITY_OFF = 0xA51D0817
    POWER_SWITCH_PROXIMITY_ON = 0x38AE2063
    POWERMODULE_NOTE_A = 0x662C5967
    POWERMODULE_NOTE_A_STOP = 0x664B9122
    POWERMODULE_NOTE_B = 0x662C5964
    POWERMODULE_NOTE_B_STOP = 0x1A3E6F83
    POWERMODULE_NOTE_C = 0x662C5965
    POWERMODULE_NOTE_C_STOP = 0x3BEAA2A8
    POWERMODULE_NOTE_D = 0x662C5962
    POWERMODULE_NOTE_D_STOP = 0x39B74521
    POWERMODULE_NOTE_E = 0x662C5963
    POWERMODULE_NOTE_E_STOP = 0x5DCA590E
    POWERMODULE_NOTE_F = 0x662C5960
    POWERMODULE_NOTE_F_STOP = 0xD89D1D4F
    POWERMODULE_NOTE_G = 0x662C5961
    POWERMODULE_NOTE_G_STOP = 0xD42B64
    PROTOROLLER = 0x98F8B9B1
    PROTOROLLER_STOP = 0xC4BC74D4
    PS5_VIBRATION_TONE = 0xCF5E1783
    PS5_VIBRATION_TONE_STOP = 0x93D00DEE
    PULSE_EMPHASISER = 0x22CEF034
    QUAD_ATTACK = 0x8DCE66F7
    QUAD_CROUCHTOSTAND = 0x9F9B4E96
    QUAD_DIE = 0x9DA4A083
    QUAD_EMOTE_LP = 0x62200770
    QUAD_EMOTE_LP_STOP = 0xF9C8B07F
    QUAD_EVADE = 0xF7EBDFCA
    QUAD_GUN = 0xB9A70BFF
    QUAD_HOP = 0xBF9A4960
    QUAD_IDLE = 0xAF14F599
    QUAD_LASER = 0xC667CC3C
    QUAD_LASER_STOP = 0x48BCC9CB
    QUAD_POUNCE = 0x4D21BF6D
    QUAD_POUNCE_BACK = 0xCB08B251
    QUAD_POUNCE_FORWARD = 0x75A11A07
    QUAD_SCAN = 0xC82A6860
    QUAD_SCAN_STOP = 0xBC4B8A4F
    QUAD_STEP = 0xAC0E650D
    QUAD_TONE = 0x9FFA9753
    RACING_DOME_NOTIFIER = 0x72791D60
    RADIO_CHATTER = 0x7E66279C
    RADIO_CHATTER_STOP = 0x66DF5E6B
    RECIPE_RECEIVE = 0xDBD7DDFD
    RESOURCE_GATHER = 0x86333C19
    RIVER = 0xD6EBF401
    ROBOT_GUNMELEE_IMPACTS = 0x4436A6B4
    ROBOT_LASER_IMPACTS = 0x49D29DA7
    ROBOT_METAL_IMPACTS = 0xD7582BF
    ROBOT_NARRATION_SINGALONG = 0x8BBB94A9
    ROBOT_NARRATION_SINGALONG_STOP = 0xCE99149C
    ROBOT_SHIP_TALK = 0x8B4C5A89
    ROBOT_SHIP_TALK_STOP = 0x702B2D3C
    ROCKCREATURE_TRANSFORM = 0x4E24239C
    RODENTATTACK1 = 0xD181620
    RODENTATTACK2 = 0xD181623
    RODENTATTACK3 = 0xD181622
    RODENTPOUNCE = 0xED010011
    RODENTPOUNCE2 = 0x29931AF1
    RODENTROAR = 0xFDD30E03
    ROLLER = 0xF1A7A7AD
    ROUNDTABLE_CLOSE = 0xB601B704
    ROUNDTABLE_OPEN = 0xD3D76000
    ROVER_BOOST_START = 0xD22AAF8A
    ROVER_BOOST_STOP = 0x696003E2
    ROVER_HORN_START = 0x4D72C430
    ROVER_HORN_STOP = 0x80EDB9C
    ROVER_IDLE_EXTERIOR = 0xCD1A7599
    ROVER_IMPACTS = 0xFA34F30F
    ROVER_JUMP = 0x892690CA
    ROVER_START = 0xEC117B92
    ROVER_STOP = 0xBFA7324A
    ROVER_SUSPENSION = 0x73640735
    RUININTERACTION_ACTIVE = 0x8A6EEEE6
    RUININTERACTION_END = 0x629E486F
    RUININTERACTION_IDLE = 0x86C1F9AE
    SANDWORM_INTOGROUND = 0x86327B5A
    SANDWORM_LP = 0x6E353C11
    SANDWORM_LP_STOP = 0xAAC8AD74
    SANDWORM_OUTOFGROUND = 0xE4FE7575
    SANDWORM_UNDERGROUND_WAIL_LP = 0xB2928D5F
    SC_TR_HARV = 0x3234D002
    SCAN_OFF = 0x70FDCEA8
    SCAN_ON = 0x8022EEB2
    SCRAP_DESTROY = 0x8ED2EF33
    SEAHORSE_SWIM = 0x22E468
    SEAURCHINCLOSE = 0x39AEF411
    SEAURCHINEXTEND = 0x7A044893
    SENTINEL_CRYSTAL = 0xD277358A
    SENTINEL_CRYSTAL_SMALL = 0xEF1AD0C6
    SENTINEL_HIVE_LP = 0xAA570111
    SENTINEL_HIVE_NODE = 0x118A84ED
    SENTINEL_HIVE_TERMINAL = 0x1352B0A9
    SENTINEL_MECH_JUMP = 0xD469C69E
    SENTINEL_MECH_LAND = 0x60F02DC9
    SENTINEL_MECH_WPN_FIRE = 0x2345B1E2
    SENTINEL_MECH_WPN_FIRE_STOP = 0x7112EA1
    SENTINEL_MECH_WPN_GRENADE = 0xECF59048
    SENTINEL_MECH_WPN_GUN = 0xF7A08AA0
    SENTINELS_INCOMING1 = 0x5862BAD0
    SENTINELS_INCOMING2 = 0x5862BAD3
    SENTINELS_INCOMING3 = 0x5862BAD2
    SENTINELS_INCOMING4 = 0x5862BAD5
    SENTINELS_INCOMING5 = 0x5862BAD4
    SENTINENCEECHO_REVEAL = 0xAC879F8
    SETTLEMENT_ALARM = 0x39A0EC12
    SETTLEMENT_ALARM_SHIP = 0x9DE3B01B
    SETTLEMENT_ANTENNA = 0x74E20ADC
    SETTLEMENT_ANTENNA0 = 0xDBD71864
    SETTLEMENT_ANTENNA1 = 0xDBD71865
    SETTLEMENT_ANTENNA2 = 0xDBD71866
    SETTLEMENT_ANTENNA3_LOOP = 0x7EE99A9C
    SETTLEMENT_ANTENNA3_SPIN = 0x1D5ED15A
    SETTLEMENT_CONSTRUCTION_TERMINAL = 0x48A1CD9B
    SETTLEMENT_FURNACE = 0x22B71075
    SETTLEMENT_GENERATOR = 0x7D11D44A
    SETTLEMENT_GLOWGLOBE = 0xF2985AF
    SETTLEMENT_LIGHTOUTDOOR = 0x8C6C2D83
    SETTLEMENT_MEDIBAY_LP = 0xEFC5D07B
    SETTLEMENT_PUMP = 0xC2F73565
    SETTLEMENT_ROBOTARM = 0xC5CE471
    SETTLEMENT_TERMINAL = 0xBD68511F
    SETTLEMENT_WATERTOWER = 0x13117793
    SFX_FADEDOWN = 0xED6AB3EB
    SFX_FADEUP = 0x71E96FAC
    SHARK_LP = 0x28B07C37
    SHIP_ALIEN_LANDING = 0x4EF74A6B
    SHIP_ALIEN_NOSTRILFLARE = 0x6300644D
    SHIP_ALIEN_TAKEOFF = 0xD387BE6
    SHIP_NORMANDY_ENGINES = 0x627E5670
    SHIP_NORMANDY_REVEAL = 0x83EEF348
    SHIP_PIRATE_LANDING_WINGS = 0x4DE7AD60
    SHIP_PIRATE_SAILS_ROUNDSAILS_FOLD = 0xBC9C3093
    SHIP_PIRATE_SAILS_ROUNDSAILS_UNFOLD = 0x2F203F2A
    SHIP_PIRATE_SAILS_SQUARE_FOLD = 0x8ADE0CE2
    SHIP_PIRATE_SAILS_SQUARE_UNFOLD = 0x8EF70A7
    SHIP_PIRATE_SAILS_TRIANGLE_FOLD = 0x96B28FFD
    SHIP_PIRATE_SAILS_TRIANGLE_UNFOLD = 0x1A6698D8
    SHIP_PIRATE_TAKEOFF_WINGS = 0x82FAE5D5
    SHIP_ROYAL_ENGINEC_LANDING = 0xA3AC816B
    SHIP_ROYAL_ENGINEC_TAKEOFF = 0x61EDB2E6
    SHIP_ROYAL_LANDINGGEAR_LANDING = 0x5E8606D2
    SHIP_ROYAL_LANDINGGEAR_TAKEOFF = 0x41A85C03
    SHIP_ROYAL_WINGSA_LANDING = 0x50E01CA7
    SHIP_ROYAL_WINGSA_TAKEOFF = 0xBC7EFDA2
    SHIP_ROYAL_WINGSB_LANDING = 0x4FF8C854
    SHIP_ROYAL_WINGSB_TAKEOFF = 0xC9965D21
    SHIP_ROYAL_WINGSC_LANDING = 0x9ACB3D2D
    SHIP_ROYAL_WINGSC_TAKEOFF = 0xBC3F8694
    SHIP_SQUID_LANDINGGEAR_LANDING = 0xA7B106E1
    SHIP_SQUID_LANDINGGEAR_TAKEOFF = 0xE4DA94B8
    SHIP_SQUID_NOSE_LANDING = 0xCC0E542
    SHIP_SQUID_NOSE_TAKEOFF = 0xE2EA8853
    SHIP_TOUCHDOWN_IMPACT = 0xF0555EF0
    SHIPREPAIR_IDLE = 0x2CD1DD7D
    SHORELINE = 0x1A1A962
    SHUTTLE_CLOSE = 0xA8262171
    SHUTTLE_MAINTHRUSTER = 0x8BB99737
    SHUTTLE_OPEN = 0xD82737F3
    SHUTTLE_THRUSTERS_STOP = 0x6211B2EE
    SHUTTLE_TOPTHRUSTER = 0x5FE94583
    SIGNALSCANNER = 0x300E2B2D
    SILO_LOOSECLOTH = 0x47EB586F
    SIXLEGCATPERFORM01 = 0xD1CA7463
    SIXLEGGEDCOWPERFORM01 = 0xFA1323E2
    SLIMEDOOR_BREAKA = 0x2AE26AA0
    SLIMEDOOR_BREAKB = 0x2AE26AA3
    SLIMEDOOR_BREAKC = 0x2AE26AA2
    SLIMEDOOR_BREAKD = 0x2AE26AA5
    SMALLPROPC = 0x90279B9C
    SPACE_STATION_EXTERIOR = 0x11D75F19
    SPACE_STATION_INTERIOR_01 = 0xD20E04AB
    SPACE_STATION_INTERIOR_01_STOP = 0xE63C38E6
    SPACESTATION_ATLAS_DOOR_CLOSE = 0xF3BCBD6B
    SPACESTATION_ATLAS_DOOR_OPEN = 0x115E98AD
    SPACESTATION_ENGINES_INTERIOR = 0x7039CB96
    SPACESTATION_PLANET_HOLOGRAM = 0x68D3A8E6
    SPARKS = 0x9160603F
    SPGEK_CHATTER = 0xA9537B9
    SPGEK_CHATTER_STOP = 0x6E4D844C
    SPIDERATTACK = 0x4090D662
    SPIDERATTACK2 = 0x6017C74
    SPIDERATTACK3 = 0x6017C75
    SPIDERFLOATSAD = 0xF0824E34
    SPIDERPERFORM01 = 0xB731D638
    SPIDERPOUNCE = 0x5D37D550
    SPIDERROAR = 0x711887FE
    SPKORVAX_CHATTER = 0x27F01D43
    SPKORVAX_CHATTER_STOP = 0xC02D15AE
    SPOOKHEATER_IDLE = 0xB909848F
    SPOOKHEATER_LP = 0x2EE47329
    SPOOKHEATER_START = 0x64601067
    SPOOKYTENTACLES = 0x6B387ED7
    SPOOKYTENTACLES_STOP = 0xF16E3972
    SPORE = 0x11268644
    SPOREBAG_IDLE = 0xF7CA9B97
    SPOREBAG_WOBBLE = 0x5AA09996
    SPOREBAGEXPLODE = 0x631A514D
    SPOREVENT_IDLE = 0x598D4C12
    SPOREVENT_INFLATE = 0x92414141
    SPVYKEEN_CHATTER = 0x1B77C414
    SPVYKEEN_CHATTER_STOP = 0x26C45A13
    STARSHIP_OUTFITTING_LP = 0xF353E7CE
    STARSHIP_VIEW_SWITCH_EXTERIOR = 0xF31B791
    STARSHIP_VIEW_SWITCH_INTERIOR = 0x52B4A22F
    STATION_CONSOLE_SWITCH = 0x9CD9E964
    STATIONB_CRANELOADCARGO_FR1 = 0xF54FF1EB
    STATIONB_CRANELOADCARGO_FR446 = 0xE2F1938C
    STATIONB_ORB_IDLE = 0x1E239542
    STATIONB_ORB_LOOM = 0xDE339A2B
    STATIONB_ORB_RETRACT = 0xA1A8F223
    STATIONB_ORB_ZOOM = 0x9BE92935
    STING_LOGO = 0xEE2BDB9E
    STONE_DOOR1_SETTLEMENT_CLOSE = 0xBA754903
    STONE_DOOR1_SETTLEMENT_OPEN = 0x2623C975
    STONEFLOATER_CORE_EXPLODE = 0x61572F39
    STONEFLOATER_LEFT_RIGHT_THROW = 0x5962235B
    STONEFLOATER_MELEE = 0x851C0C16
    STONEFLOATER_SPAWN = 0x8CD5AACB
    STONEFLOATER_SPIN = 0x343E3246
    STONEFLOATER_THROW = 0xC909CC2E
    STOP_MAP_CENTRECHORD_01_INDEX_01_MAP_CENTRECHORD_01 = 0x244CA730
    STOP_MAP_CENTRECHORD_02_INDEX_01_MAP_CENTRECHORD_02 = 0xA78A1418
    STOP_MAP_DRONENOISE_01_INDEX_01_MAP_SPACE_NOISE_DRONE = 0x542550E2
    STOP_MAP_DRONENOISE_02_INDEX_01_MAP_SPACE_NOISE_DRONE_RR = 0x983118E
    STOP_MAP_DRONETONE_01_INDEX_01_MUS_MAP1_DRONE_E = 0x38932291
    STOP_MAP_PIANO_INDEX_01_MUS_MAP01_PIANO_01 = 0x6EC06ADD
    STOP_MAP_SINGLES_01_INDEX_01_MUS_MAP01_SINGLES1_04 = 0xD6E366A7
    STOP_MAP_SINGLES_02_INDEX_01_MUS_MAP01_SINGLES2_09 = 0xD92015F6
    STOP_MAP_ZONE01_INDEX_01_MAP_ZONE01 = 0x18F8DB64
    STOP_MAP_ZONE02_INDEX_01_MAP_ZONE02 = 0x54A95BC0
    STOP_SP_ARP_HI_INDEX_02_ASIMOVARP_A1 = 0x657B7953
    STOP_SP_ARP_HI_INDEX_03_SUPERMOON_17 = 0xC0DE7CE0
    STOP_SP_ARP_HI_INDEX_04_BLUEPRINT_ARPEMIN_128BPM_3 = 0xAE4D8FAB
    STOP_SP_ARP_HI_INDEX_05_REDPARA_SPACEARP_AMIN_7 = 0x5F7A92B2
    STOP_SP_ARP_HI_INDEX_07_ARPEOTWS_A11 = 0x37B14CD4
    STOP_SP_ARP_HI_INDEX_08_HUSK_7 = 0x4545DC2D
    STOP_SP_ARP_HI_INDEX_09_RIPLEY_12 = 0xCCAC66C8
    STOP_SP_ARP_HI_INDEX_10_ARPTETSUO_B9 = 0x3B73F3F2
    STOP_SP_ARP_HI_INDEX_12_ATWOOD_10 = 0xC93C9B99
    STOP_SP_ARP_HI_INDEX_13_ARPBEYOND_A9 = 0xD3038103
    STOP_SP_ARP_HI_INDEX_14_EOTWSALT_11 = 0x6B902D07
    STOP_SP_ARP_HI_INDEX_15_MACREADY_4 = 0xA55C6A95
    STOP_SP_ARP_HI_INDEX_16_MONOALT_7 = 0x4892E98D
    STOP_WT_DRUMS_INDEX_01_MONOLITH_WANTED_DRUMLOOPS_20 = 0x9DAB5CC
    STOP_WT_DRUMS_INDEX_02_ASIM_DRUMSDIRTY_128BPM_6 = 0x8DEF0354
    STOP_WT_DRUMS_INDEX_03_SM_WANTED_DRUMLOOPS_15 = 0xBD85203A
    STOP_WT_DRUMS_INDEX_04_BLUEPRINT_DRMSGLITCHYBEATS_128BPM_5 = 0xD5DE6FAE
    STOP_WT_DRUMS_INDEX_05_REDPARA_WANTEDDRUMLOOPS_1 = 0xC295CDD1
    STOP_WT_DRUMS_INDEX_06_EV_DRUMLOOPS_138BPM_9 = 0xB42E15D
    STOP_WT_DRUMS_INDEX_07_EOTWS_WANTEDBEATS_1 = 0x19E54EC8
    STOP_WT_DRUMS_INDEX_08_HUSKWANTEDBEATS11 = 0xEA903FC3
    STOP_WT_DRUMS_INDEX_09_RIPLEY_DRUMLOOPS_120BPM_1 = 0x10F5BF
    STOP_WT_DRUMS_INDEX_10_TETSUO_DRUMLOOPS_1 = 0x28264EB3
    STOP_WT_DRUMS_INDEX_11_AKIRAWANTEDBEATS3 = 0x34EAABBF
    STOP_WT_DRUMS_INDEX_12_ATWOOD_WANTEDARPBEATS_24 = 0xCA2352DA
    STOP_WT_DRUMS_INDEX_13_BEYONDTOMORROW1 = 0x89E4122D
    STOP_WT_DRUMS_INDEX_14_EOTWS_WANTEDDRUMS_2 = 0x2F23E907
    STOP_WT_DRUMS_INDEX_15_MAC_DRUMLOOP_5 = 0xAD5677B4
    STOP_WT_DRUMS_INDEX_16_MONOALT_WANTEDLOOPS_8 = 0x86A0D375
    STOP_WT_DRUMS_INDEX_17_APORIA_WANTEDBEATS_2 = 0xDC40C4C8
    STOP_WT_DRUMS_INDEX_18_NMS2017_WANTEDSYNTHBEATS_1 = 0xC65EED56
    STOP_WT_DRUMS_INDEX_19_TUES_WANTEDBEATS4 = 0x650EEF52
    STOP_WT_DRUMS_INDEX_20_TUNG_WANTEDBEATS_3 = 0xB1534DD1
    STOP_WT_DRUMS_INDEX_21_OCT_WANTEDBEATS_1 = 0x772C6BC
    STOP_WT_DRUMS_INDEX_22_VOSTOK_WANTEDDRUMS_2 = 0xD1F2B5C0
    STOP_WT_DRUMS_INDEX_23_ECHO_WANTEDLOOPS_2 = 0xFD2B3514
    STOP_WT_DRUMS_INDEX_24_DOMO_WANTEDDRUMS_3 = 0xC9F1D682
    STOP_WT_DRUMS_INDEX_25_DASHKA_WANTEDBEATS_3 = 0x2090B95E
    STOP_WT_DRUMS_INDEX_26_MELB_WANTEDBEATS_6 = 0xFA930376
    STOP_WT_DRUMS_INDEX_27_OVERSEER_WANTEDDRUMS_6 = 0xD262EB32
    STOP_WT_DRUMS_INDEX_28_SCRAPER_WANTEDBEATS_8 = 0xBB18CA00
    STORMCRYSTAL = 0xB8B92596
    STRIDERATTACK = 0x70596ECC
    STRIDERATTACK2 = 0xA8C96B16
    STRIDERATTACK3 = 0xA8C96B17
    STRIDERROAR = 0x6C9FC7B4
    SUBMARINE_BOOST_START = 0x3227AA1A
    SUBMARINE_BOOST_STOP = 0x865165B2
    SUBMARINE_HORN_START = 0x35490700
    SUBMARINE_HORN_STOP = 0x31E249AC
    SUBMARINE_IDLE_EXTERIOR = 0x68EC56E9
    SUBMARINE_IMPACTS = 0x83505C1F
    SUBMARINE_JUMP = 0x2ACCB55A
    SUBMARINE_START = 0x8B430A02
    SUBMARINE_STOP = 0xFC46C37A
    SUBMARINE_SUBMERGE = 0x74187E58
    SUBMARINE_SURFACE = 0xD10F00A7
    SUBMARINE_SUSPENSION = 0xC8164665
    SUIT_INIT_END = 0x9A042E1
    SUIT_INIT_JETPACK = 0xC3E71CD0
    SUIT_INIT_LIFESUPPORT = 0x307E8019
    SUIT_INIT_SCANNER = 0xE637BC54
    SUIT_INIT_STARTUP = 0x7BE29729
    SUIT_UPGRADE_TERMINAL_INTERACT = 0xF69FA17
    SUIT_UPGRADE_TERMINAL_LP = 0xE5E4EDD9
    SUITBOOT_FINISHED = 0x2FA0AF23
    SUITBOOT_FREIGHTERINTRO_01 = 0x7F32ABF3
    SUITBOOT_FREIGHTERINTRO_02 = 0x7F32ABF0
    SUITBOOT_FREIGHTERINTRO_03 = 0x7F32ABF1
    SUITBOOT_FREIGHTERINTRO_04 = 0x7F32ABF6
    SUITBOOT_FREIGHTERINTRO_05 = 0x7F32ABF7
    SUITBOOT_FREIGHTERINTRO_06 = 0x7F32ABF4
    SUITBOOT_FREIGHTERINTRO_07 = 0x7F32ABF5
    SUITBOOT_INIT = 0x53D1EA23
    SUITBOOT_JETPACK = 0xD03EEDFD
    SUITBOOT_LIFESUPPORT = 0x871648A8
    SUITBOOT_SCANNER = 0xB6C45955
    SUITBOOT_SHIELD = 0x76ED680A
    SUITBOOT_WEAPON = 0x19BC0505
    SUMMONSHIPBEACON_CLOSE = 0x8A5AA3F3
    SUMMONSHIPBEACON_OPEN = 0x96E60D05
    TELEPORT = 0x1F992208
    TELEPORT_ACTIVATED_LOOP = 0xB794E78D
    TELEPORT_END = 0xDDE9F36E
    TELEPORT_LOOP_STOP = 0xDCD2E4FC
    TELEPORT_START = 0x26CB3885
    TENTACLE_IN = 0xD373FFC3
    TENTACLE_LP = 0xCE73F7BE
    TENTACLE_OUT = 0xBB8CBCBE
    TENTPLANT_CLOSE = 0x4248A730
    TENTPLANT_OPEN = 0xEDC2EF44
    TERMINAL_ABANDONED_GROWTH = 0xF753A4AA
    TERMINAL_ABANDONED_GROWTH_CLOSE = 0x403391D3
    TERMINAL_ABANDONED_GROWTH_OPEN = 0x9845265
    TERMINAL_ABANDONED_OPEN = 0x294C2E5B
    TERMINAL_BOOTUP = 0x183AB7F3
    TERMINAL_INDOORS = 0x6138EE88
    TERMINAL_INTERACT = 0x4387FCEE
    TERMINAL_OUTDOORS = 0xC48D4C4B
    TERRAIN_CREATE = 0xA095FDCF
    TERRAIN_DESTROY = 0xD6350E47
    TERRAIN_UNDO = 0x1EEA9A75
    TIMBER_DOOR1_SETTLEMENT_CLOSE = 0x43A6512B
    TIMBER_DOOR1_SETTLEMENT_OPEN = 0x18A8586D
    TIMBER_DOOR2_SETTLEMENT_CLOSE = 0xCD38E81A
    TIMBER_DOOR2_SETTLEMENT_OPEN = 0x66990C1E
    TORCH_OFF = 0x74CB5DB
    TORCH_ON = 0xABE43D67
    TORNADO = 0x9A2BAEE8
    TORNADO_STOP = 0xBAAC64C7
    TREXATTACK = 0x4BDEEBF0
    TREXATTACK2 = 0x5FED6AE2
    TREXATTACK3 = 0x5FED6AE3
    TREXHAPPY = 0x88CF37AE
    TREXPERFORM03 = 0xC8FBA2B8
    TREXROAR = 0xABA96530
    TRIATTACK = 0x5C7D1FC4
    TRIATTACK2 = 0x5CF901BE
    TRIATTACK3 = 0x5CF901BF
    TRIPERFORM01 = 0xF294FEC6
    TRIROAR = 0xD1FE084C
    TURRET_DEPLOY = 0x4DD50ACB
    TURRET_INACTIVE_IDLE = 0x19F5429E
    TURRET_LASER = 0xD1A672EB
    TURRET_LASER_STOP = 0x3EF4C726
    TURRET_RETRACT = 0x823861B5
    TURRET_SHOOT = 0xAC2966DB
    TUT_ELEMENT_TRANSFER_SUCCESS = 0xEEF3B67D
    TXT_RADIONOISE = 0x911C13D3
    TXT_SPECIAL_CHIME = 0x6A37C076
    TXT_STATICNOISE_END = 0xC44B58B8
    TXT_STATICNOISE_START = 0x55C1C063
    UI_ACTION_CONFIRMED = 0x18AECCF6
    UI_ALERT_DAMAGE_WARNING_CRITICAL_LP = 0x9BC95F06
    UI_ALERT_DAMAGE_WARNING_CRITICAL_LP_STOP = 0xE832F3D5
    UI_ALERT_POLICE = 0x8A53362D
    UI_ALIEN_RESPONSE = 0x938DD3E3
    UI_BADGE = 0xD22C90A7
    UI_BARTER_SUCCESS = 0xC3A759FE
    UI_BASEBUILD_CALLFREIGHTER = 0x7E2FF586
    UI_BASEBUILD_CHANGECATEGORY = 0x7F2F183A
    UI_BASEBUILD_CHANGESELECTION = 0xC950BE50
    UI_BASEBUILD_DELETE = 0xB00017EF
    UI_BASEBUILD_INVALIDPOSITION = 0xF1FDD4EA
    UI_BASEBUILD_MENU_CLOSE = 0x7C7C81DE
    UI_BASEBUILD_MENU_OPEN = 0x412ACD7A
    UI_BASEBUILD_PLACEBUILDING = 0x5EB87AEF
    UI_BASEBUILD_REPAIRTECH = 0xAB2C9A05
    UI_BASEBUILD_REPAIRTECH_ERROR = 0xE1303E62
    UI_BASEBUILD_ROTATE = 0xEF9C456B
    UI_BASEBUILD_ROTATE_LOOP_START = 0xED43B465
    UI_BASEBUILD_ROTATE_LOOP_STOP = 0xED2E9987
    UI_BASEBUILD_SETCOLOUR = 0xA55D8932
    UI_BASEBUILD_SNAP = 0x79A35452
    UI_BEACON_DISCOVER = 0x75B9A824
    UI_BIOSHIP_ADDORGAN = 0xF5166DC5
    UI_BLUEPRINT_KNOWN = 0x6D5C3D63
    UI_BUILD_ERROR = 0x75AC6211
    UI_BUILDABLESHIP_CREATENEW = 0x6FC84A5B
    UI_BUILDABLESHIP_DELETE = 0xB8C56DC6
    UI_BUILDABLESHIP_DUPLICATE = 0xEE5122CA
    UI_BUILDABLESHIP_HIGHLIGHT = 0xB4BBDA95
    UI_BUILDABLESHIP_MODULE_MENU = 0xEA694FBB
    UI_BUILDABLESHIP_PLACE = 0x522B6A3C
    UI_BUILDABLESHIP_PURCHASE = 0xDFDE10AE
    UI_BUILDABLESHIP_VALIDPLACEMENT = 0x6E4F1F34
    UI_BUY = 0xC18CADCA
    UI_CHOICETEXT_WOOSH = 0x8D7D9943
    UI_CLICK_GENERIC = 0x114B52C4
    UI_COMBAT_UNIT_DEPLOYED_01 = 0x221ADFB2
    UI_COMBAT_UNIT_DEPLOYED_02 = 0x221ADFB1
    UI_COMBAT_UNIT_DEPLOYED_03 = 0x221ADFB0
    UI_COMMUNICATOR_HAIL_ALARM = 0x820AE7EA
    UI_CREDITS_INCREASE = 0x12183687
    UI_CRITICAL_HIT = 0x8D307B3B
    UI_DECISIONTEXT_MOUSEOVER = 0x2986B81F
    UI_DESTINATION_REACHED = 0x6C649E5D
    UI_DISMANTLE = 0x86CF5DA3
    UI_DUMMY_EVENT = 0xD6C96D03
    UI_EPIC_ITEM = 0xFB7EBFED
    UI_ERROR = 0x3C2700B8
    UI_FRIGATE_LIVING_FEED = 0x5679A6D
    UI_FRONTEND_BACK = 0x9E331224
    UI_FRONTEND_ENTER = 0xAA0B552D
    UI_FRONTEND_EXIT = 0xC9410141
    UI_FRONTEND_PRODUCTSBUILD = 0x1C2B169B
    UI_FRONTEND_SELECTGENERIC = 0xD8AF6F74
    UI_FRONTEND_TECHBUILD = 0xCA798E63
    UI_FRONTEND_TEXTOVERLAY_DISCOVERY = 0x185DAFCB
    UI_FRONTEND_TEXTOVERLAY_EMPTY = 0xBC089316
    UI_FRONTEND_TEXTOVERLAY_SUBSTANCE = 0x1240C80B
    UI_FRONTEND_TEXTOVERLAY_TECH = 0x14743037
    UI_FRONTEND_TRANSFER = 0x44713ED8
    UI_GAMEMODE_ERASE_COMPLETE = 0xEDE52A4
    UI_GAMEMODE_ERASE_ERROR = 0x68702A95
    UI_GAMEMODE_HOVER = 0xEE0CC5FE
    UI_GAMEMODE_SELECT = 0x2E8FBD50
    UI_GAMEMODE_WARNING = 0x2FB112AC
    UI_GLITCHED_MEMORY = 0x608D8720
    UI_HEALTH_INCREASE = 0xD2D6DFE3
    UI_INCOMING_FRIGATE_LIVING_WARNING = 0xF9E01984
    UI_INCOMING_MESSAGE = 0x6A39A46E
    UI_INCOMING_NORMANDY_WARNING = 0x1EE13682
    UI_INCOMING_STARSHIP_WARNING = 0xFB031F6
    UI_INSUFFICIENT_FUEL = 0x302A36D2
    UI_INSUFFICIENT_STANDING = 0xC49AAA32
    UI_INSUFFICIENT_TECH_FRAGMENTS = 0x9A0D4494
    UI_INTERACT_TIMER = 0x62988FE
    UI_INTERACT_TIMER_STOP = 0x587C411D
    UI_INTERACTIVEFLORA_COLLECT = 0xCAC28EDB
    UI_ITEM_TELEPORTTOSHIP = 0x8738FC46
    UI_ITEM_TRANSFERTOSUIT = 0x4FDFB677
    UI_JUICYGRUB = 0x9D5ABD74
    UI_KEYBINDING = 0xA541E36
    UI_KNOWLEDGE_EXPANDED = 0x6F259D9A
    UI_LANDINGPOST_LOCKON = 0x3241196A
    UI_LAUNCH_CONFIRMATION = 0xA217EA09
    UI_LAUNCH_NOTIFICATION = 0x2EDEE04B
    UI_LEVEL_UP_TEXT = 0xA22D01BE
    UI_MANAGE_EXOSUIT_INVENTORY = 0xA8202B36
    UI_MAP_ENTRY = 0xA4B39221
    UI_MAP_EXIT = 0xB2526227
    UI_MAP_FILTER_CHANGE = 0x57BB81D0
    UI_MAP_HIGHLIGHT_HOVER = 0xA9310FCE
    UI_MAP_INFO = 0xFA9400A7
    UI_MAP_INTERACT_TIMER = 0x3A90F61B
    UI_MAP_LINES = 0x41EB3474
    UI_MAP_MENUDOWN = 0xAC6E86A6
    UI_MAP_MENUUP = 0x15E6E0CD
    UI_MAP_NAV_MODE_BACK = 0x6C37A7AE
    UI_MAP_NAV_MODE_NEXT = 0x65D24B80
    UI_MAP_NAV_MODE_SWITCH_FAIL = 0x809B54D6
    UI_MAP_NAV_PATH_BACK = 0xA8B966DE
    UI_MAP_NAV_PATH_NEXT = 0x82556BF0
    UI_MAP_PLANET_HOVER = 0x5E11CDF2
    UI_MAP_PLANET_SELECT = 0xC49E774
    UI_MAP_PLANET_UNSELECT = 0x16C9D0D
    UI_MAP_POINT_SELECT = 0x9BFF4F86
    UI_MAP_SELECT = 0x4FA1AADF
    UI_MAP_TEXT = 0x1ADD72A
    UI_MAP_TEXT_OUT = 0xBC076EE7
    UI_MAP_WAYPOINT_ADDED = 0xE4BFD309
    UI_MAP_WAYPOINT_DELETED = 0x13DF9858
    UI_MAP_WAYPOINT_ERROR = 0xBEEBD855
    UI_MARKER = 0x2B07DD4C
    UI_MENU_BUILD_TAB = 0x79CE128A
    UI_MENU_INCORRECT = 0x1F60B11B
    UI_MENU_OPTION_SWITCH = 0xFF2FBCA4
    UI_MESSAGE_GENERIC = 0x3A148ACD
    UI_MISSION_NEWSECONDARY_COMPLETE = 0xD8AFAE1F
    UI_MISSION_NEWSECONDARY_OBJECTIVE = 0x2BAC95E3
    UI_MISSION_NOTIFYSCAN = 0x73345F47
    UI_MISSION_NOTIFYSCAN_END = 0xC46B3C49
    UI_MISSIONPRIMARY_UPDATE = 0xF2CE94C6
    UI_NANITES_INSUFFICIENT = 0x9134500C
    UI_NANITES_RECEIVED = 0xEE872C40
    UI_NEW_DISCOVERY = 0x9F19BAC7
    UI_NEW_SUIT_SLOT = 0x1C7D7573
    UI_NEW_TECH = 0xC0882ABB
    UI_NEWTECH_WOOSH = 0xC814BFB5
    UI_NEXT_MESSAGE = 0x30D44C11
    UI_NOWHERETOLAND = 0xC10CD558
    UI_NPC_SHIP_HIT_ALERT = 0xACC079B1
    UI_NPC_SHIP_INTERACTION = 0x3BAC3D09
    UI_OXYGEN_REPLENISHED = 0xBDCC5A4E
    UI_PAGE_CHANGE = 0xCC61961E
    UI_PHOTOMODE_CAMERAPLACE_END = 0x84F4E2DA
    UI_PHOTOMODE_CAMERAPLACE_START = 0x48E446C9
    UI_PHOTOMODE_IN = 0x3C4C263
    UI_PHOTOMODE_OUT = 0x6AAF1EDE
    UI_PHOTOMODE_TAKEPHOTO = 0xBF99F39
    UI_PHOTOMODE_VALUEDOWN = 0x15D19C71
    UI_PHOTOMODE_VALUEUP = 0x8A6C0E96
    UI_PICKUP_LOOT = 0x5CA94A23
    UI_PICKUP_NITROGENPLANT = 0x65062DDA
    UI_PICKUP_PLANT = 0x6470457C
    UI_PICKUP_RESOURCE = 0xA7CBF529
    UI_PIRATES_WARNING = 0xC9AF9145
    UI_PIRATES_WARNING_STOP = 0xB0E8ACC8
    UI_PLACEMARKER = 0xED754EB1
    UI_PRODUCT_CREATED = 0x7094C6BE
    UI_PROTECTION_OFFLINE = 0xE12D76D3
    UI_PULSEDRIVE_OFFLINE = 0x210BD31B
    UI_PURCHASE = 0x5222F6E7
    UI_QUICKMENU_CLOSE = 0x5A2D907B
    UI_QUICKMENU_NOCHARGE = 0xF7957664
    UI_QUICKMENU_OPEN = 0xFDCE559D
    UI_QUICKMENU_TAB = 0x3AC9E576
    UI_QUICKMENU_TECHCHARGE = 0x3F8067B9
    UI_RARE_ITEM = 0xEB5C5104
    UI_RECORD_UPLOADED = 0xD3A1A28C
    UI_REFINERY_DECREASE = 0x8BA635D9
    UI_REFINERY_INCREASE = 0xA2840089
    UI_RETICULE_LOCK = 0xD2C5A1B9
    UI_RETICULE_ONTARGET = 0xA784CC00
    UI_SAVE = 0x10420AD9
    UI_SCAN_PORTAL = 0xF1AA86CE
    UI_SELECT_GENERIC = 0xAEF4BC9C
    UI_SENTINELDETECTOR = 0xF6022E3C
    UI_SENTINELFORCES_ALERTED = 0xDF61DB92
    UI_SENTINELFORCES_DEACTIVATED = 0x56D6F15
    UI_SENTINELINVESTIGATORS_INCOMING = 0x49D6DFF3
    UI_SERVER_FOUND = 0xF00BB46A
    UI_SERVER_SCANDISCOVERIES = 0xECE09C45
    UI_SERVER_SEARCHING_START = 0x502FCE43
    UI_SERVER_SELECT = 0x4FC49B2E
    UI_SERVER_SELECT_POPUP = 0x6D1A2065
    UI_SETTLEMENT_BUILDINGCOMPLETE = 0xB72E6ADF
    UI_SETTLEMENT_DECISION = 0xED34CBC8
    UI_SETTLEMENT_FLOORCOMPLETE = 0xD4E70FC1
    UI_SETTLEMENT_INVEST = 0x1C799E89
    UI_SHIP_CUSTOMISATION_ASSEMBLE = 0x8DA65690
    UI_SHIP_CUSTOMISATION_CHANGE_SHIP = 0xA93A6CB5
    UI_SHIP_CUSTOMISATION_REMOVE = 0xEB26F228
    UI_SHIP_CUSTOMISATION_SELECT = 0x7F015D48
    UI_SHOP_ITEMS_MENU = 0x6192287
    UI_SHOP_SCROLL_DOWN = 0x874F66BD
    UI_SHOP_SCROLL_UP = 0x77487C8A
    UI_SHOP_SWITCH_BUYSELL = 0xEF95C71C
    UI_SHOP_SWITCH_INVENTORY = 0xD1746824
    UI_SLEEP = 0x71F138DB
    UI_SPECIALS_INSUFFICIENT = 0xD05421AC
    UI_SPOOKYMESSAGE = 0x7A28995E
    UI_STANDING_DECREASED = 0xC781ADCF
    UI_STANDING_INCREASED = 0x4D5E4C1F
    UI_STAT_CHANGE = 0xBE30492B
    UI_TARGET_ONSCREEN = 0x9C212C4F
    UI_TECH_BROKEN = 0x7F1E1E22
    UI_TECH_INSTALLED = 0x748BD54D
    UI_TERRAIN_CHANGESIZE = 0xF4C6C733
    UI_TEXT_WOOSH = 0x990CE3CE
    UI_TEXTENTRY = 0xEE38EFB9
    UI_TIP = 0xE15FC005
    UI_TRADING_MESSAGE = 0xB002EB0D
    UI_TRADING_TEXT = 0x7015F9ED
    UI_TRADING_TEXT_ONESHOT = 0xA1F6BCE4
    UI_TRADING_TEXT_STOP = 0xE3C5B820
    UI_TRADING_TEXT_TRANSLATE = 0x4022E06A
    UI_UNITS_RECEIVED = 0x898CD56B
    UI_VEGETABLE_COLLECT = 0xFC94B9A4
    UI_VR_HANDMENU_CLOSE = 0x364CF0A6
    UI_VR_HANDMENU_HIGHLIGHT = 0xE672686E
    UI_VR_HANDMENU_OPEN = 0x112C18F2
    UI_VR_HANDMENU_OPENLP = 0xD0DCFE1E
    UI_VR_WRISTMENU_HIGHLIGHT = 0xB1E07F62
    UI_VR_WRISTMENU_IN = 0xFC42EEA7
    UI_VR_WRISTMENU_OUT = 0xDD62551A
    UI_VR_WRISTMENU_SELECT = 0x52EBA056
    UI_VR_WRISTMENU_TOUCH = 0x9C3C5AF
    UI_WAKEUP = 0x57610D41
    UI_WANTED_INCREASE = 0x80BA51BA
    UI_WANTED_INCREASE_01 = 0x98402038
    UI_WANTED_INCREASE_02 = 0x9840203B
    UI_WANTED_INCREASE_03 = 0x9840203A
    UI_WANTED_INCREASE_04 = 0x9840203D
    UI_WANTED_INCREASE_05 = 0x9840203C
    UI_WEAPON_FOUND = 0x4DBA89E7
    UI_WEIRDBIOME_COUNTDOWN = 0x4A2D6533
    UI_WEIRDBIOME_COUNTDOWN_END = 0x4A1515D5
    UI_WHALESONG = 0xFDC0FA36
    UI_WORD_LEARNT = 0xA3561BAF
    UI_WPN_LOCKON = 0x9F4B5814
    UI_WPN_RETICULE_LOCK = 0x9E114361
    UI_WPN_TARGET_FOCUS = 0xF4A8A5B0
    UNDERWATER_STEAMVENT_RUMBLE = 0xC54EB9A6
    UNDERWATER_STEAMVENT_VENTING = 0xB67C3BF4
    UNDERWATER_STEAMVENT_VENTING_END = 0x6B30806A
    VAULT_CLOSE = 0x8D7D844A
    VAULT_OPEN = 0x5AE8C76E
    VEHICLE_DESTRUCTIBLE = 0x61DED67C
    VEHICLE_MARKER_COLLECT = 0xCC0C57CF
    VEHICLE_MARKER_DELETE = 0xB7B05DC2
    VEHICLE_MARKER_PLACE = 0x46C78620
    VEHICLE_RACE_END = 0x916A2903
    VEHICLE_RACE_START = 0xB3AF6D8
    VEHICLE_SPAWN = 0x5B82CC5F
    VENUSFLYTRAP_CLOSE = 0x722B8CBB
    VENUSFLYTRAP_OPEN = 0xC33559DD
    VIEW_FIRSTPERSON = 0x87AD2FC2
    VIEW_THIRDPERSON = 0x72BDEFFF
    VILESPAWN_EGG_COLLECT = 0xDB837279
    VILESPAWN_LP = 0xAC9C927F
    VILESPAWN_LP_STOP = 0x5DCB9CCA
    VO_ANOMALYDETECTED = 0xFB08E100
    VO_BASECOMPUTER_ONLINE = 0xA8C4CF0F
    VO_INVENTORY_FULL = 0x1B7EE4FB
    VO_PRODUCT_CONSTRUCTED = 0x50544311
    VO_SECURE_TRADEMODULE_LOCATED = 0x97980A7C
    VO_SECURE_TRANSMISSIONMODULE_LOCATED = 0xD9F965C8
    VO_STARSHIP_SIGNAL = 0x41EB6874
    VO_TECH_COMP_REPAIRED = 0xC1C549DE
    VO_TECH_INSTALLED = 0xF1E0AD04
    VO_TECH_OFFLINE = 0x301397AB
    VO_TECH_RECHARGED = 0x20A524C7
    VO_TECH_REPAIRED = 0xD718EFE6
    VO_TUT_COORDSRECEIVED = 0xA023F16A
    VO_TUT_STATIONCOORDSRECEIVED = 0x5B74DAC
    VR_FOLEY_ARM_MOVEMENTS = 0xFAE20B59
    VR_FOLEY_ARM_MOVEMENTS_LEFT = 0xDB88808F
    VR_FOLEY_ARM_MOVEMENTS_RIGHT = 0x84729F52
    VR_FOLEY_ARMS_WOOSH = 0x3FAF1A30
    VR_FOLEY_HAND_CLENCH_CLOSE = 0x1CA287DE
    VR_FOLEY_HAND_CLENCH_OPEN = 0xF9C86F7A
    VR_PULLTOUSE = 0x6A454EC3
    VR_PULLTOUSE_STOP = 0x324C4A2E
    VR_TELEPORTMOVE = 0xAFFEF3EA
    VR_THEREMIN = 0xC7432116
    WALKER_CHARGEUP = 0xB8A1D0D9
    WALKER_DIE = 0xAE8BE068
    WALKER_EMOTE_LP = 0x2AE78935
    WALKER_EMOTE_LP_STOP = 0xE77997D8
    WALKER_ENRAGE = 0xBB04EB24
    WALKER_FALL_IMPACT = 0x2A1F88A2
    WALKER_IDLE = 0xB2C7FAE0
    WALKER_LASER = 0xA8AC2E4F
    WALKER_LASER_STOP = 0xCCF69C7A
    WALKER_LEG_HIT_IDLE = 0x891868C1
    WALKER_LEG_HIT_LEFT_IN_01 = 0xC8452F0
    WALKER_LEG_HIT_LEFT_IN_02 = 0xC8452F3
    WALKER_LEG_HIT_LEFT_OUT_01 = 0x7F48B349
    WALKER_LEG_HIT_LEFT_OUT_02 = 0x7F48B34A
    WALKER_LEG_HIT_RIGHT_IN_01 = 0xDB3B90BF
    WALKER_LEG_HIT_RIGHT_IN_02 = 0xDB3B90BC
    WALKER_LEG_HIT_RIGHT_OUT_01 = 0xB0B8D754
    WALKER_LEG_HIT_RIGHT_OUT_02 = 0xB0B8D757
    WALKER_MOVE = 0x121B6AD1
    WALKER_SIT = 0xAE6B8C16
    WALKER_SQUAWKER = 0xB8DD2DCB
    WALKER_STAND = 0xC4C8E4FE
    WALKER_STEP = 0xB63357EC
    WALKINGBUILDING_AMBIENT_LP = 0x7F4B47C2
    WALKINGBUILDING_ATTACK = 0xE2981965
    WALKINGBUILDING_AWAKEN = 0x839CB70C
    WALKINGBUILDING_EVADE = 0xE7E0FD10
    WALKINGBUILDING_MOVE_SMALL = 0x44453B36
    WALKINGBUILDING_POUNCE = 0x33700AF
    WALKINGBUILDING_POUNCE_BACK = 0x1B4E6F97
    WALKINGBUILDING_STUNNED = 0x22567F4A
    WARN_CIVILIANSHIELDS = 0xBBF796CB
    WARN_DISTRESS_DETECTED = 0x64B78982
    WARN_HOSTILE_APPROACH = 0x41DD6191
    WARN_HOSTILE_DETECTED = 0x4BE3C41F
    WARN_HOSTILE_SCAN = 0x15472E9E
    WARRIORANGRY = 0x8489D2FC
    WARRIORCHATTER = 0xF6BE1370
    WARRIORGREET1 = 0xEDB7C38D
    WARRIORGREET2 = 0xEDB7C38E
    WARRIORGREET3 = 0xEDB7C38F
    WARRIORHAPPY01 = 0x3DEECF18
    WARRIORHAPPY02 = 0x3DEECF1B
    WARRIORHAPPY03 = 0x3DEECF1A
    WARRIORHONOUR = 0xDC70021E
    WATERFALL = 0x7BA60439
    WEAPONTECHSTATION_IN = 0x9D11B593
    WEAPONTECHSTATION_OUT = 0xCED353AE
    WEATHER_OVER = 0xF6B6BE20
    WEATHER_WARN = 0xDBD65A16
    WEIRDBEAMSTONE = 0x2F81A4D0
    WEIRDBEAMSTONE_STOP = 0xFB01B69F
    WEIRDBUBBLE = 0x99F5D6EE
    WEIRDBUBBLE_STOP = 0x40235AED
    WEIRDCONTOUR = 0x21ADDAD6
    WEIRDFLOAT_LP = 0xFAD2C455
    WEIRDFLOAT_STOP = 0xA3CC4851
    WEIRDOFRACTCUBE = 0x79920C4A
    WEIRDROLL_LP = 0x2E855EEC
    WEIRDROLL_STOP = 0x1AD9EA60
    WEIRDSHARDS = 0xF151439F
    WEIRDWIRECELL = 0xC5896FBB
    WINGFLAP = 0x13E172E1
    WOOSH_DROID_SMALL_01_FRONT = 0x11BC8ADA
    WOOSH_DROID_SMALL_01_MID = 0xCF0FF131
    WOOSH_DROID_SMALL_01_REAR = 0xEA2BF77F
    WPN_BROKEN = 0xA5FE3EFA
    WPN_GROUND_SIZZLE = 0x4222F8E2
    WPN_MELEE_IMPACT_CREATURE = 0xA2108648
    WPN_MELEE_IMPACT_GENERIC = 0xCB00CD9E
    WPN_NOAMMO = 0x139F02B6
    WPN_NOTECHTOOL = 0xD9985CA2
    WPN_NOTOOL = 0xBDA317B2
    WPN_PL_CHANGE = 0xB7746754
    WPN_PL_DEPLETED = 0xF90065F9
    WPN_PL_GRENADE = 0xF099543E
    WPN_PL_GRENADE_BOUNCE = 0xCD5D244D
    WPN_PL_GRENADE_EXPLODE = 0x183BF870
    WPN_PL_HANDLASER = 0xBEDA84FC
    WPN_PL_HANDLASER_OVERHEAT = 0xD348E403
    WPN_PL_HANDLASER_STOP = 0x82A0A48B
    WPN_PL_JAVELIN_CHARGE = 0xF04467B0
    WPN_PL_JAVELIN_CHARGE_END = 0xB6B9D056
    WPN_PL_MELEE = 0x8FC09CD8
    WPN_PL_NEUTRON_CANNON_BUILDUP = 0xD02F55E1
    WPN_PL_NEUTRON_CANNON_CHARGE_END = 0x6CF3B5E8
    WPN_PL_NEUTRON_CANNON_FIRE = 0x93C21A7E
    WPN_PL_NEUTRON_CANNON_FIRE_CHARGED = 0x8238361B
    WPN_PL_NEUTRON_CANNON_LP = 0xBEB6F46E
    WPN_PL_OUTOFAMMO_GUN = 0xB3D2327A
    WPN_PL_PISTOL = 0xC3B24F39
    WPN_PL_PISTOL_RELOAD = 0xEA835E0B
    WPN_PL_PUTAWAY = 0x8C2DCD79
    WPN_PL_RAILGUN = 0xEDBB26D2
    WPN_PL_RAILGUN_PATHFINDER = 0x709D11EC
    WPN_PL_RAILGUN_RELOAD = 0xCE68FDE6
    WPN_PL_SCAN = 0x9E35101F
    WPN_PL_SCAN_STOP = 0xE8E06EAA
    WPN_PL_SCATTERBLASTER = 0xC4F25AF5
    WPN_PL_SHOTGUN = 0x128E00C2
    WPN_PL_SHOTGUN_PATHFINDER = 0x381A3A7C
    WPN_PL_SHOTGUN_RELOAD = 0xA0D247B6
    WPN_PL_SMG = 0x3E5AE267
    WPN_PL_TAKEOUT = 0x5CE8E2AB
    WPN_SHIP_CHANGE = 0x5A129B56
    WPN_SHIP_CYCLOTRON_FIRE = 0x7611E876
    WPN_SHIP_CYCLOTRON_OVERHEAT = 0x42DE8842
    WPN_SHIP_GUN = 0x1AAC86AC
    WPN_SHIP_INFRAKNIFE_FIRE = 0xFA63876
    WPN_SHIP_INFRAKNIFE_OVERHEAT = 0xB567D842
    WPN_SHIP_LASER = 0x58B37AEF
    WPN_SHIP_LASER_STOP = 0x40FBA3DA
    WPN_SHIP_MISSILE_OVERHEAT = 0xD49513E9
    WPN_SHIP_OUTOFAMMO = 0xEDB8EC03
    WPN_SHIP_OVERHEAT = 0xBDEC12CA
    WPN_SHIP_POSITRON_FIRE = 0xE9733AD7
    WPN_SHIP_POSITRON_OVERHEAT = 0x8FDEE823
    WPN_SHIP_READY = 0xFE1BE6F7
    WPN_TERRAIN_BUILD = 0xBB4541A9
    WPN_TERRAIN_BUILD_END = 0x2BDF7F4B
    WPN_TERRAIN_DESTROY = 0x8487F81F
    WPN_TERRAIN_DESTROY_END = 0xC4E8D681
    WPN_TERRAIN_END = 0x33B1CD16
    WPN_TERRAIN_UNDO = 0x89B7D91D


class cTkWaterCondition(IntEnum):
    Absolutely_Tranquil = 0x0
    Breezy_Lake = 0x1
    Wavy_Lake = 0x2
    Still_Pond = 0x3
    Agitated_Pond = 0x4
    Agitated_Lake = 0x5
    Surf = 0x6
    Big_Surf = 0x7
    Chaotic_Sea = 0x8
    Huge_Swell = 0x9
    Choppy_Sea = 0xA
    Very_Choppy_Sea = 0xB
    White_Horses = 0xC
    Ocean_Planet = 0xD
    Wall_Of_Water = 0xE


class cTkWaterRequirement(IntEnum):
    NoStorm = 0x0
    Storm = 0x1


class cGcCustomisationComponentData(IntEnum):
    Player = 0x0
    Vehicle = 0x1
    Weapon = 0x2
    Ship_01 = 0x3
    Ship_02 = 0x4
    Ship_03 = 0x5
    Ship_04 = 0x6
    Ship_05 = 0x7
    Ship_06 = 0x8
    Vehicle_Bike = 0x9
    Vehicle_Truck = 0xA
    Vehicle_WheeledBike = 0xB
    Vehicle_Hovercraft = 0xC
    Vehicle_Submarine = 0xD
    Vehicle_Mech = 0xE
    Freighter = 0xF
    Pet = 0x10
    Ship_07 = 0x11
    Ship_08 = 0x12
    Ship_09 = 0x13
    Ship_10 = 0x14
    Ship_11 = 0x15
    Ship_12 = 0x16
    PirateFreighter = 0x17
    Skiff = 0x18
    FishingRod = 0x19


class cGcByteBeatPlayerComponentData(IntEnum):
    Player = 0x0
    Settlement = 0x1


class cGcShipFlareComponentData(IntEnum):
    Default = 0x0


class cCollisionShapeType(IntEnum):
    Box = 0x0
    Capsule = 0x1
    Sphere = 0x2
    None_ = 0x3
