from BaseClasses import ItemClassification
from collections import Counter

from .. import options, MinaTheHollowerWorld
from .bases import MinaTestBase
from ..data.locations import all_collectables


def test_all_locations(base):
    world_location_names = {location.name for location in base.world.get_locations()}

    for name in all_collectables:
        base.assertIn(name, world_location_names)
    if base.world.options.ossex_start.value:
        base.assertNotIn("LL Captain's Gift", world_location_names)
    else:
        base.assertIn("LL Captain's Gift", world_location_names)

class TestCollectablesNoOssexStart(MinaTestBase):
    options = {
        "ossex_start": "false",
    }

    def test_all_locations_loaded(self):
        test_all_locations(self)


class TestCollectablesOssexStart(MinaTestBase):
    options = {
        "ossex_start": "true",
    }

    def test_all_locations_loaded(self):
        test_all_locations(self)
