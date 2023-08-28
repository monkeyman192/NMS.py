import nmspy.data.structs as nms_structs
from nmspy.memutils import map_struct


def extract_members(meta: nms_structs.cTkMetaDataClass, metadata_registry: dict):
    member_data = []
    for member in meta.members:
        member_data.append(
            {
                "name": member.name,
                "type": member.type.name,
                "innerType": member.innerType.name,
                "size": member.size,
                "count": member.count,
                "offset": member.offset,
            }
        )
        if member.innerType == nms_structs.cTkMetaDataMember.eType.Class:
            innerTypeClass = map_struct(member.classMetadata, nms_structs.cTkMetaDataClass)
            member_data[-1]["innerType"] = innerTypeClass.name
        if member.type == nms_structs.cTkMetaDataMember.eType.Class:
            typeClass = map_struct(member.classMetadata, nms_structs.cTkMetaDataClass)
            member_data[-1]["type"] = typeClass.name
        if member.numEnumMembers != 0:
            member_data[-1]["enumLookup"] = [(x.name, x.value) for x in member.enumLookup]
            member_data[-1]["_enum_offset"] = member._enumLookup
    metadata_registry[meta.name] = {
        "nameHash": meta.nameHash,
        "templateHash": meta.templateHash,
        "members": member_data,
        "is_enum": len(member_data) == 1 and "_enum_offset" in member_data[0]
    }


def fixup_metadata_enums(metadata_registry: dict):
    """ Loop over the metadata registry twice. First time collating all the 
    enum types, and then second time replacing all the in-line enums with types.
    """
    enums = {}
    # Create enum mapping.
    for name, data in metadata_registry.items():
        if data.get("is_enum", False):
            enums[data["members"][0]["_enum_offset"]] = name
    # Now, go over the non-enum metaclasses and loop over their members.
    # Any member which has an enum offset in the above mapping will be replaced.
    for metaclass in metadata_registry.values():
        if not metaclass.get("is_enum", False):
            for member in metaclass["members"]:
                if enum_name := enums.get(member.get("_enum_offset")):
                    del member["_enum_offset"]
                    del member["enumLookup"]
                    member["enumType"] = enum_name
