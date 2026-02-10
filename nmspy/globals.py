import ctypes
import logging
import re
import struct
from typing import Type, TypeVar, Union

import pymhf.core.caching as cache
from pymhf.core._internal import BASE_ADDRESS, BINARY_PATH
from typing_extensions import get_type_hints

import nmspy.data.exported_types as nms_types

logger = logging.getLogger(__name__)

STATIC_BASE = 0x140000000


CTYPES = Union[ctypes._SimpleCData, ctypes.Structure, ctypes._Pointer, ctypes.Array]
Struct = TypeVar("Struct", bound=CTYPES)


def _map_struct(offsets: dict[str, int], type_: Type[Struct]) -> Struct:
    """Modified version of `pymhf.core.memutils.map_struct` to raise a warning instead of an error."""
    name = type_.__name__
    if name.startswith("cGc"):
        name = name[1:]
    offset = offsets.get(name)
    if not offset:
        logger.warning(f"Could not find the global {name} in memory. This may cause issues...!!")
        return  # type: ignore
    instance = ctypes.cast(BASE_ADDRESS + offset, ctypes.POINTER(type_))
    return instance.contents


def extract_global_offsets(global_names: set[str]) -> dict[str, int]:
    """Extract the offsets within the binary to various globals."""
    # First, check to see if the offsets are cached.
    cached_data = {x[0]: x[1] for x in cache.offset_cache.items()}
    if global_names <= set(cached_data.keys()):
        # Use the cached values.
        return {name: cached_data[name] for name in global_names}
    else:
        logger.debug("No globals were found in the offset cache. Finding and storing them.")

    try:
        with open(BINARY_PATH, "rb") as f:
            whole_file = f.read()
    except:  # noqa
        logger.exception("There was an error reading the binary. No globals will be mapped.")
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
    data_size, data_offset, _, data_ptr_address = struct.unpack_from("<IIII", whole_file, offset=data_hdr + 8)
    data_virtual_offset = data_offset - data_ptr_address
    data = whole_file[data_offset : data_offset + data_size]

    # .text
    text_hdr = whole_file.find(b".text")
    text_size, text_offset, _, text_ptr_address = struct.unpack_from("<IIII", whole_file, offset=text_hdr + 8)
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

    # Store the global offsets so that we can skip the above lookup in the future.
    for name, value in return_data.items():
        cache.offset_cache.set(name, value, save=False)
    cache.offset_cache.save()

    return return_data


class Globals:
    GcAISpaceshipGlobals: nms_types.cGcAISpaceshipGlobals
    GcAtlasGlobals: nms_types.cGcAtlasGlobals
    GcAudioGlobals: nms_types.cGcAudioGlobals
    GcBuildableShipGlobals: nms_types.cGcBuildableShipGlobals
    GcBuildingGlobals: nms_types.cGcBuildingGlobals
    GcCameraGlobals: nms_types.cGcCameraGlobals
    GcCharacterGlobals: nms_types.cGcCharacterGlobals
    GcCreatureGlobals: nms_types.cGcCreatureGlobals
    GcCollisionTable: nms_types.cGcCollisionTable
    GcDebugEditorGlobals: nms_types.cGcDebugEditorGlobals
    GcDebugOptions: nms_types.cGcDebugOptions
    GcEffectsGlobals: nms_types.cGcEffectsGlobals
    GcEnvironmentGlobals: nms_types.cGcEnvironmentGlobals
    GcFishingGlobals: nms_types.cGcFishingGlobals
    GcFleetGlobals: nms_types.cGcFleetGlobals
    GcFreighterBaseGlobals: nms_types.cGcFreighterBaseGlobals
    GcGalaxyGlobals: nms_types.cGcGalaxyGlobals
    GcGameplayGlobals: nms_types.cGcGameplayGlobals
    GcGraphicsGlobals: nms_types.cGcGraphicsGlobals
    GcMultiplayerGlobals: nms_types.cGcMultiplayerGlobals
    GcNavigationGlobals: nms_types.cGcNavigationGlobals
    GcPlacementGlobals: nms_types.cGcPlacementGlobals
    GcPlayerGlobals: nms_types.cGcPlayerGlobals
    GcRichPresenceGlobals: nms_types.cGcRichPresenceGlobals
    GcRobotGlobals: nms_types.cGcRobotGlobals
    GcSceneOptions: nms_types.cGcSceneOptions
    GcScratchpadGlobals: nms_types.cGcScratchpadGlobals
    GcSettlementGlobals: nms_types.cGcSettlementGlobals
    GcSimulationGlobals: nms_types.cGcSimulationGlobals
    GcSkyGlobals: nms_types.cGcSkyGlobals
    GcSmokeTestOptions: nms_types.cGcSmokeTestOptions
    GcSolarGenerationGlobals: nms_types.cGcSolarGenerationGlobals
    GcSpaceshipGlobals: nms_types.cGcSpaceshipGlobals
    GcTerrainGlobals: nms_types.cGcTerrainGlobals
    GcUIGlobals: nms_types.cGcUIGlobals
    GcVehicleGlobals: nms_types.cGcVehicleGlobals

    @property
    def global_names(self) -> set[str]:
        names = set()
        for field_name, annotation in get_type_hints(type(self)).items():
            if issubclass(annotation, ctypes.Structure):
                names.add(field_name)
        return names

    def instantiate_globals(self):
        offsets = extract_global_offsets(self.global_names)
        self.GcAISpaceshipGlobals = _map_struct(offsets, nms_types.cGcAISpaceshipGlobals)
        self.GcAtlasGlobals = _map_struct(offsets, nms_types.cGcAtlasGlobals)
        self.GcAudioGlobals = _map_struct(offsets, nms_types.cGcAudioGlobals)
        self.GcBuildableShipGlobals = _map_struct(offsets, nms_types.cGcBuildableShipGlobals)
        self.GcBuildingGlobals = _map_struct(offsets, nms_types.cGcBuildingGlobals)
        self.GcCameraGlobals = _map_struct(offsets, nms_types.cGcCameraGlobals)
        self.GcCharacterGlobals = _map_struct(offsets, nms_types.cGcCharacterGlobals)
        self.GcCreatureGlobals = _map_struct(offsets, nms_types.cGcCreatureGlobals)
        self.GcCollisionTable = _map_struct(offsets, nms_types.cGcCollisionTable)
        self.GcDebugEditorGlobals = _map_struct(offsets, nms_types.cGcDebugEditorGlobals)
        self.GcDebugOptions = _map_struct(offsets, nms_types.cGcDebugOptions)
        self.GcEffectsGlobals = _map_struct(offsets, nms_types.cGcEffectsGlobals)
        self.GcEnvironmentGlobals = _map_struct(offsets, nms_types.cGcEnvironmentGlobals)
        self.GcFishingGlobals = _map_struct(offsets, nms_types.cGcFishingGlobals)
        self.GcFleetGlobals = _map_struct(offsets, nms_types.cGcFleetGlobals)
        self.GcFreighterBaseGlobals = _map_struct(offsets, nms_types.cGcFreighterBaseGlobals)
        self.GcGalaxyGlobals = _map_struct(offsets, nms_types.cGcGalaxyGlobals)
        self.GcGameplayGlobals = _map_struct(offsets, nms_types.cGcGameplayGlobals)
        self.GcGraphicsGlobals = _map_struct(offsets, nms_types.cGcGraphicsGlobals)
        self.GcMultiplayerGlobals = _map_struct(offsets, nms_types.cGcMultiplayerGlobals)
        self.GcNavigationGlobals = _map_struct(offsets, nms_types.cGcNavigationGlobals)
        self.GcPlacementGlobals = _map_struct(offsets, nms_types.cGcPlacementGlobals)
        self.GcPlayerGlobals = _map_struct(offsets, nms_types.cGcPlayerGlobals)
        self.GcRichPresenceGlobals = _map_struct(offsets, nms_types.cGcRichPresenceGlobals)
        self.GcRobotGlobals = _map_struct(offsets, nms_types.cGcRobotGlobals)
        self.GcSceneOptions = _map_struct(offsets, nms_types.cGcSceneOptions)
        self.GcScratchpadGlobals = _map_struct(offsets, nms_types.cGcScratchpadGlobals)
        self.GcSettlementGlobals = _map_struct(offsets, nms_types.cGcSettlementGlobals)
        self.GcSimulationGlobals = _map_struct(offsets, nms_types.cGcSimulationGlobals)
        self.GcSkyGlobals = _map_struct(offsets, nms_types.cGcSkyGlobals)
        self.GcSmokeTestOptions = _map_struct(offsets, nms_types.cGcSmokeTestOptions)
        self.GcSolarGenerationGlobals = _map_struct(offsets, nms_types.cGcSolarGenerationGlobals)
        self.GcSpaceshipGlobals = _map_struct(offsets, nms_types.cGcSpaceshipGlobals)
        self.GcTerrainGlobals = _map_struct(offsets, nms_types.cGcTerrainGlobals)
        self.GcUIGlobals = _map_struct(offsets, nms_types.cGcUIGlobals)
        self.GcVehicleGlobals = _map_struct(offsets, nms_types.cGcVehicleGlobals)


globals = Globals()
