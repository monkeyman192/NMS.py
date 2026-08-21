# NOTE: This mod is here mostly as a reference. It is not complete but it may be useful for anyone wanting to
# look at making a mod to do stuff with the inventory.

import colorsys
from ctypes import _Pointer, byref
from dataclasses import dataclass
from logging import getLogger

from pymhf import Mod, ModState
from pymhf.core.memutils import get_addressof
from pymhf.gui.decorators import INTEGER, gui_button

import nmspy.data.basic_types as basics
import nmspy.data.enums as enums
import nmspy.data.exported_types as nmse
import nmspy.data.types as nms
from nmspy.common import gameData

logger = getLogger("InventoryMod")


def rainbow():
    theta = 0
    while True:
        hue = theta / 360
        yield colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        theta += 1


@dataclass
class InventoryState(ModState):
    inventory_index: int = 0
    x: int = 0
    y: int = 0


class InventoryMod(Mod):
    __author__ = "monkeyman192"
    __description__ = "A WIP mod which can be used to access inventory data"

    inventory_state = InventoryState()

    def __init__(self):
        super().__init__()
        self._supercharged_slot_index = 0
        self.rainbow = rainbow()
        self.supercharged_colour = basics.Colour(0, 0, 0, 0)

    @property
    @INTEGER("Inventory index")
    def inventory_index(self):
        return self.inventory_state.inventory_index

    @inventory_index.setter
    def inventory_index(self, value):
        self.inventory_state.inventory_index = value

    @property
    @INTEGER("Supercharged slot index")
    def supercharged_slot_index(self):
        return self._supercharged_slot_index

    @supercharged_slot_index.setter
    def supercharged_slot_index(self, value: int):
        self._supercharged_slot_index = value

    @property
    @INTEGER("Slot X")
    def slot_x(self):
        return self.inventory_state.x

    @slot_x.setter
    def slot_x(self, value):
        self.inventory_state.x = value

    @property
    @INTEGER("Slot Y")
    def slot_y(self):
        return self.inventory_state.y

    @slot_y.setter
    def slot_y(self, value):
        self.inventory_state.y = value

    @gui_button("press me")
    def press(self):
        if (ps := gameData.player_state) is not None:
            self.pymhf_gui.hex_view.add_snapshot(get_addressof(ps))
            logger.info("Inventories with something in them:")
            for i, inventory in enumerate(ps.mInventories):
                store = inventory.mStore
                if len(store) > 0:
                    logger.info(
                        f"Inventory ({i}) | Width: {inventory.miWidth} Height: {inventory.miHeight}, "
                        f"capacity: {inventory.miCapacity}"
                    )
                    logger.info(
                        f"Inventory store ({store.vector_size}/{store.allocated_size}). Next free address: "
                        f"0x{store._next_empty_addr:X}"
                    )
                    for item in store:
                        idx = item.Index
                        logger.info(f"Item: {item.Id}, Index: ({idx.X} {idx.Y}), Amount: {item.Amount}")
                    logger.info("BITARRAY:")
                    for bitarray in inventory.mxValidSlots:
                        if ones := bitarray.ones():
                            logger.info(f"addr: 0x{get_addressof(bitarray):X} -> {ones}")
                if len(inventory.maSpecialSlots) > 0:
                    logger.info(f"Special slots (@ 0x{get_addressof(inventory.maSpecialSlots):X}):")
                    for special_slot in inventory.maSpecialSlots:
                        idx = special_slot.Index
                        logger.info(f"Location: ({idx.X} {idx.Y}), Type: {special_slot.Type.name}")

    @gui_button("Add a thing")
    def add_a_thing(self):
        if (ps := gameData.player_state) is not None:
            inventory = ps.mInventories[self.inventory_state.inventory_index]
            if len(inventory.mStore) > 0:
                new_obj = nmse.cGcInventoryElement(
                    basics.TkID0x10(b"SPACEGUNK1"),
                    nmse.cGcInventoryIndex(self.inventory_state.x, self.inventory_state.y),
                    123,
                    1.0,
                    9999,
                    enums.cGcInventoryType.Substance,
                    False,
                    True,
                )
                inventory.mStore.add(new_obj)
                inventory.mxValidSlots[self.inventory_state.y][self.inventory_state.x] = True

    @gui_button("Toggle supercharged slot")
    def toggle_supercharged(self):
        if (ps := gameData.player_state) is not None:
            inventory = ps.mInventories[self.inventory_state.inventory_index]
            scslots = [(slot.Index.X, slot.Index.Y) for slot in inventory.maSpecialSlots]
            if (coord := (self.inventory_state.x, self.inventory_state.y)) in scslots:
                del inventory.maSpecialSlots[scslots.index(coord)]
            else:
                new_slot = nmse.cGcInventorySpecialSlot(
                    nmse.cGcInventoryIndex(self.inventory_state.x, self.inventory_state.y), 4
                )
                inventory.maSpecialSlots.append(new_slot)

    @gui_button("Toggle slot activation")
    def toggle_activation(self):
        if (ps := gameData.player_state) is not None:
            inventory = ps.mInventories[self.inventory_state.inventory_index]
            if len(inventory.mStore) > 0:
                current_state = inventory.mxValidSlots[self.inventory_state.y][self.inventory_state.x]
                logger.info(
                    f"Changing ({self.inventory_state.x}, {self.inventory_state.y}) to "
                    f"{int(not current_state)}"
                )
                inventory.mxValidSlots[self.inventory_state.y][self.inventory_state.x] = bool(
                    not current_state
                )

    @gui_button("Increment selected inventory slot")
    def increment_slot(self):
        if (ps := gameData.player_state) is not None:
            inventory = ps.mInventories[self.inventory_state.inventory_index]
            if len(inventory.mStore) > 0:
                found = False
                for item in inventory.mStore:
                    if item.Index.X == self.inventory_state.x and item.Index.Y == self.inventory_state.y:
                        found = True
                        item.Amount += 1
                        logger.info(f"Added 1 to {item.Id}")
                        break
                if not found:
                    logger.error(
                        f"Could not find at item in the inventory at ({self.inventory_state.x}, "
                        f"{self.inventory_state.y})"
                    )

            else:
                logger.error("Nothing in specified inventory")

    @nms.cGcFrontendPageFunctions.SetPopupBasics.before
    def before_SetPopupBasics(
        self,
        lpParentLayer,
        lpacTitle,
        lColour: _Pointer[basics.Colour],
        lpacDescription,
        lpacSubtitle,
        lpacType,
        lpacTechTreeCost,
        lpacTechTreeCostAlt,
        lbSpecialSubtitle,
        liAmountToShow,
        lLayerIDOverride,
    ):
        # logger.info(f"Popup: {lpacTitle} with colour: {lColour.contents}")
        if str(lpacTitle) == "UI_SUPERSLOT_TITLE":
            # colour_ptr = lColour
            r, g, b = next(self.rainbow)
            self.supercharged_colour.update(r, g, b, 1)
            colour_ptr = byref(self.supercharged_colour)
        else:
            colour_ptr = lColour
        return (
            lpParentLayer,
            lpacTitle,
            colour_ptr,
            lpacDescription,
            lpacSubtitle,
            lpacType,
            lpacTechTreeCost,
            lpacTechTreeCostAlt,
            lbSpecialSubtitle,
            liAmountToShow,
            lLayerIDOverride,
        )
