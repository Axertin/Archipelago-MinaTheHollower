from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

boss_locations: dict[str, LocationData] = {
}
collectable_locations: dict[str, LocationData] = {
    "Left Shipwreck Weapon": LocationData(17, "ShipWreck", Has("Left Shipwreck Weapon Kear")),
    "Right Shipwreck Weapon": LocationData(18, "ShipWreck", Has("Right Shipwreck Weapon Kear")),
    # "Loners Landing_o_1011": LocationData(19, "Loners Landing"), lock
    # "Loners Landing_o_1453": LocationData(20, "Loners Landing"),lock
    # "Loners Landing_o_14532": LocationData(21, "Loners Landing"),lock
    # "Loners Landing_o_14531": LocationData(22, "Loners Landing"),lock
"LL Residence Bubble": LocationData(23, "Loners Landing"),
"Shipwreck Cappy Chat": LocationData(24, "Loners Landing"),
"LL Defeat Kraken": LocationData(25, "Loners Landing", progress_type=LocationProgressType.EXCLUDED), # maybe seed a lot of Bonestone in here in defeat
"LL Knight Room Chest": LocationData(26, "LL Lower Bridge", CanClimb() & CanBurrow()),
"LL Boardwalk Fire Bounce Chest": LocationData(27, "LL Boardwalk", CanBounce()),
"LL Fences Side Cave Chest": LocationData(28, "LL Fences"),
    "LL Blighted Docks Tall Room Chest": LocationData(29, "LL Bridge"),
    "LL Boardwalk Sandfalls Ledge Chest": LocationData(30, "LL Boardwalk", CanBounce()),
"LL Bridge Cliff Chest": LocationData(31, "LL Bridge"),
    "LL Shipwreck Beach" : LocationData(32,"Loners Landing"),
"Bone Beach Outlook Chest": LocationData(324,"LL Boardwalk", CanBounce()),
}


