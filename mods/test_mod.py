import logging
import ctypes

import nmspy.data.function_hooks as hooks
from nmspy.hooking import disable, main_loop, on_key_pressed, on_key_release
from nmspy.memutils import map_struct
import nmspy.data.structs as nms_structs
from nmspy.mod_loader import NMSMod, ModState
from nmspy.calling import call_function


class TestModState(ModState):
    def __init__(self):
        self.value: int = 1


@disable
class TestMod(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "A simple test mod"
    __version__ = "0.1"
    __NMSPY_required_version__ = "0.6.0"

    state = TestModState()

    def __init__(self):
        super().__init__()
        self.text: str = "NO"
        self.should_print = False

    @property
    def _text(self):
        return self.text.encode()

    @on_key_pressed("space")
    def press(self):
        self.text = f"BBB {self.state.value}"

    @on_key_release("space")
    def release(self):
        self.text = "NO"
        self.state.value += 1

    @hooks.nvgText
    def change_test(self, ctx, x: float, y: float, string, end):
        if string == b"Options":
            string = ctypes.c_char_p(b"Hi")
            call_function("nvgText", ctx, x + 30, y, ctypes.c_char_p(self._text), end)
        return hooks.nvgText.original(ctx, x, y, string, end)

    # @nvgText.before
    # def change_test_after(self, ctx, x: float, y: float, string, end):
    #     # logging.info("change_test")
    #     logging.info(string)
    #     # logging.info(self._text)
    #     if string == b"Options":
    #         string = ctypes.c_char_p(b"Hi")
    #         call_function("nvgText", ctx, x + 30, y, ctypes.c_char_p(self._text), end)
    #     logging.info("about to return")
    #     return (ctx, x, y, string, end)

    # @hook_function("nvgEndFrame")
    # class nvgHook(NMSHook):
    #     def detour(self, ctx):
    #         # Draw something somewhere
    #         call_function("nvgBeginPath", ctx)
    #         call_function("nvgRect", ctx, 100, 100, 100, 100)
    #         colour = nms_structs.NVGColor(r=1, g=0, b=0, a=1)
    #         colour_addr = ctypes.addressof(colour)
    #         logging.info(colour_addr)
    #         call_function("nvgFillColor", ctx, colour_addr)
    #         call_function("nvgFill", ctx)
    #         logging.info("Drew a rectangle?")
    #         ret = self.original(ctx)
    #         logging.info(f"nvgEnd: ctx: {ctx}")
    #         return ret

    @hooks.cGcPlanet.SetupRegionMap.after
    @disable
    def detour(self, this):
        logging.info(f"cGcPlanet*: {this}")
        planet = map_struct(this, nms_structs.cGcPlanet)
        logging.info(f"Planet {planet.planetIndex} name: {planet.planetData.name}")

    # @cGcPlanet.SetupRegionMap
    # def setup_regions(self, this):
    #     logging.info(f"cGcPlanet*: {this}")
    #     ret = cGcPlanet.SetupRegionMap.original(this)
    #     planet = map_struct(this, nms_structs.cGcPlanet)
    #     logging.info(f"Planet {planet.planetIndex} name: {planet.planetData.name}")
    #     return ret

    @main_loop.before
    def do_something(self):
        if self.should_print:
            logging.info(self.text)
