from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...items import SingleKears, PermanentUpgrades
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasFishingRod
from ...rules.movement_rules import CanJumpTiles
from ...rules.state_rules import HasKear

collectable_locations: dict[str, LocationData] = {
    "CTP Frigid Station Missed Train Chest": LocationData(113, "Coltrane Peak Station Tracks"),
    "CTP Frozen Pass Rope Chest": LocationData(112, "Coltrane Peak Frozen Pass", CanClimb()),
    "CTP Dead Man's Gorge Passage Trinket": LocationData(110, "Coltrane Peak Gorge Ice Gauntlet"),
    "CTP Dead Man's Gorge Rail Kear": LocationData(111, "Coltrane Peak Train Tracks Secret", CanBurrow()),
    "CTP Frostbite Woods Mirren Trinket": LocationData(114, "Coltrane Peak Frostbite Woods"),
    "CTP Rail Yard Purple Structure Chest": LocationData(118, "Coltrane Peak Rail Yard"),
    "CTP Rail Yard Cliff Chest": LocationData(117, "Coltrane Peak Rail Yard"),
    "CTP Rail Yard Weapon Chest": LocationData(119, "Coltrane Peak Rail Yard Chest"),
    "CTP Fish Fishcicle Core": LocationData(122, "Coltrane Peak Frozen River", CanBurrow() & HasFishingRod()),
    "CTP Rail Yard Kear Room Rupert Shop Trinket": LocationData(120, "Coltrane Peak Frozen River", CanBurrow()),
    "CTP Rail Yard Kear Room Rupert Shop Kear": LocationData(121, "Coltrane Peak Frozen River", CanBurrow()),
    "CTP Spiral Summit Kear": LocationData(116, "Coltrane Peak Spiral Summit Secret", CanBurrow() & CanClimb()),
    "CTP Agnes Express Bone Mimic Bonestone": LocationData(123, "Coltrane Peak Agnes Express Rear"),
    "CTP Maelstrom Locomotress Health Rose": LocationData(124, "Coltrane Peak Agnes Express Arena"),
    "CTP Frozen Pass Chest" : LocationData(232, "Coltrane Peak Frozen Pass"),
    "CTP Frozen Pass Ice Block Trinket" : LocationData(237, "Coltrane Peak Frozen Pass Bottom"),
    "WW Balcony Snowball Fight Trinket" : LocationData(242, "Western Wilds Balcony", HasKear(kear=SingleKears.WESTERN_WILDS_BALCONY_KEAR.value) & CanBurrow() & CanCarry() & CanClimb()
                                                           & Has(PermanentUpgrades.TRAIN_PASS.value) & Has(PermanentUpgrades.COLTRANE_PEAK_TICKET.value)),
}


boss_locations: dict[str, LocationData] = {
    "CTP Frozen Generator Activated": LocationData(None, "Coltrane Peak Frozen Generator"),
    "CTP Maelstrom Locomotress Agnes Boss": LocationData(None, "Coltrane Peak Agnes Express Arena"),
    "CTP Icebound Cavern Frozen Horror Boss": LocationData(None, "Coltrane Peak Frozen Horror Arena"),
    "CTP Frostbite Woods Mirren": LocationData(None, "Coltrane Peak Mirren Room"),
    "CTP Fateful Cliff Thorne CTP Boss": LocationData(None, "Coltrane Peak Thorne Arena"),  # needs climb,
}
