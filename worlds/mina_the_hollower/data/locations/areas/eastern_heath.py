from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...items import Trinkets, SingleKears, PermanentUpgrades, Wallets
from ...rules.ability_rules import CanBurrow, CanBounce, HasReachingSideArm, CanClimb, \
    CanSwim, HasFishingRod
from ...rules.state_rules import HasKear, RepairedGeneratorCount
from ...rules.movement_rules import CanJumpTiles

collectable_locations: dict[str, LocationData] = {
    "EH Maxi Fight Reward" : LocationData(221, "Eastern Heath Grassland", RepairedGeneratorCount(count=1)),
    "EH Fish Dork Eyes" : LocationData(241, "Eastern Heath Grassland Bridge Left", HasFishingRod()), #needs fishing rod,
    "EH Ossex Entry Chest" : LocationData(231, "Eastern Heath I Screen", CanBurrow()),
    "EH Bush Room Locked Bonestone" : LocationData(236, "Eastern Heath Bush Room", HasKear(kear=SingleKears.EASTERN_HEATH_GRASSLAND_BUSHROOM_KEAR.value)), #needs kear,
    "EH Riverbed Chest" : LocationData(233, "Eastern Heath Grassland Riverbed Bottom", item_rule=lambda item: item.name != Wallets.WALLET_SIZE.value),
    "EH Choppe Shoppe Trinket" : LocationData(226, "Eastern Heath Choppe Shoppe"),
    "EH Hidden Slime Cave Chest" : LocationData(228, "Eastern Heath Hidden Grotto"),
    "EH Beside Kite Chest" : LocationData(234, "Eastern Heath Grassland Waterfall Second Level"),
    "EH Kite Trinket" : LocationData(223, "Eastern Heath Grassland Waterfall Second Level", HasReachingSideArm() & (
            (CanJumpTiles(distance=4, has_wall=True, no_sidearms=True) & CanClimb()) |
            (CanBurrow() & CanClimb()) |
            (CanBurrow() & HasKear(kear=SingleKears.EASTERN_HEATH_WATERFALL_KEAR.value)) |
            (Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value) & Has(PermanentUpgrades.TRAIN_PASS.value) & CanClimb()))
    ),
    "EH Mimic Chest" : LocationData(230, "Eastern Heath Under Bridge West"),
    "EH Buckler's Bluff Joule Box" : LocationData(229, "Eastern Heath Buckler's Bluff Cliff", CanClimb()),
    "EH Poppit Cave Chest" : LocationData(235, "Eastern Heath Grassland Poppit Cave"),
    "EH Poppit Cave Willow" : LocationData(239, "Eastern Heath Poppit"),
    "EH Poppit Cave Kear" : LocationData(240, "Eastern Heath Poppit"),
    "EH Frozen Pass Trinket" : LocationData(237, "Coltrane Peak Frozen Pass Bottom"),
}

boss_locations: dict[str, LocationData] = {
    "EH Maxi": LocationData(1018, "Eastern Heath Grassland", RepairedGeneratorCount(count=1)),
}
