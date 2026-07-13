from rule_builder.rules import Has
from .data.rules.state_rules import RepairedGeneratorCount
from .data.rules.ability_rules import PowerLevelThreshold


def set_goal(world):
    if world.options.goal.value == world.options.goal.option_radientManorGenerator:
        world.set_completion_rule(Has("Victory") & PowerLevelThreshold(power=60))
    if world.options.goal.value == world.options.goal.option_fixGenerators:
        world.set_completion_rule(RepairedGeneratorCount(count=world.options.goal_generators.value))