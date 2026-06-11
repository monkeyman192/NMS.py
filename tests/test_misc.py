# For now this will just contain some misc tests until it grows large enough to need to properly categorise
# them.

from nmspy.data.exported_types import cGcGalacticAddressData
from nmspy.data.types import cGcUniverseAddressData


def convert(miVoxelX, miVoxelY, miVoxelZ, miRealityIndex, miSolarSystemIndex, miPlanetIndex):
    LODWORD = miVoxelX & 0xFFF | ((((miVoxelY & 0xFF) << 12) | miVoxelZ & 0xFFF) << 12)
    HIDWORD = miRealityIndex | ((miSolarSystemIndex & 0xFFF | ((miPlanetIndex & 0xF) << 12)) << 8)
    print(f"0x{HIDWORD:X}{LODWORD:X}")


def test_cGcUniverseAddressData_to_UA():
    uad = cGcUniverseAddressData(
        GalacticAddress=cGcGalacticAddressData(
            PlanetIndex=1,
            SolarSystemIndex=5,
            VoxelX=563,
            VoxelY=86,
            VoxelZ=181,
        ),
        RealityIndex=2,
    )
    assert uad.to_UA() == 0x001_005_02_56_0B5_233

    uad = cGcUniverseAddressData(
        GalacticAddress=cGcGalacticAddressData(
            PlanetIndex=2,
            SolarSystemIndex=4,
            VoxelX=-563,
            VoxelY=-86,
            VoxelZ=-181,
        ),
        RealityIndex=3,
    )
    assert uad.to_UA() == 0x002_004_03_AA_F4B_DCD
