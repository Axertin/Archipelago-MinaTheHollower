from typing import ClassVar, Dict

from .data.items import all_items
from .data.locations import all_locations
from .world import MinaTheHollowerWorldBase
from .world_base import MinaTheHollowerWeb
from .constants import MINA_THE_HOLLOWER


class MinaTheHollowerWorld(MinaTheHollowerWorldBase):
    game = MINA_THE_HOLLOWER
    web = MinaTheHollowerWeb()

    item_name_to_id: ClassVar[Dict[str, int]] = {item_name: item_data.item_id for item_name, item_data in
                                                 all_items.items()}

    location_name_to_id: ClassVar[Dict[str, int]] = {loc_name: loc_data.location_id for loc_name, loc_data in all_locations.items()}

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)