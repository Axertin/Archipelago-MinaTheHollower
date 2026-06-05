from rule_builder.rules import Has, True_, CanReachLocation
from .. import RegionConnectionData, EntranceType
from ..rules.ability_rules import CanJumpOneTile, CanBurrow, CanJumpTiles
from ...world_base import MinaTheHollowerBase

connections: dict[str, RegionConnectionData] = {
    "Menu_region18" : RegionConnectionData("Menu", "region18"),
    "region18_introBeach" : RegionConnectionData("region18", "introBeach"),
    "introBeach_bayou" : RegionConnectionData("introBeach", "bayou"),
    "bayou_cryptB" : RegionConnectionData("bayou", "cryptB"),
    "cryptB_boneBeachA" : RegionConnectionData("cryptB", "boneBeachA"),
    "boneBeachA_septemburgB" : RegionConnectionData("boneBeachA", "septemburgB"),
    "septemburgB_frozenTrainyardA" : RegionConnectionData("septemburgB", "frozenTrainyardA"),
    "frozenTrainyardA_astralOrrery" : RegionConnectionData("frozenTrainyardA", "astralOrrery"),
    "astralOrrery_mansion" : RegionConnectionData("astralOrrery", "mansion"),
    "mansion_hub" : RegionConnectionData("mansion", "hub"),
    "hub_hub_overworld_east" : RegionConnectionData("hub", "hub_overworld_east"),
    "hub_overworld_east_hub_overworld_west" : RegionConnectionData("hub_overworld_east", "hub_overworld_west"),
    "hub_overworld_west_hub_overworld_south" : RegionConnectionData("hub_overworld_west", "hub_overworld_south"),
    "hub_overworld_south_hub_mansion" : RegionConnectionData("hub_overworld_south", "hub_mansion"),
    "hub_mansion_bayou_overworld" : RegionConnectionData("hub_mansion", "bayou_overworld"),
    "bayou_overworld_boneBeach_overworld" : RegionConnectionData("bayou_overworld", "boneBeach_overworld"),
    "boneBeach_overworld_septemburg_overworld" : RegionConnectionData("boneBeach_overworld", "septemburg_overworld"),
    "septemburg_overworld_crypt_overworld" : RegionConnectionData("septemburg_overworld", "crypt_overworld"),
}

#"test_test" : RegionConnectionData("test", "test"),
#"test_test" : RegionConnectionData("test", "LL Boardwalk"),
game_connections: dict[str, RegionConnectionData] = {
    #Loners landing
    "Loners Landing_Shipwreck" : RegionConnectionData("Loners Landing", "ShipWreck", CanReachLocation("Thorne 1", parent_region_name="mansion"), EntranceType.DOORS),
    "Shipwreck_Loners Landing" : RegionConnectionData("ShipWreck", "Loners Landing", entrance_group=EntranceType.DOORS),
    "Bounce Rope_Loners Landing" : RegionConnectionData("LL Rope and Bounce Area", "Loners Landing", CanJumpOneTile() & CanBurrow()),
    "Loners Landing_Bounce Rope" : RegionConnectionData("Loners Landing", "LL Rope and Bounce Area", CanJumpOneTile() & CanBurrow()),

    "LL Boardwalk_Bounce Rope" : RegionConnectionData("LL Boardwalk", "LL Rope and Bounce Area", CanJumpTiles(distance=2) & Has("LL Boardwalk Kear")),
    "Bounce Rope_LL Boardwalk" : RegionConnectionData("LL Rope and Bounce Area", "LL Boardwalk", CanJumpTiles(distance=2) & Has("LL Boardwalk Kear")),


    #southern outskirts
    "LL Boardwalk_Southern Outskirts" : RegionConnectionData("LL Boardwalk", "Southern Outskirts"),
    "Southern Outskirts_LL Boardwalk" : RegionConnectionData("Southern Outskirts", "LL Boardwalk"),
}

menu_starts = {
    "Menu_Loners Landing" : RegionConnectionData("Menu", "Loners Landing"),
}