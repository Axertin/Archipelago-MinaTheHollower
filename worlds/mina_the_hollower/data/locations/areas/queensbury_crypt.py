from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...events import QUEENSBURY_CRYPT_DATA
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, \
    HasFishingRod, HasVialsCount
from ...rules.movement_rules import CanJumpTiles
from ...rules.state_rules import RepairedGenerator, HasKear

collectable_locations: dict[str, LocationData] = {
    "QC Old Graveyard Bonestone": LocationData(51, "Queensbury Crypt Old Graveyard Main"),
    "QC Mrs. Sodsby Reward": LocationData(52, "Queensbury Crypt Old Graveyard Sodsby", CanBurrow()),
    "QC Bonnet Tomb Trinket": LocationData(57, "Queensbury Crypt Bonnet Tomb Inner"),
    "QC Broken Bridge Bonestone": LocationData(54, "Queensbury Crypt Broken Bridge"),
    "QC Pipe Room Bonestone": LocationData(53, "Queensbury Crypt Pipe Room"),
    "QC Castle Entry Weapon Chest": LocationData(56, "Queensbury Crypt Castle Entry"),
    "QC Midden 1 Kear": LocationData(64, "Queensbury Crypt Smelly Secret"),
    "QC Hidden Tunnel Bonestone": LocationData(61, "Queensbury Crypt Hidden Tunnel"),
    "QC Statue Head Hall Chest": LocationData(63, "Queensbury Crypt Statue Head Hall Entrance"),
    "QC Mirror Room Chest": LocationData(65, "Queensbury Crypt Mirror Room West"),
    "QC Mirror Room Belvedere Trinket": LocationData(66, "Queensbury Crypt Mirror Room West"),
    "QC Mirror Room Belvedere Kear": LocationData(67, "Queensbury Crypt Mirror Room West"),
    "QC Midden 2 Bonestone": LocationData(62, "Queensbury Crypt Putrid Place"),
    "QC Fish Tombstone": LocationData(68, "Queensbury Crypt Putrid Place", HasFishingRod()),
    "QC Midden Fight Reward": LocationData(59, "Queensbury Crypt Rancid Room"),
    "QC The Duchess Fight Reward": LocationData(58, "Queensbury Crypt Ancestral Chamber"),
    "QC The Duke Escort Reward": LocationData(60, "Queensbury Crypt Royal Tomb", HasVialsCount(count=2) & CanClimb()),
    "EH Post Generator Head Escort Chest": LocationData(238, "Eastern Heath East Corner", CanCarry() & CanClimb() & RepairedGenerator(event=QUEENSBURY_CRYPT_DATA) & HasKear(kear=SingleKears.MOURNERS_MILE_AFTER_GENERATOR_KEAR.value)),
    "MM Knight's Rest Post Generator Bonestone": LocationData(303, "Mourner's Mile Knight's Guard Hill", CanCarry()),
}
boss_locations: dict[str, LocationData] = {
    "QC Rancid Room Midden": LocationData(0, "Queensbury Crypt Rancid Room"),
    "QC Ancestral Chamber The Duchess": LocationData(1018, "Queensbury Crypt Ancestral Chamber"),
    "QC Solemn Generator Activated": LocationData(0, "Queensbury Crypt Solemn Generator"),
}
