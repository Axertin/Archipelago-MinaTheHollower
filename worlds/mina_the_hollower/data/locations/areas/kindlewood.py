from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...items import Trinkets, SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, \
    HasReachingSideArm, HasFishingRod, HasTrinket
from ...rules.state_rules import HasKear, ShopPrice
from ...rules.movement_rules import CanJumpTiles

collectable_locations: dict[str, LocationData] = {
    "KW Overgrowth Bonfire Chest": LocationData(340, "Kindlewood Overgrowth Bonfire Main"),
    "KW Residence Basement Chest": LocationData(341, "Kindlewood Overgrowth Residence Basement"),
    "KW Madd House Draining Beastium": LocationData(348, "Kindlewood Overgrowth Madd House", ShopPrice(cost=2000)),
    "KW Madd House Oozing Organ": LocationData(347, "Kindlewood Overgrowth Madd House", ShopPrice(cost=2000)),
    "KW Madd House Voltaic Guard": LocationData(349, "Kindlewood Overgrowth Madd House", ShopPrice(cost=2000)),
    "KW Madd House Kear": LocationData(350, "Kindlewood Overgrowth Madd House"),
    "KW Behind Madd House Bonestone": LocationData(339, "Kindlewood Behind Madd House", CanBurrow() & CanCarry()),
    "KW Train Station Gourdan": LocationData(335, "Kindlewood Farm Crossing Pumpkin Patch", HasTrinket(trinket=Trinkets.OOZING_ORGAN.value)),
    "KW Fish Gazeworm Eye": LocationData(104, "Kindlewood Farm Crossing Pumpkin Patch", HasFishingRod()),
    "KW Train Station Ledge Chest": LocationData(346, "Kindlewood Farm Crossing Pumpkin Patch", CanBurrow()),
    "KW Farm Crossing Shack Chest": LocationData(342, "Kindlewood Farm Crossing Shack", HasReachingSideArm() & CanBurrow()),
    "KW Wallower's Room Trinket": LocationData(344, "Kindlewood Wallowers Path", HasKear(kear=SingleKears.KINDLEWOOD_WALLOWERS_PATH_TRINKET_KEAR.value)),  # needs kear, burrow,
    "KW Wallower's Room Chest": LocationData(345, "Kindlewood Wallowers Path", (CanBurrow() & HasTrinket(trinket=Trinkets.WALLOWERS_GAUNTLETS.value)) | CanJumpTiles(distance=6)),
    "KW Rail Tunnel Vial Pouch": LocationData(343, "Kindlewood Rail Tunnel", CanBurrow() & CanCarry()),
}

boss_locations: dict[str, LocationData] = {
    "KW Madd House": LocationData(None, "Kindlewood Overgrowth Madd House"),
}

