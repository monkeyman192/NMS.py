from nmspy.hooking import cTkFileSystem, one_shot_func
from nmspy.memutils import map_struct
import nmspy.data.structs as nms_structs
from nmspy.mod_loader import NMSMod


class DisableModWarning(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Disable mod warning screen"
    __version__ = "1.0"

    @one_shot_func
    @cTkFileSystem.Construct.after
    def isModded(self, this, flags: int):
        fs = map_struct(this, nms_structs.cTkFileSystem)
        fs.data.contents.isModded = False
