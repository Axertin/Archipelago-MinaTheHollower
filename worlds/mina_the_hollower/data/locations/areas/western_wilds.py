from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData
from ...items import SingleKears, Trinkets, Wallets, PermanentUpgrades
from ...rules.ability_rules import CanBurrow, CanBounce, CanCarry, HasFishingRod, CanClimb, HasTrinket
from ...rules.state_rules import HasKear
from ...rules.movement_rules import CanJumpTiles

collectable_locations: dict[str, LocationData] = {
    "WW Secret Passage Chest" : LocationData(251, "Western Wilds Secret Passageway East", CanJumpTiles(distance=3), item_rule=lambda item: item.name != Wallets.WALLET_SIZE.value),
    "WW Secret Passage Locked Chest" : LocationData(248, "Western Wilds Secret Passageway East", CanJumpTiles(distance=5) & HasKear(kear=SingleKears.WESTERN_WILDS_SECRET_PASSAGE_KEAR.value)),
    "WW Brute Chest" : LocationData(253, "Western Wilds Brutes"),
    "WW Leaf Area Chest" : LocationData(250, "Western Wilds End", CanBurrow()),
    "WW Leaf Area Trinket" : LocationData(245, "Western Wilds Brutes", (CanBurrow() & CanCarry()) | (CanBurrow() &  Has(PermanentUpgrades.TRAIN_PASS.value) & Has(PermanentUpgrades.SEPTEMBURG_TICKET.value))), #needs kill the other leaf,
    "WW Fish Cuddlepus Shell" : LocationData(259, "Western Wilds Main", HasFishingRod()),
    "WW Occupied Bridge Underneath Chest" : LocationData(252, "Western Wilds Foundry Path"),
    "WW Molten Foundry Poppit Trinket" : LocationData(256, "Western Wilds Molten Foundry Dark Poppit"),
    "WW Molten Foundry Poppit Kear" : LocationData(257, "Western Wilds Molten Foundry Dark Poppit"),
    "WW Molten Foundry Dark Chest" : LocationData(255, "Western Wilds Molten Foundry Dark", CanBurrow() | HasTrinket(trinket=Trinkets.POLYP_LAMP.value)),
    "WW Molten Foundry Trinket" : LocationData(249, "Western Wilds Molten Dungeon End"),
    "WW Fish Glomper Stalk" : LocationData(258, "Western Wilds Western Pond", HasFishingRod()),
    "WW Balcony Chest" : LocationData(254, "Western Wilds Balcony", HasKear(kear=SingleKears.WESTERN_WILDS_BALCONY_KEAR.value)),
}

boss_locations: dict[str, LocationData] = {
}
