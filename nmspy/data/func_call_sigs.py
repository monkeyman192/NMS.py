from ctypes import CFUNCTYPE
from ctypes import c_char, c_longlong, c_uint32, c_char_p, c_ulonglong, c_int32
import ctypes.wintypes as wintypes


FUNC_CALL_SIGS = {
    "cGcApplication::Construct": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "cGcApplication::Update": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "cGcApplicationGameModeSelectorState::UpdateStartUI": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "cGcGameState::LoadSpecificSave": CFUNCTYPE(
        c_char,
        c_longlong,
        c_uint32,
    ),
    "cTkMetaDataXML::GetLookup": CFUNCTYPE(
        c_longlong,
        c_char_p,
    ),
    "cTkMetaData::GetLookup": CFUNCTYPE(
        c_longlong,
        c_ulonglong,
    ),
    "cTkMetaData::Register": CFUNCTYPE(
        None,
        c_longlong,
        c_longlong,
        c_longlong,
        c_longlong,
        c_longlong,
        c_longlong,
        c_longlong,
        c_longlong,
        c_longlong,
        c_longlong,
    ),
    "cTkMetaData::ReadGlobalFromFile<cGcWaterGlobals>": CFUNCTYPE(
        c_longlong,
        c_longlong,
        c_char_p,
    ),
    "cTkDynamicGravityControl::Construct": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "AK::SoundEngine::PostEvent": CFUNCTYPE(
        c_longlong,
        c_uint32,
        c_ulonglong,
        c_uint32,
        c_ulonglong,
        c_ulonglong,
        c_uint32,
        c_longlong,
        c_uint32,
    ),
    "cTkAudioManager::Play": CFUNCTYPE(
        wintypes.BOOLEAN,
        c_longlong,  # cTkAudioManager *
        c_longlong,
        c_longlong,
    ),
    "cTkInputPort::SetButton": CFUNCTYPE(
        None,
        c_longlong,
        c_uint32,
    ),
    "cGcSolarSystem::Generate": CFUNCTYPE(
        None,
        c_longlong,
        wintypes.BOOLEAN,
        c_longlong,
    ),
    "cGcPlanet::SetupRegionMap": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "cTkMetaDataXML::Register": CFUNCTYPE(
        None,
        c_char_p,
        c_longlong,
        c_longlong,
        c_longlong,
    ),
}
