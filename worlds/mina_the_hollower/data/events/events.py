from worlds.mina_the_hollower.data import EventTypeEnum
from worlds.mina_the_hollower.data.items.blockers import GeneratorsComplete, AstralPlatforms


#TODO: Move region to an enum
class RepairGenerators(EventTypeEnum):
    REPAIR_QUEENSBURY_CRYPT = ("Repair Queensbury Crypt Generator", "Queensbury Crypt Solemn Generator", GeneratorsComplete.REPAIR_SOLEMN_GENERATOR.value)
    REPAIR_NOXS_BAYOU = ("Repair Nox's Bayou Generator", "Nox's Bayou Swampy Generator", GeneratorsComplete.REPAIR_SWAMPY_GENERATOR.value)
    REPAIR_SEPTEMBURG = ("Repair Septemburg Generator", "Septemburg Windy Generator", GeneratorsComplete.REPAIR_WINDY_GENERATOR.value)
    REPAIR_BONE_BEACH = ("Repair Bone Beach Generator", "Bone Beach Shoreline Generator", GeneratorsComplete.REPAIR_SHORELINE_GENERATOR.value)
    REPAIR_COLTRANE_PEAK = ("Repair Coltrane Peak Generator", "Coltrane Peak Frozen Generator", GeneratorsComplete.REPAIR_FROZEN_GENERATOR.value)
    REPAIR_ASTRAL_ORRERY = ("Repair Astral Orrery Generator", "Astral Orrery Starry Generator", GeneratorsComplete.REPAIR_STARRY_GENERATOR.value)

class MirrorsEndSwitches(EventTypeEnum):
    BLUE_SWITCH = ("Blue Switch", "Astral Orrery Queensbury Mirror", AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value)
    GREEN_SWITCH = ("Green Switch", "Astral Orrery Bayou Mirror", AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value)
    RED_SWITCH = ("Red Switch", "Astral Orrery Bone Beach Mirror", AstralPlatforms.RED_ASTRAL_PLATFORMS.value)
    YELLOW_SWITCH = ("Yellow Switch", "Astral Orrery Septemburg Mirror", AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value)
    PURPLE_SWITCH = ("Purple Switch", "Astral Orrery Coltrane Peak Mirror", AstralPlatforms.PURPLE_ASTRAL_PLATFORMS.value)
