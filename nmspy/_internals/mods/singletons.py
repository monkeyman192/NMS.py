import logging

import nmspy.common as nms
import nmspy.data.structs as structs
import nmspy.data.function_hooks as hooks
from nmspy.hooking import one_shot, disable
from nmspy.memutils import map_struct
from nmspy.mod_loader import NMSMod


class _INTERNAL_LoadSingletons(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Load singletons and other important objects"
    __version__ = "0.1"

    @one_shot
    @hooks.cTkDynamicGravityControl.Construct.before
    def load_gravity_singleton(self, this):
        logging.info("Loaded grav singleton")
        nms.gravity_singleton = this
        # TODO: map to the struct.
        # nms.gravity_singleton = map_struct(this, local_types.cTkDynamicGravityControl)

    @one_shot
    @hooks.cGcApplication.cGcApplication.before
    def load_cGcApplication(self, this):
        logging.info(f"cGcApplication constructor: 0x{this:X}")
        logging.info(f"Diff: 0x{this - nms.BASE_ADDRESS:X}")
        nms.GcApplication = this + 0x50  # WHY??

    @disable
    @hooks.cGcApplication.Update.before
    def _main_loop_pre(self, _):
        logging.info("before update")

    # @hooks.cGcApplication.Update.after
    # def _main_loop_post(self, _):
    #     logging.info("after update")
