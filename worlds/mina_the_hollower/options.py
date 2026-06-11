from dataclasses import dataclass

from Options import DeathLink, DefaultOnToggle, Toggle, OptionSet, OptionDict, Choice, OptionGroup, \
    PerGameCommonOptions, Range


class Goal(Choice):
    """
    Goal
    """
    display_name = "Goal"
    option_radientManorGenerator = 0

class NumberOfGenerators(Range):
    """
    The number of generators required to go to radient manor
    """
    display_name = "Generators Required"
    range_start = 1
    range_end = 6
    default = 6

class EssexStart(Toggle):
    """
    Start In Essex
    """
    display_name = "Essex Start"

class AbilityRando(Toggle):
    """
    Randomize abilities. You will always start in Ossex
    """
    display_name = "Abilty Rando"

class RandomizeEntrances(OptionSet):
    """
    Currently there are no valid keys. Only give this []

    - **Doors** - Randomizes All Doors between eachother
    - **Stairs** - Randomizes All Stairs between eachother
    - **Area Transitions** - Randomizes All Screen transitions that change areas
    - **Screen Transitions** - Randomizes All Screen transitions
    """
    display_name = "Entrance Randomization"
    valid_keys = []
    # valid_keys = ["Doors", "Stairs", "Area Transitions", "Screen Transitions"]

class ExcludedAreas(OptionSet):
    """
    Each Region you add to this list will not have any location in them have any items. If it includes a Spark Generator Area, that generator will be marked complete

    Valid Area Names
    - **Mourner's Mile** -
    - **Queensbury Crypt** -
    """
    display_name = "Excluded Areas"
    valid_keys = []
    # valid_keys = ["Mourner's Mile", "Queensbury Crypt"]

class KearRandomization(Choice):
    """
    Vanilla: Universal Kears are in the multiworld. Every Kear Lock you open before receiving all universal Kears will be OUT OF LOGIC
    AP Items: Each Kear Lock is removed by a unique AP item
    Area AP Items: All Kear Locks in an area are removed by a single AP Item
    """
    # option_vanilla = 0
    option_apItems = 1
    option_areaApItems = 2
    default = 1

#TODO:implement this
# class ShuffledSidearms(Toggle):
#     """
#     Sidearms are shuffled so each type always becomes the same other type
#     """
#     display_name = "Shuffled Sidearms"



mina_the_hollower_option_groups= [
    OptionGroup("AP Options", [
        Goal,
        RandomizeEntrances,
        AbilityRando,
        DeathLink,
    ]),
]

@dataclass
class MinaTheHollowerOptions(PerGameCommonOptions):
    goal: Goal
    entrance_rando: RandomizeEntrances
    ability_rando: AbilityRando
    death_link: DeathLink
    # shuffled_sidearms: ShuffledSidearms
    # shuffle_enemy_level: ShuffleEnemyLevel
    # shuffled_items: ShuffledItems


