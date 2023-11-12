from ctypes import c_char, c_longlong, c_uint32, c_char_p, c_ulonglong, c_int32, c_float
import ctypes.wintypes as wintypes
from typing import Union

from collections import namedtuple

FUNCTION_DEF = namedtuple("FUNCTION_DEF", ["restype", "argtypes"])


FUNC_CALL_SIGS: dict[str, Union[FUNCTION_DEF, dict[str, FUNCTION_DEF]]] = {
    "cGcApplication::Construct": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong],
    ),
    "cGcApplication::Update": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong],
    ),
    "cGcApplication::cGcApplication": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong],
    ),
    "cGcApplicationGameModeSelectorState::UpdateStartUI": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong],
    ),
    "cGcGameState::LoadSpecificSave": FUNCTION_DEF(
        restype=c_char,
        argtypes=[
            c_longlong,
            c_uint32,
        ]
    ),
    "cGcGameState::LoadSpecificSave": FUNCTION_DEF(
        restype=c_char,
        argtypes=[
            c_longlong,
            c_uint32,
        ]
    ),
    "cTkMetaDataXML::GetLookup": FUNCTION_DEF(
        restype=c_longlong,
        argtypes=[c_char_p]
    ),
    "cTkMetaData::GetLookup": FUNCTION_DEF(
        restype=c_longlong,
        argtypes=[c_ulonglong]
    ),
    "cTkMetaData::Register": FUNCTION_DEF(
        restype=None,
        argtypes=[
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
        ]
    ),
    "nvgBeginFrame": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            c_int32,
            c_int32,
            wintypes.FLOAT,
        ]
    ),
    "nvgBeginPath": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong]
    ),
    "nvgRect": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            wintypes.FLOAT,
            wintypes.FLOAT,
            wintypes.FLOAT,
            wintypes.FLOAT,
        ]
    ),
    "nvgFillColor": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            c_longlong,
        ]
    ),
    "nvgFill": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong]
    ),
    "nvgEndFrame": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong]
    ),
    "nvgText": FUNCTION_DEF(
        restype=wintypes.FLOAT,
        argtypes=[
            c_longlong,
            wintypes.FLOAT,
            wintypes.FLOAT,
            c_char_p,
            c_char_p,
        ]
    ),
    "cGcApplicationDeathState::Update": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            wintypes.DOUBLE,
        ]
    ),
    "cTkMetaData::ReadGlobalFromFile<cGcWaterGlobals>": FUNCTION_DEF(
        restype=c_longlong,
        argtypes=[
            c_longlong,
            c_char_p,
        ]
    ),
    "cTkDynamicGravityControl::Construct": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong]
    ),
    "AK::SoundEngine::PostEvent": FUNCTION_DEF(
        restype=c_longlong,
        argtypes=[
            c_uint32,
            c_ulonglong,
            c_uint32,
            c_ulonglong,
            c_ulonglong,
            c_uint32,
            c_longlong,
            c_uint32,
        ]
    ),
    "cTkAudioManager::Play": FUNCTION_DEF(
        restype=wintypes.BOOLEAN,
        argtypes=[
            c_longlong,  # cTkAudioManager *
            c_longlong,
            c_longlong,
        ]
    ),
    "cTkInputPort::SetButton": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            c_uint32,
        ]
    ),
    "cGcSolarSystem::Generate": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            wintypes.BOOLEAN,
            c_longlong,
        ]
    ),
    "cGcPlanet::SetupRegionMap": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong]
    ),
    "cTkMetaDataXML::Register": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_char_p,
            c_longlong,
            c_longlong,
            c_longlong,
        ]
    ),
    "cGcApplicationGameModeSelectorState::RenderWarning": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            c_char_p,
            c_char_p,
            c_char_p,
            c_char_p,
            wintypes.FLOAT,
        ]
    ),
    "cGcApplicationGameModeSelectorState::RenderWarningMessages": FUNCTION_DEF(
        restype=None,
        argtypes=[c_longlong]
    ),
    "cTkFileSystem::IsModded": FUNCTION_DEF(
        restype=wintypes.BOOLEAN,
        argtypes=[c_longlong]
    ),
    "cTkFileSystem::Construct": FUNCTION_DEF(
        restype=None,
        argtypes=[
            c_longlong,
            c_int32,
        ]
    ),
}
