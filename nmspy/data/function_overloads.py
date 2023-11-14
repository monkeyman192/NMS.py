from typing import Literal

class StringCchCopyW:
    overloads = Literal[
        "STRSAFE_LPWSTR, size_t, STRSAFE_LPCWSTR",
        "wchar_t *, unsigned __int64, const wchar_t *",
    ]

class StringCchCatW:
    overloads = Literal[
        "STRSAFE_LPWSTR, size_t, STRSAFE_LPCWSTR",
        "wchar_t *, unsigned __int64, const wchar_t *",
    ]

class cTkSeed:
    class cTkSeed:
        overloads = Literal[
            "cTkSeed *",
            "cTkSeed *, const cTkSeed *",
            "cTkSeed *, int",
            "cTkSeed *, unsigned __int64",
            "cTkSeed *, const cTkVector3 *",
        ]

class cTkResourceDescriptor:
    class cTkResourceDescriptor:
        overloads = Literal[
            "cTkResourceDescriptor *",
            "cTkResourceDescriptor *, const cTkResourceDescriptor *",
        ]
    class DistortInstance:
        overloads = Literal[
            "cTkResourceDescriptor *, const char *, const cTkSeed *, const cTkSeed *, const TkID<256> *, const TkID<256> *",
            "cTkResourceDescriptor *, const char *, const float, const float, const cTkSeed *, const cTkSeed *, const TkID<256> *, const TkID<256> *",
        ]
    class GenerateInstance:
        overloads = Literal[
            "cTkResourceDescriptor *, const char *, const cTkSeed *, const TkID<256> *, const TkID<256> *",
            "cTkResourceDescriptor *, const char *, const std::vector<TkID<256>,TkSTLAllocatorShim<TkID<256>,8,-1> > *",
        ]
    class ShouldLoadMesh:
        overloads = Literal[
            "cTkResourceDescriptor *, const TkID<256> *, const TkID<256> *",
            "cTkResourceDescriptor *, const TkID<256> *",
            "cTkResourceDescriptor *, const char *, TkID<256> *",
        ]

class cTkSmartResHandle:
    class cTkSmartResHandle:
        overloads = Literal[
            "cTkSmartResHandle *",
            "cTkSmartResHandle *, const cTkSmartResHandle *",
        ]

class BaseIndex:
    class BaseIndex:
        overloads = Literal[
            "BaseIndex *",
            "BaseIndex *, unsigned __int16",
            "BaseIndex *, const BaseIndex *",
        ]

class cGcProjectileImpact:
    class cGcProjectileImpact:
        overloads = Literal[
            "cGcProjectileImpact *",
            "cGcProjectileImpact *, const cGcProjectileImpact *",
        ]
    class Init:
        overloads = Literal[
            "cGcProjectileImpact *, cGcProjectileData *, const cTkVector3 *, const cTkVector3 *, const cTkVector3 *, float, cTkRigidBody *, cGcOwnerConcept *, int, eDamageType, const std::vector<cGcImpactCombatEffectData,TkSTLAllocatorShim<cGcImpactCombatEffectData,4,-1> > *, const std::vector<cGcCombatEffectDamageMultiplier,TkSTLAllocatorShim<cGcCombatEffectDamageMultiplier,4,-1> > *, float, float",
            "cGcProjectileImpact *, cGcProjectileData *, const cTkVector3 *, const cTkVector3 *, const cTkVector3 *, float, cTkRigidBody *, cGcOwnerConcept *, int, eDamageType, const cTkDynamicArray<cGcImpactCombatEffectData> *, const std::vector<cGcCombatEffectDamageMultiplier,TkSTLAllocatorShim<cGcCombatEffectDamageMultiplier,4,-1> > *, float, float",
        ]

class cTkRigidBody:
    class cTkRigidBody:
        overloads = Literal[
            "cTkRigidBody *",
            "cTkRigidBody *, const cTkRigidBody *",
        ]
    class GetAabb:
        overloads = Literal[
            "cTkRigidBody *, cTkVector3 *, cTkVector3 *, const cTkMatrix34 *",
            "cTkRigidBody *, cTkPhysRelVec3 *, cTkPhysRelVec3 *",
            "cTkRigidBody *, cTkVector3 *, cTkVector3 *",
        ]

class MenuAction:
    class MenuAction:
        overloads = Literal[
            "MenuAction *",
            "MenuAction *, const MenuAction *",
            "MenuAction *, eQuickMenuActions, const cGcInventoryElement *, const bool",
            "MenuAction *, eQuickMenuActions, const cGcInventoryElement *, int, const bool",
            "MenuAction *, eQuickMenuActions, const cGcInventoryElement *, const eWeaponMode, const bool",
        ]

class cGcResourceCustomisation:
    class cGcResourceCustomisation:
        overloads = Literal[
            "cGcResourceCustomisation *",
            "cGcResourceCustomisation *, const cGcResourceCustomisation *",
        ]

class cTkModelResourceRenderer:
    class cTkModelResourceRenderer:
        overloads = Literal[
            "cTkModelResourceRenderer *",
            "cTkModelResourceRenderer *, const cTkModelResourceRenderer *",
        ]
    class CalcFocusPoint:
        overloads = Literal[
            "TkHandle, const char *, const cTkVector3 *, cTkVector3 *",
            "TkHandle, const char *, const cTkVector3 *, cTkPhysRelVec3 *",
        ]

class cGcApplication:
    class DrainFileLoadsAndPollableTasks:
        overloads = Literal[
            "bool",
            "bool, int",
        ]

class cGcEncounterComponent:
    class GetTypedComponent:
        overloads = Literal[
            "int",
            "cTkAttachment *",
        ]
    class ApplyScriptedOverride:
        overloads = Literal[
            "cGcEncounterComponent *, const TkID<128> *",
            "cGcEncounterComponent *, const cGcSentinelEncounterOverride *, StackAllocator<cTkSmartResHandle,4,-1> *",
        ]

class OSDMessage:
    class OSDMessage:
        overloads = Literal[
            "OSDMessage *, const OSDMessage *",
            "OSDMessage *, OSDMessage *",
        ]

class sPlayerTitleStatWatcher:
    class StatChanged:
        overloads = Literal[
            "sPlayerTitleStatWatcher *, const TkID<128> *, __int64",
            "sPlayerTitleStatWatcher *, const TkID<128> *, long double",
        ]

class cGcPlayerWeapon:
    class CanCharge:
        overloads = Literal[
            "cGcPlayerWeapon *, eWeaponMode",
            "cGcPlayerWeapon *",
        ]
    class GetAvailableAmmo:
        overloads = Literal[
            "cGcPlayerWeapon *",
            "cGcPlayerWeapon *, eWeaponMode",
        ]
    class UsesInventoryAmmo:
        overloads = Literal[
            "cGcPlayerWeapon *",
            "cGcPlayerWeapon *, __int64",
        ]
    class Reload:
        overloads = Literal[
            "cGcPlayerWeapon *",
            "cGcPlayerWeapon *, eWeaponMode, bool",
        ]

class cGcNGuiManager:
    class ScopedScaleChange:
        class ScopedScaleChange:
            overloads = Literal[
                "cGcNGuiManager::ScopedScaleChange *, float, __int64",
                "cGcNGuiManager::ScopedScaleChange *, const cTkVector2 *, __int64",
            ]
    class BeginFrame:
        overloads = Literal[
            "cGcNGuiManager *, cTkNGuiInput *, bool, float",
            "cGcNGuiManager *, cTkNGuiInput *, const cTkVector2 *, bool, float",
        ]

class cGcSolarSystem:
    class InPlanetRange:
        overloads = Literal[
            "cGcSolarSystem *",
            "cGcSolarSystem *, const cTkVector3 *",
        ]

class hknpShapeProperties:
    class Entry:
        class Entry:
            overloads = Literal[
                "cGcUniverseAddressLayout::Bitfield *",
                "hknpShapeProperties::Entry *, hknpShapeProperties::Entry *",
                "hknpShapeProperties::Entry *, const hknpShapeProperties::Entry *",
            ]
    class hknpShapeProperties:
        overloads = Literal[
            "std::initializer_list<char const *> *",
            "hknpShapeProperties *, const hknpShapeProperties *",
        ]

class cGcGalacticVoxelCoordinate:
    class cGcGalacticVoxelCoordinate:
        overloads = Literal[
            "cGcGalacticVoxelCoordinate *, const cGcGalacticAddressData *",
            "cGcGalacticVoxelCoordinate *",
            "cGcGalacticVoxelCoordinate *, __int16, __int16, __int16",
        ]

class cGcSettlementState:
    class cGcSettlementState:
        overloads = Literal[
            "cGcSettlementState *, const cGcSettlementState *",
            "cGcSettlementState *",
        ]

class cTkGraphicsManagerBase:
    class GetProjectionMatrix:
        overloads = Literal[
            "cTkGraphicsManagerBase *, cTkMatrix44 *",
            "cTkGraphicsManagerBase *, cTkMatrix44 *, float",
        ]

class cGcBinoculars:
    class cGcBinoculars:
        overloads = Literal[
            "cGcBinoculars *",
            "cGcBinoculars *, const cGcBinoculars *",
        ]

class cGcMaintenanceContainer:
    class cGcMaintenanceContainer:
        overloads = Literal[
            "cGcMaintenanceContainer *, cGcMaintenanceContainer *",
            "cGcMaintenanceContainer *, const cGcMaintenanceContainer *",
        ]

class cTk3dLayer:
    class ConstructDynamicSize:
        overloads = Literal[
            "cTk3dLayer *, const cTkVector2 *, const cTkVector2 *",
            "cTk3dLayer *, const cTkVector3 *, const cTkVector2 *",
        ]
    class Construct:
        overloads = Literal[
            "cTk3dLayer *, const cTkVector2 *, const cTkVector2 *, const cTkVector2 *",
            "cTk3dLayer *, const cTkVector3 *, const cTkVector2 *, const cTkVector2 *",
        ]
    class SetPosition:
        overloads = Literal[
            "cTk3dLayer *, const cTkVector3 *",
            "cTk3dLayer *, const cTkPhysRelVec3 *",
        ]

class cTk2dLayer:
    class GetPosition:
        overloads = Literal[
            "cTk2dLayer *, cTkVector2 *, const cTkVector2 *",
            "cTk2dObject *, cTkVector2 *",
        ]
    class Construct:
        overloads = Literal[
            "cTk2dLayer *, const cTkVector2 *, const cTkVector2 *, const cTkVector2 *, const cTkColour *",
            "cTk2dLayer *, const cTkVector2 *, const cTkVector2 *, const cTkVector2 *",
        ]

class cTkShader:
    class cTkShader:
        overloads = Literal[
            "cTkShader *, int",
            "cTkShader *, const cTkShader *",
        ]

class FloatEditOptions:
    class FloatEditOptions:
        overloads = Literal[
            "FloatEditOptions *",
            "FloatEditOptions *, float, int",
        ]

class cTkNGuiEditor:
    class DoText:
        overloads = Literal[
            "cTkNGuiEditor *, const char *, eNGuiSizeType, float, float",
            "cTkNGuiEditor *, const char *, const char *, eNGuiSizeType",
        ]
    class DoEditFloat:
        overloads = Literal[
            "cTkNGuiEditor *, float *, float, bool, float, int, bool",
            "cTkNGuiEditor *, const char *, float *, float, bool, float, int, bool",
        ]
    class DoEditText:
        overloads = Literal[
            "cTkNGuiEditor *, char *, int, int, eNGuiSizeType, float, float, bool",
            "cTkNGuiEditor *, const char *, char *, int",
        ]
    class DoEditVector:
        overloads = Literal[
            "cTkNGuiEditor *, const char *, cTkVector2 *, const FloatEditOptions *, const FloatLimits *",
            "cTkNGuiEditor *, const char *, cTkVector3 *, const FloatEditOptions *, const FloatLimits *",
        ]
    class DoIconListItem:
        overloads = Literal[
            "cTkNGuiEditor *, unsigned int, const char *, bool",
            "cTkNGuiEditor *, unsigned int, const char *, bool, float, eNGuiInputType *",
        ]
    class DoSliderFloat:
        overloads = Literal[
            "cTkNGuiEditor *, float *, float, float, float, float",
            "cTkNGuiEditor *, const char *, float *, float, float, float",
        ]
    class OpenFileBrowser:
        overloads = Literal[
            "char *, const char *, const char *, const char *, bool, const char *",
            "char *, int, const char *, bool, bool, bool",
        ]

class cGcAtlasBrokerAzure:
    class DoCompletion:
        overloads = Literal[
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestDiscoveryExact *, cGcAtlasRecvDiscoveryExact *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestDiscoveryCategory *, cGcAtlasRecvDiscoveryList *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestDiscoveryAllOnPlanet *, cGcAtlasRecvDiscoveryList *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestBases *, cGcAtlasRecvBaseList *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendQueryFeaturedBases *, cGcAtlasRecvFeaturedBasesQueryList *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendSubmitMonument *, cGcAtlasRecvBasic *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendQueryActiveFeaturedBases *, cGcAtlasRecvActiveFeaturedBasesQuery *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendQueryBaseImages *, cGcAtlasRecvBaseImages *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestVoxel *, cGcAtlasRecvVoxel *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestBlob *, cGcAtlasRecvBlob *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestMonument *, cGcAtlasRecvMonumentList *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestTotalContribution *, cGcAtlasRecvTotalContribution *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendQuerySeasonData *, cGcAtlasRecvBasic *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendSubmitSettlement *, cGcAtlasRecvBasic *",
            "cGcAtlasBrokerAzure *, cGcIBrokerData *, const cGcAtlasSendRequestSettlements *, cGcAtlasRecvSettlementList *",
        ]

class cGcURL:
    class cGcURL:
        overloads = Literal[
            "cGcURL *, const cGcURL *",
            "cGcURL *, unsigned __int64",
        ]

class cGcAudioPulseMusic:
    class SoundScape:
        class Load:
            overloads = Literal[
                "cGcAudioPulseMusic::SoundScape *, const XMLNode *",
                "cGcAudioPulseMusic::SoundScape *, const cTkFixedString<256,char> *",
            ]
    class Instrument:
        class Load:
            overloads = Literal[
                "cGcAudioPulseMusic::Instrument *, const XMLNode *",
                "cGcAudioPulseMusic::Instrument *, const cTkFixedString<256,char> *",
            ]

class cGcByteBeatSequencer:
    class cGcByteBeatSequencer:
        overloads = Literal[
            "cGcByteBeatSequencer *",
            "cGcByteBeatSequencer *, const cGcByteBeatSequencer *",
        ]

class cGcInteractionComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]
    class IsInteractionWithAnAlien:
        overloads = Literal[
            "cGcInteractionComponent *",
            "unsigned __int64",
        ]
    class IsNPCInteraction:
        overloads = Literal[
            "unsigned __int64",
            "cGcInteractionComponent *",
        ]
    class ScansAsType:
        overloads = Literal[
            "cGcInteractionComponent *, eInteractionType",
            "cGcInteractionComponent *, eInteractionType, eTechnologyCategory",
        ]

class cGcBaseBuildingBaseLayout:
    class GenerateLayout:
        overloads = Literal[
            "cGcBaseBuildingBaseLayout *, cGcPlayerBasePersistentBuffer *",
            "cGcBaseBuildingBaseLayout *, unsigned __int64, const cTkVector3 *, const cTkMatrix34 *, const cGcPersistentBaseEntry *, int",
        ]

class cGcBuildingList:
    class FindNearest:
        overloads = Literal[
            "cGcBuildingList *, const cTkVector3 *, eBuildingClass, float *",
            "cGcBuildingList *, const cTkVector3 *, float *, bool",
            "cGcBuildingList *, const cTkVector3 *, cTkBitArray<unsigned __int64,1,128> *, float *, bool",
        ]

class cGcBaseBuildingManager:
    class SetNodeColour:
        overloads = Literal[
            "cGcBaseBuildingManager *, TkHandle, unsigned __int8",
            "TkHandle, const cTkColour *, const cTkColour *, const cTkColour *, const cTkColour *",
        ]
    class FindBaseBuildingObject:
        overloads = Literal[
            "cGcBaseBuildingManager *, TkHandle",
            "cGcBaseBuildingManager *, sBaseObjectHandle",
        ]

class cGcOutpostComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcProjectileData:
    class cGcProjectileData:
        overloads = Literal[
            "cGcProjectileData *, const cGcProjectileData *",
            "cGcProjectileData *, cGcProjectileData *",
        ]

class cGcResourceElement:
    class cGcResourceElement:
        overloads = Literal[
            "cGcResourceElement *, const cGcResourceElement *",
            "cGcResourceElement *, cGcResourceElement *",
        ]

class cGcProjectileManager:
    class SpawnResourceBlobs:
        overloads = Literal[
            "cGcProjectileManager *, const cTkMatrix34 *, int, const TkID<128> *, eResourceBlobSpawnStyle, bool, cTkAttachment *",
            "cGcProjectileManager *, const cTkPhysRelMat34 *, int, const TkID<128> *, eResourceBlobSpawnStyle, bool, cTkAttachment *",
        ]

class cGcSpaceshipComponent:
    class GetTypedComponent:
        overloads = Literal[
            "int",
            "cTkAttachment *",
        ]
    class SetLanding:
        overloads = Literal[
            "cGcSpaceshipComponent *, cGcOutpostComponent *",
            "cGcSpaceshipComponent *, const cTkPhysRelMat34 *",
        ]

class cGcBaseBuildingNavigationManager:
    class sObjectNavData:
        class sObjectNavData:
            overloads = Literal[
                "cGcBaseBuildingNavigationManager::sObjectNavData *, const cGcBaseBuildingNavigationManager::sObjectNavData *",
                "cGcBaseBuildingNavigationManager::sObjectNavData *",
            ]

class cGcBaseBuildingObject:
    class sSnappingState:
        class IsSnappedToObject:
            overloads = Literal[
                "cGcBaseBuildingObject::sSnappingState *, const TkID<128> *, int",
                "cGcBaseBuildingObject::sSnappingState *, const TkID<128> *, int, unsigned __int8",
            ]

class cGcBaseSearch:
    class Match:
        overloads = Literal[
            "const cGcBaseSearchFilter *, cGcPlayerBasePersistentBuffer *",
            "const cGcBasePartSearchFilter *, GcPersistencyHandle, const cGcBaseBuildingEntry *, cGcPlayerBasePersistentBuffer *",
            "const cGcBasePartSearchFilter *, const cGcBaseSearchFilter *, const cGcPersistentBBObjectData *, const cGcBaseBuildingEntry *",
        ]

class GetDistance:
    overloads = Literal[
        "const cTkAABB *, const cTkVector3 *",
        "const cGcWFCBaseGenerator::ClusterNavGraphConstructionData::sBuildingData *, const cTkVector3 *",
    ]

class cGcWFCBuildingState:
    class GetSecondsUntilConstructionEnds:
        overloads = Literal[
            "const cGcBuilding *, unsigned __int64 *",
            "const cGcSettlementState *, const int, const eBuildingClass, unsigned __int64 *",
        ]

class cGcNavGraphNode:
    class cGcNavGraphNode:
        overloads = Literal[
            "cGcNavGraphNode *, const cGcNavGraphNode *",
            "cGcNavGraphNode *, const eNPCNavGraphNodeType, TkHandle, cGcNPCInteractiveObjectComponent *",
            "cGcNavGraphNode *, const eNPCNavGraphNodeType, TkHandle, const cTkVector3 *, cGcNPCInteractiveObjectComponent *",
        ]

class cGcScanEventManager:
    class GetActiveEvent:
        overloads = Literal[
            "cGcScanEventManager *, const TkID<256> *",
            "cGcScanEventManager *, int",
        ]
    class GetEventData:
        overloads = Literal[
            "cGcScanEventManager *, const TkID<256> *, eScanTable",
            "cGcScanEventManager *, const TkID<256> *",
        ]
    class ClearMissionEvents:
        overloads = Literal[
            "cGcScanEventManager *, const std::vector<std::pair<TkID<128>,cTkSeed>,TkSTLAllocatorShim<std::pair<TkID<128>,cTkSeed>,8,-1> > *",
            "cGcScanEventManager *, const std::pair<TkID<128>,cTkSeed> *",
        ]
    class AddEvent:
        overloads = Literal[
            "cGcScanEventManager *, cGcScanEventManager::AddEventResult *, eScanTable, const TkID<256> *, float, bool",
            "cGcScanEventManager *, eSignalScanType",
            "cGcScanEventManager *, cGcScanEventManager::AddEventResult *, eScanTable, cGcScanEventData *, cGcPlayerMissionParticipant *, bool, float, std::pair<TkID<128>,cTkSeed> *, unsigned __int64 *, bool, bool",
        ]

class cGcDroneComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcDiscoveryRecord:
    class cGcDiscoveryRecord:
        overloads = Literal[
            "cGcDiscoveryRecord *, const cGcDiscoveryData *",
            "cGcDiscoveryRecord *",
        ]

class cGcCreatureComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]
    class GetFeedingProduct:
        overloads = Literal[
            "cGcCreatureComponent *, TkID<128> *",
            "TkID<128> *, unsigned __int64, unsigned __int64, bool",
        ]

class cGcAISpaceshipComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcCharacterCustomisationData:
    class cGcCharacterCustomisationData:
        overloads = Literal[
            "cGcCharacterCustomisationData *",
            "cGcCharacterCustomisationData *, const cGcCharacterCustomisationData *",
        ]

class cGcMaintenanceComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcExpeditionHologramComponent:
    class GetTypedComponent:
        overloads = Literal[
            "int",
            "cTkAttachment *",
        ]

class cGcFleetExpedition:
    class cGcFleetExpedition:
        overloads = Literal[
            "cGcFleetExpedition *",
            "cGcFleetExpedition *, const cGcFleetExpedition *",
        ]
    class Load:
        overloads = Literal[
            "cGcFleetExpedition *, cGcPlayerFleetManager *, const cGcFleetExpeditionSaveData *",
            "cGcFleetExpedition *, const cGcPlayerFleetManager *, const cGcNetworkFleetExpeditionsSyncMessage *, int, int",
        ]

class cGcGameState:
    class GetPlayerFreighterOwnership:
        overloads = Literal[
            "cGcGameState *, int",
            "cGcGameState *, const cTkUserIdBase<cTkFixedString<64,char> > *",
        ]
    class GetPlayerFleetManagerWriteable:
        overloads = Literal[
            "cGcGameState *, int",
            "cGcGameState *, const cTkUserIdBase<cTkFixedString<64,char> > *, bool",
        ]

class sOwnedCreatureInfo:
    class sOwnedCreatureInfo:
        overloads = Literal[
            "sOwnedCreatureInfo *, const sOwnedCreatureInfo *",
            "sOwnedCreatureInfo *",
        ]

class cGcPlayerState:
    class TryRemoveFromInventories:
        overloads = Literal[
            "cGcPlayerState *, const std::vector<enum InventoryChoice,TkSTLAllocatorShim<enum InventoryChoice,4,-1> > *, const cGcInventoryElement *, TryStoreMode",
            "cGcPlayerState *, const std::vector<enum InventoryChoice,TkSTLAllocatorShim<enum InventoryChoice,4,-1> > *, const cGcInventoryElement *, std::vector<enum InventoryChoice,TkSTLAllocatorShim<enum InventoryChoice,4,-1> > *",
        ]
    class FindExistingSettlementState:
        overloads = Literal[
            "cGcPlayerState *, const unsigned __int64, const cTkVector3 *, const float",
            "cGcPlayerState *, const unsigned __int64, const unsigned __int64",
        ]
    class TryStoreInCurrentInventory:
        overloads = Literal[
            "cGcPlayerState *, const cGcRealitySubstanceData *, int, TryStoreMode",
            "cGcPlayerState *, const cGcProductData *, int, TryStoreMode",
            "cGcPlayerState *, const cGcInventoryElement *, int, TryStoreMode",
        ]
    class TryStoreInInventory_Internal:
        overloads = Literal[
            "cGcPlayerState *, int, const cGcInventoryElement *, cGcInventoryIndex, TryStoreMode",
            "cGcPlayerState *, cGcInventoryStore *, const cGcInventoryElement *, cGcInventoryIndex, TryStoreMode, bool",
        ]
    class TryStoreInInventory:
        overloads = Literal[
            "cGcPlayerState *, int, const cGcInventoryElement *, cGcInventoryIndex, TryStoreMode",
            "cGcPlayerState *, int, const cGcRealitySubstanceData *, int, TryStoreMode",
            "cGcPlayerState *, int, const cGcProductData *, int, TryStoreMode",
        ]
    class QueryAmountInInventory:
        overloads = Literal[
            "cGcPlayerState *, const InventoryChoice, const cGcInventoryElement *, bool, bool, int",
            "cGcPlayerState *, int, const eProceduralProductCategory, const eRarity",
        ]
    class QueryAmountInAllInventories:
        overloads = Literal[
            "cGcPlayerState *, const cGcInventoryElement *, bool, bool, bool, bool",
            "cGcPlayerState *, const eProceduralProductCategory, const eRarity",
            "cGcPlayerState *, const TkID<128> *, bool, bool, bool",
        ]
    class CanRepairTechnology:
        overloads = Literal[
            "cGcPlayerState *, const cGcInventoryStore *, const InventoryChoice, const cGcInventoryIndex *, const bool",
            "cGcPlayerState *, const cGcInventoryElement *, const InventoryChoice, const bool",
        ]
    class DismantleTechnology:
        overloads = Literal[
            "cGcPlayerState *, cGcInventoryStore *, cGcInventoryStore *, const cGcInventoryElement *, const cGcInventoryIndex *, int",
            "cGcPlayerState *, int, const cGcInventoryElement *, const cGcInventoryIndex *",
        ]
    class GetInventoriesFor:
        overloads = Literal[
            "cGcPlayerState *, int, std::vector<enum InventoryChoice,TkSTLAllocatorShim<enum InventoryChoice,4,-1> > *, bool",
            "cGcPlayerState *, InventoryChoice, std::vector<enum InventoryChoice,TkSTLAllocatorShim<enum InventoryChoice,4,-1> > *",
        ]
    class ChargeAllowed:
        overloads = Literal[
            "cGcPlayerState *, const cGcTechnology *, const cGcRealitySubstanceData *",
            "cGcPlayerState *, const cGcTechnology *, const cGcProductData *",
        ]
    class GetElementAdjacencyBonusAmount:
        overloads = Literal[
            "cGcPlayerState *, const cGcInventoryStore *, const cGcInventoryElement *, AdjacencyBonus",
            "cGcPlayerState *, const cGcInventoryStore *, const cGcInventoryElement *, const cGcStatsBonus *, AdjacencyBonus",
        ]
    class GetPrimaryItemForStat:
        overloads = Literal[
            "cGcPlayerState *, eStatsType, InventoryChoice, ItemLookupType, int",
            "cGcPlayerState *, eStatsType, const cGcInventoryStore *, ItemLookupType",
        ]
    class AwardTechnology:
        overloads = Literal[
            "cGcPlayerState *, const cGcTechnology *, bool, bool",
            "cGcPlayerState *, const TkID<128> *, bool, bool",
        ]
    class GetTeleportEndpointsVector:
        overloads = Literal[
            "cGcPlayerState *, eTeleporterType, const cGcTeleportEndpoint *, std::vector<cGcTeleportEndpoint,TkSTLAllocatorShim<cGcTeleportEndpoint,16,-1> > *, float, bool",
            "cGcPlayerState *, const std::vector<enum eTeleporterType,TkSTLAllocatorShim<enum eTeleporterType,4,-1> > *, const cGcTeleportEndpoint *, std::vector<cGcTeleportEndpoint,TkSTLAllocatorShim<cGcTeleportEndpoint,16,-1> > *, float, bool",
        ]

class cGcInventoryStore:
    class cGcInventoryStore:
        overloads = Literal[
            "cGcInventoryStore *",
            "cGcInventoryStore *, cGcInventoryStore *",
            "cGcInventoryStore *, const cGcInventoryStore *",
        ]
    class GenerateProceduralInventory:
        overloads = Literal[
            "cGcInventoryStore *, unsigned int, const cTkSeed *, int, eSizeType, eWeaponStatClass, LayoutGenerationMode, LayoutCompareGenerationType, eInventoryClass, std::vector<cGcInventoryTechProbability,TkSTLAllocatorShim<cGcInventoryTechProbability,8,-1> > *",
            "cGcInventoryStore *, std::vector<cGcInventoryTechProbability,TkSTLAllocatorShim<cGcInventoryTechProbability,8,-1> > *, TkHandle, const cTkSeed *, int, LayoutGenerationMode, LayoutCompareGenerationType, eInventoryClass",
        ]

class cGcMPMissionSelectionHelper:
    class HasMissionStarted:
        overloads = Literal[
            "cGcMPMissionSelectionHelper *, const cTkUserIdBase<cTkFixedString<64,char> > *",
            "cGcMPMissionSelectionHelper *, const TkID<128> *, const cTkSeed *",
        ]

class cGcDestructableComponent:
    class GetTypedComponent:
        overloads = Literal[
            "int",
            "cTkAttachment *",
        ]
    class Destroy:
        overloads = Literal[
            "cGcDestructableComponent *",
            "cGcDestructableComponent *, eDestroyedBy, const cTkUserIdBase<cTkFixedString<64,char> > *",
            "cGcDestructableComponent *, const cGcProjectileImpact *",
        ]

class cGcPlayerBasePersistentBuffer:
    class cGcPlayerBasePersistentBuffer:
        overloads = Literal[
            "cGcPlayerBasePersistentBuffer *",
            "cGcPlayerBasePersistentBuffer *, cGcPlayerBasePersistentBuffer *",
        ]
    class PlayerBasePersistentData:
        class PlayerBasePersistentData:
            overloads = Literal[
                "cGcPlayerBasePersistentBuffer::PlayerBasePersistentData *",
                "cGcPlayerBasePersistentBuffer::PlayerBasePersistentData *, const cGcPersistentBaseEntry *",
            ]

class cGcPlayerByteBeatLibrary:
    class RemoveFromPlaylist:
        overloads = Literal[
            "cGcPlayerByteBeatLibrary *, int",
            "cGcPlayerByteBeatLibrary *, const TkID<128> *",
        ]

class cGcPlayerCreatureOwnership:
    class GetMoodValue:
        overloads = Literal[
            "cGcPlayerCreatureOwnership *, int, ePetMood, bool",
            "cGcPlayerCreatureOwnership *, ePetMood, bool",
        ]

class cGcPlayerFleetManager:
    class IsPointInsideFrigate:
        overloads = Literal[
            "cGcPlayerFleetManager *, const cTkVector3 *, const cGcFleetFrigate *, float",
            "cGcPlayerFleetManager *, const cTkVector3 *, const cGcFleetFrigate **",
        ]

class cGcPlayerFreighterOwnership:
    class RequestFreighterSpawn:
        overloads = Literal[
            "cGcPlayerFreighterOwnership *",
            "cGcPlayerFreighterOwnership *, const cTkMatrix34 *, const cGcUniverseAddressData *, float",
        ]

class cGcExperienceSpawn:
    class cGcExperienceSpawn:
        overloads = Literal[
            "cGcExperienceSpawn *, cGcExperienceSpawn *",
            "cGcExperienceSpawn *",
        ]

class cGcPortalComponent:
    class GetTypedComponent:
        overloads = Literal[
            "int",
            "cTkAttachment *",
        ]

class cGcShootableComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcLootComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcPlayerExperienceDirector:
    class ValidShipSpawn:
        overloads = Literal[
            "cGcPlayerExperienceDirector *, const cTkVector3 *",
            "cGcPlayerExperienceDirector *, const cTkVector3 *, float *",
        ]
    class GetCreatureResource:
        overloads = Literal[
            "cGcPlayerExperienceDirector *, TkStrongType<int,TkStrongTypeIDs::TkResHandleID> *, eCreatureType",
            "cGcPlayerExperienceDirector *, TkStrongType<int,TkStrongTypeIDs::TkResHandleID> *, const TkID<128> *",
        ]
    class StartFrigateFlyby:
        overloads = Literal[
            "cGcPlayerExperienceDirector *, const sFrigateFlybyRequest *",
            "cGcPlayerExperienceDirector *",
        ]

class cTkAnimationComponent:
    class SetAnimSpeed:
        overloads = Literal[
            "cTkAnimationComponent *, float, const TkID<128> *",
            "cTkAnimationComponent *, float, const cTkAnimInstanceHandle *",
        ]
    class SetAnimTime:
        overloads = Literal[
            "cTkAnimationComponent *, float, const TkID<128> *",
            "cTkAnimationComponent *, float, const cTkAnimInstanceHandle *",
        ]
    class GetAnimLength:
        overloads = Literal[
            "cTkAnimationComponent *, const TkID<128> *",
            "cTkAnimationComponent *, const cTkAnimInstanceHandle *",
        ]
    class GetAnimTime:
        overloads = Literal[
            "cTkAnimationComponent *, const cTkAnimInstanceHandle *",
            "cTkAnimationComponent *, const TkID<128> *",
        ]
    class GetAnimActionFrame:
        overloads = Literal[
            "cTkAnimationComponent *, const TkID<128> *",
            "cTkAnimationComponent *, const cTkAnimInstanceHandle *",
        ]
    class GetLocatorForAnim:
        overloads = Literal[
            "cTkAnimationComponent *, const TkID<128> *, const TkID<128> *, float, bool, cTkVector3 *, cTkQuaternion *",
            "cTkAnimationComponent *, const cTkAnimInstanceHandle *, const TkID<128> *, float, bool, cTkVector3 *, cTkQuaternion *",
        ]
    class IsAnimActive:
        overloads = Literal[
            "cTkAnimationComponent *, const TkID<128> *, bool",
            "cTkAnimationComponent *, const cTkAnimLayerHandle *, bool, bool",
        ]
    class Stop:
        overloads = Literal[
            "cTkAnimationComponent *, const TkID<128> *, float, eCurve",
            "cTkAnimationComponent *, const cTkAnimLayerHandle *, float, eCurve",
        ]

class cGcPlayerVehicleOwnership:
    class GetPlayerVehicleName:
        overloads = Literal[
            "cGcPlayerVehicleOwnership *",
            "cGcPlayerVehicleOwnership *, eVehicleType",
        ]

class cGcRealitySubstanceData:
    class cGcRealitySubstanceData:
        overloads = Literal[
            "cGcRealitySubstanceData *, const cGcRealitySubstanceData *",
            "cGcRealitySubstanceData *, cGcRealitySubstanceData *",
        ]

class cGcProductData:
    class cGcProductData:
        overloads = Literal[
            "cGcProductData *, const cGcProductData *",
            "cGcProductData *, cGcProductData *",
        ]

class cGcTechnology:
    class cGcTechnology:
        overloads = Literal[
            "cGcTechnology *, const cGcTechnology *",
            "cGcTechnology *, cGcTechnology *",
        ]

class cGcProceduralMaterialMapping:
    class cGcProceduralMaterialMapping:
        overloads = Literal[
            "cGcProceduralMaterialMapping *, const cGcProceduralMaterialMapping *",
            "cGcProceduralMaterialMapping *",
        ]

class cGcCameraManager:
    class GetScreenPos:
        overloads = Literal[
            "cGcCameraManager *, cTkVector3 *, const cTkVector3 *, const cTkVector2 *",
            "cGcCameraManager *, cTkVector3 *, const cTkPhysRelVec3 *, const cTkVector2 *",
        ]

class cGcDiscoveryPageData:
    class DiscoveryPageInfoBase:
        class DiscoveryPageInfoBase:
            overloads = Literal[
                "cGcDiscoveryPageData::DiscoveryPageInfoBase *, const cGcDiscoveryPageData::DiscoveryPageInfoBase *",
                "cGcDiscoveryPageData::DiscoveryPageInfoBase *, const char *, const char *, const cTkFixedString<3,char> *, const cGcDiscoveryData *, const int",
            ]

class cGcPlayer:
    class AdjustPositionForRespawn:
        overloads = Literal[
            "cGcPlayer *, cTkVector3 *, const cTkVector3 *, bool",
            "cGcPlayer *, cTkPhysRelVec3 *, const cTkPhysRelVec3 *, bool",
        ]
    class TakeDamage:
        overloads = Literal[
            "cGcPlayer *, const TkID<128> *, const TkID<128> *, const cTkVector3 *, float",
            "cGcPlayer *, const TkID<128> *, const TkID<128> *, float",
            "cGcPlayer *, const TkID<128> *, const TkID<128> *, const cTkVector3 *, cGcOwnerConcept *, float, const std::vector<cGcCombatEffectDamageMultiplier,TkSTLAllocatorShim<cGcCombatEffectDamageMultiplier,4,-1> > *",
            "cGcPlayer *, float, eDamageType, const TkID<128> *, const cTkVector3 *, cGcOwnerConcept *, const std::vector<cGcCombatEffectDamageMultiplier,TkSTLAllocatorShim<cGcCombatEffectDamageMultiplier,4,-1> > *",
        ]
    class SetToPosition:
        overloads = Literal[
            "cGcPlayer *, const cTkVector3 *, const cTkVector3 *, const cTkVector3 *",
            "cGcPlayer *, const cTkPhysRelVec3 *, const cTkVector3 *, const cTkVector3 *",
        ]
    class ThrowCreatureFood:
        overloads = Literal[
            "cGcPlayer *, TkID<128>, cGcCreatureComponent *",
            "cGcPlayer *, TkID<128> *, cTkVector3 *, cTkVector3 *, cGcCreatureComponent *",
        ]
    class SummonPet:
        overloads = Literal[
            "cGcPlayer *, unsigned int",
            "cGcPlayer *, unsigned int, const cTkMatrix34 *, eCreatureType, float, float, cTkSmartResHandle *, cTkSeed *, TkHandle",
        ]
    class IsRidingCreature:
        overloads = Literal[
            "cGcPlayer *, bool",
            "cGcPlayer *, cGcCreatureComponent *",
        ]

class cGcFrontendPageFunctions:
    class SetIconImage:
        overloads = Literal[
            "cGcNGuiLayer *, const cTkTextureResource *, const cTkColour *",
            "cGcNGuiLayer *, const TkStrongType<int,TkStrongTypeIDs::TkResHandleID> *, const cTkColour *",
        ]
    class SetColour:
        overloads = Literal[
            "cTkNGuiGraphicStyle *, const cTkColour *, bool",
            "cTkNGuiTextStyle *, const cTkColour *, bool",
        ]
    class SetQuantityBar:
        overloads = Literal[
            "cGcNGuiLayer *, const cGcInventoryElement *, eQuantityBarType, bool",
            "cGcNGuiLayer *, float, const cTkColour *, const cTkTextureResource *",
            "cGcNGuiLayer *, const char *, int, int, const cTkColour *, eQuantityBarType, const char *, const cTkTextureResource *",
        ]
    class DoCrossplayPlatform:
        overloads = Literal[
            "cGcNGuiLayer *, const cTkFixedString<64,char> *",
            "cGcNGuiLayer *, cGcNetworkConstants::OnlinePlatformType",
        ]
    class DoSingleInventorySlot:
        overloads = Literal[
            "cGcFrontendPage *, cGcNGuiLayer *, cGcInventoryStore *, const cGcInventoryIndex *, int, std::vector<enum ePopupAction,TkSTLAllocatorShim<enum ePopupAction,4,-1> > *, bool, bool, bool",
            "cGcFrontendPage *, cGcNGuiLayer *, cGcInventoryStore *, const cGcInventoryIndex *, const cGcInventoryElement *, int, std::vector<enum ePopupAction,TkSTLAllocatorShim<enum ePopupAction,4,-1> > *, bool, bool, bool",
        ]

class cGcNGuiElement:
    class SetPosition:
        overloads = Literal[
            "cGcNGuiElement *, float, float, cGcNGuiElement::PositionType",
            "cGcNGuiElement *, const cTkVector2 *, cGcNGuiElement::PositionType",
        ]

class cGcNGuiText:
    class SetText:
        overloads = Literal[
            "cGcNGuiText *, const TkID<256> *",
            "cGcNGuiText *, const char *",
        ]

class cGcAlienPuzzleOption:
    class cGcAlienPuzzleOption:
        overloads = Literal[
            "cGcAlienPuzzleOption *, const cGcAlienPuzzleOption *",
            "cGcAlienPuzzleOption *, cGcAlienPuzzleOption *",
        ]

class cGcEggMachineComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcFrontendPageInteractions:
    class TeleporterNexusEndpoint:
        class TeleporterNexusEndpoint:
            overloads = Literal[
                "cGcFrontendPageInteractions::TeleporterNexusEndpoint *",
                "cGcFrontendPageInteractions::TeleporterNexusEndpoint *, const cGcFrontendPageInteractions::TeleporterNexusEndpoint *",
            ]

class cGcRealityManager:
    class GetAlienPuzzle:
        overloads = Literal[
            "cGcRealityManager *, const TkID<256> *, eInteractionType, eAlienRace, cTkSeed",
            "cGcRealityManager *, const TkID<256> *, eInteractionType, eAlienRace, std::vector<enum eAlienPuzzleCategory,TkSTLAllocatorShim<enum eAlienPuzzleCategory,4,-1> > *, cTkSeed",
            "cGcRealityManager *, const TkID<256> *, cTkSeed",
        ]
    class GenerateProceduralProduct:
        overloads = Literal[
            "cGcRealityManager *, eProceduralProductCategory, const cTkSeed *, eRarity, eQuality",
            "cGcRealityManager *, const TkID<128> *",
        ]
    class GenerateProceduralTechnologyID:
        overloads = Literal[
            "cGcRealityManager *, TkID<128> *, eProceduralTechnologyCategory, const cTkSeed *",
            "cGcRealityManager *, TkID<128> *, const TkID<128> *, const cTkSeed *",
        ]

class cTkNGuiStyles:
    class Blend:
        overloads = Literal[
            "cTkNGuiTextStyleData *, cTkNGuiTextStyleData *, cTkNGuiTextStyleData *, float",
            "cTkNGuiGraphicStyleData *, cTkNGuiGraphicStyleData *, cTkNGuiGraphicStyleData *, float",
        ]
    class RenderText:
        overloads = Literal[
            "cTkNGui *, void *, const char *, cTkBBox2d *, eNGuiInputType, cTkNGuiElementData *",
            "cTkNGui *, cTkNGuiElementData *, cTkNGuiTextStyleData *, const char *, float, float, float, float",
            "cTkNGui *, cTkNGuiTextStyleData *, const char *, cTkBBox2d *, cTkNGuiElementData *",
        ]
    class CopyChanges:
        overloads = Literal[
            "cTkNGuiGraphicStyleData *, cTkNGuiGraphicStyleData *, cTkNGuiGraphicStyleData *",
            "cTkNGuiTextStyleData *, cTkNGuiTextStyleData *, cTkNGuiTextStyleData *",
        ]
    class RenderGraphic:
        overloads = Literal[
            "cTkNGui *, cTkNGuiGraphicStyleData *, cTkBBox2d *",
            "cTkNGui *, void *, cTkBBox2d *, eNGuiInputType, cTkNGuiElementData *",
        ]

class cGcNGuiGame:
    class PushStyle:
        overloads = Literal[
            "cGcNGuiGame *, eNGuiGameTextType, cTkNGuiTextStyle *",
            "cGcNGuiGame *, eNGuiGameGraphicType, cTkNGuiGraphicStyle *",
        ]

class cGcMarkerRenderData:
    class Render:
        overloads = Literal[
            "void *",
            "void *, cTkVector2",
        ]

class cGcFrontendPageNetworkSettings:
    class DoPopupOption:
        overloads = Literal[
            "cGcFrontendPage *, cGcNGuiLayer *, cGcNGuiLayer *, int, const TkID<256> *",
            "cGcFrontendPage *, cGcNGuiLayer *, cGcNGuiLayer *, int, cTkFixedString<64,char> *, bool",
        ]

class ShopItemData:
    class Set:
        overloads = Literal[
            "ShopItemData *, const cGcRealitySubstanceData *",
            "ShopItemData *, const cGcProductData *",
            "ShopItemData *, const cGcTechnology *",
        ]
    class GeneratePrice:
        overloads = Literal[
            "ShopItemData *, const bool, const bool, const cTkSeed, const ShopItemData::eShopItemPriceType, const bool",
            "ShopItemData *, const bool, const bool, const float, const ShopItemData::eShopItemPriceType, const bool, const bool",
        ]

class cGcRewardManager:
    class GiveGenericReward:
        overloads = Literal[
            "cGcRewardManager *, const TkID<128> *, const TkID<128> *, const cTkSeed *, const bool, const bool, const bool, InventoryChoice, const bool",
            "cGcRewardManager *, const TkID<128> *, const TkID<128> *, const cTkSeed *, const bool, const bool, int *, const bool, int, const bool",
        ]
    class RewardTriggersExchange:
        overloads = Literal[
            "cGcRewardManager *, const TkID<128> *",
            "cGcRewardManager *, const cGcRewardTableItemList *, int *",
        ]

class cGcFrontendPageShop:
    class GenerateShopElement:
        overloads = Literal[
            "cGcInventoryElement *, const TkID<128> *, const eInventoryType, const cGcTradeData *, cGcInteractionComponent *, const int",
            "cGcInventoryElement *, const TkID<128> *, cGcTradingSupplyBuffer::TradingUA *, const eInventoryType, const cGcTradeData *, const int",
        ]

class cGcVehicleRaceInviteComponent:
    class GetTypedComponent:
        overloads = Literal[
            "int",
            "cTkAttachment *",
        ]

class cGcFrontendPage:
    class PickItem:
        overloads = Literal[
            "cGcFrontendPage *, const cGcInventoryIndex *, cGcInventoryStore *, ItemPicking::ActivationType",
            "cGcFrontendPage *, const cGcInventoryIndex *, int, int",
        ]

class cGcFrontendManager:
    class Activate:
        overloads = Literal[
            "cGcFrontendManager *",
            "cGcFrontendManager *, eFrontendPage, bool",
        ]

class cGcGraphicsManager:
    class SetShaderUniformDefault:
        overloads = Literal[
            "cGcGraphicsManager *, const char *, double, double, float, float",
            "cGcGraphicsManager *, unsigned __int64, double, double, float, float",
        ]

class cGcInWorldUIManager:
    class ApplyTransforms:
        overloads = Literal[
            "cTkPhysRelMat34 *, const cTkPhysRelMat34 *, const cGcInWorldUIScreenData *",
            "cTkPhysRelMat34 *, const cTkPhysRelMat34 *, const cTkVector3 *, double, const cTkVector3 *",
        ]
    class ActivateScreenAndClear:
        overloads = Literal[
            "cGcInWorldUIManager *, eInWorldScreens",
            "cGcInWorldUIManager *, cTkClassPoolHandle, __int64",
        ]
    class DeactivateScreen:
        overloads = Literal[
            "cGcInWorldUIManager *, eInWorldScreens",
            "cGcInWorldUIManager *, cTkClassPoolHandle",
        ]
    class GetRayUIQuadIntersectionPointAsScreenPos:
        overloads = Literal[
            "cGcInWorldUIManager *, eInWorldScreens, const cTkPhysRelVec3 *, const cTkPhysRelVec3 *, const cTkVector2 *, cTkVector2 *",
            "cGcInWorldUIManager *, const cTkPhysRelMat34 *, const cTkVector2 *, const cTkVector2 *, const cTkVector2 *, const cTkPhysRelVec3 *, const cTkPhysRelVec3 *, const cTkVector2 *, cTkVector2 *",
        ]
    class GetScreenMatrix:
        overloads = Literal[
            "cGcInWorldUIManager *, cTkPhysRelMat34 *, eInWorldScreens",
            "cGcInWorldUIManager *, cTkPhysRelMat34 *, cTkClassPoolHandle",
        ]

class cGcPlayerNotifications:
    class SetConstantMessage:
        overloads = Literal[
            "cGcPlayerNotifications *, int, bool, const cGcSlotIcon *, eFrontendPage, const TkID<256> *, const char *, const char *, unsigned int, bool",
            "cGcPlayerNotifications *, int, bool, const cGcInventoryElement *, eFrontendPage, const TkID<256> *, const char *, const char *, unsigned int, bool",
            "cGcPlayerNotifications *, int, bool, const cTkSmartResHandle *, eFrontendPage, const TkID<256> *, const char *, const char *, unsigned int, bool, eMessageCategory",
            "cGcPlayerNotifications *, int, bool, eFrontendPage, const TkID<256> *, const char *, const char *, unsigned int, bool, eMessageCategory",
        ]
    class SendMissionMessage:
        overloads = Literal[
            "cGcPlayerNotifications *, const TkID<128> *, bool, bool",
            "cGcPlayerNotifications *, const TkID<128> *, const TkID<128> *, const cTkSeed *, bool, bool",
            "cGcPlayerNotifications *, const TkID<128> *, const cTkSeed *, bool, bool",
        ]
    class SimpleMessage:
        class SimpleMessage:
            overloads = Literal[
                "cGcPlayerNotifications::SimpleMessage *, const cGcPlayerNotifications::SimpleMessage *",
                "cGcPlayerNotifications::SimpleMessage *, cGcPlayerNotifications::SimpleMessage *",
            ]

class cGcGenericSectionCondition:
    class EqualityText:
        overloads = Literal[
            "cGcGenericSectionCondition *, eEqualityEnum, __int64, cTkFixedString<1024,char> *",
            "cGcGenericSectionCondition *, eEqualityEnum, float, cTkFixedString<1024,char> *",
        ]
    class DebugText:
        overloads = Literal[
            "eConditionTest, std::vector<cGcGenericSectionCondition *,TkSTLAllocatorShim<cGcGenericSectionCondition *,8,-1> > *, eRepeatLogic, cTkFixedString<1024,char> *",
            "eConditionTest, std::vector<cGcGenericSectionCondition *,TkSTLAllocatorShim<cGcGenericSectionCondition *,8,-1> > *, eRepeatLogic, cTkFixedString<1024,char> *, std::vector<cTkFixedString<256,char>,TkSTLAllocatorShim<cTkFixedString<256,char>,1,-1> > *",
        ]

class cGcNotificationSequence:
    class GetMultiplayerMissionType:
        overloads = Literal[
            "const TkID<128> *, const cTkSeed *, const bool, const cGcGenericMissionSequence *",
            "cGcNotificationSequence *, const bool",
        ]

class cGcNotificationTextHelper:
    class GetMarkedUpItemString:
        overloads = Literal[
            "const TkID<128> *, cTkFixedString<256,char> *, bool",
            "const TkID<128> *, int, cTkFixedString<256,char> *",
        ]
    class GetMarkedUpItemStringWithIcon:
        overloads = Literal[
            "const TkID<128> *, cTkFixedString<256,char> *",
            "const TkID<128> *, int, cTkFixedString<256,char> *",
        ]

class cGcNotificationSequenceGroupCode:
    class cGcNotificationSequenceGroupCode:
        overloads = Literal[
            "cGcNotificationSequenceGroupCode *, const char *, const char *",
            "cGcNotificationSequenceGroupCode *, const char *, const TkID<128> *, const TkID<128> *",
        ]

class cGcNotificationSequenceCollect:
    class cGcNotificationSequenceCollect:
        overloads = Literal[
            "cGcNotificationSequenceCollect *, cGcMissionSequenceCollectSubstance *, const TkID<128> *, const cTkSeed *, const int",
            "cGcNotificationSequenceCollect *, cGcMissionSequenceCollectProduct *, const TkID<128> *, const cTkSeed *, const int",
        ]

class cGcNGuiLayer:
    class ConvertText:
        overloads = Literal[
            "cGcNGuiLayer *, cGcNGuiText *",
            "cGcNGuiLayer *, cGcNGuiTextSpecial *",
        ]

class cGcUndoableNGuiElementOperation:
    class cGcUndoableNGuiElementOperation:
        overloads = Literal[
            "cGcUndoableNGuiElementOperation *, cGcNGuiLayer *, cGcNGuiElement *, int, int",
            "cGcUndoableNGuiElementOperation *, cGcNGuiLayer *, cGcNGuiElement *, int",
            "cGcUndoableNGuiElementOperation *, cGcNGuiLayer *, cGcNGuiLayer *, cGcNGuiElement *, int",
        ]

class cGcNGuiEffectViewer:
    class EmitterData:
        class EmitterData:
            overloads = Literal[
                "cGcNGuiEffectViewer::EmitterData *, const cGcNGuiEffectViewer::EmitterData *",
                "cGcNGuiEffectViewer::EmitterData *, cGcNGuiEffectViewer::EmitterData *",
            ]

class cGcParticleManager:
    class AddPermanentEffect:
        overloads = Literal[
            "cGcParticleManager *, EffectInstance *, const TkID<128> *, const cTkMatrix34 *",
            "cGcParticleManager *, EffectInstance *, const TkID<128> *, TkHandle, const cTkMatrix34 *",
        ]
    class AddManagedEffect:
        overloads = Literal[
            "cGcParticleManager *, EffectInstance *, const TkID<128> *, const cTkMatrix34 *",
            "cGcParticleManager *, EffectInstance *, const TkID<128> *, TkHandle, const cTkMatrix34 *",
        ]

class cGcNetworkComponent:
    class SendAll:
        overloads = Literal[
            "cGcNetworkComponent *, unsigned __int8 *, unsigned int, float",
            "cGcNetworkComponent *, unsigned __int8 *, unsigned int, cGcNetworkComponentMessage::eType, unsigned __int16, float",
        ]

class cGcTextChatManager:
    class Say:
        overloads = Literal[
            "cGcTextChatManager *, const cTkFixedString<1023,char> *, bool",
            "cGcTextChatManager *, const cTkFixedString<1023,char> *, const cTkUserIdBase<cTkFixedString<64,char> > *, const std::vector<cTkUserIdBase<cTkFixedString<64,char> >,TkSTLAllocatorShim<cTkUserIdBase<cTkFixedString<64,char> >,1,-1> > *, bool, bool, bool, TextChatMessageType, const cTkColour *, int, float",
        ]

class cGcRichPresence:
    class StatChanged:
        overloads = Literal[
            "cGcRichPresence *, const TkID<128> *, __int64",
            "cGcRichPresence *, const TkID<128> *, long double",
        ]

class cGcNameGenerator:
    class GeneratePirateName:
        overloads = Literal[
            "cGcNameGenerator *, const unsigned __int64, cTkFixedString<127,char> *",
            "cGcNameGenerator *, const eAlienRace, const unsigned __int64, cTkFixedString<127,char> *",
        ]

class WikiItemData:
    class Set:
        overloads = Literal[
            "WikiItemData *, const cGcRealitySubstanceData *",
            "WikiItemData *, const cGcProductData *",
            "WikiItemData *, const cGcTechnology *, char",
            "WikiItemData *, const cGcStoneRuneData *",
            "WikiItemData *, const cGcRecipeWikiData *",
            "WikiItemData *, const cGcWikiTopic *",
            "WikiItemData *, const cGcAlienSpeechEntry *",
        ]

class cGcProceduralTechnologyData:
    class cGcProceduralTechnologyData:
        overloads = Literal[
            "cGcProceduralTechnologyData *, cGcProceduralTechnologyData *",
            "cGcProceduralTechnologyData *, const cGcProceduralTechnologyData *",
        ]

class cGcLocalPlayerCharacterInterface:
    class SetToPosition:
        overloads = Literal[
            "cGcLocalPlayerCharacterInterface *, const cTkVector3 *, const cTkVector3 *, const cTkVector3 *",
            "cGcLocalPlayerCharacterInterface *, const cTkPhysRelVec3 *, const cTkVector3 *, const cTkVector3 *",
        ]

class cGcAbandonedFreighterComponent:
    class GetTypedComponent:
        overloads = Literal[
            "cTkAttachment *",
            "int",
        ]

class cGcChairComponent:
    class Sit:
        overloads = Literal[
            "cGcChairComponent *, cGcCharacterSit *",
            "cGcChairComponent *, cGcCharacterSit *, TkHandle",
        ]

class cTkEulerVector:
    class cTkEulerVector:
        overloads = Literal[
            "cTkEulerVector *, const cTkQuaternion *",
            "cTkEulerVector *, const cTkMatrix34 *",
        ]

class cGcNPCComponent:
    class SetToPosition:
        overloads = Literal[
            "cGcNPCComponent *, const cTkVector3 *, const cTkVector3 *, const cTkVector3 *",
            "cGcNPCComponent *, const cTkPhysRelVec3 *, const cTkVector3 *, const cTkVector3 *",
            "cGcNPCComponent *, bool, const cTkPhysRelVec3 *, const cTkVector3 *, const cTkVector3 *",
        ]

class cGcMarkerPoint:
    class cGcMarkerPoint:
        overloads = Literal[
            "cGcMarkerPoint *, cGcMarkerPoint *",
            "cGcMarkerPoint *",
        ]
    class GetHorizonPosition:
        overloads = Literal[
            "cGcMarkerPoint *, cTkPhysRelVec3 *",
            "cGcMarkerPoint *, cTkPhysRelVec3 *, const cTkPhysRelVec3 *, int *",
        ]

class cGcTurretComponent:
    class MoveToFaceTarget:
        overloads = Literal[
            "cGcTurretComponent *, cTkAttachment *",
            "cGcTurretComponent *, const cTkVector3 *, cTkAttachment *",
        ]

class cTrackedNode:
    class cTrackedNode:
        overloads = Literal[
            "cTrackedNode *, TkHandle, int, int",
            "cTrackedNode *, const cTrackedNode *",
        ]

class cClothPiece:
    class cClothPiece:
        overloads = Literal[
            "cClothPiece *, cGcClothComponent *, cGcClothPiece *, TkVector_BoundChecked<cTkVector2> *, TkVector_BoundChecked<cTkVector3> *",
            "cClothPiece *, const cClothPiece *",
        ]
    class GetPointOfParameter:
        overloads = Literal[
            "cClothPiece *, cTkVector3 *, const cTrackedNodeWithData<cGcClothAttachmentCirlce> *, float, bool",
            "cClothPiece *, cTkVector3 *, const cTrackedNodeWithData<cGcClothAttachmentLine> *, double",
        ]
    class CalcClothMatrix:
        overloads = Literal[
            "cClothPiece *, cTkMatrix34 *, int, int",
            "cClothPiece *, cTkMatrix34 *, const cAttachedNode *",
        ]

class cGcFootConstraint:
    class cGcFootConstraint:
        overloads = Literal[
            "cGcFootConstraint *, const cGcFootConstraint *",
            "cGcFootConstraint *",
        ]

class cGcDungeonGenerationParams:
    class cGcDungeonGenerationParams:
        overloads = Literal[
            "cGcDungeonGenerationParams *, const cGcDungeonGenerationParams *",
            "cGcDungeonGenerationParams *, cGcDungeonGenerationParams *",
        ]

class cGcPlayerControlComponent:
    class UpdateControl:
        overloads = Literal[
            "cGcPlayerControlComponent *, float, float",
            "cGcPlayerControlComponent *, const cGcCharacterMove *, float",
            "cGcPlayerControlComponent *, const cGcCharacterRotate *, float",
        ]

class cGcMetadataBehaviour:
    class GetBlackboardOrDefaultValue:
        overloads = Literal[
            "cGcMetadataBehaviour *, cTkBlackboardDefaultValueBool *",
            "cGcMetadataBehaviour *, cTkBlackboardDefaultValueFloat *",
        ]

class cGcRegionKnowledge:
    class RoughHeightEstimate:
        overloads = Literal[
            "cGcRegionKnowledge *, const cTkVector3 *, int",
            "cGcRegionKnowledge *, int, int, const cTkVector3 *, int",
        ]

class cGcFadeNodeInstance:
    class cGcFadeNodeInstance:
        overloads = Literal[
            "cGcFadeNodeInstance *, const cGcFadeNodeInstance *",
            "cGcFadeNodeInstance *, cGcFadeNodeInstance *",
            "cGcFadeNodeInstance *, unsigned __int64",
        ]

class cGcMarkerList:
    class RemoveMarker:
        overloads = Literal[
            "cGcMarkerList *, int",
            "cGcMarkerList *, cGcMarkerPoint *",
        ]
    class TryAddMarker:
        overloads = Literal[
            "cGcMarkerList *, const cGcMarkerPoint *, bool, float, float, float, float, const cTkVector3 *",
            "cGcMarkerList *, const cGcMarkerPoint *, bool",
        ]

class sSolarDay:
    class GetRelativeSunAngle:
        overloads = Literal[
            "sSolarDay *, const cTkVector3 *, float",
            "float",
        ]

class cGcWeatherColourModifiers:
    class cGcWeatherColourModifiers:
        overloads = Literal[
            "cGcWeatherColourModifiers *, const cGcWeatherColourModifiers *",
            "cGcWeatherColourModifiers *, cGcWeatherColourModifiers *",
        ]

class cGcGalaxyAttributeGenerator:
    class ClassifyStarKeyAttributes:
        overloads = Literal[
            "const unsigned __int64, cGcGalaxyAttributeGenerator::StarSystemKeyAttributes *",
            "cTkParallelRNG *, unsigned __int16, cGcGalaxyVoxelAttributesData *, cGcGalaxyAttributeGenerator::StarSystemKeyAttributes *, unsigned __int64",
        ]

class cGcGalaxyMap:
    class Data:
        class GetScreenSpacePosition:
            overloads = Literal[
                "cGcGalaxyMap::Data *, cTkVector2 *, const cTkVector3 *, bool *",
                "cGcGalaxyMap::Data *, cTkVector2 *, const cTkPhysRelVec3 *, bool *",
            ]
        class DrawLine:
            overloads = Literal[
                "cGcGalaxyMap::Data *, const cTkPhysRelVec3 *, const cTkPhysRelVec3 *, const cTkColour *, float, bool",
                "cGcGalaxyMap::Data *, const cTkVector3 *, const cTkVector3 *, const cTkColour *, float, bool",
            ]

class cGcNavigation:
    class NavigateToPoint:
        overloads = Literal[
            "cGcNavigation *, const cTkPhysRelVec3 *, float",
            "cGcNavigation *, const cTkVector3 *, float",
        ]

class cGcNavMeshTile:
    class cGcNavMeshTile:
        overloads = Literal[
            "cGcNavMeshTile *",
            "cGcNavMeshTile *, cGcNavMeshTile *",
        ]

class cGcPlayerCommunicator:
    class RemoveSignal:
        overloads = Literal[
            "cGcPlayerCommunicator *, const TkID<256>",
            "cGcPlayerCommunicator *, const cTkAttachment *",
            "cGcPlayerCommunicator *",
        ]

class cGcMuzzleFlash:
    class Construct:
        overloads = Literal[
            "cGcMuzzleFlash *, const char *",
            "cGcMuzzleFlash *, const char *, const eRemoteWeaponType",
            "cGcMuzzleFlash *, cTkSmartResHandle *",
        ]

class cGcMechBehaviourTree:
    class Construct:
        overloads = Literal[
            "cGcMechBehaviourTree *, cTkAttachment *",
            "cGcMechBehaviourTree *, cTkAttachment *, cGcMechControl *, cGcMechAIController *, cGcWeapon *",
        ]

class cGcInstancedPhysicsAsteroidGrid:
    class NotifyDataChanged:
        overloads = Literal[
            "cGcInstancedPhysicsAsteroidGrid *",
            "cGcInstancedPhysicsAsteroidGrid *, int, int *, cTkMatrix44 *",
        ]

class cGcAsteroidPatternGenerator:
    class Generate:
        overloads = Literal[
            "const cGcAsteroidGeneratorRing *, cGcAsteroidLayout *, const cTkSphere *",
            "const cGcAsteroidGeneratorSurround *, cGcAsteroidLayout *, const cTkSphere *",
            "const cGcAsteroidGeneratorSlab *, cGcAsteroidLayout *, const cTkSphere *",
        ]

class cGcMap:
    class PickDecorationItems:
        overloads = Literal[
            "cGcMap *",
            "cGcMap *, eWFCDecorationTheme, std::vector<std::pair<cTkIntTuple3<int,0>,sSlotDecoration>,TkSTLAllocatorShim<std::pair<cTkIntTuple3<int,0>,sSlotDecoration>,8,-1> > *",
        ]

class cGcSlot:
    class IsBuildingEntrance:
        overloads = Literal[
            "cGcSlot *, eBlockDirection",
            "cGcSlot *",
        ]

class cGcPlanetGenerator:
    class RandomiseNoiseData:
        overloads = Literal[
            "cGcPlanetGenerator *, cTkNoiseUberLayerData *, cTkNoiseUberLayerData *, cTkNoiseUberLayerData *, cGcTerrainControls *",
            "cGcPlanetGenerator *, cTkNoiseGridData *, cTkNoiseGridData *, cTkNoiseGridData *, cGcTerrainControls *",
            "cGcPlanetGenerator *, cTkNoiseFeatureData *, cTkNoiseFeatureData *, cTkNoiseFeatureData *, cGcTerrainControls *",
        ]
    class UpdateProceduralTextureColours:
        overloads = Literal[
            "cGcPlanetGenerator *, std::vector<cGcPlanetObjectSpawnData,TkSTLAllocatorShim<cGcPlanetObjectSpawnData,8,-1> > *, cGcPlanetData *",
            "cGcPlanetGenerator *, cTkDynamicArray<cGcCreatureSpawnData> *, cGcPlanetData *",
        ]

class cGcPlanetObjectSpawnData:
    class cGcPlanetObjectSpawnData:
        overloads = Literal[
            "cGcPlanetObjectSpawnData *, cGcPlanetObjectSpawnData *",
            "cGcPlanetObjectSpawnData *, const cGcPlanetObjectSpawnData *",
        ]

class cGcShipAIBehaviour:
    class Travel:
        overloads = Literal[
            "cGcShipAIBehaviour *, const cTkVector3 *, const cGcSpaceshipTravelData *, const cTkVector3 *, cGcShipAIAvoidanceTracking *, bool, cTkRigidBody *",
            "cGcShipAIBehaviour *, const cTkVector3 *, const cGcSpaceshipTravelData *, cGcShipAIAvoidanceTracking *, bool, cTkRigidBody *",
        ]

class cGcAISpaceshipManager:
    class CacheHangar:
        overloads = Literal[
            "cGcAISpaceshipManager *, cTkModelResource *, const cGcPlanetColourData *, const cTkSeed *",
            "cGcAISpaceshipManager *, cGcPlayerFreighterOwnership *",
        ]

class cGcCarSuspensionAction:
    class TransformedMotion:
        class ApplyImpulseAtPoint:
            overloads = Literal[
                "cGcCarSuspensionAction::TransformedMotion *, const cTkVector3 *, const cTkVector3 *, double",
                "cGcCarSuspensionAction::TransformedMotion *, const cTkVector3 *, const cTkVector3 *, const cTkVector3 *",
            ]

class cGcInputRemap:
    class RemapAction:
        overloads = Literal[
            "cGcInputRemap *, eActionSetType, eInputAction, eInputButton",
            "cGcInputRemap *, eActionSetType, eInputAction, eInputAxis",
        ]

class cEgGeometryResource:
    class InsertElement:
        overloads = Literal[
            "cEgGeometryResource *, char *, int, const cTkVector2 *, const cTkVertexElement *",
            "cEgGeometryResource *, char *, int, const cTkVector3 *, const cTkVertexElement *",
            "cEgGeometryResource *, char *, int, const cTkVector4 *, const cTkVertexElement *",
        ]

class cEgCameraNode:
    class cEgCameraNode:
        overloads = Literal[
            "cEgCameraNode *, const cEgCameraNodeTemplate *",
            "cEgCameraNode *, const cEgCameraNode *",
        ]

class cEgSceneGraphResource:
    class GetBoundingBox:
        overloads = Literal[
            "cEgSceneGraphResource *, cTkAABB *, bool",
            "cEgSceneGraphResource *, cTkAABB *",
        ]

class Engine:
    class SetUniformArrayDefaultMultipleShaders:
        overloads = Literal[
            "TkStrongType<int,TkStrongTypeIDs::TkResHandleID> *, int, const char *, const float *, int",
            "TkStrongType<int,TkStrongTypeIDs::TkResHandleID> *, int, unsigned __int64, const float *, int",
        ]
    class GetNodeTransMats:
        overloads = Literal[
            "TkHandle, cTkMatrix34 *, cTkMatrix34 *",
            "TkHandle, VecIntrinsics::V128Matrix *, VecIntrinsics::V128Matrix *",
        ]
    class IterateNode:
        overloads = Literal[
            "TkHandle, cEgSceneNode *, __int64, __int64 *",
            "TkHandle, const char *, __int64, __int64 *",
        ]

class PCVoidVec4Param:
    class Set:
        overloads = Literal[
            "PCVoidVec4Param *, unsigned int, unsigned int, unsigned int, unsigned int",
            "PCVoidVec4Param *, float, float, float, float",
        ]

class PCID128Param:
    class PCID128Param:
        overloads = Literal[
            "PCID128Param *, const TkID<128> *",
            "PCID128Param *, const std::string *",
        ]

class cEgRenderTarget:
    class cEgRenderTarget:
        overloads = Literal[
            "cEgRenderTarget *",
            "cEgRenderTarget *, const cEgRenderTarget *",
            "cEgRenderTarget *, cEgRenderTarget *",
        ]

class cEgMaterialResource:
    class SetUniformArray:
        overloads = Literal[
            "cEgMaterialResource *, const char *, const float *, int",
            "cEgMaterialResource *, unsigned __int64, const float *, int",
        ]

class cEgShaderCombination:
    class cEgShaderCombination:
        overloads = Literal[
            "cEgShaderCombination *, cEgShaderCombination *",
            "cEgShaderCombination *, const cEgShaderCombination *",
        ]

class cEgCodeResource:
    class cEgCodeResource:
        overloads = Literal[
            "cEgCodeResource *, const cEgCodeResource *",
            "cEgCodeResource *, const std::basic_string<char,std::char_traits<char>,TkSTLAllocatorShim<char,1,-1> > *, int",
        ]

class cEgShaderContext:
    class cEgShaderContext:
        overloads = Literal[
            "cEgShaderContext *",
            "cEgShaderContext *, const cEgShaderContext *",
        ]

class cEgSceneNode:
    class cEgSceneNode:
        overloads = Literal[
            "cEgSceneNode *, const cEgSceneNode *",
            "cEgSceneNode *, const cEgSceneNodeTemplate *",
        ]

class cEgSceneManager:
    class FindType:
        overloads = Literal[
            "cEgSceneManager *, int",
            "cEgSceneManager *, const TkID<128> *",
        ]
    class IterateNode:
        overloads = Literal[
            "cEgSceneManager *, __int64, const char *, int, __int64 *",
            "cEgSceneManager *, __int64, unsigned int, int, __int64 *",
        ]

class cEgRenderBuffer:
    class cEgRenderBuffer:
        overloads = Literal[
            "cEgRenderBuffer *",
            "cEgRenderBuffer *, const cEgRenderBuffer *",
        ]

class XMLNode:
    class XMLNode:
        overloads = Literal[
            "XMLNode *, XMLNode::XMLNodeDataTag *, char *, char",
            "XMLNode *, const XMLNode *",
        ]
    class deleteAttribute:
        overloads = Literal[
            "XMLNode *, int",
            "XMLNode *, const char *",
        ]
    class nChildNode:
        overloads = Literal[
            "XMLNode *, const char *",
            "XMLNode *",
        ]
    class getChildNode:
        overloads = Literal[
            "XMLNode *, XMLNode *, const char *, int *",
            "XMLNode *, XMLNode *, const char *, int",
            "XMLNode *, XMLNode *, int",
        ]
    class getAttribute:
        overloads = Literal[
            "XMLNode *, const char *, int *",
            "XMLNode *, const char *, const char *",
        ]

class Json:
    class Value:
        class Value:
            overloads = Literal[
                "Json::Value *, int",
                "Json::Value *, unsigned int",
                "Json::Value *, long double",
                "Json::Value *, const char *",
                "Json::Value *, const std::string *",
                "Json::Value *, bool",
                "Json::Value *, const Json::Value *",
            ]
    class Reader:
        class decodeNumber:
            overloads = Literal[
                "Json::Reader *, Json::Reader::Token *",
                "Json::Reader *, Json::Reader::Token *, Json::Value *",
            ]
    class OurReader:
        class decodeString:
            overloads = Literal[
                "Json::Reader *, Json::Reader::Token *",
                "Json::Reader *, Json::Reader::Token *, std::string *",
            ]
        class decodeNumber:
            overloads = Literal[
                "Json::OurReader *, Json::OurReader::Token *",
                "Json::OurReader *, Json::OurReader::Token *, Json::Value *",
            ]
    class valueToString:
        overloads = Literal[
            "std::string *, __int64",
            "std::string *, unsigned __int64",
        ]

class TkLineRenderer:
    class AddLineImmediatePhysRel:
        overloads = Literal[
            "TkHandle, cTkPhysRelVec3 *, const cTkColour *, int, float",
            "TkHandle, cTkPhysRelVec3 *, cTkColour *, int, float",
        ]

class cTkMetaDataXML:
    class ReadElementXML:
        overloads = Literal[
            "cTkFixedString<128,char> *, XMLNode *, const char *",
            "cTkSeed *, XMLNode *, const char *",
            "TkID<256> *, XMLNode *, const char *",
            "TkID<128> *, XMLNode *, const char *",
            "cTkFixedString<32,char> *, XMLNode *, const char *",
            "cTkFixedString<64,char> *, XMLNode *, const char *",
            "cTkFixedString<256,char> *, XMLNode *, const char *",
            "cTkFixedString<1024,char> *, XMLNode *, const char *",
            "cTkFixedString<512,char> *, XMLNode *, const char *",
            "cTkFixedString<2048,char> *, XMLNode *, const char *",
            "cTkColour *, XMLNode *, const char *",
            "cTkHalfVector4 *, XMLNode *, const char *",
            "cTkVector2 *, XMLNode *, const char *",
            "cTkVector3 *, XMLNode *, const char *",
            "cTkVector4 *, XMLNode *, const char *",
        ]
    class WriteXML:
        overloads = Literal[
            "const float *, XMLNode *, const char *, bool, bool",
            "const bool *, XMLNode *, const char *, bool, bool",
            "const cTkSeed *, XMLNode *, const char *, bool, bool",
            "const int *, XMLNode *, const char *, bool, bool",
            "const char *, XMLNode *, const char *, bool, bool",
            "const unsigned __int64 *, XMLNode *, const char *, bool, bool",
            "const cTkColour *, XMLNode *, const char *, bool, bool",
            "const cTkHalfVector4 *, XMLNode *, const char *, bool, bool",
            "const cTkVector2 *, XMLNode *, const char *, bool, bool",
            "const cTkVector3 *, XMLNode *, const char *, bool, bool",
            "const cTkVector4 *, XMLNode *, const char *, bool, bool",
        ]
    class IsDefault:
        overloads = Literal[
            "const float *, const float *",
            "const cTkVector2 *, const cTkVector2 *",
            "const TkID<256> *, const TkID<256> *",
        ]

class cGcGenericMissionSequence:
    class cGcGenericMissionSequence:
        overloads = Literal[
            "cGcGenericMissionSequence *, cGcGenericMissionSequence *",
            "cGcGenericMissionSequence *, const cGcGenericMissionSequence *",
        ]

class cGcScanEventData:
    class cGcScanEventData:
        overloads = Literal[
            "cGcScanEventData *, cGcScanEventData *",
            "cGcScanEventData *, const cGcScanEventData *",
        ]

class cGcNPCDebugSpawnData:
    class cGcNPCDebugSpawnData:
        overloads = Literal[
            "cGcNPCDebugSpawnData *, cGcNPCDebugSpawnData *",
            "cGcNPCDebugSpawnData *, const cGcNPCDebugSpawnData *",
        ]

class cGcObjectSpawnData:
    class cGcObjectSpawnData:
        overloads = Literal[
            "cGcObjectSpawnData *, cGcObjectSpawnData *",
            "cGcObjectSpawnData *, const cGcObjectSpawnData *",
        ]

class cGcRewardTableItemList:
    class cGcRewardTableItemList:
        overloads = Literal[
            "cGcRewardTableItemList *",
            "cGcRewardTableItemList *, const cGcRewardTableItemList *",
        ]

class hkMemory:
    class memCheck4:
        overloads = Literal[
            "const void *, const int, unsigned __int64, unsigned __int64, unsigned __int64 *",
            "const void *, const int, unsigned __int64, unsigned __int64 *",
        ]
    class Detail:
        class FwdToSharedAllocator:
            class malloc:
                overloads = Literal[
                    "hkMemory::Detail::FwdToSharedAllocator *, unsigned __int64",
                    "hkMemory::Detail::FwdToSharedAllocator *, unsigned __int64, unsigned __int64 *",
                ]

class hkCriticalSection:
    class hkCriticalSection:
        overloads = Literal[
            "hkCriticalSection *",
            "hkCriticalSection *, int",
        ]

class hkTransformf:
    class setMulInverseMul:
        overloads = Literal[
            "hkTransformf *, const hkTransformf *, const hkTransformf *",
            "hkTransformf *, const hkPreciseTransform *, const hkPreciseTransform *",
        ]

class hkQuaternionf:
    class setAxisAngle:
        overloads = Literal[
            "hkQuaternionf *, const hkVector4f *, const hkSimdFloat32 *",
            "hkQuaternionf *, const hkVector4f *, float",
        ]
    class setUsingEulerAngles:
        overloads = Literal[
            "hkQuaternionf *, float, float, float",
            "hkQuaternionf *, hkQuaternionAxisOrder, const hkSimdFloat32 *, const hkSimdFloat32 *, const hkSimdFloat32 *",
        ]

class toString:
    overloads = Literal[
        "const hkMpRational *, unsigned int, hkStringBuf *",
        "const hkMpUint *, unsigned int, hkStringBuf *",
    ]

class hkGeometry:
    class hkGeometry:
        overloads = Literal[
            "hkGeometry *, const hkGeometry *",
            "hkGeometry *",
        ]

class hkRefCountedProperties:
    class hkRefCountedProperties:
        overloads = Literal[
            "hkRefCountedProperties *, const hkRefCountedProperties *",
            "hkRefCountedProperties *",
        ]

class hkSignal:
    class unsubscribeInternal:
        overloads = Literal[
            "hkSignal *, hkBool *, void *, const void *, int",
            "hkSignal *, hkBool *, void *, const void *, int, const char *, int",
        ]

class hkVector4f:
    class setRotatedDir:
        overloads = Literal[
            "hkVector4f *, const hkMatrix3Impl<float> *, const hkVector4f *",
            "hkVector4f *, const hkQuaternionf *, const hkVector4f *",
        ]
    class setRotatedInverseDir:
        overloads = Literal[
            "hkVector4f *, const hkMatrix3Impl<float> *, const hkVector4f *",
            "hkVector4f *, const hkQuaternionf *, const hkVector4f *",
        ]
    class setTransformedInversePos:
        overloads = Literal[
            "hkVector4f *, const hkQTransformf *, const hkVector4f *",
            "hkVector4f *, const hkTransformf *, const hkVector4f *",
        ]
    class setTransformedPos:
        overloads = Literal[
            "hkVector4f *, const hkPreciseTransform *, const hkVector4f *",
            "hkVector4f *, const hkQTransformf *, const hkVector4f *",
            "hkVector4f *, const hkQsTransformf *, const hkVector4f *",
            "hkVector4f *, const hkTransformf *, const hkVector4f *",
        ]

class hkLog:
    class formatLogMessage:
        overloads = Literal[
            "const hkLog::Message *, hkIo::WriteBuffer *, int, bool",
            "const hkLog::Message *, hkStringBuf *, int, bool",
        ]

class hkFileSystem:
    class _handleFlags:
        overloads = Literal[
            "hkFileSystem *, hkStreamReader *, hkFileSystem::OpenFlags",
            "hkFileSystem *, hkStreamWriter *, hkFileSystem::OpenFlags",
        ]

class hkStackTracer:
    class dumpStackTrace:
        overloads = Literal[
            "hkStackTracer *, const unsigned __int64 *, int, __int64 *, void *",
            "hkStackTracer *, const unsigned __int64 *, int, char *, unsigned __int64",
        ]

class hkAttributeParser:
    class currentAttrName:
        overloads = Literal[
            "hkAttributeParser *, hkStringBuf *, hkStringBuf *",
            "hkAttributeParser *, hkStringView *, hkStringBuf *, hkStringBuf *",
        ]

class hkUtf8:
    class Utf8FromWide:
        class Utf8FromWide:
            overloads = Literal[
                "hkUtf8::Utf8FromWide *, const wchar_t *",
                "hkUtf8::Utf8FromWide *, const wchar_t *, unsigned __int64",
            ]
    class WideFromUtf8:
        class WideFromUtf8:
            overloads = Literal[
                "hkUtf8::WideFromUtf8 *, const hkStringBuf *",
                "hkUtf8::WideFromUtf8 *, const char *",
                "hkUtf8::WideFromUtf8 *, const char *, unsigned __int64",
            ]

class hkDetail:
    class Func:
        class FuncBase:
            class FuncBase:
                overloads = Literal[
                    "hkDetail::Func::FuncBase *, hkDetail::Func::FuncBase *",
                    "hkDetail::Func::FuncBase *, unsigned __int64, unsigned __int64, void *, __int64 *",
                ]

class hkDefaultTaskQueue:
    class processUntilFinished:
        overloads = Literal[
            "hkDefaultTaskQueue *, struct hkTaskQueue::_Handle **, int",
            "hkDefaultTaskQueue *, struct hkTaskQueue::_Handle *",
        ]

class hkBufferedStreamWriter:
    class hkBufferedStreamWriter:
        overloads = Literal[
            "hkBufferedStreamWriter *, hkStreamWriter *, int",
            "hkBufferedStreamWriter *, void *, int, hkBool",
        ]

class hkDefaultError:
    class hkDefaultError:
        overloads = Literal[
            "hkDefaultError *, __int64 *, void *",
            "hkDefaultError *",
        ]

class hkFreeList:
    class hkFreeList:
        overloads = Literal[
            "hkFreeList *",
            "hkFreeList *, unsigned __int64, unsigned __int64, unsigned __int64, const hkContainerAllocator *, const hkContainerAllocator *",
        ]

class hkThreadLocalBlockStreamAllocator:
    class hkThreadLocalBlockStreamAllocator:
        overloads = Literal[
            "hkThreadLocalBlockStreamAllocator *, hkBlockStreamAllocator *",
            "hkThreadLocalBlockStreamAllocator *, hkBlockStreamAllocator *, int",
        ]

class hknp6DofConstraintData:
    class hknp6DofConstraintData:
        overloads = Literal[
            "hknp6DofConstraintData *, const hknp6DofConstraintData *",
            "hknp6DofConstraintData *",
        ]

class hknpBodyQualityLibrary:
    class hknpBodyQualityLibrary:
        overloads = Literal[
            "hknpBodyQualityLibrary *, const hknpBodyQualityLibrary *",
            "hknpBodyQualityLibrary *",
        ]

class hknpCharacterProxy:
    class hknpCharacterProxy:
        overloads = Literal[
            "hknpCharacterProxy *, const hknpCharacterProxy *",
            "hknpCharacterProxy *, const hknpCharacterProxyCinfo *",
        ]

class hknpCompoundShapeData:
    class hknpCompoundShapeData:
        overloads = Literal[
            "hknpCompoundShapeData *, const hknpCompoundShapeData *",
            "hknpCompoundShapeData *, hknpCompoundShapeBoundingVolumeType::Enum",
        ]

class hknpCompressedMeshShape:
    class hknpCompressedMeshShape:
        overloads = Literal[
            "hknpCompressedMeshShape *, const hknpCompressedMeshShape *",
            "hknpCompressedMeshShape *, const hknpCompressedMeshShape *, hknpShape::CloneMode, hknpShapeMap *",
            "hknpCompressedMeshShape *, const hknpCompressedMeshShapeCinfo *",
        ]

class hknpFirstPersonGun:
    class hknpFirstPersonGun:
        overloads = Literal[
            "hknpFirstPersonGun *, const hknpFirstPersonGun *",
            "hknpFirstPersonGun *",
        ]

class hknpStorageParticleSystem:
    class hknpStorageParticleSystem:
        overloads = Literal[
            "hknpStorageParticleSystem *, hknpStorageParticleSystem *",
            "hknpStorageParticleSystem *, const hknpStorageParticleSystem *",
        ]

class hknpWorldCinfo:
    class hknpWorldCinfo:
        overloads = Literal[
            "hknpWorldCinfo *, const hknpWorldCinfo *",
            "hknpWorldCinfo *",
        ]

class hknpScaledConvexShapeBase:
    class hknpScaledConvexShapeBase:
        overloads = Literal[
            "hknpScaledConvexShapeBase *, const hknpScaledConvexShapeBase *",
            "hknpScaledConvexShapeBase *, const hknpConvexShape *, const hkVector4f *, hknpShape::ScaleMode",
        ]
    class createInPlace:
        overloads = Literal[
            "hknpShapeBuffer *, const hknpConvexShape *, const hknpShapeQueryScalingData *",
            "hknpShapeBuffer *, const hknpConvexShape *, const hkVector4f *, hknpShape::ScaleMode",
        ]

class hknpScaledConvexShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpExternMeshShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpGravityGun:
    class hknpGravityGun:
        overloads = Literal[
            "hknpGravityGun *, const hknpGravityGun *",
            "hknpGravityGun *",
        ]

class hknpBodyCinfo:
    class hknpBodyCinfo:
        overloads = Literal[
            "hknpBodyCinfo *",
            "hknpBodyCinfo *, const hknpBodyCinfo *",
        ]

class hknpGroupCollisionFilter:
    class hknpGroupCollisionFilter:
        overloads = Literal[
            "hknpGroupCollisionFilter *, const hknpGroupCollisionFilter *",
            "hknpGroupCollisionFilter *",
        ]

class hknpShape:
    class setMassProperties:
        overloads = Literal[
            "hknpShape *, const hknpShape::MassConfig *",
            "hknpShape *, const hkDiagonalizedMassProperties *",
        ]

class hknpConvexShape:
    class calcAabbNoRadius:
        overloads = Literal[
            "hknpConvexShape *, hkAabb *",
            "hknpConvexShape *, const hkTransformf *, hkAabb *",
        ]

class hknpConvexShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpTriangleShape:
    class setVertices:
        overloads = Literal[
            "hknpTriangleShape *, const hkVector4f *, const hkVector4f *, const hkVector4f *, const hkVector4f *",
            "hknpTriangleShape *, const hkVector4f *, const hkVector4f *, const hkVector4f *",
        ]

class hknpLodShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpDecoratorShape:
    class hknpDecoratorShape:
        overloads = Literal[
            "hknpDecoratorShape *, const hknpDecoratorShape *",
            "hknpDecoratorShape *, hknpShapeType::Enum, const hknpShape *",
        ]

class hknpMaskedShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpCompositeShape:
    class hknpCompositeShape:
        overloads = Literal[
            "hknpCompositeShape *, const hknpCompositeShape *",
            "hknpCompositeShape *, hknpShapeType::Enum",
        ]

class hknpCompoundShape:
    class hknpCompoundShape:
        overloads = Literal[
            "hknpCompoundShape *, const hknpCompoundShapeCinfo *, const hknpCompoundShape::Layout *",
            "hknpCompoundShape *, const hknpCompoundShape *, hknpShape::CloneMode, hknpShapeMap *",
        ]

class hknpCompoundShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpMaterial:
    class hknpMaterial:
        overloads = Literal[
            "hknpMaterial *, const hknpMaterial *",
            "hknpMaterial *",
        ]

class hknpCompressedMeshShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpPairCollisionFilter:
    class hknpPairCollisionFilter:
        overloads = Literal[
            "hknpPairCollisionFilter *, const hknpPairCollisionFilter *",
            "hknpPairCollisionFilter *, const hknpCollisionFilter *",
        ]
    class isCollisionEnabled:
        overloads = Literal[
            "hknpPairCollisionFilter *, __int64, const hknpQueryFilterData *, const hknpBody *",
            "hknpPairCollisionFilter *, __int64, __int64, unsigned __int64",
            "hknpPairCollisionFilter *, __int64, _BOOL8, const hknpCollisionFilter::FilterInput *, const hknpCollisionFilter::FilterInput *",
        ]

class hknpConstraintCollisionFilter:
    class hknpConstraintCollisionFilter:
        overloads = Literal[
            "hknpConstraintCollisionFilter *, const hknpConstraintCollisionFilter *",
            "hknpConstraintCollisionFilter *, const hknpCollisionFilter *",
        ]

class hknpBreakableCompoundShapeKeyMask:
    class hknpBreakableCompoundShapeKeyMask:
        overloads = Literal[
            "hknpBreakableCompoundShapeKeyMask *, const hknpBreakableCompoundShapeKeyMask *, const hknpCompoundShape *",
            "hknpBreakableCompoundShapeKeyMask *, const hknpBreakableCompoundShape *",
            "hknpBreakableCompoundShapeKeyMask *",
        ]

class hknpBreakableCompoundShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpCompoundShapeInternalsCdDynamicTreeKeyMask:
    class hknpCompoundShapeInternalsCdDynamicTreeKeyMask:
        overloads = Literal[
            "hknpCompoundShapeInternalsCdDynamicTreeKeyMask *, const hknpCompoundShapeInternalsCdDynamicTreeKeyMask *, const hknpCompoundShape *",
            "hknpCompoundShapeInternalsCdDynamicTreeKeyMask *, const hknpCompoundShape *",
        ]

class hknpCompoundShapeInternalsSimdTreeKeyMask:
    class hknpCompoundShapeInternalsSimdTreeKeyMask:
        overloads = Literal[
            "hknpCompoundShapeInternalsSimdTreeKeyMask *, const hknpCompoundShapeInternalsSimdTreeKeyMask *, const hknpCompoundShape *",
            "hknpCompoundShapeInternalsSimdTreeKeyMask *, const hknpCompoundShape *",
        ]

class hknpTransformedShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpParticlesColliderShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpMaterialLibrary:
    class addEntry:
        overloads = Literal[
            "hknpMaterialLibrary *, hknpMaterialId *, const hknpMaterialDescriptor *",
            "hknpMaterialLibrary *, hknpMaterialId *, const hknpMaterial *",
        ]

class hknpParticlesColliderCinfo:
    class hknpParticlesColliderCinfo:
        overloads = Literal[
            "hknpParticlesColliderCinfo *, const hknpParticlesColliderCinfo *",
            "hknpParticlesColliderCinfo *",
        ]

class hknpCharacterRigidBody:
    class onCollisionDetected:
        overloads = Literal[
            "hknpCharacterRigidBody *, const hknpEventHandlerInput *, const hknpBinaryBodyEvent *, hknpManifoldCollisionCache *, const hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant> *, const hkVector4f *, const hkVector4f *, const hkSimdFloat32 *",
            "hknpCharacterRigidBody *, const hknpEventHandlerInput *, const hknpEvent *",
        ]

class hknpRagdollData:
    class hknpRagdollData:
        overloads = Literal[
            "hknpRagdollData *, const hknpRagdollData *",
            "hknpRagdollData *",
        ]

class hknpShapeUtil:
    class createConvexHullGeometry:
        overloads = Literal[
            "const hknpConvexHull *, float, __int64, const hkVector4f *, const hkVector4f *, hkGeometry *, hkGeometry *, int",
            "const hkFloat3 *, unsigned __int64 *, float, hknpShape::ConvexRadiusDisplayMode, const hkVector4f *, const hkVector4f *, hkGeometry *, hkGeometry *, int",
        ]

class hknpShapeNullFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *",
        ]

class hknpMeshShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpHeightFieldShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class hknpDeflectedLinearCast:
    class QueryFilter:
        class isCollisionEnabled:
            overloads = Literal[
                "hknpDeflectedLinearCast::QueryFilter *, __int64, const hknpQueryFilterData *, const hknpBody *",
                "hknpParticlesCollisionFilter *, __int64, __int64, unsigned __int64",
                "hknpDeflectedLinearCast::QueryFilter *, __int64, _BOOL8, const hknpCollisionFilter::FilterInput *, const hknpCollisionFilter::FilterInput *",
            ]

class hknpWorld:
    class allocateMaterial:
        overloads = Literal[
            "hknpWorld *, hknpMaterialId *, const hknpMaterialDescriptor *",
            "hknpWorld *, hknpMaterialId *, const hknpMaterial *",
        ]
    class castAabb:
        overloads = Literal[
            "hknpWorld *, const hknpAabbCastQuery *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
            "hknpWorld *, const hknpAabbCastQuery *, hknpBroadPhaseQueryCollector *",
        ]
    class queryAabb:
        overloads = Literal[
            "hknpWorld *, const hknpAabbQuery *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
            "hknpWorld *, const hknpAabbQuery *, hknpBroadPhaseQueryCollector *",
            "hknpWorld *, const hknpAabbQuery *, hknpCollisionQueryCollector *",
        ]
    class queryAabbNmp:
        overloads = Literal[
            "hknpWorld *, const hknpAabbQuery *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "hknpWorld *, const hknpAabbQuery *, hknpBroadPhaseQueryCollector *, hkAabb *",
        ]

class hknpBodyManager:
    class allocateBody:
        overloads = Literal[
            "hknpBodyManager *, _DWORD *, unsigned int",
            "hknpBodyManager *, hknpBodyIndex *",
        ]

class hknpConvexHull:
    class calcAabb:
        overloads = Literal[
            "hknpConvexHull *, hkAabb *",
            "hknpConvexHull *, const hkTransformf *, hkAabb *",
        ]

class hknpConstraintManager:
    class forceGroupToOneMotionCell:
        overloads = Literal[
            "hknpConstraintManager *",
            "hknpWorld *, const hknpConstraintGroup *, unsigned __int8",
        ]

class hknpInplaceTriangleShape:
    class hknpInplaceTriangleShape:
        overloads = Literal[
            "hknpInplaceTriangleShape *, bool",
            "hknpInplaceTriangleShape *",
        ]

class hknpShapeQueryInterface:
    class castShape:
        overloads = Literal[
            "hknpCollisionQueryContext *, const hknpShapeCastQuery *, const hknpShapeQueryInfo *, const hknpShape *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hknpCollisionQueryCollector *",
            "hknpCollisionQueryContext *, const hknpShapeCastQuery *, const hkRotationImpl<float> *, const hknpShape *, const hkTransformf *, hknpCollisionQueryCollector *, hknpCollisionQueryCollector *",
        ]

class hknpCheckDeterminismUtilities:
    class QueryCheckingBroadPhase:
        class appendHitsImpl:
            overloads = Literal[
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, hkCheckDeterminismThreadData *, const hknpCollisionQueryCollector *",
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, hkCheckDeterminismThreadData *, const hknpParticlesStaticCollector *",
            ]
        class castAabb:
            overloads = Literal[
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbCastQuery *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbCastQuery *, hknpBroadPhaseQueryCollector *",
            ]
        class queryAabb:
            overloads = Literal[
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, hkArray<hknpBodyIndex,hkBuiltinContainerAllocator<0,0> > *",
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, hknpBroadPhaseQueryCollector *",
            ]
        class queryAabbNmp:
            overloads = Literal[
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, const hkAabb *, hkAabb *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, const hkAabb *, hkAabb *, hkArray<hknpBodyIndex,hkBuiltinContainerAllocator<0,0> > *",
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, const hkAabb *, hkAabb *, hknpBroadPhaseQueryCollector *",
            ]
        class queryOutsideOfAabb:
            overloads = Literal[
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, hkArray<hknpBodyIndex,hkBuiltinContainerAllocator<0,0> > *",
                "hknpCheckDeterminismUtilities::QueryCheckingBroadPhase *, const hknpAabbQuery *, hknpBroadPhaseQueryCollector *",
            ]

class hknpParticlesCollisionFilter:
    class isCollisionEnabled:
        overloads = Literal[
            "hknpParticlesCollisionFilter *, hknpCollisionQueryType::Enum, const hknpQueryFilterData *, const hknpBody *",
            "hknpParticlesCollisionFilter *, __int64, __int64, const hknpCollisionFilter::FilterInput *",
        ]

class hknpCollidePipeline:
    class mergeAndCollide2Streams:
        overloads = Literal[
            "const hknpSimulationThreadContext *, const hknpInternalCollideSharedData *, int, hknpCollisionCacheConsumers *, hknpCollisionCache::RebuildMode, hknpCollisionCacheConsumers *, hknpCollisionCache::RebuildMode, hknpCollisionCacheWriters *, hknpCollisionCacheWriters *, hknpCdPairStream *, hknpCsContactJacInjector *, hknpCsContactJacInjector *, hkBlockStream::Writer *, hknpCollideTimers *",
            "const hknpSimulationThreadContext *, const hknpInternalCollideSharedData *, int, hknpCollisionCache::RebuildMode, bool *, hknpCollisionCacheConsumers *, hkTypedBlockStream<hknpBlockStreamBlockOffsetPair>::Consumer *, hkBlockStream::RandomAccessConsumer *, hknpCollisionCacheBatchConsumer *, hkTypedBlockStream<hknpCollisionCacheWorkItem>::Writer *, hknpStreamWorkItemWriter *, hknpCollisionCacheWriters *, hknpCollisionCacheWriters *, hknpCdPairStream *, hkBlockStream::Writer *, hkBlockStream::Writer *, hknpCsContactJacInjector *, hknpCsContactJacInjector *, hknpCollideTimers *",
        ]

class hknpApplyDragTask:
    class process:
        overloads = Literal[
            "hknpApplyDragTask *, hknpSimulationThreadContext *",
            "hknpApplyDragTask *, const hkTask::Input *",
        ]

class cTkAtomicLinearMemoryPool:
    class Malloc:
        overloads = Literal[
            "cTkAtomicLinearMemoryPool *, int, int, int *",
            "cTkSmallBlockMemoryPool *, __int64, int *",
        ]

class cTkLSystemManager:
    class LSystem:
        class LSystem:
            overloads = Literal[
                "cTkLSystemManager::LSystem *, cTkLSystemManager::LSystem *",
                "cTkLSystemManager::LSystem *, const cTkLSystemManager::LSystem *, __int64, __int64",
                "cTkLSystemManager::LSystem *",
            ]
    class GenerateProceduralLSystem:
        overloads = Literal[
            "cTkLSystemManager *, TkHandle, int, const cTkSeed *, const cTkMatrix34 *, bool",
            "cTkLSystemManager *, TkHandle, cTkLSystemRulesData *, const cTkSeed *, const cTkMatrix34 *, cTkLSystemManager::LoadType, bool",
        ]

class cTkPhysicsManager:
    class CastRay:
        overloads = Literal[
            "cTkPhysicsManager *, const cTkPhysRelVec3 *, const cTkPhysRelVec3 *, cTkContactPoint *, unsigned __int16, cTkRigidBody *",
            "cTkPhysicsManager *, const cTkVector3 *, const cTkVector3 *, cTkContactPoint *, unsigned __int16, cTkRigidBody *",
        ]
    class CastSphere:
        overloads = Literal[
            "cTkPhysicsManager *, float, const cTkVector3 *, const cTkVector3 *, cTkContactPoint *, int, unsigned int",
            "cTkPhysicsManager *, float, const cTkPhysRelVec3 *, const cTkPhysRelVec3 *, cTkContactPoint *, unsigned __int16, cTkRigidBody *",
            "cTkPhysicsManager *, float, const cTkVector3 *, const cTkVector3 *, cTkContactPoint *, unsigned __int16, cTkRigidBody *",
        ]

class cTkRaycastJob:
    class SetAllCollideFilters:
        overloads = Literal[
            "cTkRaycastJob *, unsigned __int16",
            "cTkRaycastJob *, unsigned __int16, unsigned __int16",
        ]
    class SetUsingDelta:
        overloads = Literal[
            "cTkRaycastJob *, unsigned int, const cTkPhysRelVec3 *, const cTkVector3 *",
            "cTkRaycastJob *, unsigned int, const cTkVector3 *, const cTkVector3 *",
        ]
    class SetUsingExtents:
        overloads = Literal[
            "cTkRaycastJob *, unsigned int, const cTkPhysRelVec3 *, const cTkPhysRelVec3 *",
            "cTkRaycastJob *, unsigned int, const cTkVector3 *, const cTkVector3 *",
        ]

class cTkHavokAabbSizeFilter:
    class isCollisionEnabled:
        overloads = Literal[
            "cTkHavokAabbSizeFilter *, __int64, const hknpQueryFilterData *, const hknpBody *",
            "cTkHavokAabbSizeFilter *, __int64, __int64, unsigned __int64",
            "cTkHavokAabbSizeFilter *, __int64, __int64, const hknpCollisionFilter::FilterInput *, const hknpCollisionFilter::FilterInput *",
        ]

class cTkLayeredNoise:
    class GenerateUberNoiseLayer3D_Vector:
        overloads = Literal[
            "const float *, const float *, const float *, float, cTkNoiseUberData *, int, float *, cTkVector4 *, unsigned int",
            "const GPU::vec3 *, float, cTkNoiseUberData *, int, float *, unsigned int",
        ]

class cTkSimplexNoise:
    class Noise2d:
        overloads = Literal[
            "const float, const float",
            "const float, const float, float *, float *",
        ]
    class Noise3d:
        overloads = Literal[
            "const float, const float, const float",
            "const float, const float, const float, float *, float *, float *",
        ]
    class Noise3dVectorised:
        overloads = Literal[
            "double, double, double",
            "double, double, double, float *, float *, float *",
        ]

class cTkCollision:
    class AddFromTerrain:
        overloads = Literal[
            "cTkCollision *, cTkQuadElement *, int, bool, float",
            "cTkCollision *, cTkTerrainVertex *, int, bool, float",
        ]

class cTkPhysicsBvMeshShapeFunctions:
    class queryAabb:
        overloads = Literal[
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hkArray<hkHandle<unsigned int,4294967295,hknpShapeKeyDiscriminant>,hkBuiltinContainerAllocator<0,0> > *, hkAabb *",
            "const hknpShape *, hknpCollisionQueryContext *, const hknpAabbQuery *, const hknpShapeQueryInfo *, const hknpQueryFilterData *, const hknpShapeQueryInfo *, hknpCollisionQueryCollector *, hkAabb *",
        ]

class cTk2dText:
    class Construct:
        overloads = Literal[
            "cTk2dText *, const cTkVector2 *, const cTkVector2 *, const cTkVector2 *, const cTk2dTextPreset *, const TkID<256> *",
            "cTk2dText *, const cTkVector2 *, const cTkVector2 *, const cTkVector2 *, const cTk2dTextPreset *, const wchar_t *",
            "cTk2dText *, const cTkVector2 *, const cTkVector2 *, const cTk2dTextPreset *, const TkID<256> *",
            "cTk2dText *, const cTkVector2 *, const cTkVector2 *, const cTk2dTextPreset *, const wchar_t *",
        ]

class cTkBehaviourTree:
    class Construct:
        overloads = Literal[
            "cTkBehaviourTree *, cTkAttachment *",
            "cTkBehaviourTree *, TkHandle",
        ]

class cTkNodeAnimationController:
    class GetAnimDuration:
        overloads = Literal[
            "cTkNodeAnimationController *, const cTkAnimInstanceHandle *",
            "cTkNodeAnimationController *, int",
        ]
    class GetAnimName:
        overloads = Literal[
            "cTkNodeAnimationController *, const cTkAnimInstanceHandle *",
            "cTkNodeAnimationController *, int",
        ]

class ITkDocumentWriter:
    class AddValue:
        overloads = Literal[
            "ITkDocumentWriter *, int",
            "ITkDocumentWriter *, unsigned int",
            "ITkDocumentWriter *, float",
        ]

class cTkDocumentStreamWriterJSON:
    class AddValue:
        overloads = Literal[
            "cTkDocumentStreamWriterJSON *, const TkID<128> *",
            "cTkDocumentStreamWriterJSON *, const cTkHalfVector4 *",
            "cTkDocumentStreamWriterJSON *, const cTkPhysRelVec3 *",
            "cTkDocumentStreamWriterJSON *, const cTkSeed *",
            "cTkDocumentStreamWriterJSON *, const cTkVector2 *",
            "cTkDocumentStreamWriterJSON *, const cTkVector3 *",
            "cTkDocumentStreamWriterJSON *, const cTkVector4 *",
            "cTkDocumentStreamWriterJSON *, const long double",
            "cTkDocumentStreamWriterJSON *, const char *",
            "cTkDocumentStreamWriterJSON *, const wchar_t *",
            "cTkDocumentStreamWriterJSON *, const __int64",
            "cTkDocumentStreamWriterJSON *, const unsigned __int64",
            "cTkDocumentStreamWriterJSON *, const bool",
        ]

class cTkDocumentWriterJSON:
    class AddValue:
        overloads = Literal[
            "cTkDocumentWriterJSON *, const TkID<128> *",
            "cTkDocumentWriterJSON *, const cTkHalfVector4 *",
            "cTkDocumentWriterJSON *, const cTkPhysRelVec3 *",
            "cTkDocumentWriterJSON *, const cTkSeed *",
            "cTkDocumentWriterJSON *, const cTkVector2 *",
            "cTkDocumentWriterJSON *, const cTkVector3 *",
            "cTkDocumentWriterJSON *, const cTkVector4 *",
            "cTkDocumentWriterJSON *, const long double",
            "cTkDocumentWriterJSON *, const char *",
            "cTkDocumentWriterJSON *, const wchar_t *",
            "cTkDocumentWriterJSON *, const __int64",
            "cTkDocumentWriterJSON *, const unsigned __int64",
            "cTkDocumentWriterJSON *, const bool",
        ]

class cTkDocumentReaderJSON:
    class MoveCursor:
        overloads = Literal[
            "cTkDocumentReaderJSON *, const unsigned int",
            "cTkDocumentReaderJSON *, const char *",
        ]
    class ReadValue:
        overloads = Literal[
            "cTkDocumentReaderJSON *, long double *",
            "cTkDocumentReaderJSON *, const char **",
            "cTkDocumentReaderJSON *, const wchar_t **",
            "cTkDocumentReaderJSON *, TkID<256> *",
            "cTkDocumentReaderJSON *, TkID<128> *",
            "cTkDocumentReaderJSON *, cTkHalfVector4 *",
            "cTkDocumentReaderJSON *, cTkPhysRelVec3 *",
            "cTkDocumentReaderJSON *, cTkSeed *",
            "cTkDocumentReaderJSON *, cTkVector2 *",
            "cTkDocumentReaderJSON *, cTkVector3 *",
            "cTkDocumentReaderJSON *, cTkVector4 *",
            "cTkDocumentReaderJSON *, __int64 *",
            "cTkDocumentReaderJSON *, unsigned __int64 *",
            "cTkDocumentReaderJSON *, bool *",
        ]

class ITkDocumentReader:
    class ReadValue:
        overloads = Literal[
            "ITkDocumentReader *, unsigned __int8 *",
            "ITkDocumentReader *, __int16 *",
            "ITkDocumentReader *, unsigned __int16 *",
            "ITkDocumentReader *, int *",
            "ITkDocumentReader *, unsigned int *",
            "ITkDocumentReader *, float *",
            "ITkDocumentReader *, TkHandle *",
            "ITkDocumentReader *, cTkDynamicString *",
            "ITkDocumentReader *, cTkDynamicWideString *",
        ]

class MetadataNGuiRender:
    class RenderData:
        overloads = Literal[
            "const char *, float *, const FloatEditOptions *, const FloatLimits *",
            "const char *, TkID<128> *",
            "const char *, cTkSeed *",
            "const char *, bool *",
            "const char *, const cTkMetaDataEnumLookup *, int, unsigned __int8 *",
            "const char *, const cTkMetaDataEnumLookup *, int, int *",
        ]

class cTkCurveFunction:
    class Calculate:
        overloads = Literal[
            "float, const cTkInOutCurve *",
            "float, eCurve",
        ]

class cTkInputPort:
    class AddBindings:
        overloads = Literal[
            "cTkInputPort *, eInputButtonType, ePadType, ITkInputDevice *, int, int, int",
            "cTkInputPort *, eInputButtonType, int, int, int",
            "cTkInputPort *, ePadType, int, int, int",
        ]

class cTkInputDeviceManagerBase:
    class CheckSupport:
        overloads = Literal[
            "eInputButtonType, eInputAxis",
            "eInputButtonType, eInputButton",
        ]
    class FindIconMap:
        overloads = Literal[
            "cTkInputDeviceManagerBase *, const cTkControllerSpecification *, eInputButtonType, ePadType",
            "cTkInputDeviceManagerBase *, eInputButtonType, ePadType",
        ]

class cTkInputManager:
    class EditBinding:
        overloads = Literal[
            "cTkInputManager *, int, int, int, eInputAxis",
            "cTkInputManager *, int, int, int, eInputButton",
        ]
    class GetBindings:
        overloads = Literal[
            "cTkInputManager *, int, int",
            "cTkInputManager *, int",
        ]
    class HasAnalogActionBound:
        overloads = Literal[
            "cTkInputManager *, int, eInputPort",
            "cTkInputManager *, int, int, eInputPort",
        ]
    class HasDigitalActionBound:
        overloads = Literal[
            "cTkInputManager *, int, eInputPort",
            "cTkInputManager *, int, int, eInputPort",
        ]
    class RegisterBinding:
        overloads = Literal[
            "cTkInputManager *, int, eInputAxis, const char *",
            "cTkInputManager *, int, eInputButton, const char *",
        ]

class cTkBase2DRenderer:
    class AddTranslate:
        overloads = Literal[
            "cTkBase2DRenderer *, const cTkVector2 *",
            "cTkBase2DRenderer *, const cTkVector3 *",
        ]

class cTkResourceCopier:
    class Download:
        overloads = Literal[
            "cTkResourceCopier *, struct VkBuffer_T *, void *, int, int",
            "cTkResourceCopier *, cTkTexture *, unsigned int, unsigned int, const void *",
        ]
    class Upload:
        overloads = Literal[
            "cTkResourceCopier *, struct VkBuffer_T *, const void *, int, int",
            "cTkResourceCopier *, cTkTexture *, unsigned int, unsigned int, const void *",
        ]

class TextureTiler:
    class UnmapAndFreePages:
        overloads = Literal[
            "TextureTiler *, VkQueue_T *, struct VkImage_T *, unsigned __int16 *, int, int *, unsigned int, unsigned int",
            "TextureTiler *, VkQueue_T *, struct VkImage_T *, unsigned __int16 *, int, unsigned __int64, unsigned int, unsigned int, unsigned int, unsigned int",
        ]

class cTkStringAssembler:
    class cTkStringAssembler:
        overloads = Literal[
            "cTkStringAssembler *, int, int",
            "cTkStringAssembler *, char *, int",
        ]

class cTkEngineUtils:
    class FindNode:
        overloads = Literal[
            "TkHandle *, TkHandle, unsigned int, int",
            "TkHandle *, TkHandle, const char *, int",
        ]
    class SetNodeMatrixWorld:
        overloads = Literal[
            "TkHandle, const cTkMatrix34 *",
            "TkHandle, const cTkPhysRelMat34 *",
        ]

class cTkBasicNoiseHelper:
    class GenerateNoiseFromUberData3D_Vector:
        overloads = Literal[
            "const float *, const float *, const float *, cTkNoiseUberLayerData *, int, float *, cTkVector4 *, int",
            "const GPU::vec3 *, cTkNoiseUberLayerData *, int, float *, int",
        ]
    class GenerateUberNoiseFromData2D_Bucketed:
        overloads = Literal[
            "cTkNoiseUberLayerData *, float *, float *, float *, int *, int, float *, int",
            "cTkNoiseUberLayerData *, GPU::sVoronoiResults *, int *, int, float *, int",
        ]

class cTkLanguageManagerBase:
    class Translate:
        overloads = Literal[
            "cTkLanguageManagerBase *, const TkID<256> *",
            "cTkLanguageManagerBase *, const TkID<256> *, const char *",
            "cTkLanguageManagerBase *, const char *, const char *",
        ]

class cTkJobManager:
    class SuspendJob:
        overloads = Literal[
            "__int64 *, void *",
            "void **",
        ]

class cTkAudioWwiseIO:
    class Open:
        overloads = Literal[
            "cTkAudioWwiseIO *, const wchar_t *, AkOpenMode, AkFileSystemFlags *, bool *, AkFileDesc *",
            "cTkAudioWwiseIO *, unsigned int, AkOpenMode, AkFileSystemFlags *, bool *, AkFileDesc *",
        ]

class TkAudioID:
    class TkAudioID:
        overloads = Literal[
            "TkAudioID *, const char *, const char *",
            "TkAudioID *, const char *",
        ]

class AkToneGenParamBlock:
    class GenerateParameterisedCombinedVarianceAndJitter:
        overloads = Literal[
            "AkToneGenParamBlock *, unsigned int, unsigned int",
            "AkToneGenParamBlock *, float, float",
        ]

class cTkAudioManager:
    class Stop:
        overloads = Literal[
            "cTkAudioManager *, TkAudioObject",
            "cTkAudioManager *, TkAudioObject, ITkAudioStream *",
        ]

class cTkSystemBase:
    class RunPollableTaskQueue:
        overloads = Literal[
            "cTkSystemBase *, _BOOL8",
            "cTkSystemBase *, _BOOL8, int",
        ]

class VmaStringBuilder:
    class AddNumber:
        overloads = Literal[
            "VmaStringBuilder *, unsigned int",
            "VmaStringBuilder *, unsigned __int64",
        ]

class cTkGraphicsAPI:
    class CreateSampler:
        overloads = Literal[
            "VkSamplerCreateInfo *",
            "eTextureAddressMode, eTextureFilterMode, unsigned int, float, float",
        ]
    class SetViewMatrix:
        overloads = Literal[
            "const cTkMatrix44 *, __int64, __int64",
            "const cTkMatrix44 *, __int64",
        ]

class VmaBlockMetadata_Buddy:
    class FreeAtOffset:
        overloads = Literal[
            "VmaBlockMetadata_Buddy *, VmaAllocation_T *, unsigned __int64",
            "VmaBlockMetadata_Buddy *, unsigned __int64",
        ]

class cTkHavokGroupMaskFilter:
    class isCollisionEnabled:
        overloads = Literal[
            "cTkHavokGroupMaskFilter *, hknpCollisionQueryType::Enum, const hknpQueryFilterData *, const hknpBody *",
            "cTkHavokGroupMaskFilter *, hknpCollisionQueryType::Enum, bool, const hknpCollisionFilter::FilterInput *, const hknpCollisionFilter::FilterInput *",
        ]

class cTkFileSystem:
    class GetFileSize:
        overloads = Literal[
            "cTkFileSystem *, FIOS2HANDLE *",
            "cTkFileSystem *, const char *",
        ]

class DSP:
    class Mix2:
        overloads = Literal[
            "float *, float *, float *, double, float, unsigned int",
            "float *, float *, double, double, unsigned int",
        ]
    class Mix2Interp:
        overloads = Literal[
            "float *, float *, float *, float, float, float, float, unsigned int",
            "float *, float *, float, double, float, float, unsigned int",
        ]
    class MixStereoWidth:
        overloads = Literal[
            "float *, float *, float *, float *, unsigned int, float, float",
            "float *, float *, unsigned int, float, float",
        ]
    class CAkOLACircularBuffer:
        class PushOverlappedWindow:
            overloads = Literal[
                "DSP::CAkOLACircularBuffer *, float *, unsigned int, float *",
                "DSP::CAkOLACircularBuffer *, float *, unsigned int",
            ]
    class CAkTimeWindow:
        class Apply:
            overloads = Literal[
                "DSP::CAkTimeWindow *, float *, unsigned int, float *",
                "DSP::CAkTimeWindow *, float *, unsigned int, double, float *",
                "DSP::CAkTimeWindow *, float *, unsigned int, double",
            ]
    class BUTTERFLYSET_NAMESPACE:
        class CAkFreqWindow:
            class CartToPol:
                overloads = Literal[
                    "DSP::BUTTERFLYSET_NAMESPACE::CAkFreqWindow *, AkFft::cpx_bin *",
                    "DSP::BUTTERFLYSET_NAMESPACE::CAkFreqWindow *",
                ]
            class ComputeVocoderSpectrum:
                overloads = Literal[
                    "DSP::BUTTERFLYSET_NAMESPACE::CAkFreqWindow *, DSP::AkPolar *, DSP::AkPolar *, float *, unsigned int, float, bool, DSP::AkPolar *",
                    "DSP::BUTTERFLYSET_NAMESPACE::CAkFreqWindow *, DSP::AkPolar *, DSP::AkPolar *, float *, unsigned int, float, bool",
                ]
    class DelayLine:
        class ProcessBuffer:
            overloads = Literal[
                "DSP::DelayLine *, float *, float *, unsigned int",
                "DSP::DelayLine *, float *, unsigned int",
            ]
    class FDN4:
        class ProcessBufferAccum:
            overloads = Literal[
                "DSP::FDN4 *, float *, float *, float *, float *, unsigned int",
                "DSP::FDN4 *, float *, float *, float *, unsigned int",
                "DSP::FDN4 *, float *, float *, unsigned int",
            ]

class AkPBIParams:
    class AkPBIParams:
        overloads = Literal[
            "AkPBIParams *",
            "AkPBIParams *, PlayHistory *",
            "AkPBIParams *, const AkPBIParams *",
        ]

class CAkMusicPBI:
    class _Stop:
        overloads = Literal[
            "CAkMusicPBI *, AkPBIStopMode, bool",
            "CAkMidiClipCtx *, __int64",
        ]

class CAkMusicTransAware:
    class GetTransitionRule:
        overloads = Literal[
            "CAkMusicTransAware *, unsigned int, unsigned int",
            "CAkMusicTransAware *, CAkParameterNodeBase *, unsigned int, CAkParameterNodeBase *, unsigned int, CAkParameterNodeBase *",
        ]

class CAkScheduleWindow:
    class CAkScheduleWindow:
        overloads = Literal[
            "CAkScheduleWindow *, CAkMatrixAwareCtx *, bool",
            "CAkScheduleWindow *, bool",
        ]

class CAkMusicNode:
    class SetAkProp:
        overloads = Literal[
            "CAkMusicNode *, AkPropID, int, int, int",
            "CAkMusicNode *, AkPropID, float, float, float",
        ]

class CAkMusicSwitchCntr:
    class SetAkProp:
        overloads = Literal[
            "CAkMusicSwitchCntr *, AkPropID, int, int, int",
            "CAkMusicSwitchCntr *, AkPropID, float, float, float",
        ]

class CAkMusicTrack:
    class MuteNotification:
        overloads = Literal[
            "CAkMusicTrack *, float, AkMutedMapItem *, bool",
            "CAkMusicTrack *, float, CAkRegisteredObj *, AkMutedMapItem *, bool",
        ]

class AkRSIterator:
    class CreateRSInfo:
        overloads = Literal[
            "CAkRSSub *",
            "RSType, unsigned __int16, unsigned __int16",
        ]

class CAkMusicSwitchCtx:
    class SetPlaybackHistory:
        overloads = Literal[
            "CAkMusicSwitchCtx *, unsigned int, const CAkMusicPackedHistory *",
            "CAkMusicSwitchCtx *, unsigned int, int, unsigned int",
        ]

class AK:
    class SoundEngine:
        class ExecuteActionOnEvent:
            overloads = Literal[
                "unsigned int, AK::SoundEngine::AkActionOnEventType, unsigned __int64, int, AkCurveInterpolation, unsigned int",
                "const char *, AK::SoundEngine::AkActionOnEventType, unsigned __int64, int, AkCurveInterpolation, unsigned int",
                "const wchar_t *, AK::SoundEngine::AkActionOnEventType, unsigned __int64, int, AkCurveInterpolation, unsigned int",
            ]
        class GetBufferStatusForPinnedEvent:
            overloads = Literal[
                "unsigned int, float *, bool *",
                "const char *, float *, bool *",
                "const wchar_t *, float *, bool *",
            ]
        class GetDeviceList:
            overloads = Literal[
                "unsigned int, unsigned int *, AkDeviceDescription *",
                "unsigned int, unsigned int, unsigned int *, AkDeviceDescription *",
            ]
        class DynamicDialogue:
            class GetDialogueEventCustomPropertyValue:
                overloads = Literal[
                    "unsigned int, unsigned int, int *",
                    "unsigned int, unsigned int, float *",
                ]
            class ResolveDialogueEvent:
                overloads = Literal[
                    "unsigned int, unsigned int *, unsigned int, unsigned int, __int64 *, void *",
                    "const char *, const char **, unsigned int, unsigned int, __int64 *, void *",
                    "const wchar_t *, const wchar_t **, unsigned int, unsigned int, __int64 *, void *",
                ]
        class GetIDFromString:
            overloads = Literal[
                "const char *",
                "const wchar_t *",
            ]
        class GetOutputID:
            overloads = Literal[
                "unsigned int, unsigned int",
                "const char *, unsigned int",
                "const wchar_t *, unsigned int",
            ]
        class LoadBank:
            overloads = Literal[
                "unsigned int",
                "unsigned int, __int64 *, void *",
                "const char *, unsigned int *",
                "const char *, __int64 *, void *, unsigned int *",
                "const wchar_t *, unsigned int *",
                "const wchar_t *, __int64 *, void *, unsigned int *",
            ]
        class LoadBankMemoryCopy:
            overloads = Literal[
                "const void *, unsigned int, unsigned int *",
                "const void *, unsigned int, __int64 *, void *, unsigned int *",
            ]
        class LoadBankMemoryView:
            overloads = Literal[
                "const void *, unsigned int, unsigned int *",
                "const void *, unsigned int, __int64 *, void *, unsigned int *",
            ]
        class PinEventInStreamCache:
            overloads = Literal[
                "unsigned int, char, char",
                "const char *, char, char",
                "const wchar_t *, char, char",
            ]
        class PostEvent:
            overloads = Literal[
                "unsigned int, unsigned __int64, unsigned int, __int64 *, void *, unsigned int, AkExternalSourceInfo *, unsigned int",
                "unsigned int, unsigned __int64, unsigned int, __int64 *, void *, AkCustomParamType *, unsigned int",
                "const char *, unsigned __int64, unsigned int, __int64 *, void *, unsigned int, AkExternalSourceInfo *, unsigned int",
                "const wchar_t *, unsigned __int64, unsigned int, __int64 *, void *, unsigned int, AkExternalSourceInfo *, unsigned int",
            ]
        class PostTrigger:
            overloads = Literal[
                "StopParticles *, unsigned __int64",
                "const char *, unsigned __int64",
                "const wchar_t *, unsigned __int64",
            ]
        class PrepareBank:
            overloads = Literal[
                "AK::SoundEngine::PreparationType, unsigned int, __int64 *, void *, AK::SoundEngine::AkBankContent",
                "AK::SoundEngine::PreparationType, unsigned int, AK::SoundEngine::AkBankContent",
                "AK::SoundEngine::PreparationType, const char *, __int64 *, void *, AK::SoundEngine::AkBankContent",
                "AK::SoundEngine::PreparationType, const char *, AK::SoundEngine::AkBankContent",
                "AK::SoundEngine::PreparationType, const wchar_t *, __int64 *, void *, AK::SoundEngine::AkBankContent",
                "AK::SoundEngine::PreparationType, const wchar_t *, AK::SoundEngine::AkBankContent",
            ]
        class PrepareEvent:
            overloads = Literal[
                "AK::SoundEngine::PreparationType, unsigned int *, unsigned int",
                "AK::SoundEngine::PreparationType, unsigned int *, unsigned int, __int64 *, void *",
                "AK::SoundEngine::PreparationType, const char **, unsigned int",
                "AK::SoundEngine::PreparationType, const char **, unsigned int, __int64 *, void *",
                "AK::SoundEngine::PreparationType, const wchar_t **, unsigned int",
                "AK::SoundEngine::PreparationType, const wchar_t **, unsigned int, __int64 *, void *",
            ]
        class PrepareGameSyncs:
            overloads = Literal[
                "AK::SoundEngine::PreparationType, AkGroupType, unsigned int, unsigned int *, unsigned int",
                "AK::SoundEngine::PreparationType, AkGroupType, unsigned int, unsigned int *, unsigned int, __int64 *, void *",
                "AK::SoundEngine::PreparationType, AkGroupType, const char *, const char **, unsigned int",
                "AK::SoundEngine::PreparationType, AkGroupType, const char *, const char **, unsigned int, __int64 *, void *",
                "AK::SoundEngine::PreparationType, AkGroupType, const wchar_t *, const wchar_t **, unsigned int",
                "AK::SoundEngine::PreparationType, AkGroupType, const wchar_t *, const wchar_t **, unsigned int, __int64 *, void *",
            ]
        class ResetRTPCValue:
            overloads = Literal[
                "SpawnParticles *, unsigned __int64, int, AkCurveInterpolation, bool",
                "const char *, unsigned __int64, int, AkCurveInterpolation, bool",
                "const wchar_t *, unsigned __int64, int, AkCurveInterpolation, bool",
            ]
        class DynamicSequence:
            class Seek:
                overloads = Literal[
                    "unsigned int, int, bool",
                    "unsigned int, float, bool",
                ]
        class SeekOnEvent:
            overloads = Literal[
                "unsigned int, unsigned __int64, int, bool, unsigned int",
                "unsigned int, unsigned __int64, float, bool, unsigned int",
                "const char *, unsigned __int64, int, bool, unsigned int",
                "const char *, unsigned __int64, float, bool, unsigned int",
                "const wchar_t *, unsigned __int64, int, bool, unsigned int",
                "const wchar_t *, unsigned __int64, float, bool, unsigned int",
            ]
        class SetBusDevice:
            overloads = Literal[
                "unsigned int, unsigned int",
                "const char *, const char *",
                "const wchar_t *, const wchar_t *",
            ]
        class SetBusEffect:
            overloads = Literal[
                "unsigned int, unsigned int, unsigned int",
                "const char *, unsigned int, unsigned int",
                "const wchar_t *, unsigned int, unsigned int",
            ]
        class SetMixer:
            overloads = Literal[
                "unsigned int, unsigned int",
                "const char *, unsigned int",
                "const wchar_t *, unsigned int",
            ]
        class SetMultiplePositions:
            overloads = Literal[
                "unsigned __int64, const AkChannelEmitter *, unsigned __int16, AK::SoundEngine::MultiPositionType",
                "unsigned __int64, const AkTransform *, unsigned __int16, AK::SoundEngine::MultiPositionType",
            ]
        class SetRTPCValue:
            overloads = Literal[
                "SurveyVariableValue *, float, unsigned __int64, int, AkCurveInterpolation, bool",
                "const char *, float, unsigned __int64, int, AkCurveInterpolation, bool",
                "const wchar_t *, float, unsigned __int64, int, AkCurveInterpolation, bool",
            ]
        class SetRTPCValueByPlayingID:
            overloads = Literal[
                "unsigned int, float, unsigned int, int, AkCurveInterpolation, bool",
                "const char *, float, unsigned int, int, AkCurveInterpolation, bool",
                "const wchar_t *, float, unsigned int, int, AkCurveInterpolation, bool",
            ]
        class SetState:
            overloads = Literal[
                "StopParticles *, unsigned int",
                "StopParticles *, unsigned int, bool, bool",
                "const char *, const char *",
                "const wchar_t *, const wchar_t *",
            ]
        class SetSwitch:
            overloads = Literal[
                "unsigned int, unsigned int, unsigned __int64",
                "const char *, const char *, unsigned __int64",
                "const wchar_t *, const wchar_t *, unsigned __int64",
            ]
        class UnloadBank:
            overloads = Literal[
                "unsigned int, const void *",
                "unsigned int, const void *, __int64 *, void *",
                "const char *, const void *",
                "const char *, const void *, __int64 *, void *",
                "const wchar_t *, const void *",
                "const wchar_t *, const void *, __int64 *, void *",
            ]
        class UnpinEventInStreamCache:
            overloads = Literal[
                "unsigned int",
                "const char *",
                "const wchar_t *",
            ]
        class Query:
            class GetMaxRadius:
                overloads = Literal[
                    "AkArray<AK::SoundEngine::Query::GameObjDst,AK::SoundEngine::Query::GameObjDst const &,AkArrayAllocatorNoAlign<0>,AkGrowByPolicy_Proportional,AkAssignmentMovePolicy<AK::SoundEngine::Query::GameObjDst> > *",
                    "unsigned __int64",
                ]
            class GetRTPCValue:
                overloads = Literal[
                    "unsigned int, unsigned __int64, unsigned int, float *, AK::SoundEngine::Query::RTPCValue_type *",
                    "const char *, unsigned __int64, unsigned int, float *, AK::SoundEngine::Query::RTPCValue_type *",
                    "const wchar_t *, unsigned __int64, unsigned int, float *, AK::SoundEngine::Query::RTPCValue_type *",
                ]
            class GetState:
                overloads = Literal[
                    "unsigned int, unsigned int *",
                    "const char *, unsigned int *",
                    "const wchar_t *, unsigned int *",
                ]
            class GetSwitch:
                overloads = Literal[
                    "unsigned int, unsigned __int64, unsigned int *",
                    "const char *, unsigned __int64, unsigned int *",
                    "const wchar_t *, unsigned __int64, unsigned int *",
                ]
            class QueryAudioObjectIDs:
                overloads = Literal[
                    "unsigned int, unsigned int *, AkObjectInfo *",
                    "const char *, unsigned int *, AkObjectInfo *",
                    "const wchar_t *, unsigned int *, AkObjectInfo *",
                ]
    class ReadBytesMem:
        class ReadBytesMem:
            overloads = Literal[
                "AK::ReadBytesMem *, const void *, int",
                "AK::ReadBytesMem *",
            ]
    class ReadBytesSkip:
        class ReadBytesSkip:
            overloads = Literal[
                "AK::ReadBytesSkip *, const void *, int",
                "AK::ReadBytesSkip *",
            ]
    class CAkBusCtx:
        class CAkBusCtx:
            overloads = Literal[
                "AK::CAkBusCtx *, AK::CAkBusCtx *",
                "AK::CAkBusCtx *, CAkBus *, CAkRegisteredObj *",
                "AK::CAkBusCtx *",
            ]
    class StreamMgr:
        class AkDeferredOpenData:
            class Create:
                overloads = Literal[
                    "unsigned int, AkFileSystemFlags *, AkOpenMode",
                    "const wchar_t *, AkFileSystemFlags *, AkOpenMode",
                ]
        class CAkStreamMgr:
            class CreateAuto:
                overloads = Literal[
                    "AK::StreamMgr::CAkStreamMgr *, unsigned int, AkFileSystemFlags *, const AkAutoStmHeuristics *, AkAutoStmBufSettings *, AK::IAkAutoStream **, bool",
                    "AK::StreamMgr::CAkStreamMgr *, void *, unsigned __int64, const AkAutoStmHeuristics *, AK::IAkAutoStream **",
                    "AK::StreamMgr::CAkStreamMgr *, const wchar_t *, AkFileSystemFlags *, const AkAutoStmHeuristics *, AkAutoStmBufSettings *, AK::IAkAutoStream **, bool",
                ]
            class CreateStd:
                overloads = Literal[
                    "AK::StreamMgr::CAkStreamMgr *, unsigned int, AkFileSystemFlags *, AkOpenMode, AK::IAkStdStream **, bool",
                    "AK::StreamMgr::CAkStreamMgr *, const wchar_t *, AkFileSystemFlags *, AkOpenMode, AK::IAkStdStream **, bool",
                ]
        class CAkStmTask:
            class SetDeferredFileOpen:
                overloads = Literal[
                    "AK::StreamMgr::CAkStmTask *, AkFileDesc *, unsigned int, AkFileSystemFlags *, AkOpenMode",
                    "AK::StreamMgr::CAkStmTask *, AkFileDesc *, const wchar_t *, AkFileSystemFlags *, AkOpenMode",
                ]

class CAkPBI:
    class IsUsingThisSlot:
        overloads = Literal[
            "CAkPBI *, const unsigned __int8 *",
            "CAkPBI *, const CAkUsageSlot *",
        ]
    class SeekTimeAbsolute:
        overloads = Literal[
            "CAkPBI *, int",
            "CAkPBI *, int, bool",
        ]
    class _Pause:
        overloads = Literal[
            "CAkPBI *, bool",
            "CAkPBI *, TransParams *",
        ]
    class _Resume:
        overloads = Literal[
            "CAkPBI *",
            "CAkPBI *, TransParams *, bool",
        ]
    class _Stop:
        overloads = Literal[
            "CAkPBI *, const TransParams *, _BOOL8",
            "CAkPBI *, AkPBIStopMode, bool",
        ]

class CAkURenderer:
    class GetMaxRadius:
        overloads = Literal[
            "AkArray<AK::SoundEngine::Query::GameObjDst,AK::SoundEngine::Query::GameObjDst const &,AkArrayAllocatorNoAlign<0>,AkGrowByPolicy_Proportional,AkAssignmentMovePolicy<AK::SoundEngine::Query::GameObjDst> > *",
            "unsigned __int64",
        ]

class CAkPlayingMgr:
    class AddPlayingID:
        overloads = Literal[
            "CAkPlayingMgr *, AkQueuedMsg_EventBase *, __int64 *, void *, unsigned int, unsigned int",
            "CAkPlayingMgr *, unsigned int, unsigned __int64, AkCustomParamType *, __int64 *, void *, unsigned int, unsigned int",
            "CAkPlayingMgr *, unsigned int, unsigned __int64, __int64 *, void *, unsigned int, unsigned int",
        ]

class CAkParameterNodeBase:
    class SetAkProp:
        overloads = Literal[
            "CAkParameterNodeBase *, AkPropID, int, int",
            "CAkParameterNodeBase *, AkPropID, float, float",
        ]

class CAkAudioMgr:
    class PausePendingAction:
        overloads = Literal[
            "CAkAudioMgr *, CAkAction *",
            "CAkAudioMgr *, CAkParameterNodeBase *, CAkRegisteredObj *, bool, unsigned int",
        ]
    class ProcessAllActions:
        overloads = Literal[
            "CAkAudioMgr *, CAkEvent *, AkQueuedMsg_EventAction *, CAkRegisteredObj *",
            "CAkAudioMgr *, CAkEvent *, AkQueuedMsg_EventPostMIDI *, CAkRegisteredObj *",
            "CAkAudioMgr *, CAkEvent *, AkQueuedMsg_EventStopMIDI *, CAkRegisteredObj *",
        ]
    class ResumePausedPendingAction:
        overloads = Literal[
            "CAkAudioMgr *, CAkAction *",
            "CAkAudioMgr *, CAkParameterNodeBase *, CAkRegisteredObj *, bool, unsigned int",
        ]

class CAkSoundBase:
    class MuteNotification:
        overloads = Literal[
            "CAkSoundBase *, float, AkMutedMapItem *, bool",
            "CAkSoundBase *, float, CAkRegisteredObj *, AkMutedMapItem *, bool",
        ]

class CAkTransitionManager:
    class ProcessTransitionsList:
        overloads = Literal[
            "CAkTransitionManager *, unsigned int, AkArray<CAkTransition *,CAkTransition *,AkArrayAllocatorNoAlign<0>,AkGrowByPolicy_Proportional,AkAssignmentMovePolicy<CAkTransition *> > *",
            "CAkTransitionManager *, unsigned int",
        ]

class CAkAudioLibIndex:
    class GetNodePtrAndAddRef:
        overloads = Literal[
            "CAkAudioLibIndex *, WwiseObjectIDext *",
            "CAkAudioLibIndex *, unsigned int, AkNodeType",
        ]

class CAkStateMgr:
    class GetState:
        overloads = Literal[
            "CAkStateMgr *, unsigned int",
            "CAkStateMgr *, unsigned int, unsigned int *",
        ]

class CAkBankReader:
    class SetFile:
        overloads = Literal[
            "CAkBankReader *, __int64, unsigned int, unsigned int, void *, bool",
            "CAkBankReader *, const char *, unsigned int, void *",
            "CAkBankReader *, const void *, unsigned int",
        ]

class AkFileNameString:
    class Copy:
        overloads = Literal[
            "AkFileNameString *, const char *, const char *",
            "AkFileNameString *, const wchar_t *, const wchar_t *",
        ]

class CAkParameterNode:
    class SetAkProp:
        overloads = Literal[
            "CAkParameterNode *, AkPropID, int, int, int",
            "CAkParameterNode *, AkPropID, float, float, float",
            "CAkParameterNode *, AkPropID, CAkRegisteredObj *, AkValueMeaning, float, AkCurveInterpolation, int",
        ]

class CAkRTPCMgr:
    class ResetRTPCValue:
        overloads = Literal[
            "CAkRTPCMgr *, unsigned int, const AkRTPCKey *, TransParamsBase *",
            "CAkRTPCMgr *, unsigned int, CAkRegisteredObj *, unsigned int, TransParamsBase *",
        ]
    class SetRTPCInternal:
        overloads = Literal[
            "CAkRTPCMgr *, unsigned int, float, const AkRTPCKey *, TransParamsBase *, AkValueMeaning, bool",
            "CAkRTPCMgr *, unsigned int, float, CAkRegisteredObj *, unsigned int, TransParamsBase *, AkValueMeaning",
        ]
    class UnSubscribeRTPC:
        overloads = Literal[
            "CAkRTPCMgr *, void *, unsigned int",
            "CAkRTPCMgr *, void *, unsigned int, unsigned int, bool *",
        ]

class CAkSwitchMgr:
    class GetSwitch:
        overloads = Literal[
            "CAkSwitchMgr *, unsigned int, const AkRTPCKey *",
            "CAkSwitchMgr *, unsigned int, const AkRTPCKey *, unsigned int *",
        ]

class CAkSource:
    class SetSource:
        overloads = Literal[
            "CAkSource *, unsigned int",
            "CAkSource *, unsigned int, unsigned int, const wchar_t *, unsigned int, bool, bool",
        ]

class CAkBus:
    class SetAkProp:
        overloads = Literal[
            "CAkBus *, AkPropID, float, float",
            "CAkBus *, AkPropID, CAkRegisteredObj *, AkValueMeaning, float, AkCurveInterpolation, int",
        ]

class CAkModulatorMgr:
    class Trigger:
        overloads = Literal[
            "CAkModulatorMgr *, const AkModulatorSubscriberInfo *, const AkModulatorTriggerParams *, CAkModulatorData *",
            "CAkModulatorMgr *, const AkArray<AkModulatorToTrigger,AkModulatorToTrigger const &,AkHybridAllocator<256,1,0>,AkGrowByPolicy_Proportional,AkAssignmentMovePolicy<AkModulatorToTrigger> > *, const AkModulatorTriggerParams *, CAkModulatorData *",
        ]

class CAkOutputMgr:
    class GetDevice:
        overloads = Literal[
            "unsigned int, unsigned int",
            "unsigned __int64",
        ]

class CAkDialogueEvent:
    class ResolveArgumentValueNames:
        overloads = Literal[
            "CAkDialogueEvent *, const char **, unsigned int *, unsigned int",
            "CAkDialogueEvent *, const wchar_t **, unsigned int *, unsigned int",
        ]

class CAkVPLSrcCbxNode:
    class AddSrc:
        overloads = Literal[
            "CAkVPLSrcCbxNode *, CAkPBI *, bool",
            "CAkVPLSrcCbxNode *, CAkVPLSrcNode *, bool, bool",
        ]
    class IsUsingThisSlot:
        overloads = Literal[
            "CAkVPLSrcCbxNode *, const unsigned __int8 *",
            "CAkVPLSrcCbxNode *, const CAkUsageSlot *",
        ]

class PluginRTPCSub:
    class Clone:
        overloads = Literal[
            "PluginRTPCSub *, CAkFxBase *, const AkRTPCKey *, CAkModulatorData *, bool",
            "PluginRTPCSub *, CAkFxBase *, CAkBehavioralCtx *",
        ]

class CAkAction:
    class SetAkProp:
        overloads = Literal[
            "CAkAction *, AkPropID, int, int, int",
            "CAkAction *, AkPropID, float, float, float",
        ]

class CAkActionPlayAndContinue:
    class AssignModulator:
        overloads = Literal[
            "CAkActionPlayAndContinue *, CAkModCtxRefContainer *",
            "CAkActionPlayAndContinue *, CAkModulatorData *",
        ]

class AkVBAPMap:
    class ComputeVBAPSquared:
        overloads = Literal[
            "AkVBAPMap *, float, float, unsigned int, float *",
            "AkVBAPMap *, float, float, double, unsigned int, float *",
        ]

class CAkEffectContextBase:
    class IsUsingThisSlot:
        overloads = Literal[
            "CAkEffectContextBase *, const unsigned __int8 *",
            "CAkEffectContextBase *, const CAkUsageSlot *, AK::IAkPlugin *",
        ]

class CAkActionMute:
    class ExecResetValue:
        overloads = Literal[
            "CAkActionMute *, CAkParameterNodeBase *",
            "CAkActionMute *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]
    class ExecResetValueExcept:
        overloads = Literal[
            "CAkActionMute *, CAkParameterNodeBase *",
            "CAkActionMute *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]
    class ExecSetValue:
        overloads = Literal[
            "CAkActionMute *, CAkParameterNodeBase *",
            "CAkActionMute *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]

class CAkActionSetAkProp:
    class ExecResetValue:
        overloads = Literal[
            "CAkActionSetAkProp *, CAkParameterNodeBase *",
            "CAkActionSetAkProp *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]
    class ExecResetValueExcept:
        overloads = Literal[
            "CAkActionSetAkProp *, CAkParameterNodeBase *",
            "CAkActionSetAkProp *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]
    class ExecSetValue:
        overloads = Literal[
            "CAkActionSetAkProp *, CAkParameterNodeBase *",
            "CAkActionSetAkProp *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]

class CAkActionSetGameParameter:
    class ExecResetValue:
        overloads = Literal[
            "CAkActionSetGameParameter *, CAkParameterNodeBase *",
            "CAkActionSetGameParameter *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]
    class ExecSetValue:
        overloads = Literal[
            "CAkActionSetGameParameter *, CAkParameterNodeBase *",
            "CAkActionSetGameParameter *, CAkParameterNodeBase *, CAkRegisteredObj *",
        ]

class CAkSrcPhysModel:
    class IsUsingThisSlot:
        overloads = Literal[
            "CAkSrcPhysModel *, const unsigned __int8 *",
            "CAkSrcPhysModel *, const CAkUsageSlot *",
        ]

class hkcdObb:
    class set:
        overloads = Literal[
            "hkcdObb *, const hkStridedVertices *",
            "hkcdObb *, const hkgpConvexHull *",
            "hkcdObb *, const hkVector4f *, int",
            "hkcdObb *, const hkRotationImpl<float> *, const hkVector4f *, const hkVector4f *",
            "hkcdObb *, const hkTransformf *, const hkVector4f *",
        ]

class hkcdSimdTree:
    class buildFromAabbs:
        overloads = Literal[
            "hkcdSimdTree *, hkcdSimdTree::BuildContext *, const hkAabbFloat3 *",
            "hkcdSimdTree *, hkcdSimdTree::BuildContext *, const hkAabb *",
        ]

class hkcdPlanarGeometryPolygonCollection:
    class hkcdPlanarGeometryPolygonCollection:
        overloads = Literal[
            "hkcdPlanarGeometryPolygonCollection *, const hkcdPlanarGeometryPolygonCollection *",
            "hkcdPlanarGeometryPolygonCollection *",
        ]

class hkcdPlanarGeometryPlanesCollection:
    class hkcdPlanarGeometryPlanesCollection:
        overloads = Literal[
            "hkcdPlanarGeometryPlanesCollection *, const hkcdPlanarGeometryPlanesCollection *",
            "hkcdPlanarGeometryPlanesCollection *",
        ]

class hkcdPlanarGeometry:
    class hkcdPlanarGeometry:
        overloads = Literal[
            "hkcdPlanarGeometry *, const hkcdPlanarGeometry *",
            "hkcdPlanarGeometry *, hkcdPlanarGeometryPlanesCollection *, int, hkcdPlanarEntityDebugger *",
        ]

class hkcdPlanarSolid:
    class hkcdPlanarSolid:
        overloads = Literal[
            "hkcdPlanarSolid *, const hkcdPlanarSolid *",
            "hkcdPlanarSolid *, const hkcdPlanarGeometryPlanesCollection *, int, hkcdPlanarEntityDebugger *",
        ]

class hkCompressedMassProperties:
    class unpack:
        overloads = Literal[
            "hkCompressedMassProperties *, hkMassProperties *",
            "hkCompressedMassProperties *, hkDiagonalizedMassProperties *",
        ]

class hkaSkeleton:
    class hkaSkeleton:
        overloads = Literal[
            "hkaSkeleton *, const hkaSkeleton *",
            "hkaSkeleton *",
        ]

class hkDefaultCompoundMeshBody:
    class completeUpdate:
        overloads = Literal[
            "hkDefaultCompoundMeshBody *, const hkMatrix4Impl<float> *",
            "hkDefaultCompoundMeshBody *",
        ]

class hkVertexFormat:
    class hkVertexFormat:
        overloads = Literal[
            "hkVertexFormat *, const hkVertexFormat *",
            "hkVertexFormat *",
        ]

class hkMemoryMeshVertexBuffer:
    class hkMemoryMeshVertexBuffer:
        overloads = Literal[
            "hkMemoryMeshVertexBuffer *, const hkVertexFormat *, int",
            "hkMemoryMeshVertexBuffer *",
        ]

class hkMeshVertexBufferUtil:
    class getElementVectorArray:
        overloads = Literal[
            "const hkMeshVertexBuffer::LockedVertices::Buffer *, float *, char *, int",
            "const hkMeshVertexBuffer::LockedVertices *, __int64, float *, char *",
        ]
    class setElementVectorArray:
        overloads = Literal[
            "const hkMeshVertexBuffer::LockedVertices::Buffer *, const float *, __m128 *, unsigned int",
            "const hkMeshVertexBuffer::LockedVertices *, __int64, const float *, __m128 *",
        ]

class hkgpConvexHull:
    class build:
        overloads = Literal[
            "hkgpConvexHull *, const hkStridedVertices *, const hkgpConvexHull::BuildConfig *",
            "hkgpConvexHull *, const hkVector4f *, int, const hkgpConvexHull::BuildConfig *",
        ]
    class buildFromPlanes:
        overloads = Literal[
            "hkgpConvexHull *, const hkVector4f *, int, const hkgpConvexHull::BuildConfig *",
            "hkgpConvexHull *, const hkVector4f *, int, const hkVector4f *, const hkgpConvexHull::BuildConfig *",
        ]
    class buildPlanar:
        overloads = Literal[
            "hkgpConvexHull *, const hkStridedVertices *, const hkVector4f *, const hkgpConvexHull::BuildConfig *",
            "hkgpConvexHull *, const hkVector4f *, int, const hkVector4f *, const hkgpConvexHull::BuildConfig *",
        ]

class hkSerialize:
    class Detail:
        class TypeWriterMap:
            class enqueueForWrite:
                overloads = Literal[
                    "hkSerialize::Detail::TypeWriterMap *, const hkReflect::Type *",
                    "hkSerialize::Detail::TypeWriterMap *, int",
                ]

class hkAabb:
    class includePoints:
        overloads = Literal[
            "hkAabb *, const hkFloat3 *, int",
            "hkAabb *, const hkVector4f *, int",
        ]

class hkAabbUtil:
    class calcAabb:
        overloads = Literal[
            "const hkTransformf *, const hkAabb *, hkAabb *",
            "const hkTransformf *, const hkAabb *, const hkSimdFloat32 *, hkAabb *",
            "const hkFloat3 *, int, const hkTransformf *, hkAabb *",
            "const hkVector4f *, int, hkAabb *",
        ]

class hkIo:
    class ReadBuffer:
        class attach:
            overloads = Literal[
                "hkIo::ReadBuffer *, const hkIo::Detail::ReadBufferAdapter *",
                "hkIo::ReadBuffer *, const void *, __int64",
            ]

class hkPrimaryCommandDispatcher:
    class hkPrimaryCommandDispatcher:
        overloads = Literal[
            "hkPrimaryCommandDispatcher *, hkPrimaryCommandDispatcher *",
            "hkPrimaryCommandDispatcher *",
        ]

class hkInt256:
    class setMul:
        overloads = Literal[
            "hkInt256 *, const hkInt128 *, const hkInt128 *",
            "hkInt256 *, const hkInt128 *, __int64",
        ]

class hknpSimdTreeBroadPhase:
    class castAabb:
        overloads = Literal[
            "hknpSimdTreeBroadPhase *, const hknpAabbCastQuery *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
            "hknpSimdTreeBroadPhase *, const hknpAabbCastQuery *, hknpBroadPhaseQueryCollector *",
        ]
    class queryAabb:
        overloads = Literal[
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, hkArray<hknpBodyIndex,hkBuiltinContainerAllocator<0,0> > *",
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, hknpBroadPhaseQueryCollector *",
        ]
    class queryAabbNmp:
        overloads = Literal[
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, const hkAabb *, hkAabb *, hkArray<hknpBodyId,hkBuiltinContainerAllocator<0,0> > *",
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, const hkAabb *, hkAabb *, hkArray<hknpBodyIndex,hkBuiltinContainerAllocator<0,0> > *",
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, const hkAabb *, hkAabb *, hknpBroadPhaseQueryCollector *",
        ]
    class queryOutsideOfAabb:
        overloads = Literal[
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, hkArray<hknpBodyIndex,hkBuiltinContainerAllocator<0,0> > *",
            "hknpSimdTreeBroadPhase *, const hknpAabbQuery *, hknpBroadPhaseQueryCollector *",
        ]

