from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from .. import LocationData
from ... import RegionConnectionData, EntranceType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBlossomBounce, CanJumpTiles

collectable_locations: dict[str, LocationData] = {
    "Left Shipwreck Weapon": LocationData(17, "ShipWreck", Has("Left Shipwreck Weapon Kear")),
    "Right Shipwreck Weapon": LocationData(18, "ShipWreck", Has("Right Shipwreck Weapon Kear")),
    # "Loners Landing_o_1011": LocationData(19, "Loners Landing"), lock
    # "Loners Landing_o_1453": LocationData(20, "Loners Landing"),lock
    # "Loners Landing_o_14532": LocationData(21, "Loners Landing"),lock
    # "Loners Landing_o_14531": LocationData(22, "Loners Landing"),lock
    "LL Blighted Docks Burrow Residence Bubble": LocationData(23, "Loners Landing"),
    "ShipWreck Cappy Chat": LocationData(24, "Loners Landing"),
    "LL Defeat Kraken": LocationData(25, "Loners Landing", progress_type=LocationProgressType.EXCLUDED), # maybe seed a lot of Bonestone in here in defeat
    "LL Blighted Docks Residence Chest": LocationData(26, "LL Rope and Bounce Area"),
    "LL Boardwalk Fire Bounce Chest": LocationData(27, "LL Boardwalk", CanBlossomBounce()),
    "LL Blighted Docks Side Cave Chest": LocationData(28, "Loners Landing"),
    "LL Blighted Docks Tall Room Chest": LocationData(29, "LL Rope and Bounce Area"),
    "LL Boardwalk Sandfalls Ledge Chest": LocationData(30, "LL Boardwalk", CanBlossomBounce()),
    "LL Belowdecks Chest": LocationData(31, "ShipWreck"),
    "LL Shipwreck Beach" : LocationData(32,"Loners Landing"),
}

connections: dict[str, RegionConnectionData] = {
    "Loners Landing_Shipwreck" : RegionConnectionData("Loners Landing", "ShipWreck", CanReachLocation("Thorne 1", parent_region_name="mansion"), EntranceType.DOORS),
    "Shipwreck_Loners Landing" : RegionConnectionData("ShipWreck", "Loners Landing", entrance_group=EntranceType.DOORS),
    "Bounce Rope_Loners Landing" : RegionConnectionData("LL Rope and Bounce Area", "Loners Landing", CanJumpOneTile() & CanBurrow()),
    "Loners Landing_Bounce Rope" : RegionConnectionData("Loners Landing", "LL Rope and Bounce Area", CanJumpOneTile() & CanBurrow()),

    "LL Boardwalk_Bounce Rope" : RegionConnectionData("LL Boardwalk", "LL Rope and Bounce Area", CanJumpTiles(distance=2) & Has("LL Boardwalk Kear")),
    "Bounce Rope_LL Boardwalk" : RegionConnectionData("LL Rope and Bounce Area", "LL Boardwalk", CanJumpTiles(distance=2) & Has("LL Boardwalk Kear")),

    "LL Boardwalk_Southern Outskirts" : RegionConnectionData("LL Boardwalk", "Southern Outskirts", CanJumpTiles(distance=2)),
}