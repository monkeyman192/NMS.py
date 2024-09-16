from typing import Union


FUNC_PATTERNS: dict[str, Union[str, dict[str, str]]] = {
    "cGcPlayerState::AwardUnits": "48 89 5C 24 08 48 89 6C 24 10 48 89 74 24 18 57 48 83 EC 40 44 8B 81 BC",
    "cGcPlayerState::RemoveUnits": "40 53 48 83 EC 40 44 8B 81 BC",
    "cGcPlayerState::Construct": "40 55 53 57 41 55 41 57 48 8B",
    "cGcPlanet::SetupRegionMap": "48 89 5C 24 10 48 89 6C 24 18 56 57 41 56 48 83 EC 40 48 8B D9 8B",
    "cGcPlanet::UpdateGravity": "40 53 48 83 EC 40 83 B9 78",
    "cGcSpaceshipComponent::GetTakeOffCost": "40 53 48 83 EC 40 48 8B D9 48 8B 0D ?? ?? ?? ?? 48 8B",
    "cTkDynamicGravityControl::Construct": "4C 8B DC 49 89 5B 10 49 89 6B 18 49 89 73 20 41 56 48 81 EC 10",
    "cGcSolarSystem::Generate": "48 8B C4 48 89 58 18 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 98 F8",
    "cGcApplicationLocalLoadState::GetRespawnReason": "48 89 5C 24 08 57 48 83 EC 20 80 B9 D4 05",
    "cGcShipHUD::RenderHeadsUp": "40 55 53 41 56 48 8D AC 24 30 F7",
    "cGcSolarSystem::OnEnterPlanetOrbit": "48 8B C4 55 41 54 48 8D A8 A8",
    "cGcSolarSystem::OnLeavePlanetOrbit": "48 89 5C 24 20 55 56 57 41 55 41 57 48 8B EC 48 83 EC 60",
    "cGcApplication::Update": "40 53 48 83 EC 20 E8 ?? ?? ?? ?? 48 89",
    "cTkFSMState::StateChange": "4C 8B 51 18 4D 8B D8 48 8B 05 ?? ?? ?? ?? 4D 8D 42 18 49 39 40 08 75 1C 48 8B 05 ?? ?? ?? ?? 49 39 00 75 10 0F 10 02 4D 89 5A 28 45 88 4A 30 41 0F 11 00 C3 48 8D 0D ?? ?? ?? ?? E9 ?? ?? ?? ??",
    "cGcSpaceshipComponent::UpdateLanding": "F3 0F 11 4C 24 10 55 41 56 41",
    "cGcGameState::GetPlayerFreighterOwnership": {
        "cGcGameState *, int": "48 83 EC 48 4C 8B D1 83 FA 03 77 4A 48 63 C2 4C 69 C8 A0",
    },
    "cGcPlayerVehicleOwnership::GetPlayerVehicleName": {
        "cGcPlayerVehicleOwnership *": "40 53 48 83 EC 20 48 8B 05 ?? ?? ?? ?? 48 63 98",  # 0x4DA610
        "cGcPlayerVehicleOwnership *, eVehicleType": "40 53 48 83 EC 20 48 8B 05 ?? ?? ?? ?? 48 63 DA 48",  # 0x4DA660
    },
}