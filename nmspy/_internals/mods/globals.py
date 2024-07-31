# Load all the globals.

import logging

import pymhf.core._internal as _internal
from pymhf.core.memutils import map_struct
from nmspy.caching import globals_cache
import nmspy.common as nms
import nmspy.data.structs as structs
import nmspy.data.functions.hooks as hooks
from nmspy._types import NMSMod
from pymhf.gui.decorators import no_gui


@no_gui
class _INTERNAL_LoadGlobals(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Load globals for internal use"
    __version__ = "0.1"

    # @hooks.cTkMetaData.ReadGlobalFromFile[structs.cGcWaterGlobals].after
    # def read_water_globals(self, lpData: int, lpacFilename: bytes):
    #     logging.info(f"cGcWaterGlobals*: 0x{lpData:X}, filename: {lpacFilename}")
    #     globals_cache.set("GcWaterGlobals", lpData - _internal.BASE_ADDRESS)
    #     nms.GcWaterGlobals = map_struct(lpData, structs.cGcWaterGlobals)

    # TODO: Add others...
