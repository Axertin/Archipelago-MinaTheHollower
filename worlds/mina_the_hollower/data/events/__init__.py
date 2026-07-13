from .events import RepairGenerators
from .. import RepairEventData
from ...constants import *

QUEENSBURY_CRYPT_DATA = RepairEventData(RepairGenerators.REPAIR_QUEENSBURY_CRYPT, QUEENSBURY_CRYPT, 0)
NOXS_BAYOU_DATA = RepairEventData(RepairGenerators.REPAIR_NOXS_BAYOU, NOXS_BAYOU, 1)
SEPTEMBURG_DATA = RepairEventData(RepairGenerators.REPAIR_SEPTEMBURG, SEPTEMBURG, 2)
BONE_BEACH_DATA = RepairEventData(RepairGenerators.REPAIR_BONE_BEACH, BONE_BEACH, 3)
COLTRANE_PEAK_DATA = RepairEventData(RepairGenerators.REPAIR_COLTRANE_PEAK, COLTRANE_PEAK, 4)
ASTRAL_ORRERY_DATA = RepairEventData(RepairGenerators.REPAIR_ASTRAL_ORRERY, ASTRAL_ORRERY, 5)
RADIANT_MANOR_DATA = RepairEventData(RepairGenerators.REPAIR_PRIME_GENERATOR, "Randiant Manor", 10)
repair_generator_data: list[RepairEventData] = [
    QUEENSBURY_CRYPT_DATA,
    NOXS_BAYOU_DATA,
    SEPTEMBURG_DATA,
    BONE_BEACH_DATA,
    COLTRANE_PEAK_DATA,
    ASTRAL_ORRERY_DATA
]