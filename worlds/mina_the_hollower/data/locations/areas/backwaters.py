from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, CanSwim, CanCarry, CanClimb

collectable_locations: dict[str, LocationData] = {
    "BW Upper Shanty Swamp Plasma Jug": LocationData(290, "Backwaters Upper Swamp Waterfall"),
    "BW Upper Shanty Swamp Glutton's Jug": LocationData(289, "Backwaters Upper Swamp Waterfall"),  # needs plasma jug,
    "BW Upper Swamp Side Room Chest": LocationData(296, "Backwaters Upper Swamp Secret Room"),  # needs swim,
    "BW Lantern Cave Bonestone": LocationData(287, "Backwaters Upper Lantern Cave"),
    "BW Lantern Cave Vial Pouch": LocationData(295, "Backwaters Upper Lantern Cave"),
    "BW Pinky's Parlor Spark Catcher": LocationData(297, "Backwaters Pinky Shop"),
    "BW Pinky's Parlor Kear": LocationData(298, "Backwaters Pinky Shop"),
    "BW Pinky's Parlor Joule Box": LocationData(286, "Backwaters Pinky Shop Back"),  # needs hasladder(),
    "BW Lower Shanty Swamp Bonestone Block": LocationData(293, "Backwaters Lower Swamp Fishing"),
    # needs kear, burrow, swim,
    "BW Lower Shanty Swamp Evasion Powder": LocationData(294, "Backwaters Lower Swamp Station Entrance"),
    # needs hasladder(),
    "BW Lower Shanty Swamp Bonestone": LocationData(288, "Backwaters Lower Swamp Station Entrance"),
    # needs hasladder(),
    "BW Lower Shanty Swamp Tumbling Tutu": LocationData(291, "Backwaters Lower Swamp Shanty Band"),
    # needs burrow, climb, carry, swim,
    "BW Lucky's Lair Kear": LocationData(292, "Backwaters Lucky's Lair"),  # needs burrow,
    "BW Fishing Hole Fishing Rod": LocationData(300, "Backwaters Fishing Hole"),
    "BW Fishing Hole Fleeper Head": LocationData(299, "Backwaters Fishing Hole"),  # needs fishing rod,
    "BW Fishing Hole Thalessian Pearl": LocationData(302, "Backwaters Fishing Hole"),
    # needs fishing raft or (fishing rod + tunneler's codex, swim),
    "BW Fishing Hole Gilded Rod": LocationData(301, "Backwaters Fishing Hole"),
    # needs fishing raft or fishing rod + tunneler's codex, swim),
}

boss_locations: dict[str, LocationData] = {
    "Defeat Fish Boss": LocationData(0, "Waterfall Backwaters"),
}

