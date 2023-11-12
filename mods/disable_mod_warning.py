from nmspy.hooking import one_shot
from nmspy.memutils import map_struct
import nmspy.data.structs as nms_structs
import nmspy.data.function_hooks as hooks
from nmspy.mod_loader import NMSMod


class DisableModWarning(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Disable mod warning screen"
    __version__ = "1.0"
    __NMSPY_required_version__ = "0.6.0"

    @one_shot
    @hooks.cTkFileSystem.Construct.after
    def isModded(self, this, flags: int):
        fs = map_struct(this, nms_structs.cTkFileSystem)
        fs.data.contents.isModded = False
