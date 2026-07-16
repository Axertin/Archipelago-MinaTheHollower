from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...items import AstralPlatforms, SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasFishingRod
from ...rules.state_rules import HasKear
from ...rules.movement_rules import CanJumpTiles

collectable_locations: dict[str, LocationData] = {
    "AO Stellarium East Chest": LocationData(129, "Astral Orrery Stellarium", HasKear(kear=SingleKears.ASTRAL_ORRERY_STELLARIUM_KEAR.value)),
    "AO Tubert Trinket": LocationData(137, "Astral Orrery Stellarium Mutant Switch"),
    "AO Tubert Kear": LocationData(138, "Astral Orrery Stellarium Mutant Switch"),
    "AO Gravity Zone Long Hallway Chest": LocationData(133, "Astral Orrery Gravity Zone", CanJumpTiles(distance=2)),
    "AO Gravity Zone Secret Room #1 Kear": LocationData(134, "Astral Orrery Gravity Zone"),
    "AO Gravity Zone Secret Room #2 Chest": LocationData(128, "Astral Orrery Gravity Zone", CanBurrow()),
    "AO Cog Chamber Secret Room #1 Chest": LocationData(130, "Astral Orrery Cog Chamber", CanBurrow() & CanCarry()),
    "AO Cog Chamber Secret Room #1 Kear": LocationData(135, "Astral Orrery Cog Chamber", CanBurrow() & CanCarry()),
    "AO Mutant Lab Secret Room #1 Chest": LocationData(131, "Astral Orrery Mutant Lab", CanBurrow()),
    "AO Mutant Lab Secret Room #2 Trinket": LocationData(132, "Astral Orrery Mutant Lab", CanBurrow()),
    "AO Hall of Scholars Below Boss Chamber Bonestone": LocationData(126, "Astral Orrery Hall Of Scholars"),
    "AO Hall of Scholars Exit Chest": LocationData(136, "Astral Orrery Hall Of Scholars End", CanBurrow()),
    "AO Sealed Archive Health Rose": LocationData(125, "Astral Orrery Sealed Archive Congealed Chamber"),


}
boss_locations: dict[str, LocationData] = {
    "AO Defeat Lumenarks": LocationData(None, "Astral Orrery Hall Of Scholars"),
    "AO Sealed Archive The Congealed": LocationData(None, "Astral Orrery Sealed Archive Congealed Chamber"),
    "AO Starry Generator Activated": LocationData(None, "Astral Orrery Starry Generator"),
}

