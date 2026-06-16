from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasVialsCount, CanClimb

collectable_locations: dict[str, LocationData] = {
    "SO Commons Ossex Entry Left Chest" : LocationData(270, "SO Commons Ossex Entry", CanBurrow() & (CanJumpTiles(distance=6) | CanBounce()) ),
    "SO Commons Ossex Entry Right Chest" : LocationData(266, "SO Commons Ossex Entry", Has("Ossex High Street SE Garden Kear")),
    "SO Commons Chest" : LocationData(264, "SO Commons Main", CanBurrow() & CanBounce()),
    "SO Commons Crumblefin Head" : LocationData(274, "SO Commons Cliff", Has("FishingRod")),
    "SO Cave Network Chest" : LocationData(265, "SO Cave Network Deep"),
    "SO Cave Network Side Room Chest" : LocationData(268, "SO Cave Network Deep"),
    "SO Poppit Keri" : LocationData(272, "SO Poppit"),
    "SO Poppit Kear" : LocationData(273, "SO Poppit"),
    "SO Southern Pit Room Bonestone" : LocationData(261, "SO Commons Southern Pit Room", CanJumpTiles(distance=5)),
    "SO Western Pit Room Chest" : LocationData(267, "SO Commons Western Pit Room Main"),
    "SO Residence Primed Vial Pouch" : LocationData(269, "SO Residence Basement"),
    "SO Mining Passage Chest" : LocationData(331, "SO Mining Passage Secret"),
    "SO Moonbath Lace Glove" : LocationData(263, "SO Moonbath"),
    "SO Four Flowers Chest" : LocationData(271, "SO Four Flowers", CanBounce()),
}

boss_locations: dict[str, LocationData] = {
}
