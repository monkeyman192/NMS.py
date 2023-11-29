from typing import TypedDict, Protocol


class cGcRealityManager_Protocols:
    class GenerateProceduralProduct_1(Protocol):
        # "cGcRealityManager *, int, const cTkSeed *, eRarity, eQuality"
        def __call__(self, result: int, leProcProdCategory: int, lSeed: int, leRarityOverride: int, leQualityOverride: int) -> int: ...
    class GenerateProceduralProduct_2(Protocol):
        # "cGcRealityManager *, const TkID<128> *"
        def __call__(self, result: int, lProcProdID: bytes) -> int: ...
    class GenerateProceduralTechnologyID_1(Protocol):
        # "cGcRealityManager *, TkID<128> *, eProceduralTechnologyCategory, const cTkSeed *"
        def __call__(self, result: int, leProcTechCategory: int, lSeed: int) -> int: ...
    class GenerateProceduralTechnologyID_2(Protocol):
        # "cGcRealityManager *, TkID<128> *, const TkID<128> *, const cTkSeed *"
        def __call__(self, result: int, lBaseTechID: bytes, lSeed: int) -> int: ...


class cGcRealityManager:
    GenerateProceduralProduct = TypedDict(
        "GenerateProceduralProduct",
        {
            "cGcRealityManager *, int, const cTkSeed *, eRarity, eQuality": cGcRealityManager_Protocols.GenerateProceduralProduct_1,
            "cGcRealityManager *, const TkID<128> *": cGcRealityManager_Protocols.GenerateProceduralProduct_2,
        }
    )
    GenerateProceduralTechnologyID = TypedDict(
        "GenerateProceduralTechnologyID",
        {
            "cGcRealityManager *, TkID<128> *, eProceduralTechnologyCategory, const cTkSeed *": cGcRealityManager_Protocols.GenerateProceduralTechnologyID_1,
            "cGcRealityManager *, TkID<128> *, const TkID<128> *, const cTkSeed *": cGcRealityManager_Protocols.GenerateProceduralTechnologyID_2,
        }
    )
