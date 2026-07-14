from .events import RepairGenerators
from .. import RepairEventData
from ..items import AreaKears
from ...constants import *

QUEENSBURY_CRYPT_DATA = RepairEventData(RepairGenerators.REPAIR_QUEENSBURY_CRYPT, QUEENSBURY_CRYPT, 0, AreaKears.QUEENSBURY_KEARS)
NOXS_BAYOU_DATA = RepairEventData(RepairGenerators.REPAIR_NOXS_BAYOU, NOXS_BAYOU, 1, AreaKears.BAYOU_KEARS)
SEPTEMBURG_DATA = RepairEventData(RepairGenerators.REPAIR_SEPTEMBURG, SEPTEMBURG, 2, AreaKears.SEPTEMBURG_KEARS)
BONE_BEACH_DATA = RepairEventData(RepairGenerators.REPAIR_BONE_BEACH, BONE_BEACH, 3, AreaKears.BONE_BEACH_KEARS)
COLTRANE_PEAK_DATA = RepairEventData(RepairGenerators.REPAIR_COLTRANE_PEAK, COLTRANE_PEAK, 4, AreaKears.COLTRANE_PEAK_KEARS)
ASTRAL_ORRERY_DATA = RepairEventData(RepairGenerators.REPAIR_ASTRAL_ORRERY, ASTRAL_ORRERY, 5, AreaKears.ASTRAL_ORRERY_KEARS)
RADIANT_MANOR_DATA = RepairEventData(RepairGenerators.REPAIR_PRIME_GENERATOR, "Randiant Manor", 10, AreaKears.RADIANT_MANOR_KEARS)

repair_generator_data: list[RepairEventData] = [
    QUEENSBURY_CRYPT_DATA,
    NOXS_BAYOU_DATA,
    SEPTEMBURG_DATA,
    BONE_BEACH_DATA,
    COLTRANE_PEAK_DATA,
    ASTRAL_ORRERY_DATA
]

all_generator_data: list[RepairEventData] = [
    QUEENSBURY_CRYPT_DATA,
    NOXS_BAYOU_DATA,
    SEPTEMBURG_DATA,
    BONE_BEACH_DATA,
    COLTRANE_PEAK_DATA,
    ASTRAL_ORRERY_DATA,
    RADIANT_MANOR_DATA
]