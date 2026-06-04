from BaseClasses import Region, Location
from .data.locations.regions import region_list
from .data.locations.game_locations import collectable_locations
from .data.locations.region_entrances import connections
from .data import LocationData, RegionConnectionData

def create_region(world, name: str, hint: str = ""):
    region = Region(name, world.player, world.multiworld)

    valid_locations: dict[str, (Location, LocationData)] = {}

    for loc_name, data in collectable_locations.items():
        if data.region != name:
            continue
        location = Location(world.player, loc_name, data.location_id, region)
        location.progress_type = data.progress_type
        valid_locations[loc_name] = (location, data)
        region.locations.append(location)

    world.multiworld.regions.append(region)

    # for loc_name, (location, data) in valid_locations.items():
    #     world.set_rule(location, data.rule)

def create_regions(world, regions: set[str]):
    for region in regions:
        create_region(world, region)

def get_regions(world) ->  set[str]:
    #logic to handle which regions are being created
    return region_list

def connect_entrances(world, regions):
    for name, data in connections.items():
        exiting_region = world.get_region(data.exiting_region)
        entering_region = world.get_region(data.entering_region)
        entrance = world.create_entrance(exiting_region, entering_region, rule=data.rule, name=name, force_creation=True)