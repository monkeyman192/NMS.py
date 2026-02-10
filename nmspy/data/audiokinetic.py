# pyright: reportReturnType=false
# pyright: reportArgumentType=false

# NMS uses AudioKinetic as a 3rd party audio library.
# This exposes a number of useful functions relating to audio.
# These functions are all the direct AK functions which are provided as exports by the binary.

import ctypes

from pymhf.core.hooking import Structure, static_function_hook


class AK(Structure):
    class SoundEngine(Structure):
        @static_function_hook(exported_name="?RegisterGameObj@SoundEngine@AK@@YA?AW4AKRESULT@@_KPEBD@Z")
        @staticmethod
        def RegisterGameObj(
            in_GameObj: ctypes.c_uint64,
            in_pszObjName: ctypes.c_uint64,
        ) -> ctypes.c_int64:
            pass

        @static_function_hook(
            exported_name=(
                "?PostEvent@SoundEngine@AK@@YAII_KIP6AXW4AkCallbackType@@PEAUAkCallbackInfo@@@ZPEAXIPEAUAkExt"
                "ernalSourceInfo@@I@Z"
            )
        )
        @staticmethod
        def PostEvent(
            in_ulEventID: ctypes.c_uint32,
            in_GameObjID: ctypes.c_uint64,
            in_uiFlags: ctypes.c_uint32 = 0,
            callback: ctypes.c_uint64 = 0,
            in_pCookie: ctypes.c_void_p = 0,
            in_cExternals: ctypes.c_uint32 = 0,
            in_pExternalSources: ctypes.c_uint64 = 0,
            in_PlayingID: ctypes.c_uint32 = 0,
        ) -> ctypes.c_uint64:
            pass
