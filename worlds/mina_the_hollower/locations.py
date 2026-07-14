from BaseClasses import Region, Location, ItemClassification, LocationProgressType
from .data.events import RADIANT_MANOR_DATA
from .data.items import BoneFiller
from .data.locations import all_regions, all_region_transitions, all_internal_region_connections, \
    all_permanent_locations, dungeon_locations
from .data import LocationData, RegionConnection, Transition, matching_transition_types
from typing import TYPE_CHECKING
from .items import MinaTheHollowerItem

if TYPE_CHECKING:
    from . import MinaTheHollowerWorld


def create_location(world, name: str, data: LocationData, bonestone: bool = False):
    region = world.get_region(data.region)
    location = Location(world.player, name, data.location_id, region)
    location.progress_type = LocationProgressType.EXCLUDED if bonestone else data.progress_type
    location.item_rule = data.item_rule
    if bonestone:
        item = MinaTheHollowerItem(BoneFiller.BONE_STONE_2.value, ItemClassification.filler, BoneFiller.BONE_STONE_2.item_id, world.player)
        location.place_locked_item(item)
    region.locations.append(location)
    world.set_rule(location, data.rule)

def create_region(world: "MinaTheHollowerWorld", name: str, hint: str = ""):
    region = Region(name, world.player, world.multiworld)
    valid_locations: dict[str, (Location, LocationData)] = {}
    # TODO: dont loop through all locations for each region
    for loc_name, data in all_permanent_locations.items():
        if loc_name == "LL Captain's Gift" and world.options.ossex_start:
            continue
        if data.region != name:
            continue
        location = Location(world.player, loc_name, data.location_id, region)
        location.progress_type = data.progress_type
        location.item_rule = data.item_rule
        valid_locations[loc_name] = (location, data)
        region.locations.append(location)

    world.multiworld.regions.append(region)

    for loc_name, (location, data) in valid_locations.items():
        world.set_rule(location, data.rule)


def create_regions(world: "MinaTheHollowerWorld", regions: set[str]):
    # TODO: check if regions being a set introduces nondeterminism
    create_region(world, "Menu")
    for region in regions:
        create_region(world, region)
    for index, loc_map in dungeon_locations.items():
        for name, data in loc_map.items():
            override = index == RADIANT_MANOR_DATA.index and world.options.goal.value == world.options.goal.option_fixGenerators
            create_location(world, name, data, bonestone=(index in world.lit_generators) or override)





def get_regions(world: "MinaTheHollowerWorld") -> set[str]:
    # TODO: logic to handle which regions are being created based on yaml
    return all_regions


def create_entrances(world: "MinaTheHollowerWorld", regions):
    menu = world.get_region("Menu")

    world.create_entrance(menu, world.get_region("Ossex City Center Main"), name="Menu To Ossex")
    world.create_entrance(menu, world.get_region("Loner's Landing Shipwreck"), name="Menu To Shipwreck")
    for name, data in all_region_transitions.items():
        exiting_region = world.get_region(data.exiting_screen)
        entering_region = world.get_region(data.entering_screen)
        entrance = world.create_entrance(exiting_region, entering_region, rule=data.rule, name=name, force_creation=True)
        if data.entrance_group != 0 and world.entrance_rando:
            entrance.randomization_group = data.entrance_group
            world.disconnect_entrance_for_randomization(entrance)
    for name, data in all_internal_region_connections.items():
        exiting_region = world.get_region(data.exiting_region)
        entering_region = world.get_region(data.entering_region)
        entrance = world.create_entrance(exiting_region, entering_region, rule=data.rule, name=name,
                                         force_creation=True)
