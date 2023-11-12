import logging
# import asyncio

import nmspy.common as nms
import nmspy.data.structs as structs
import nmspy.data.function_hooks as hooks
from nmspy.hooking import one_shot, hook_manager
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
        # try:
        #     loop = asyncio.get_event_loop()
        #     logging.info(loop)
        # except (RuntimeError, ValueError) as e:
        #     logging.info("bad loop!")
        # TODO: map to the struct.
        # nms.gravity_singleton = map_struct(this, local_types.cTkDynamicGravityControl)

    @one_shot
    @hooks.cGcApplication.cGcApplication.before
    def load_cGcApplication(self, this):
        logging.info(f"cGcApplication constructor: 0x{this:X}")
        logging.info(f"Diff: 0x{this - nms.BASE_ADDRESS:X}")
        nms.GcApplication = this + 0x50  # WHY??

    @hooks.cGcApplication.Update
    def _main_loop(self, *args):
        """ The main application loop. Run any before or after functions here. """
        for func in hook_manager.main_loop_before_funcs:
            func()
        hooks.cGcApplication.Update.original(*args)
        for func in hook_manager.main_loop_after_funcs:
            func()
