from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, ReachingSideArm, CanClimb, \
    CanSwim
from ...rules.state_rules import HasCompletedOneSparkGenerator


collectable_locations: dict[str, LocationData] = {
    "EH Grassland Trinket Bag" : LocationData(221, "Eastern hearth Grassland", HasCompletedOneSparkGenerator()),
    "EH Grassland Dork Eyes" : LocationData(241, "Eastern Hearth Grassland Bridge Right"), #needs fishing rod,
    "EH Grassland Ossex Patio Chest" : LocationData(231, "Eastern Hearth I Screen"), #needs burrow,
    "EH Grassland Bush Room Bonestone" : LocationData(236, "Eastern hearth Bush Room"), #needs kear,
    "EH Grassland Riverbed Chest" : LocationData(233, "Eastern Hearth Grassland Riverbed Bottom"),
    "EH Choppe Shoppe Chain Capacitor" : LocationData(226, "Eastern Hearth Choppe Shoppe"),
    "EH Hidden Grotto Chest" : LocationData(228, "Eastern Hearth Hidden Grotto"), #needs kear, burrow,
    "EH Grassland Waterfall Chest" : LocationData(234, "Eastern Hearth Grassland Waterfall Second Level"), #needs burrow,
    "EH Grassland Waterfall Windfall Charm" : LocationData(223, "Eastern Hearth Grassland Waterfall Second Level"), #needs volt axe or (spring heeled boots, kear, burrow),
    "EH Grassland Vertical Spinner Room Chest" : LocationData(238, "Eastern hearth East Corner"), #needs (beat  queensbury spark generator),
    "EH Under the Bridge Chest" : LocationData(230, "Eastern hearth Under Bridge West"),
    "EH Buckler's Bluff Joule Box" : LocationData(229, "Eastern Hearth Buckler's Bluff Cliff"),
    "EH Grassland Poppit Cave Chest" : LocationData(235, "Eastern Hearth Grassland Poppit Cave"), #needs burrow,
    "EH Grassland Poppit Cave Willow" : LocationData(239, "Eastern Hearth Poppit"), #needs burrow,
    "EH Grassland Poppit Cave Kear" : LocationData(240, "Eastern Hearth Poppit"),
    "EH Frozen Pass Chest" : LocationData(232, "Eastern hearth Frozen Pass"), #needs burrow, climb,
    "EH Frozen Pass IceBlock" : LocationData(237, "Eastern hearth Frozen Pass"), #needs burrow,
}

boss_locations: dict[str, LocationData] = {
    "EH Grassland Maxi": LocationData(1018, "Eastern Heath Grassland", HasCompletedOneSparkGenerator()),
}
