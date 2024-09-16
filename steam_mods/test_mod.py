import logging
from dataclasses import dataclass

from pymhf.core.calling import call_function
from pymhf.core.hooking import disable, manual_hook, one_shot
from nmspy.decorators import main_loop
from pymhf.core.mod_loader import ModState
from nmspy import NMSMod
from pymhf.gui.decorators import INTEGER, gui_button, STRING
import nmspy.data.functions.hooks as hooks


@dataclass
class TestModState(ModState):
    takeoff_cost = 50
    val = "HI"


@disable
class TakeOffCost(NMSMod):
    __author__ = "monkeyman192"
    __description__ = "Modify the spaceship takeoff cost"
    __version__ = "0.1"
    __NMSPY_required_version__ = "0.7.0"

    state = TestModState()

    def __init__(self):
        super().__init__()
        self.player_state = 0
        self.val = 0

    @gui_button("Remove doots")
    def remove_units(self):
        logging.info("Calling remove doots function")
        if self.player_state:
            logging.info("Removing 100 units")
            call_function(
                "cGcPlayerState::RemoveUnits",
                self.player_state,
                100,
            )

    @gui_button("Log val")
    def log_hi(self):
        logging.info(f"VAL: {self.state.val}")

    @property
    @STRING("Value: ", uppercase=True)
    def mystring(self):
        return self.state.val

    @mystring.setter
    def mystring(self, value):
        self.state.val = value

    @property
    @INTEGER("Launch Cost: ")
    def takeoff_cost(self):
        return self.state.takeoff_cost

    @takeoff_cost.setter
    def takeoff_cost(self, value):
        logging.info(value)
        self.state.takeoff_cost = value

    @hooks.cGcSpaceshipComponent.GetTakeOffCost.after
    def get_takeoff_cost_after(self, this):
        return self.state.takeoff_cost

    @hooks.cGcPlayerVehicleOwnership.GetPlayerVehicleName.overload("cGcPlayerVehicleOwnership *").after
    def after_vehicle_name_1(self, *args):
        logging.info("Getting vehicle name with overload 1")

    @hooks.cGcPlayerVehicleOwnership.GetPlayerVehicleName.overload("cGcPlayerVehicleOwnership *, eVehicleType").after
    def after_vehicle_name_2(self, *args):
        logging.info("Getting vehicle name with overload 2")

    @hooks.cGcPlayerState.AwardUnits.after
    def AwardUnits(self, this, liChange, _result_):
        logging.info(f"AwardUnits: 0x{this:X}: {liChange} -> {_result_}")

    @hooks.cGcPlayerState.RemoveUnits.after
    def RemoveUnits(self, this, liChange, _result_):
        logging.info(f"RemoveUnits: 0x{this:X}: {liChange} -> {_result_}")

    @hooks.cGcPlayerState.Construct.after
    def ConstructPlayerState(self, this):
        logging.info(f"Setting player state: 0x{this:X}")
        self.player_state = this

    @main_loop.after
    def after_main(self):
        if self.val < 100:
            logging.info(self.val)
            self.val += 1
