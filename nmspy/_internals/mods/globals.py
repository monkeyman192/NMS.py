# Load all the globals.

import logging

from nmspy.caching import globals_cache
import nmspy.common as nms
import nmspy.data.structs as structs
import nmspy.data.function_hooks as hooks
from nmspy.memutils import map_struct
from nmspy.mod_loader import NMSMod


class _INTERNAL_LoadGlobals(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Load globals for internal use"
    __version__ = "0.1"

    @hooks.cTkMetaData.ReadGlobalFromFile[structs.cGcWaterGlobals]
    def read_water_globals(self, lpData: int, lpacFilename: bytes):
        logging.info(f"cGcWaterGlobals*: 0x{lpData:X}, filename: {lpacFilename}")
        globals_cache.set("GcWaterGlobals", lpData - nms.BASE_ADDRESS)
        ret = hooks.cTkMetaData.ReadGlobalFromFile[structs.cGcWaterGlobals].original(lpData, lpacFilename)
        data = map_struct(lpData, structs.cGcWaterGlobals)
        nms.GcWaterGlobals = data
        for field in data._fields_:
            logging.info(f"{field[0]}: {getattr(data, field[0])}")
        nms.GcWaterGlobals.UseNewWater = False
        return ret
