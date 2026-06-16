from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce

collectable_locations: dict[str, LocationData] = {
    "WW Secret Passage Chest" : LocationData(251, "Western Wilds Secret Passageway East"), #needs 3 tiles of air movement,
    "WW Secret Passage Joule Box" : LocationData(248, "Western Wilds Secret Passageway East"), #needs kear, 5 tiles of air movement,
    "WW Occupied Bridge Brute Chest" : LocationData(253, "Western Wilds Brutes"),
    "WW Occupied Bridge Far Chest" : LocationData(250, "Western Wilds End"), #needs burrow,
    "WW Occupied Bridge Dead Leaf" : LocationData(245, "Western Wilds Brutes"), #needs kill the other leaf,
    "WW Occupied Bridge Cuddlepus Shell" : LocationData(259, "Western Wilds Western Pond"), #needs fishing rod,
    "WW Occupied Bridge Underneath Chest" : LocationData(252, "Western Wilds Foundry Path"), #needs burrow,
    "WW Molten Foundry Poppit Helio" : LocationData(256, "Western Wilds Molten Foundry Dark Poppit"),
    "WW Molten Foundry Poppit Kear" : LocationData(257, "Western Wilds Molten Foundry Dark Poppit"),
    "WW Molten Foundry Dark Chest" : LocationData(255, "Western Wilds Molten Foundry Dark"), #needs burrow,
    "WW Molten Foundry Flame Guard" : LocationData(249, "Western Wilds Molten Dungeon End"),
    "WW Western Pond Glomper Stalk" : LocationData(258, "Western Wilds Western Pond"), #needs fishing rod, burrow,
    "WW Balcony Chest" : LocationData(254, "Western Wilds Balcony"), #needs kear, burrow,
    "WW Balcony Dummy Cache" : LocationData(242, "Western Wilds Balcony"), #needs kear, burrow, carry, climb,
}

boss_locations: dict[str, LocationData] = {
}
