from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...items import Wallets
from ...rules.ability_rules import CanBurrow, CanBounce, HasVialsCount, CanClimb, CanCarry, HasFishingRod
from ...rules.state_rules import RepairedGeneratorCount
from ...rules.movement_rules import CanJumpTiles

collectable_locations: dict[str, LocationData] = {
    "SO Commons Ossex Entry Left Chest" : LocationData(270, "Ossex Entry Western Wall Chest", CanJumpTiles(distance=5, has_wall=True)),
    "SO Commons Ossex Entry Right Chest" : LocationData(266, "Ossex Entry Eastern Wall Chest"),
    "SO Commons Chest" : LocationData(264, "Southern Outskirts Commons Main", CanBurrow() & CanBounce()),
    "SO Fish Crumblefin Head" : LocationData(274, "Southern Outskirts Commons Main", HasFishingRod() & CanCarry()),
    "SO Cave Network Chest" : LocationData(265, "Southern Outskirts Cave Network Deep Exit"),
    "SO Cave Network Side Room Chest" : LocationData(268, "Southern Outskirts Cave Deep Arena"),
    "SO Poppit Keri" : LocationData(272, "Southern Outskirts Poppit"),
    "SO Poppit Kear" : LocationData(273, "Southern Outskirts Poppit"),
    "SO Southern Pit Room Bonestone" : LocationData(261, "Southern Outskirts Commons Southern Pit Room Main", CanJumpTiles(distance=5, has_wall=True) & CanBurrow()),
    "SO Western Pit Room Chest" : LocationData(267, "Southern Outskirts Commons Western Pit Room Main", item_rule=lambda item: item.name != Wallets.WALLET_SIZE.value),
    "SO Thorne Residence Basement Trinket" : LocationData(269, "Southern Outskirts Residence Basement", item_rule=lambda item: item.name != Wallets.WALLET_SIZE.value),
    "SO Mining Passage Chest" : LocationData(331, "Southern Outskirts Mining Passage Secret", CanBurrow() & CanBounce() &  HasVialsCount(count=2)),
    "Dugin Fight 2 Trinket" : LocationData(263, "Southern Outskirts Moonbath", RepairedGeneratorCount(count=2)),
    "SO Four Flowers Chest" : LocationData(271, "Southern Outskirts Four Flowers Shortcut", CanBounce()),
}

boss_locations: dict[str, LocationData] = {
    "SO Moonbath Dugin #1" : LocationData(None, "Southern Outskirts Moonbath"),
    "SO Moonbath Dugin #2" : LocationData(None, "Southern Outskirts Moonbath"),
}
