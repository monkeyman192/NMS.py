import ctypes
import re
import struct
from typing import Union, TypeVar, Type

import nmspy.data.exported_types as nms_types
from pymhf.core._internal import BASE_ADDRESS, BINARY_PATH

import logging

logger = logging.getLogger(__name__)

STATIC_BASE = 0x140000000


CTYPES = Union[ctypes._SimpleCData, ctypes.Structure, ctypes._Pointer, ctypes.Array]
Struct = TypeVar("Struct", bound=CTYPES)


def _map_struct(offsets: dict[str, int], name: str, type_: Type[Struct]) -> Struct:
    """Modified version of `pymhf.core.memutils.map_struct` to raise a warning instead of an error."""
    offset = offsets.get(name)
    if not offset:
        logger.warning(
            f"Could not find the global {name} in memory. This may cause issues..."
        )
        return  # type: ignore
    instance = ctypes.cast(BASE_ADDRESS + offset, ctypes.POINTER(type_))
    return instance.contents


def extract_global_offsets() -> dict[str, int]:
    """Extract the offsets within the binary to various globals."""
    try:
        with open(BINARY_PATH, "rb") as f:
            whole_file = f.read()
    except:  # noqa
        logger.exception(
            "There was an error reading the binary. No globals will be mapped."
        )
        return {}

    # Read some section data
    # .rdata
    rdata_hdr = whole_file.find(b".rdata")
    rdata_size, rdata_offset, _, rdata_ptr_address = struct.unpack_from(
        "<IIII", whole_file, offset=rdata_hdr + 8
    )
    rdata_virtual_offset = rdata_offset - rdata_ptr_address
    rdata = whole_file[rdata_offset : rdata_offset + rdata_size]

    # .data
    data_hdr = whole_file.find(b".data")
    data_size, data_offset, _, data_ptr_address = struct.unpack_from(
        "<IIII", whole_file, offset=data_hdr + 8
    )
    data_virtual_offset = data_offset - data_ptr_address
    data = whole_file[data_offset : data_offset + data_size]

    # .text
    text_hdr = whole_file.find(b".text")
    text_size, text_offset, _, text_ptr_address = struct.unpack_from(
        "<IIII", whole_file, offset=text_hdr + 8
    )
    text_virtual_offset = text_offset - text_ptr_address
    text = whole_file[text_offset : text_offset + text_size]

    def addr_conv(addr: int, segment: str):
        # Convert the address to the address including base and virtual offset.
        if segment == ".rdata":
            return STATIC_BASE + rdata_offset + addr + rdata_virtual_offset
        elif segment == ".data":
            return STATIC_BASE + data_offset + addr + data_virtual_offset
        elif segment == ".text":
            return STATIC_BASE + text_offset + addr + text_virtual_offset
        else:
            raise ValueError

    offsets = {}

    # Unfortunately HG are not consistent with naming. This seems to get all of them though.
    re_strings = [
        rb"/(\w+)\.global\.mbin\x00",
        rb"/(\w+)\.globals\.mbin\x00",
        rb"/(\w+Globals).mbin\x00",
    ]

    for re_string in re_strings:
        for m in re.finditer(re_string, rdata, flags=re.IGNORECASE):
            name = m.group(1).decode()
            addr = addr_conv(m.span()[0], ".rdata")
            found_addr = addr_conv(data.find(struct.pack("<Q", addr)), ".data")
            offsets[found_addr] = name

    # Next, we need to look over the entire .text section for the `mov rdx,QWORD PTR` instruction.
    # This looks like `48 8B 15` in bytes.
    # We then read the proceeding 4 bytes and add this relative jump to the address of the instruction
    # resolved to the segment.
    # This final address will then be able to matched against the list of known addresses.

    return_data = {}

    found_count = 0
    for m in re.finditer(rb"\x48\x8B\x15", text):
        found_count += 1
        addr = m.span()[0]
        ptr = struct.unpack_from("<I", text, offset=addr + 3)[0]
        ida_addr = addr_conv(addr, ".text")
        # Add 7 since the ptr is relative to the start of the next instruction.
        result = ida_addr + ptr + 7
        if (name := offsets.get(result)) is not None:
            # Now, read the next 7 bytes. We should have `lea rcx,[rip+0xXXX]`
            # Read the pointer and again resolve to the correct region.
            # Add 10 = 7 + 3 (3 bytes for 48 8D 0D instruction)
            global_ptr = struct.unpack_from("<I", text, offset=addr + 10)[0]
            global_addr = addr_conv(addr + 14, ".text") + global_ptr
            logger.debug(f"{name} found at 0x{global_addr - STATIC_BASE:X}")
            return_data[name] = global_addr - STATIC_BASE

    return return_data


offsets = extract_global_offsets()

gGcAISpaceshipGlobals = _map_struct(
    offsets, "GcAISpaceshipGlobals", nms_types.cGcAISpaceshipGlobals
)
gGcAtlasGlobals = _map_struct(offsets, "GcAtlasGlobals", nms_types.cGcAtlasGlobals)
gGcAudioGlobals = _map_struct(offsets, "GcAudioGlobals", nms_types.cGcAudioGlobals)
gGcBuildableShipGlobals = _map_struct(
    offsets, "GcBuildableShipGlobals", nms_types.cGcBuildableShipGlobals
)
gGcBuildingGlobals = _map_struct(
    offsets, "GcBuildingGlobals", nms_types.cGcBuildingGlobals
)
gGcCameraGlobals = _map_struct(offsets, "GcCameraGlobals", nms_types.cGcCameraGlobals)
gGcCharacterGlobals = _map_struct(
    offsets, "GcCharacterGlobals", nms_types.cGcCharacterGlobals
)
gGcCreatureGlobals = _map_struct(
    offsets, "GcCreatureGlobals", nms_types.cGcCreatureGlobals
)
gGcCollisionTable = _map_struct(
    offsets, "GcCollisionTable", nms_types.cGcCollisionTable
)
gGcDebugEditorGlobals = _map_struct(
    offsets, "GcDebugEditorGlobals", nms_types.cGcDebugEditorGlobals
)
gGcDebugOptions = _map_struct(offsets, "GcDebugOptions", nms_types.cGcDebugOptions)
gGcEffectsGlobals = _map_struct(
    offsets, "GcEffectsGlobals", nms_types.cGcEffectsGlobals
)
gGcEnvironmentGlobals = _map_struct(
    offsets, "GcEnvironmentGlobals", nms_types.cGcEnvironmentGlobals
)
gGcFishingGlobals = _map_struct(
    offsets, "GcFishingGlobals", nms_types.cGcFishingGlobals
)
gGcFleetGlobals = _map_struct(offsets, "GcFleetGlobals", nms_types.cGcFleetGlobals)
gGcFreighterBaseGlobals = _map_struct(
    offsets, "GcFreighterBaseGlobals", nms_types.cGcFreighterBaseGlobals
)
gGcGalaxyGlobals = _map_struct(offsets, "GcGalaxyGlobals", nms_types.cGcGalaxyGlobals)
gGcGameplayGlobals = _map_struct(
    offsets, "GcGameplayGlobals", nms_types.cGcGameplayGlobals
)
gGcGraphicsGlobals = _map_struct(
    offsets, "GcGraphicsGlobals", nms_types.cGcGraphicsGlobals
)
gGcMultiplayerGlobals = _map_struct(
    offsets, "GcMultiplayerGlobals", nms_types.cGcMultiplayerGlobals
)
gGcNavigationGlobals = _map_struct(
    offsets, "GcNavigationGlobals", nms_types.cGcNavigationGlobals
)
gGcPlacementGlobals = _map_struct(
    offsets, "GcPlacementGlobals", nms_types.cGcPlacementGlobals
)
gGcPlayerGlobals = _map_struct(offsets, "GcPlayerGlobals", nms_types.cGcPlayerGlobals)
gGcRichPresenceGlobals = _map_struct(
    offsets, "GcRichPresenceGlobals", nms_types.cGcRichPresenceGlobals
)
gGcRobotGlobals = _map_struct(offsets, "GcRobotGlobals", nms_types.cGcRobotGlobals)
gGcSceneOptions = _map_struct(offsets, "GcSceneOptions", nms_types.cGcSceneOptions)
gGcScratchpadGlobals = _map_struct(
    offsets, "GcScratchpadGlobals", nms_types.cGcScratchpadGlobals
)
gGcSettlementGlobals = _map_struct(
    offsets, "GcSettlementGlobals", nms_types.cGcSettlementGlobals
)
gGcSimulationGlobals = _map_struct(
    offsets, "GcSimulationGlobals", nms_types.cGcSimulationGlobals
)
gGcSkyGlobals = _map_struct(offsets, "GcSkyGlobals", nms_types.cGcSkyGlobals)
gGcSmokeTestOptions = _map_struct(
    offsets, "GcSmokeTestOptions", nms_types.cGcSmokeTestOptions
)
gGcSolarGenerationGlobals = _map_struct(
    offsets, "GcSolarGenerationGlobals", nms_types.cGcSolarGenerationGlobals
)
gGcSpaceshipGlobals = _map_struct(
    offsets, "GcSpaceshipGlobals", nms_types.cGcSpaceshipGlobals
)
gGcTerrainGlobals = _map_struct(
    offsets, "GcTerrainGlobals", nms_types.cGcTerrainGlobals
)
gGcUIGlobals = _map_struct(offsets, "GcUIGlobals", nms_types.cGcUIGlobals)
gGcVehicleGlobals = _map_struct(
    offsets, "GcVehicleGlobals", nms_types.cGcVehicleGlobals
)
