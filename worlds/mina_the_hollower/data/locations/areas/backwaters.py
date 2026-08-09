from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData
from ...items import Trinkets, SingleKears, Sidearms, FishingUpgrades, Wallets
from ...rules.ability_rules import CanBurrow, CanBounce, CanSwim, CanCarry, CanClimb, \
    HasFishingRod, PowerLevelThreshold, HasTrinket
from ...rules.state_rules import HasLadder, HasKear, RepairedGeneratorCount
from ...rules.movement_rules import CanJumpTiles

collectable_locations: dict[str, LocationData] = {

    "BW Buffo The Frog Gift": LocationData(289, "Backwaters Upper Swamp Waterfall", item_rule=lambda item: item.name != Wallets.WALLET_SIZE.value),
    "BW Side Room Chest": LocationData(296, "Backwaters Upper Swamp Secret Room", CanSwim() & (((CanJumpTiles(distance=2, no_sidearms=True) | CanJumpTiles(distance=4, has_wall=True)) | CanBurrow()) | (CanBurrow() & HasTrinket(trinket=Trinkets.WALLOWERS_GAUNTLETS.value)))),
    "BW Lantern Cave Bonestone": LocationData(287, "Backwaters Upper Lantern Cave"),
    "BW Lantern Cave Vial Pouch": LocationData(295, "Backwaters Upper Lantern Cave"),
    "BW Pinky's Parlor Trinket": LocationData(297, "Backwaters Pinky Shop"),
    "BW Pinky's Parlor Kear": LocationData(298, "Backwaters Pinky Shop"),
    "BW Pinky's Parlor Joule Box": LocationData(286, "Backwaters Pinky Shop Back", HasLadder()),
    "BW Fishing Hole Entrance Locked Chest": LocationData(293, "Backwaters Lower Swamp Fishing", HasKear(kear=SingleKears.BACKWATERS_FISHING_KEAR.value) & (CanSwim() | CanJumpTiles(distance=4))),
    "BW Ladder Trinket": LocationData(294, "Backwaters Lower Swamp Station Entrance", HasLadder()),
    "BW Ladder Bonestone": LocationData(288, "Backwaters Lower Swamp Station Entrance", HasLadder()),
    "BW Rescue Cliff Band Reward": LocationData(291, "Backwaters Lower Swamp Shanty Band", CanCarry() & CanBurrow() & CanSwim() & CanClimb()),
    "BW Lucky's Lair Gift": LocationData(292, "Backwaters Lucky's Lair", CanBurrow() & CanCarry()),
    "BW Fishing Hole Fishing Rod": LocationData(300, "Backwaters Fishing Hole"), CanBurrow() & CanJumpTiles(distance=5) | CanSwim() & HasJoulesBox(),
    "BW Fish Fleeper Head": LocationData(299, "Backwaters Fishing Hole", HasFishingRod()),
    "BW Fishing Hole Thalassian Pearl": LocationData(302, "Backwaters Fishing Hole", PowerLevelThreshold(power=35) & HasFishingRod() & CanSwim() & (HasTrinket(trinket=Trinkets.TUNNELING_CODEX.value) | Has(FishingUpgrades.FISHING_ROD.value, count=2))),
    "BW Fishing Hole Gilded Rod": LocationData(301, "Backwaters Fishing Hole", RepairedGeneratorCount(count=6) & HasFishingRod() & CanSwim() & (HasTrinket(trinket=Trinkets.TUNNELING_CODEX.value) | Has(FishingUpgrades.FISHING_ROD.value, count=2))),
}

boss_locations: dict[str, LocationData] = {
    "BW Buffo The Frog Fight Plasma Jug": LocationData(290, "Backwaters Upper Swamp Waterfall", HasTrinket(trinket=Trinkets.EMPTY_JUG.value) & PowerLevelThreshold(power=24)),
}

