import logging
import ctypes
import traceback

from nmspy.hooking import NMSHook, hook_function, main_loop, cGcPlanet, nvgText
from nmspy.memutils import map_struct, get_addressof
import nmspy.data.structs as nms_structs
from nmspy.mod_loader import NMSMod
from nmspy.calling import call_function


class TestMod(NMSMod):

    __author__ = "monkeyman192"
    __description__ = "A simple test mod"
    __version__ = "0.1"

    def __init__(self):
        super().__init__()
        self.text: str = "mm"
        self.should_print = False

    @property
    def _text(self):
        return self.text.encode()

    # @hook_function("nvgText")
    # class nvgHook(NMSHook):
    #     mod: "TestMod"

    #     def detour(self, ctx, x: float, y: float, string, end):
    #         if string == b"Options":
    #             string = ctypes.c_char_p(b"Hi")
    #             call_function("nvgText", ctx, x + 30, y, ctypes.c_char_p(self.mod._text), end)
    #         return self.original(ctx, x, y, string, end)

    @nvgText
    def change_test(self, ctx, x: float, y: float, string, end):
        if string == b"Options":
            string = ctypes.c_char_p(b"Hi")
            call_function("nvgText", ctx, x + 30, y, ctypes.c_char_p(self._text), end)
        return nvgText.original(ctx, x, y, string, end)

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

    @hook_function("cGcPlanet::SetupRegionMap")
    class PlanetSetup(NMSHook):
        def detour(self, this):
            logging.info(f"cGcPlanet*: {this}")
            ret = self.original(this)
            planet = map_struct(this, nms_structs.cGcPlanet)
            logging.info(f"Planet {planet.planetIndex} name: {planet.planetData.name}")
            return ret

    # @cGcPlanet.SetupRegionMap
    # def setup_regions(self, this):
    #     logging.info(f"cGcPlanet*: {this}")
    #     ret = cGcPlanet.SetupRegionMap.original(this)
    #     planet = map_struct(this, nms_structs.cGcPlanet)
    #     logging.info(f"Planet {planet.planetIndex} name: {planet.planetData.name}")
    #     return ret

    @main_loop
    def do_something(self):
        if self.should_print:
            logging.info(self.text)
