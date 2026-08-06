from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...items import PlayerUpgrades, Trinkets, Sidearms
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasTrinket
from ...rules.movement_rules import CanJumpTiles

boss_locations: dict[str, LocationData] = {
}

collectable_locations: dict[str, LocationData] = {
    "MM Knight's Rest Chest": LocationData(311, "Mourner's Mile Knight's Rest Chest"),
    "MM Statue Room Bonestone": LocationData(315, "Mourner's Mile Statue Room Rope", CanBurrow()),
    "MM Shallow Tomb Kear": LocationData(305, "Mourner's Mile Dark Shallow Tomb Dark"),
    "MM Spike Tomb Trinket": LocationData(316, "Mourner's Mile Shallow Tomb"),
    "MM Spike Vault Vial Pouch": LocationData(312, "Mourner's Mile Spike Vault Upper"),
    "MM Spike Vault Hidden Room Kear": LocationData(310, "Mourner's Mile Spike Vault Hidden Room"),
    "MM Tower Tunnel Chest #1": LocationData(313, "Mourner's Mile Tower Tunnel Dark", CanBurrow()),
    "MM Tower Tunnel Chest #2": LocationData(314, "Mourner's Mile Tower Tunnel Dark", CanBurrow()),
    "MM Mina's Grave Chest": LocationData(309, "Mourner's Mile Mina's Grave"),
    "MM Mina's Grave Trinket": LocationData(308, "Mourner's Mile Mina's Grave"),
    "MM Spike Hell Chest": LocationData(355, "Mourner's Mile Spike Hell Sandfall", (HasTrinket(trinket=Trinkets.SPIKE_SPURS.value) & Has(PlayerUpgrades.HEALTH_ROSE.value, count=6)) | (Has(Sidearms.MIST_JAR.value) & Has(PlayerUpgrades.JOULE_BOX.value, count=2))),
}


