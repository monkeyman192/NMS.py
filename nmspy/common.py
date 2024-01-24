from concurrent.futures import ThreadPoolExecutor
import os
import os.path as op

import nmspy._internal as _internal
import nmspy.data.structs as nms_structs

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

GcApplication: nms_structs.cGcApplication = None  # type: ignore
gravity_singleton: nms_structs.cTkDynamicGravityControl = None  # type: ignore
memory_manager: int = 0

# TODO: Move somewhere else? Not sure where but this doesn't really fit here...
executor: ThreadPoolExecutor = None  # type: ignore

mod_save_dir = op.join(_internal.NMS_ROOT_DIR, "NMSPY_SAVES")
if not op.exists(mod_save_dir):
    os.makedirs(mod_save_dir)
