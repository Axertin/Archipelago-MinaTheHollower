from enum import Enum, IntEnum
from typing import NamedTuple, Any, Union

from BaseClasses import ItemClassification, LocationProgressType, CollectionState, CollectionRule
from rule_builder.rules import Rule, True_
from ..world_base import MinaTheHollowerBase

class EntranceType(IntEnum):
    DO_NOT_RANDOMIZE_ENTRANCE = 0
    DOORS = 1


class ItemData(NamedTuple):
    item_id: int
    classification: ItemClassification
    amount: int = 1

class MovementItemData(NamedTuple):
    item_id: int
    distance: int
    classification: ItemClassification
    amount: int = 1

class RegionConnectionData(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()
    entrance_group: int = EntranceType.DO_NOT_RANDOMIZE_ENTRANCE

class LocationData(NamedTuple):
    location_id: int
    region: str
    rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()
    progress_type: LocationProgressType = LocationProgressType.DEFAULT

AnyItemData: type = Union[ItemData, MovementItemData]