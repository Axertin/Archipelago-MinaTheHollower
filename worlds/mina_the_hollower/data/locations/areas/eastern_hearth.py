from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, ReachingSideArm, CanClimb, \
    CanSwim
from ...rules.state_rules import HasCompletedOneSparkGenerator


collectable_locations: dict[str, LocationData] = {
    "EH Grassland Trinket Bag" : LocationData(221, "Eastern Heath Grassland", HasCompletedOneSparkGenerator()),
    "EH Grassland Waterfall Windfall Charm" : LocationData(223, "Eastern Hearth Grassland Waterfall Second Level"),
    "EH Choppe Shoppe Chain Capacitor" : LocationData(226, "Eastern Hearth Choppe Shoppe"),
    "EH Grassland Waterfall Chest" : LocationData(234, "Eastern Hearth Grassland Waterfall Second Level"),
    "EH Buckler's Bluff Joule Box": LocationData(229, "Eastern Hearth Bucklers Bluff Cliff"),
    "EH Under the Bridge Chest" : LocationData(230, "Eastern Hearth Under Bridge West"),
    "EH Grassland Riverbed Chest" : LocationData(233, "Eastern Hearth Grassland Riverbed Dive"),
    "EH Grassland Bush Room Bonestone" : LocationData(236, "Eastern Hearth Bush Room", Has("Eastern Hearth Grassland Bushroom Kear")),
    "EH Grassland Horizontal Spinner Room Chest" : LocationData(231, "Eastern Hearth Grassland Horizontal Spinner Room"),
    "EH Grotto Chest" : LocationData(228, " Eastern Hearth Hidden Cave"),
    "EH Grassland Poppit Cave Chest" : LocationData(235, "Eastern Hearth Grassland Poppit Cave"),
    "EH Frozen Pass Chest" : LocationData(232, "Eastern Heath Frozen Pass", Has("FrozenTrainyardTicket")),
    "EH Frozen Pass IceBlock" : LocationData(237, "Eastern Heath Frozen Pass"),
    "EH Grassland Vertical Spinner Room Chest" : LocationData(238, "Eastern Hearth East Corner"),#TODO: CanReachLocation(HEAD AFTER SPARK GEN)
    "EH Grassland Poppit Cave Willow" : LocationData(239, "Eastern Hearth Grassland Poppit Cave"),
    "EH Grassland Poppit Cave Kear" : LocationData(240, "Eastern Hearth Grassland Poppit Cave"),
    "EH Grassland Dork Eyes" : LocationData(241, "Eastern Heath Grassland Bridge", Has("FishingRod")),
}

boss_locations: dict[str, LocationData] = {
    "EH Grassland Maxi": LocationData(1018, "Eastern Heath Grassland", HasCompletedOneSparkGenerator()),
}
