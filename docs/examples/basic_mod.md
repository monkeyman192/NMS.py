# First Mod

Our first mod will be something simple which will demonstate a number of concepts.

```py
import nmspy.data.function_hooks as hooks
from nmspy.hooking import disable, main_loop, on_key_pressed, on_key_release
from nmspy.memutils import map_struct
import nmspy.data.structs as nms_structs
from nmspy.mod_loader import NMSMod


@disable
class TestMod(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "A simple test mod"
    __version__ = "0.1"

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

    @hooks.cGcPlanet.SetupRegionMap.after
    @disable
    def detour(self, this):
        logging.info(f"cGcPlanet*: {this}")
        planet = map_struct(this, nms_structs.cGcPlanet)
        logging.info(f"Planet {planet.planetIndex} name: {planet.planetData.name}")

    @main_loop.before
    def do_something(self):
        if self.should_print:
            logging.info(self.text)
```
