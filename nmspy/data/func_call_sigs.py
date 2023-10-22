from ctypes import CFUNCTYPE
from ctypes import c_char, c_longlong, c_uint32, c_char_p, c_ulonglong, c_int32, c_float
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
    "cGcApplication::cGcApplication": CFUNCTYPE(
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
    "nvgBeginFrame": CFUNCTYPE(
        None,
        c_longlong,
        c_int32,
        c_int32,
        wintypes.FLOAT,
    ),
    "nvgBeginPath": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "nvgRect": CFUNCTYPE(
        None,
        c_longlong,
        wintypes.FLOAT,
        wintypes.FLOAT,
        wintypes.FLOAT,
        wintypes.FLOAT,
    ),
    "nvgFillColor": CFUNCTYPE(
        None,
        c_longlong,
        c_longlong,
    ),
    "nvgFill": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "nvgEndFrame": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "nvgText": CFUNCTYPE(
        wintypes.FLOAT,
        c_longlong,
        wintypes.FLOAT,
        wintypes.FLOAT,
        c_char_p,
        c_char_p,
    ),
    "cGcApplicationDeathState::Update": CFUNCTYPE(
        None,
        c_longlong,
        wintypes.DOUBLE,
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
    "cGcApplicationGameModeSelectorState::RenderWarning": CFUNCTYPE(
        None,
        c_longlong,
        c_char_p,
        c_char_p,
        c_char_p,
        c_char_p,
        wintypes.FLOAT,
    ),
    "cGcApplicationGameModeSelectorState::RenderWarningMessages": CFUNCTYPE(
        None,
        c_longlong,
    ),
    "cTkFileSystem::IsModded": CFUNCTYPE(
        wintypes.BOOLEAN,
        c_longlong,
    ),
    "cTkFileSystem::Construct": CFUNCTYPE(
        None,
        c_longlong,
        c_int32,
    ),
}
