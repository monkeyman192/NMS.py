# Extract all the class definitions from the NMS.exe

from abc import ABC
import json
import os
import os.path as op
import re
from signal import SIGTERM
import struct
import subprocess
import time
from typing import Optional
import keyword

import pymem


GUID_REGEX = re.compile(r'GUID = (0x[a-fA-F0-9]+)')


ENUM_OVERRIDES = {
    'GcCreatureGlobals': {
        'Temperments': 'GcCreatureRoles.CreatureRoleEnum',
        'TempermentDescriptions': 'GcCreatureRoles.CreatureRoleEnum',
        'Diets': 'GcCreatureDiet.DietEnum',
        'WaterDiets': 'GcCreatureDiet.DietEnum',
        'DietMeat': 'GcBiomeType.BiomeEnum',
        'DietVeg': 'GcBiomeType.BiomeEnum',
        'DietDescriptions': 'GcCreatureDiet.DietEnum',
        'WaterDietDescriptions': 'GcCreatureDiet.DietEnum',
        'BiomeDescriptions': 'GcBiomeType.BiomeEnum',
        'BiomeWaterDescriptions': 'GcBiomeType.BiomeEnum',
        'BiomeAirDescriptions': 'GcBiomeType.BiomeEnum',
        'WeirdBiomeDescriptions': 'GcBiomeSubType.BiomeSubTypeEnum',
        'PetBiomeClimates': 'GcBiomeType.BiomeEnum',
    },
    'GcEnvironmentProperties': {'SkyHeight': 'GcPlanetSize.PlanetSizeEnum'},
    'GcGalaxyGenerationSetupData': {
        'StarSize': 'GcGalaxyStarTypes.GalaxyStarTypeEnum',
    },
    'GcGalaxyGlobals': {
        'RaceFilterDefaultColours': 'GcAlienRace.AlienRaceEnum',
        'RaceFilterProtanopiaColours': 'GcAlienRace.AlienRaceEnum',
        'RaceFilterDeuteranopiaColours': 'GcAlienRace.AlienRaceEnum',
        'RaceFilterTritanopiaColours': 'GcAlienRace.AlienRaceEnum',
        'EconomyFilterDefaultColours': 'GcTradingClass.TradingClassEnum',
        'EconomyFilterProtanopiaColours': 'GcTradingClass.TradingClassEnum',
        'EconomyFilterDeuteranopiaColours': 'GcTradingClass.TradingClassEnum',
        'EconomyFilterTritanopiaColours': 'GcTradingClass.TradingClassEnum',
        'ConflictFilterDefaultColours': 'GcPlayerConflictData.ConflictLevelEnum',
        'ConflictFilterProtanopiaColours': 'GcPlayerConflictData.ConflictLevelEnum',
        'ConflictFilterDeuteranopiaColours': 'GcPlayerConflictData.ConflictLevelEnum',
        'ConflictFilterTritanopiaColours': 'GcPlayerConflictData.ConflictLevelEnum',
        'MarkerSettings': 'GcGalaxyMarkerTypes.GalaxyMarkerTypeEnum',
    },
    'GcGameplayGlobals': {
        'SalvageRewardsShuttle': 'GcInventoryClass.InventoryClassEnum',
        'SalvageRewardsDropship': 'GcInventoryClass.InventoryClassEnum',
        'SalvageRewardsFighter': 'GcInventoryClass.InventoryClassEnum',
        'SalvageRewardsScience': 'GcInventoryClass.InventoryClassEnum',
        'FreighterTechQualityWeightings': 'GcProceduralTechnologyData.QualityEnum',
    },
    'GcSolarGenerationGlobals': {
        'ExtremePlanetChance': 'GcGalaxyStarTypes.GalaxyStarTypeEnum',
        'AbandonedSystemProbability': 'GcGalaxyStarTypes.GalaxyStarTypeEnum',
        'EmptySystemProbability': 'GcGalaxyStarTypes.GalaxyStarTypeEnum',
        'PirateSystemProbability': 'GcGalaxyStarTypes.GalaxyStarTypeEnum',
    },
    'GcTerrainGlobals': {'MiningSubstanceBiome': 'GcBiomeType.BiomeEnum'},
    'GcPlayerSquadronConfig': {
        'PilotRankTraitRanges': 'GcInventoryClass.InventoryClassEnum',
        'PilotRankAttackDefinitions': 'GcInventoryClass.InventoryClassEnum',
    },
    'GcUIGlobals': {
        'CrosshairTargetLockSizeSpecific': 'GcPlayerWeapons.WeaponModeEnum',
    },
}

EXTRA_CLASSES = [
    'cAxisSpecification', 'cSimShape', 'cMapping', 'cDirectMesh',
    'cMappedMesh', 'cInfluencesOnMappedPoint', 'cShapePoint', 'cMappingInfluence',
    'cCollisionShapeType',
]
NAME_MAPPING = {
    'cGcDefaulMissionProduct': 'cGcDefaultMissionProduct',
    'cGcDefaulMissionSubstance': 'cGcDefaultMissionSubstance',
    'cgcwordcategorytableEnum': 'cGcWordCategoryTableEnum',
    'cGCHUDEffectRewardData': 'cGcHUDEffectRewardData',
}
# Flag enums fixes
FLAG_ENUM_FIXES = {
    'false_positives': [],
    'false_negatives': [
        'HotspotType',
        'CollisionGroup',
        'MetadataReadMask',
        'InputActionInfoFlags',
    ],
}
# List of classes to avoid overwriting as the have custom deserialisation
# methods.
# TODO: If the GUID changes we need to raise an important message so that we may
# fix it manually.
DONT_OVERRIDE = {
    'TkAnimNodeFrameData': 0xDD8A411B84D2D5DC,
    # # 'TkAnimNodeFrameHalfData',
    'TkGeometryData': 0xE2C133EF90E9F7A3,
    'TkMeshData': 0xA5E773D3424BA9FA,
}

STATIC_BASE = 0x140000000
# This is cTkMetaDataMember::eType
TYPE_MAPPING = {
    0x00: 'undefined',
    0x01: 'bool',
    0x02: 'byte',
    0x03: 'CUSTOM',
    0x04: 'NMSTemplate',
    0x05: 'LinkableNMSTemplate',
    0x06: 'Colour',
    0x07: 'LIST',
    0x08: 'VariableSizeString',         # VariableSizeString
    0x09: 'VariableSizeWString',        # VariableSizeWString
    0x0A: 'HashedString',
    0x0B: 'ENUM',
    0x0C: 'VariableSizeString',  # Technically a "filename" -> GcFilename (?)
    0x0D: 'FLAGENUM',
    0x0E: 'float',
    0x0F: 'double',
    0x10: 'TkID0x10',
    0x11: 'TkID0x20',
    0x12: 'cTkFixedString0x20',  # LocId
    0x13: 'int8',
    0x14: 'int16',
    0x15: 'int32',
    0x16: 'int64',
    0x17: 'GcNodeID',
    0x18: 'GcResource',
    0x19: 'GcSeed',
    0x1A: 'ARRAY',
    0x1B: 'cTkFixedString0x20',
    0x1C: 'cTkFixedString0x40',
    0x1D: 'cTkFixedString0x80',
    0x1E: 'cTkFixedString0x100',
    0x1F: 'cTkFixedString0x200',
    0x20: 'cTkFixedString0x400',
    0x21: 'cTkFixedString0x800',
    0x22: 'uint8',
    0x23: 'uint16',
    0x24: 'uint32',
    0x25: 'uint64',
    0x26: 'UniqueId',
    0x27: 'Vector2f',
    0x28: 'Vector3f',
    0x29: 'Vector4f',
    0x2A: 'wchar',
    0x2B: 'halfVector4',
    0x2C: 'Vector4i',
    0x2D: 'TkPhysRelVec3',
    0x2E: 'HashMap',
    0x2F: 'Colour32',  # 4 channel colour with each channel packed as a byte
}

TYPE_MAPPING_REV = {value: key for key, value in TYPE_MAPPING.items()}

PREFIX_MAPPING = {
    'ccg': 'GameComponents',
    'cgc': 'GameComponents',
    'ctk': 'Toolkit'
}


"""
Details on the format of the 0x58 bytes for each field (from cTkMetaDataMember definition):

0x00: char *mpacName;
0x08: unsigned int miNameHash;
0x0C: cTkMetaDataMember::eType mType;
0x10: cTkMetaDataMember::eType mInnerType;
0x14: int miSize;
0x18: int miCount;
0x1C: int miOffset;
0x20: cTkMetaDataClass *mpClassMetadata;
0x28: cTkMetaDataMember *mpHashMapIdMember;
0x30: cTkMetaDataEnumLookup *mpEnumLookup;
0x38: int miNumEnumMembers;
0x3C: FloatEditOptions mFloatEditOptions;
0x48: FloatLimits mFloatLimits;
"""

"""
Details on the 0x28 bytes that is TkMetaDataClass:

0x00: char *mpacName;
0x08: unsigned __int64 muNameHash;
0x10: unsigned __int64 muTemplateHash;
0x18: cTkMetaDataMember *maMembers;
0x20: int miNumMembers;
"""


def fmt_hex(x: int) -> str:
    """ Return the integer input formatted as a upper-case hexadecimal value """
    return '0x' + hex(x).upper()[2:]


class Field(ABC):
    # Field ABC which will be inherited by the other Field concrete sub-classes.
    # This gives some basic functionality and does some common processing.
    def __init__(self, data: bytes, nms_mem):
        self.data = data
        self.raw_field_type = TYPE_MAPPING_REV['undefined']
        self.field_size = 0x0
        self.field_index = 0x0

        # properties which are overwritten by subclasses which need to specify
        # them.
        self._is_enum_field = False
        self._is_array_field = False
        self._is_list_field = False

        # Get the name of the field.
        self._field_name: str = nms_mem.read_string(
            struct.unpack_from('<Q', data, offset=0x0)[0], byte=128
        )
        # Some field names are annoyingly duplicated in the exe. c# doesn't
        # allow this, so we need to add something to the name to make it unique.
        self._field_name_is_duplicate = False
        self.name_hash = struct.unpack_from('<I', data, offset=0x8)[0]
        self.field_size = struct.unpack_from('<I', data, offset=0x14)[0]
        self._array_size = struct.unpack_from('<I', data, offset=0x18)[0]
        self._field_offset = int(struct.unpack_from('<I', data, offset=0x1C)[0])

        # Sort out the requirements for this field.
        self.required_using: set = set()

        # The number of hexadecimal digits the maximum offset has.
        self.max_offset_width = 1

    @property
    def field_type(self):
        _type = TYPE_MAPPING.get(
            self.raw_field_type,
            f'unknown ({self.raw_field_type:X})'
        )
        if "<" in _type:
            return _type[:_type.index("<")]
        return _type

    @property
    def has_mxml_name(self):
        if " " in self._field_name or self._field_name[0].isdigit():
            return True

    @property
    def field_name(self):
        field_name = self._field_name.replace(" ", "")
        if field_name[0].isdigit():
            return '_' + field_name
        if self._field_name_is_duplicate:
            return field_name + '_' + self.field_type.replace("<", "").replace(">", "")
        if field_name[:2].lower() in {'gc', 'tk'}:
            return field_name[2:]
        if keyword.iskeyword(field_name):
            return field_name + "_"
        return field_name

    @property
    def field_offset(self):
        return '0x{0:>0{width}}'.format(
            fmt_hex(self._field_offset)[2:], width=self.max_offset_width
        )

    @property
    def array_size(self):
        return fmt_hex(self._array_size)

    @classmethod
    def instantiate(cls, data: bytes, nms_mem: pymem.Pymem):
        """ Return an instance of a subclass which is of the appropriate type
        based on the raw type specified in the data.
        This allows us to simplify the logic regarding deserialising the field
        by deferring it to the individual classes.
        """
        raw_type = struct.unpack_from('<I', data, offset=0xC)[0]
        if raw_type == TYPE_MAPPING_REV['ENUM'] or raw_type == TYPE_MAPPING_REV['FLAGENUM']:
            ef = EnumField(data, nms_mem)
            if raw_type == TYPE_MAPPING_REV['FLAGENUM']:
                ef.is_flag = True
            ef.check_flag_overwrites()
            return ef
        elif raw_type == TYPE_MAPPING_REV['LIST']:
            return ListField(data, nms_mem)
        elif raw_type == TYPE_MAPPING_REV['ARRAY']:
            return ArrayField(data, nms_mem)
        elif raw_type == TYPE_MAPPING_REV['CUSTOM']:
            return CustomField(data, nms_mem)
        elif raw_type == TYPE_MAPPING_REV["HashMap"]:
            return HashMapField(data, nms_mem)
        else:
            return NormalField(data, nms_mem, raw_type)

    def write(self) -> dict:
        return {
            "Name": self.field_name,
            "Type": self.field_type,
            "Offset": self._field_offset,
        }


class NormalField(Field):
    def __init__(self, data: bytes, nms_mem: pymem.Pymem, raw_field_type):
        super().__init__(data, nms_mem)
        self.raw_field_type = raw_field_type


class CustomField(Field):
    def __init__(self, data: bytes, nms_mem: pymem.Pymem):
        super().__init__(data, nms_mem)
        self.raw_field_type = TYPE_MAPPING_REV['CUSTOM']

        # Get the pointer to the custom type name.
        ptr_custom_type = nms_mem.read_ulonglong(
            struct.unpack_from('<Q', data, offset=0x20)[0]
        )
        # Now get the actual name.
        self._field_type = nms_mem.read_string(ptr_custom_type, byte=128)

    @property
    def field_type(self):
        return NAME_MAPPING.get(self._field_type, self._field_type)



class HashMapField(Field):
    def __init__(self, data: bytes, nms_mem: pymem.Pymem):
        super().__init__(data, nms_mem)
        self.raw_field_type = TYPE_MAPPING_REV['HashMap']
        # Multiply the field size by the array size to get the correct size
        self.field_size *= self._array_size
        self.array_enum = None
        self.ptr_enum: int = 0
        self.array_enum_type: Optional[str] = None
        self._is_hash_map_field = True
        self.local_enum = False

        array_type_raw = struct.unpack_from('<I', data, offset=0x10)[0]
        # A custom array subtype.
        if array_type_raw == TYPE_MAPPING_REV['CUSTOM']:
            ptr_custom_type = nms_mem.read_ulonglong(
                struct.unpack_from('<Q', data, offset=0x20)[0]
            )
            self._field_type = nms_mem.read_string(ptr_custom_type, byte=128)
        else:
            self._field_type = TYPE_MAPPING.get(
                array_type_raw, f'unknown {array_type_raw:X}'
            )

        idField_ptr = struct.unpack_from("<Q", data, offset=0x28)[0]
        if idField_ptr != 0:
            # This is a cTkMetaDataMember*. We only need to read the first char* in it to get the field name.
            self.id_field = nms_mem.read_string(nms_mem.read_ulonglong(idField_ptr), byte=128)
        else:
            self.id_field = ""

    @property
    def field_type(self):
        return f'{NAME_MAPPING.get(self._field_type, self._field_type)}'

    def write(self) -> dict:
        return {
            "Name": self.field_name,
            "Type": self.field_type,
            "Offset": self._field_offset,
            "HashMap": True,
        }


class ArrayField(Field):
    def __init__(self, data: bytes, nms_mem: pymem.Pymem):
        super().__init__(data, nms_mem)
        self.raw_field_type = TYPE_MAPPING_REV['ARRAY']
        # Multiply the field size by the array size to get the correct size
        self.field_size *= self._array_size
        self.array_enum = None
        self.ptr_enum: int = 0
        self.array_enum_type: Optional[str] = None
        self._is_array_field = True
        self.local_enum = False

        array_type_raw = struct.unpack_from('<I', data, offset=0x10)[0]
        # A custom array subtype.
        if array_type_raw == TYPE_MAPPING_REV['CUSTOM']:
            ptr_custom_type = nms_mem.read_ulonglong(
                struct.unpack_from('<Q', data, offset=0x20)[0]
            )
            self._field_type = nms_mem.read_string(ptr_custom_type, byte=128)
        else:
            self._field_type = TYPE_MAPPING.get(
                array_type_raw, f'unknown {array_type_raw:X}'
            )
        # Determine the associated EnumType
        self.ptr_enum = struct.unpack_from('<Q', data, offset=0x30)[0]
        # This may be a nullptr, in which case we end as we have no enum to get.
        if self.ptr_enum == 0:
            return
        # If the pointer is non-zero, then it will be a pointer to the enums
        # either associated with some other class, or an inline one.
        # We need to keep track of the pointer do we can determine what class
        # it was later.
        # Get all the values of the enum:
        self.array_enum = []
        for i in range(self._array_size):
            ptr_enum_name = nms_mem.read_ulonglong(self.ptr_enum + i * 0x10 + 0x8)
            name: str = nms_mem.read_string(ptr_enum_name, byte=128)
            self.array_enum.append(name)

    @property
    def field_type(self):
        _type = NAME_MAPPING.get(self._field_type, self._field_type)
        if "<" in _type:
            return _type[:_type.index("<")]
        return _type

    def write(self) -> dict:
        return {
            "Name": self.field_name,
            "Type": self.field_type,
            "Offset": self._field_offset,
            "Array_Size": self._array_size,
            "Array_Enum": "TODO",
        }


class ListField(Field):
    def __init__(self, data: bytes, nms_mem: pymem.Pymem):
        super().__init__(data, nms_mem)
        self.raw_field_type = TYPE_MAPPING_REV['LIST']
        self.field_size = 0x10
        self.required_using.add('System.Collections.Generic')
        self._is_list_field = True

        array_type_raw = struct.unpack_from('<I', data, offset=0x10)[0]
        if array_type_raw == TYPE_MAPPING_REV['CUSTOM']:
            try:
                ptr_custom_type = nms_mem.read_ulonglong(
                    struct.unpack_from('<Q', data, offset=0x20)[0]
                )
            except:
                print(self.field_name)
                raise
            self._field_type = nms_mem.read_string(ptr_custom_type, byte=128)
        else:
            self._field_type = TYPE_MAPPING.get(
                array_type_raw, f"unknown {array_type_raw:X}"
            )

    @property
    def field_type(self):
        _type = NAME_MAPPING.get(self._field_type, self._field_type)
        if "<" in _type:
            return _type[:_type.index("<")]
        return _type

    def write(self) -> dict:
        return {
            "Name": self.field_name,
            "Type": "cTkDynamicArray",
            "Offset": self._field_offset,
            "List": True,
            "GenericTypeArgs": [self.field_type]
        }


class EnumField(Field):
    def __init__(self, data: bytes, nms_mem: pymem.Pymem):
        super().__init__(data, nms_mem)
        self._is_flag: bool = False
        self.raw_field_type = TYPE_MAPPING_REV['ENUM']
        self.requires_values = False
        self._is_enum_field = True

        enum_count = struct.unpack_from('<I', data, offset=0x38)[0]
        self.ptr_enum = struct.unpack_from('<Q', data, offset=0x30)[0]
        self.enum_data = []
        # For each enum value, read the index, and a pointer to the name.
        for i in range(enum_count):
            idx = nms_mem.read_uint(self.ptr_enum + i * 0x10)
            ptr_enum_name = nms_mem.read_ulonglong(self.ptr_enum + i * 0x10 + 0x8)
            enum_name: str = nms_mem.read_string(ptr_enum_name, byte=128)
            self.enum_data.append([enum_name, idx])

    def check_flag_overwrites(self):
        # Check our overwrites and modify the `is_flag` property appropriately.
        if self.field_name in FLAG_ENUM_FIXES['false_negatives']:
            self.is_flag = True
        elif self.field_name in FLAG_ENUM_FIXES['false_positives']:
            self.is_flag = False

    @property
    def enum_dtype(self) -> str:
        if self.field_size == 0x4:
            return 'uint'
        elif self.field_size == 0x2:
            return 'ushort'
        elif self.field_size == 0x1:
            return 'byte'
        else:
            raise ValueError(f'The field {self.field_name} has an unexpected '
                             f'size: {self.field_size}')

    @property
    def is_flag(self) -> bool:
        return self._is_flag

    @property
    def enum_count(self) -> str:
        return fmt_hex(len(self.enum_data))

    @is_flag.setter
    def is_flag(self, value: bool):
        self._is_flag = value
        if value is True:
            self.required_using.add('System')
        elif value is False:
            # Remove the System using requirement.
            self.required_using -= {'System', }

    def write(self) -> dict:
        return {
            "Name": self.field_name,
            "Type": self.field_type,
            "Offset": self._field_offset,
            "Enum_DataSize": self.field_size,
            "Enum_IsFlag": self.is_flag,
            "Enum_Values": self.enum_data,
        }


class NMSClass():
    enum_reference_data: dict = {}

    def __init__(self, name: str, name_hash: int, guid: int):
        self.fields = []
        self._field_names = set()
        self.name = name
        self.name_hash = fmt_hex(name_hash)
        self._guid = guid
        self.guid = fmt_hex(guid)
        self.required_usings = set()
        self.is_enum_class = False
        self.ptr_enum = None
        self.has_enum_arrays = False
        self.usings = []
        self.extra_attributes = ''

    def add_fields(self, fields: list[Field]):
        # Add a list of field objects.
        # This is a little hacky and could be done a bit better but this does
        # work...
        self.fields = fields
        self.fields.sort(key=lambda x: x._field_offset)
        max_offset_width = 1
        # For each field find if it requires something and add it to the
        # required usings.
        for field in fields:
            if field.required_using:
                self.required_usings.update(field.required_using)
            if field.field_name not in self._field_names:
                self._field_names.add(field.field_name)
            else:
                field._field_name_is_duplicate = True
        # If there are some fields, calculate the maximum offset so that we can
        # nicely format the offset comments.
        if self.fields:
            max_offset_width = len(self.fields[-1].field_offset) - 2
        # Finally, for each field, give it this found max_offset_width
        for field in self.fields:
            field.max_offset_width = max_offset_width

        # Determine if the class is an enum class
        if len(fields) == 1 and isinstance(fields[0], EnumField):
            self.is_enum_class = True
            self.ptr_enum = fields[0].ptr_enum
            NMSClass.enum_reference_data[fields[0].ptr_enum] = f'{self.name}.{fields[0].field_name}Enum'

    def update_array_enum_refs(self):
        # Update the enum array references for the required fields.
        # To make it faster, only do this for classes which need it.
        if self.has_enum_arrays or self.name in ENUM_OVERRIDES:
            for field in self.fields:
                if isinstance(field, ArrayField):
                    field.array_enum_type = NMSClass.enum_reference_data.get(
                        field.ptr_enum
                    )
                    if field.array_enum_type is not None:
                        pass
                    elif field.field_name in ENUM_OVERRIDES.get(self.name, {}):
                        # Check to see if the field name is in the override
                        # mapping.
                        # If it is add the type and also the required usings
                        # mapping.
                        field.array_enum_type = ENUM_OVERRIDES[self.name].get(
                            field.field_name
                        )
                        if field.array_enum_type is not None:
                            # Set the array_enum property to be an empty list so
                            # that the actual enum type is written.
                            field.array_enum = []
                    elif field.array_enum is not None:
                        field.local_enum = True
                        field.array_enum_type = f'{field.field_name}Enum'

    def finalise(self):
        if self.required_usings:
            self.usings = [x for x in self.required_usings]
            self.usings.sort(reverse=True)


    def write(self) -> dict:
        self.finalise()
        data = {
            "Name": self.name,
            "GUID": self.guid,
            "NameHash": self.name_hash,
            "Fields": [
                field.write() for field in self.fields
            ]
        }
        if self.is_enum_class:
            data["EnumClass"] = True
        return data


def read_class(nms_mem: pymem.Pymem, address: int) -> NMSClass:
    """
    Take an array of 24 bytes and extract some information:
    0x00: (uint64*): Class name
    0x08: (uint64): Name Hash
    0x10: (uint64): GUID
    0x18: (uint64*): Data
    0x20: (uint32): Number of fields.
    """
    data = nms_mem.read_bytes(address, 0x24)
    ptr_name, name_hash, guid, ptr_data, field_num = struct.unpack('<QQQQI', data)
    name: str = nms_mem.read_string(ptr_name, byte=128)
    if name in DONT_OVERRIDE and DONT_OVERRIDE[name] != guid:
        print(f'The template {name} has been updated. Please check')
    fields, has_enum_arrays = extract_fields(nms_mem, ptr_data, field_num)
    # If the name needs to be fix do so here.
    name = NAME_MAPPING.get(name, name)
    cls = NMSClass(name, name_hash, guid)
    cls.add_fields(fields)
    cls.has_enum_arrays = has_enum_arrays
    return cls


def extract_fields(nms_mem: pymem.Pymem, address: int, field_count: int) -> tuple[list[Field], bool]:
    # Take the 0x58 bytes and process them.
    fields = []
    has_enum_arrays = False
    for i in range(field_count):
        data = nms_mem.read_bytes(address + i * 0x58, 0x58)
        field = Field.instantiate(data, nms_mem)
        field.field_index = i
        # As we add fields, determine if the field is an array with an
        # associated enum. If it is then set a flag.
        if (not has_enum_arrays
            and isinstance(field, ArrayField)
            and field.array_enum is not None
        ):
            has_enum_arrays = True
        fields.append(field)

    return fields, has_enum_arrays


def find_classes(nms_path: str):
    with open(nms_path, 'rb') as f:
        data = f.read()
        # First, find the start and ends of the .rdata section.
        rdata_hdr = data.find(b'.rdata')
        rdata_size, rdata_offset, _, ptr_address = struct.unpack_from(
            '<IIII',
            data,
            offset=rdata_hdr + 8
        )

        # The pointer will different from the actual offset by some amount we
        # need to take into account.
        virtual_offset = rdata_offset - ptr_address

        subdata = data[rdata_offset: rdata_offset + rdata_size]
        # Find all the classes which match the regex.
        for m in re.finditer(b'(c((?:Gc)|(?:Tk))\w+)\x00', data, flags=re.IGNORECASE):
            # For each one, extract the name, and also record the location the
            # name occurs at.
            name = m[0].strip(b'\x00').decode()
            if not name.startswith('c'):
                continue
            addr = m.span()[0] + virtual_offset + STATIC_BASE
            # Now search the exe for this address.
            found_addr = subdata.find(struct.pack('<Q', addr))
            # If we find it, then at this location we will have all the data we
            # need.
            if found_addr != -1:
                found_addr += rdata_offset
                yield name, found_addr + virtual_offset
        for name in EXTRA_CLASSES:
            # For the extra classes we'll be lazy and find them slightly
            # differently...
            addr = data.find(name.encode() + b"\x00")
            addr = addr + virtual_offset + STATIC_BASE
            # Now search the exe for this address.
            found_addr = subdata.find(struct.pack('<Q', addr))
            # If we find it, then at this location we will have all the data we
            # need.
            if found_addr != -1:
                found_addr += rdata_offset
                yield name, found_addr + virtual_offset
            else:
                print(f"Cannot find {name}")


if __name__ == '__main__':
    # First, handle the configuration loading.
    binary_path = r"C:\Program Files (x86)\Steam\steamapps\common\No Man's Sky\Binaries\NMS.exe"

    nms_proc = subprocess.Popen(binary_path)
    print(f'Opened NMS with PID: {nms_proc.pid}')

    try:
        # Wait some time for the data to be written to memory.
        time.sleep(2)
        # Now find the process with pymem.
        # If there is for some reason multiple instances of NMS running this
        # will probably have issues...
        nms = pymem.Pymem('NMS.exe')
        nms_base = nms.base_address
        t1 = time.time()
        names: list[str] = []
        classes: list[NMSClass] = []
        class_guid_mapping: dict[str, str] = {}
        guids: list[int] = []
        for name, offset in find_classes(binary_path):
            cls_ = read_class(nms, nms_base + offset)
            name = NAME_MAPPING.get(name, name)
            names.append(f'{name}, {nms_base + offset:X}')
            classes.append(cls_)
            class_guid_mapping[cls_.guid] = cls_.name
            guids.append(cls_._guid)
        names.sort()

        master_data = []

        for cls_ in classes:
            # Before writing out, loop over the fields of the class also to
            # determine if any of the array fields need to have updated enum
            # references.
            cls_.update_array_enum_refs()
            master_data.append(cls_.write())

        with open(op.join(op.dirname(__file__), "struct_data.json"), "w") as f:
            json.dump(master_data, f, indent=1)

        print(f'Took {time.time() - t1:.3f}s')
    except Exception as exc:
        raise exc
    finally:
        # Kill the NMS process.
        nms_proc.terminate()
        nms_pid = nms.process_id
        if nms_pid and nms_pid != nms_proc.pid:
            os.kill(nms_pid, SIGTERM)
