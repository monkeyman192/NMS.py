# /// script
# dependencies = ["pymhf[gui]>=0.1.16"]
#
# [tool.pymhf]
# exe = "NMS.exe"
# steam_gameid = 275850
# start_paused = false
#
# [tool.pymhf.gui]
# always_on_top = true
#
# [tool.pymhf.logging]
# log_dir = "."
# log_level = "info"
# window_name_override = "NMS audio thing"
# ///
from __future__ import annotations

import ctypes
import logging
from dataclasses import dataclass

from pymhf import Mod, ModState
from pymhf.core.hooking import disable
from pymhf.core.utils import set_main_window_active
from pymhf.gui.decorators import BOOLEAN, STRING, gui_button, gui_combobox

from nmspy.data.audiokinetic import AK
from nmspy.data.enums import cGcAudioWwiseEvents
import nmspy.data.types as nms

logger = logging.getLogger("AudioNames")


AUDIO_EVENTS = {i.name: i.value for i in cGcAudioWwiseEvents}
AUDIO_EVENTS_REV = {i.value: i.name for i in cGcAudioWwiseEvents}
EVENT_NAMES = [i.name for i in cGcAudioWwiseEvents]


@dataclass
class AudioState(ModState):
    event_id: int = 0
    obj_id: int = 0
    log_sounds: bool = False


class AudioNames(Mod):
    __author__ = "monkeyman192"
    __description__ = "Log (almost) all audio events when they happen"
    __version__ = "0.1"

    state = AudioState()

    def __init__(self):
        super().__init__()
        self.audio_manager = None

    @gui_combobox("Audio ID:", items=EVENT_NAMES)
    def select_audio_id(self, sender, app_data: str, user_data):
        event_id = AUDIO_EVENTS.get(app_data, 0)
        self.state.event_id = event_id

    @gui_button("Play sound")
    def play_sound(self):
        if self.state.event_id and self.state.obj_id and self.audio_manager is not None:
            set_main_window_active()
            audioid = nms.TkAudioID()
            audioid.muID = self.state.event_id
            self.audio_manager.Play(
                event=ctypes.byref(audioid), object=self.state.obj_id
            )

    @property
    @STRING("Event ID", decimal=True)
    def event_id(self):
        return self.state.event_id

    @event_id.setter
    def event_id(self, value):
        self.state.event_id = int(value)

    @property
    @STRING("Object ID", decimal=True)
    def obj_id(self):
        return self.state.obj_id

    @obj_id.setter
    def obj_id(self, value):
        self.state.obj_id = int(value)

    @property
    @BOOLEAN("Log sounds")
    def log_sounds(self):
        return self.state.log_sounds

    @log_sounds.setter
    def log_sounds(self, value):
        self.state.log_sounds = value

    @AK.SoundEngine.PostEvent.before
    def play_event(self, in_ulEventID, in_GameObjID, *args):
        if self.state.log_sounds:
            event_id = in_ulEventID
            event_name = AUDIO_EVENTS_REV.get(event_id, "unknown event thing...")
            logger.info(f"Event ID: {in_ulEventID}, Object ID: {in_GameObjID} -> {event_name}")

    @disable
    @AK.SoundEngine.RegisterGameObj.before
    def register_object(self, in_GameObj, in_pszObjName):
        if self.state.log_sounds:
            logger.info(f"{in_GameObj} name: {ctypes.c_char_p(in_pszObjName).value}")

    @nms.cTkAudioManager.Play.after
    def after_play(
        self,
        this: ctypes._Pointer[nms.cTkAudioManager],
        event: ctypes._Pointer[nms.TkAudioID],
        object_,
    ):
        self.audio_manager = this.contents
