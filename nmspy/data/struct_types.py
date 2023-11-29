from typing import TypedDict, Protocol


class cGcRealityManager_Protocols:
    class GenerateProceduralTechnologyID_1(Protocol):
        # "cGcRealityManager *, TkID<128> *, eProceduralTechnologyCategory, const cTkSeed *"
        def __call__(self, result: int, leProcTechCategory: int, lSeed: int) -> int: ...
    class GenerateProceduralTechnologyID_2(Protocol):
        # "cGcRealityManager *, TkID<128> *, const TkID<128> *, const cTkSeed *"
        def __call__(self, result: int, lBaseTechID: bytes, lSeed: int) -> int: ...


class cGcRealityManager:
    GenerateProceduralTechnologyID = TypedDict(
        "GenerateProceduralTechnologyID",
        {
            "cGcRealityManager *, TkID<128> *, eProceduralTechnologyCategory, const cTkSeed *": cGcRealityManager_Protocols.GenerateProceduralTechnologyID_1,
            "cGcRealityManager *, TkID<128> *, const TkID<128> *, const cTkSeed *": cGcRealityManager_Protocols.GenerateProceduralTechnologyID_2,
        }
    )
