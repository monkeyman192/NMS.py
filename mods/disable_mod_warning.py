from pymhf.core.hooking import one_shot
from pymhf.core.memutils import map_struct
from pymhf.gui import no_gui
import nmspy.data.structs as nms_structs
import nmspy.data.functions.hooks as hooks
from nmspy import NMSMod


@no_gui
class DisableModWarning(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Disable mod warning screen"
    __version__ = "1.0"
    __NMSPY_required_version__ = "0.7.0"

    @one_shot
    @hooks.cTkFileSystem.Construct.after
    def isModded(self, this, flags: int):
        fs = map_struct(this, nms_structs.cTkFileSystem)
        fs.data.contents.isModded = False
