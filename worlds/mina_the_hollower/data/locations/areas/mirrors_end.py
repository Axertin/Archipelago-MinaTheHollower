from rule_builder.rules import Has
from worlds.mina_the_hollower import CanJumpTiles
from ... import LocationData
from ...items import SingleKears, AstralPlatforms
from ...rules.ability_rules import CanBurrow, HasFishingRod, CanCarry
from ...rules.state_rules import HasKear

collectable_locations: dict[str, LocationData] = {
    "AO Mirror's End Beach Room Chest": LocationData(281, "Astral Orrery Mirror's End", Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value) & CanBurrow()),
    "AO Mirror's End Reckless Beastium": LocationData(276, "Astral Orrery Mirror's End", CanJumpTiles(distance=3) & CanCarry() &
                                                      HasKear(kear=SingleKears.ASTRAL_ORREY_MIRROR_ROOM_RIGHT_SIDE_KEAR.value)),
    "AO Mirror's End West Ledge Trinket Bag": LocationData(279, "Astral Orrery Mirror's End",
           HasKear(kear=SingleKears.ASTRAL_ORREY_MIRROR_ROOM_LEFT_SIDE_KEAR.value)
           & ((CanBurrow() & Has(AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value))
                | ((Has(AstralPlatforms.RED_ASTRAL_PLATFORMS.value)
                | Has(AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value)
                | Has(AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value)) & ( CanJumpTiles(distance=4))))),
    "AO Mirror's End Trunkstar Core": LocationData(282, "Astral Orrery Mirror's End", HasFishingRod()),
    "AO Mirror's End Moving Platform Room Chest": LocationData(280, "Astral Orrery Mirror's End Blue Chest"),
}