from concurrent.futures import ThreadPoolExecutor

BASE_ADDRESS: int = -1
SIZE_OF_IMAGE: int = -1

# Store all the globals here like this so that we may access them easily and
# from anywhere.
GcAISpaceshipGlobals = None
GcAtlasGlobals = None
GcAudioGlobals = None
GcBuildingGlobals = None
GcCameraGlobals = None
GcCharacterGlobals = None
GcCreatureGlobals = None
GcDebugOptions = None
GcEffectsGlobals = None
GcEnvironmentGlobals = None
GcFleetGlobals = None
GcFreighterBaseGlobals = None
GcGalaxyGlobals = None
GcGameplayGlobals = None
GcGraphicsGlobals = None
GcMultiplayerGlobals = None
GcPlacementGlobals = None
GcPlayerGlobals = None
GcRichPresenceGlobals = None
GcRobotGlobals = None
GcSceneOptions = None
GcScratchpadGlobals = None
GcSettlementGlobals = None
GcSimulationGlobals = None
GcSkyGlobals = None
GcSmokeTestOptions = None
GcSolarGenerationGlobals = None
GcSpaceshipGlobals = None
GcTerrainGlobals = None
GcUIGlobals = None
GcVehicleGlobals = None
GcWaterGlobals = None

GcApplication = None
gravity_singleton = None

# TODO: Move somewhere else? Not sure where but this doesn't really fit here...
executor: ThreadPoolExecutor = None  # type: ignore
