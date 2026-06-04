from collections import ChainMap

from .. import LocationData
from .game_locations import collectable_locations

all_locations: ChainMap[str, LocationData] = ChainMap(
    collectable_locations
)