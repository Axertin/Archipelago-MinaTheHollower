from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, HasVialsCount, CanClimb

collectable_locations: dict[str, LocationData] = {
    "SO Commons Ossex Entry Left Chest" : LocationData(270, "Southern Outskirts Commons Ossex Entry", CanBurrow() & (CanJumpTiles(distance=6) | CanBounce()) ),
    "SO Commons Ossex Entry Right Chest" : LocationData(266, "Southern Outskirts Commons Ossex Entry", Has("Ossex High Street SE Garden Kear")),
    "SO Commons Chest" : LocationData(264, "Southern Outskirts Commons Main", CanBurrow() & CanBounce()),
    "SO Commons Crumblefin Head" : LocationData(274, "Southern Outskirts Commons Cliff", Has("FishingRod")),
    "SO Cave Network Chest" : LocationData(265, "Southern Outskirts Cave Network Deep"),
    "SO Cave Network Side Room Chest" : LocationData(268, "Southern Outskirts Cave Network Deep"),
    "SO Poppit Keri" : LocationData(272, "Southern Outskirts Poppit"),
    "SO Poppit Kear" : LocationData(273, "Southern Outskirts Poppit"),
    "SO Southern Pit Room Bonestone" : LocationData(261, "Southern Outskirts Commons Southern Pit Room", CanJumpTiles(distance=5)),
    "SO Western Pit Room Chest" : LocationData(267, "Southern Outskirts Commons Western Pit Room Main"),
    "SO Residence Primed Vial Pouch" : LocationData(269, "Southern Outskirts Residence Basement"),
    "SO Mining Passage Chest" : LocationData(331, "Southern Outskirts Mining Passage Secret"),
    "SO Moonbath Lace Glove" : LocationData(263, "Southern Outskirts Moonbath"),
    "SO Four Flowers Chest" : LocationData(271, "Southern Outskirts Four Flowers", CanBounce()),
}

bosses: dict[str, LocationData] = {
}

regions: set[str] = {
    "Southern Outskirts Commons Ossex Entry",
    "Southern Outskirts Commons Main",
    "Southern Outskirts Commons Upper",
    "Southern Outskirts Commons Burned",
    "Southern Outskirts Commons Cliff",
    "Southern Outskirts Commons Cave Entrance",
    "Southern Outskirts Commons Rooftop",
    "Southern Outskirts Commons Rebel",
    "Southern Outskirts Commons Residence Roof",
    "Southern Outskirts Rebel Barracks",
    "Southern Outskirts Rebel Barracks West",
    "Southern Outskirts Rebel Barracks Gauntlet",
    "Southern Outskirts Rebel Barracks Prison",
    "Southern Outskirts Rebel Barracks Companion Start",
    "Southern Outskirts Rebel Barracks Companion End",
    "Southern Outskirts Rebel Barracks Fight",
    "Southern Outskirts Commons East Ossex",
    "Southern Outskirts Commons West Ossex",
    "Southern Outskirts Moonbath",
    "Southern Outskirts Residence Main",
    "Southern Outskirts Residence Top",
    "Southern Outskirts Residence Basement",
    "Southern Outskirts Commons Southern Pit Room Main",
    "Southern Outskirts Commons Southern Pit Room Roof",
    "Southern Outskirts Commons Western Pit Room Main",
    "Southern Outskirts Commons Western Pit Room Pit",
    "Southern Outskirts Cave Network Main",
    "Southern Outskirts Cave Network Deep",
    "Southern Outskirts Cave Network Deep Exit",
    "Southern Outskirts Cave Network End",
    "Southern Outskirts Cave Network Mining Passage Entrance",
    "Southern Outskirts Cave Network Deep Entrance",
    "Southern Outskirts Cave Network Deep Arena",
    "Southern Outskirts Cave Network Deep Exit Region",
    "Southern Outskirts Poppit",
    "Southern Outskirts Mining Passage Entrance Entrance",
    "Southern Outskirts Mining Passage Entrance Main",
    "Southern Outskirts Mining Passage Entrance Exit",
    "Southern Outskirts Mining Passage Fence",
    "Southern Outskirts Mining Passage Empty",
    "Southern Outskirts Mining Passage Exit",
    "Southern Outskirts Mining Passage Secret",
    "Southern Outskirts Four Flowers Sandfall",
    "Southern Outskirts Four Flowers Shortcut",
}

connections: dict[str, RegionConnection] = {
    # --- Southern Outskirts Commons Main sub-regions ---
    "Southern Outskirts Commons Main_Cave Entrance": RegionConnection("Southern Outskirts Commons Main",
                                                                      "Southern Outskirts Commons Cave Entrance",
                                                                      CanBounce()),
    "Southern Outskirts Commons Main_Burned": RegionConnection("Southern Outskirts Commons Main",
                                                               "Southern Outskirts Commons Burned",
                                                               CanJumpTiles(distance=4)),  # "4 tiles of air movement"
    "Southern Outskirts Commons Main_Cliff": RegionConnection("Southern Outskirts Commons Main",
                                                              "Southern Outskirts Commons Cliff",
                                                              CanBurrow() & CanBounce() & CanClimb()),
    "Southern Outskirts Commons Main_Rooftop": RegionConnection("Southern Outskirts Commons Main",
                                                                "Southern Outskirts Commons Rooftop",
                                                                Has("Southern Outskirts Rooftop Kear")),

    # --- Southern Outskirts Commons Cave Entrance ---
    "Southern Outskirts Commons Cave Entrance_Main": RegionConnection("Southern Outskirts Commons Cave Entrance",
                                                                      "Southern Outskirts Commons Main", CanBounce()),

    # --- Southern Outskirts Commons Upper ---
    "Southern Outskirts Commons Upper_Burned": RegionConnection("Southern Outskirts Commons Upper",
                                                                "Southern Outskirts Commons Burned"),

    # --- Southern Outskirts Commons Burned ---
    "Southern Outskirts Commons Burned_Main": RegionConnection("Southern Outskirts Commons Burned",
                                                               "Southern Outskirts Commons Main"),
    "Southern Outskirts Commons Burned_Cliff": RegionConnection("Southern Outskirts Commons Burned",
                                                                "Southern Outskirts Commons Cliff",
                                                                CanBurrow() & CanBounce()),

    # --- Southern Outskirts Commons Cliff ---
    "Southern Outskirts Commons Cliff_Main": RegionConnection("Southern Outskirts Commons Cliff",
                                                              "Southern Outskirts Commons Main", CanClimb()),

    # --- Southern Outskirts Commons Rooftop ---
    "Southern Outskirts Commons Rooftop_Main": RegionConnection("Southern Outskirts Commons Rooftop",
                                                                "Southern Outskirts Commons Main", CanBurrow()),

    # --- Southern Outskirts Commons Rebel ---
    "Southern Outskirts Commons Rebel_Rooftop": RegionConnection("Southern Outskirts Commons Rebel",
                                                                 "Southern Outskirts Commons Rooftop", CanClimb()),

    # --- Southern Outskirts Rebel Barracks Companion Start <-> End ---
    "Southern Outskirts Rebel Barracks Companion Start_End": RegionConnection(
        "Southern Outskirts Rebel Barracks Companion Start", "Southern Outskirts Rebel Barracks Companion End",
        CanBurrow()),
    "Southern Outskirts Rebel Barracks Companion End_Start": RegionConnection(
        "Southern Outskirts Rebel Barracks Companion End", "Southern Outskirts Rebel Barracks Companion Start",
        CanBurrow()),

    # --- Southern Outskirts Residence Main <-> Top ---
    "Southern Outskirts Residence Top_Main": RegionConnection("Southern Outskirts Residence Top",
                                                              "Southern Outskirts Residence Main"),

    # --- Southern Outskirts Commons Western Pit Room Main <-> Pit ---
    # "Jump 4 tiles OR Burrow" to get from Main into Pit
    "Southern Outskirts Commons Western Pit Room Main_Pit": RegionConnection(
        "Southern Outskirts Commons Western Pit Room Main", "Southern Outskirts Commons Western Pit Room Pit",
        CanJumpTiles(distance=4) | CanBurrow()),  # "Jump 4 tiles OR Burrow" - used | for OR
    "Southern Outskirts Commons Western Pit Room Pit_Main": RegionConnection(
        "Southern Outskirts Commons Western Pit Room Pit", "Southern Outskirts Commons Western Pit Room Main",
        CanJumpTiles(distance=4)),  # "Jump 4 tiles" to get back up

    # --- Southern Outskirts Cave Network Main <-> End ---
    "Southern Outskirts Cave Network Main_End": RegionConnection("Southern Outskirts Cave Network Main",
                                                                 "Southern Outskirts Cave Network End", CanBounce()),
    "Southern Outskirts Cave Network End_Main": RegionConnection("Southern Outskirts Cave Network End",
                                                                 "Southern Outskirts Cave Network Main"),

    # --- Southern Outskirts Cave Network Main <-> Deep ---
    "Southern Outskirts Cave Network Main_Deep": RegionConnection("Southern Outskirts Cave Network Main",
                                                                  "Southern Outskirts Cave Network Deep",
                                                                  Has("Southern Outskirts Cave Network Kear") & CanBounce() & CanBurrow()),
    "Southern Outskirts Cave Network Deep_Main": RegionConnection("Southern Outskirts Cave Network Deep",
                                                                  "Southern Outskirts Cave Network Main",
                                                                  Has("Southern Outskirts Cave Network Kear") & CanBounce()),

    # --- Southern Outskirts Cave Network Deep Exit ---
    "Southern Outskirts Cave Network Deep Exit_Main": RegionConnection("Southern Outskirts Cave Network Deep Exit",
                                                                       "Southern Outskirts Cave Network Main",
                                                                       Has("Southern Outskirts Cave Network Kear") & CanBounce()),

    # --- Southern Outskirts Cave Network Deep Arena ---
    "Southern Outskirts Cave Network Deep Entrance_Arena": RegionConnection(
        "Southern Outskirts Cave Network Deep Entrance", "Southern Outskirts Cave Network Deep Arena",
        CanBurrow() & CanBounce()),
    "Southern Outskirts Cave Network Deep Arena_Exit": RegionConnection("Southern Outskirts Cave Network Deep Arena",
                                                                        "Southern Outskirts Cave Network Deep Exit Region",
                                                                        CanBurrow() & CanBounce()),

    # --- Southern Outskirts Mining Passage Entrance sub-regions ---
    "Southern Outskirts Mining Passage Entrance Entrance_Main": RegionConnection(
        "Southern Outskirts Mining Passage Entrance Entrance", "Southern Outskirts Mining Passage Entrance Main",
        HasVialsCount(count=2)),  # "2 Vials"
    "Southern Outskirts Mining Passage Entrance Main_Entrance": RegionConnection(
        "Southern Outskirts Mining Passage Entrance Main", "Southern Outskirts Mining Passage Entrance Entrance"),
    "Southern Outskirts Mining Passage Entrance Main_Exit": RegionConnection(
        "Southern Outskirts Mining Passage Entrance Main", "Southern Outskirts Mining Passage Entrance Exit"),
    # no rule listed for Main->Exit
    "Southern Outskirts Mining Passage Entrance Exit_Main": RegionConnection(
        "Southern Outskirts Mining Passage Entrance Exit", "Southern Outskirts Mining Passage Entrance Main"),
    # no rule listed

    # --- Southern Outskirts Four Flowers Sandfall <-> Shortcut ---
    "Southern Outskirts Four Flowers Sandfall_Shortcut": RegionConnection("Southern Outskirts Four Flowers Sandfall",
                                                                          "Southern Outskirts Four Flowers Shortcut",
                                                                          CanBounce()),
    "Southern Outskirts Four Flowers Shortcut_Sandfall": RegionConnection("Southern Outskirts Four Flowers Shortcut",
                                                                          "Southern Outskirts Four Flowers Sandfall",
                                                                          CanBounce()),
    # "Sandfall Bounce" listed under Shortcut - guessed bidirectional Bounce requirement
}



transitions: dict[str, Transition] = {
    # --- Southern Outskirts Commons Ossex Entry ---
    "Southern Outskirts Commons Ossex Entry Area South": Transition("Southern Outskirts Commons Ossex Entry Area South",
                                                                    "Southern Outskirts Commons Ossex Entry",
                                                                    "Ossex City Center Main", DirectionType.NORTH,
                                                                    TransitionType.AREA_SCREENS),
    "Southern Outskirts Commons Ossex Entry South Commons": Transition(
        "Southern Outskirts Commons Ossex Entry South Commons", "Southern Outskirts Commons Ossex Entry",
        "Southern Outskirts Commons Main", DirectionType.SOUTH, TransitionType.SCREENS),
    "Southern Outskirts Commons Ossex Entry East": Transition("Southern Outskirts Commons Ossex Entry East",
                                                              "Southern Outskirts Commons Ossex Entry",
                                                              "Southern Outskirts Commons East Ossex",
                                                              DirectionType.EAST, TransitionType.SCREENS),
    "Southern Outskirts Commons Ossex Entry West": Transition("Southern Outskirts Commons Ossex Entry West",
                                                              "Southern Outskirts Commons Ossex Entry",
                                                              "Southern Outskirts Commons West Ossex",
                                                              DirectionType.WEST, TransitionType.SCREENS),

    # --- Southern Outskirts Commons Main ---
    "Southern Outskirts Commons Main North Ossex Entry": Transition("Southern Outskirts Commons Main North Ossex Entry",
                                                                    "Southern Outskirts Commons Main",
                                                                    "Southern Outskirts Commons Ossex Entry",
                                                                    DirectionType.NORTH, TransitionType.SCREENS),
    "Southern Outskirts Commons Main Door North Residence": Transition(
        "Southern Outskirts Commons Main Door North Residence", "Southern Outskirts Commons Main",
        "Southern Outskirts Residence Main", DirectionType.NORTH, TransitionType.DOORS),
    "Southern Outskirts Commons Main Area North Loners": Transition("Southern Outskirts Commons Main Area North Loners",
                                                                    "Southern Outskirts Commons Main",
                                                                    "Loners Landing ???", DirectionType.NORTH,
                                                                    TransitionType.AREA_SCREENS),
    # target is "Loners Landing ???"; left as-is, fill in when known
    "Southern Outskirts Commons Main East Pit Room": Transition("Southern Outskirts Commons Main East Pit Room",
                                                                "Southern Outskirts Commons Main",
                                                                "Southern Outskirts Commons Southern Pit Room Main",
                                                                DirectionType.EAST, TransitionType.SCREENS),

    # --- Southern Outskirts Commons Cave Entrance ---
    "Southern Outskirts Commons Cave Entrance Stair North Cave": Transition(
        "Southern Outskirts Commons Cave Entrance Stair North Cave", "Southern Outskirts Commons Cave Entrance",
        "Southern Outskirts Cave Network Main", DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Commons Upper ---
    "Southern Outskirts Commons Upper NR East Ossex": Transition("Southern Outskirts Commons Upper NR East Ossex",
                                                                 "Southern Outskirts Commons Upper",
                                                                 "Southern Outskirts Commons East Ossex",
                                                                 DirectionType.EAST,
                                                                 TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBounce()),

    "Southern Outskirts Commons Upper Stair North Cave Network": Transition(
        "Southern Outskirts Commons Upper Stair North Cave Network", "Southern Outskirts Commons Upper",
        "Southern Outskirts Cave Network Mining Passage Entrance", DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Commons Cliff ---
    "Southern Outskirts Commons Cliff Burrow South Poppit": Transition(
        "Southern Outskirts Commons Cliff Burrow South Poppit", "Southern Outskirts Commons Cliff",
        "Southern Outskirts Poppit", DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),

    "Southern Outskirts Commons Cliff Stairs North Residence": Transition(
        "Southern Outskirts Commons Cliff Stairs North Residence", "Southern Outskirts Commons Cliff",
        "Southern Outskirts Residence Main", DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Commons Rooftop ---
    "Southern Outskirts Commons Rooftop Door North Rebel Barracks": Transition(
        "Southern Outskirts Commons Rooftop Door North Rebel Barracks", "Southern Outskirts Commons Rooftop",
        "Southern Outskirts Rebel Barracks", DirectionType.NORTH, TransitionType.DOORS, HasVialsCount(count=1)),

    # --- Southern Outskirts Commons Residence Roof ---
    "Southern Outskirts Commons Residence Roof Geyser Drop Residence Top": Transition(
        "Southern Outskirts Commons Residence Roof Geyser Drop Residence Top",
        "Southern Outskirts Commons Residence Roof", "Southern Outskirts Residence Top", DirectionType.OVERWORLD,
        TransitionType.GEYSER_DOWN, CanBurrow()),

    # --- Southern Outskirts Rebel Barracks ---
    "Southern Outskirts Rebel Barracks Door South Rooftop": Transition(
        "Southern Outskirts Rebel Barracks Door South Rooftop", "Southern Outskirts Rebel Barracks",
        "Southern Outskirts Commons Rooftop", DirectionType.SOUTH, TransitionType.DOORS, HasVialsCount(count=1)),
    "Southern Outskirts Rebel Barracks West": Transition("Southern Outskirts Rebel Barracks West",
                                                         "Southern Outskirts Rebel Barracks",
                                                         "Southern Outskirts Rebel Barracks West", DirectionType.WEST,
                                                         TransitionType.SCREENS),
    "Southern Outskirts Rebel Barracks North Gauntlet": Transition("Southern Outskirts Rebel Barracks North Gauntlet",
                                                                   "Southern Outskirts Rebel Barracks",
                                                                   "Southern Outskirts Rebel Barracks Gauntlet",
                                                                   DirectionType.NORTH, TransitionType.SCREENS),

    # --- Southern Outskirts Rebel Barracks West ---
    "Southern Outskirts Rebel Barracks West East": Transition("Southern Outskirts Rebel Barracks West East",
                                                              "Southern Outskirts Rebel Barracks West",
                                                              "Southern Outskirts Rebel Barracks", DirectionType.EAST,
                                                              TransitionType.SCREENS),
    # --- Southern Outskirts Rebel Barracks Gauntlet ---
    "Southern Outskirts Rebel Barracks Gauntlet South Barracks": Transition(
        "Southern Outskirts Rebel Barracks Gauntlet South Barracks", "Southern Outskirts Rebel Barracks Gauntlet",
        "Southern Outskirts Rebel Barracks", DirectionType.SOUTH, TransitionType.SCREENS),
    "Southern Outskirts Rebel Barracks Gauntlet South Prison": Transition(
        "Southern Outskirts Rebel Barracks Gauntlet South Prison", "Southern Outskirts Rebel Barracks Gauntlet",
        "Southern Outskirts Rebel Barracks Prison", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Southern Outskirts Rebel Barracks Prison ---
    "Southern Outskirts Rebel Barracks Prison Stair North Companion Start": Transition(
        "Southern Outskirts Rebel Barracks Prison Stair North Companion Start",
        "Southern Outskirts Rebel Barracks Prison", "Southern Outskirts Rebel Barracks Companion Start",
        DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Rebel Barracks Companion Start ---
    "Southern Outskirts Rebel Barracks Companion Start Stair North Prison": Transition(
        "Southern Outskirts Rebel Barracks Companion Start Stair North Prison",
        "Southern Outskirts Rebel Barracks Companion Start", "Southern Outskirts Rebel Barracks Prison",
        DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Rebel Barracks Companion End ---
    "Southern Outskirts Rebel Barracks Companion End Stair North Fight": Transition(
        "Southern Outskirts Rebel Barracks Companion End Stair North Fight",
        "Southern Outskirts Rebel Barracks Companion End", "Southern Outskirts Rebel Barracks Fight",
        DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Rebel Barracks Fight ---
    "Southern Outskirts Rebel Barracks Fight Stair North Companion End": Transition(
        "Southern Outskirts Rebel Barracks Fight Stair North Companion End", "Southern Outskirts Rebel Barracks Fight",
        "Southern Outskirts Rebel Barracks Companion End", DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Commons East Ossex ---
    "Southern Outskirts Commons East Ossex West Ossex Entry": Transition(
        "Southern Outskirts Commons East Ossex West Ossex Entry", "Southern Outskirts Commons East Ossex",
        "Southern Outskirts Commons Ossex Entry", DirectionType.WEST, TransitionType.SCREENS),
    "Southern Outskirts Commons East Ossex East Moonbath": Transition(
        "Southern Outskirts Commons East Ossex East Moonbath", "Southern Outskirts Commons East Ossex",
        "Southern Outskirts Moonbath", DirectionType.EAST, TransitionType.SCREENS),
    "Southern Outskirts Commons East Ossex NR Upper": Transition("Southern Outskirts Commons East Ossex NR Upper",
                                                                 "Southern Outskirts Commons East Ossex",
                                                                 "Southern Outskirts Commons Upper",
                                                                 DirectionType.NORTH,
                                                                 TransitionType.DO_NOT_RANDOMIZE_ENTRANCE, CanBounce()),

    # --- Southern Outskirts Commons West Ossex ---
    "Southern Outskirts Commons West Ossex East Ossex Entry": Transition(
        "Southern Outskirts Commons West Ossex East Ossex Entry", "Southern Outskirts Commons West Ossex",
        "Southern Outskirts Commons Ossex Entry", DirectionType.EAST, TransitionType.SCREENS),
    "Southern Outskirts Commons West Ossex West Pit Room": Transition(
        "Southern Outskirts Commons West Ossex West Pit Room", "Southern Outskirts Commons West Ossex",
        "Southern Outskirts Commons Western Pit Room Main", DirectionType.WEST, TransitionType.SCREENS),

    # --- Southern Outskirts Moonbath ---
    "Southern Outskirts Moonbath West East Ossex": Transition("Southern Outskirts Moonbath West East Ossex",
                                                              "Southern Outskirts Moonbath",
                                                              "Southern Outskirts Commons East Ossex",
                                                              DirectionType.WEST, TransitionType.SCREENS),
    "Southern Outskirts Moonbath Area North Eastern Hearth": Transition(
        "Southern Outskirts Moonbath Area North Eastern Hearth", "Southern Outskirts Moonbath",
        "Eastern Hearth Bush Room", DirectionType.NORTH, TransitionType.AREA_SCREENS),

    # --- Southern Outskirts Residence Main ---
    "Southern Outskirts Residence Main Door South Commons": Transition(
        "Southern Outskirts Residence Main Door South Commons", "Southern Outskirts Residence Main",
        "Southern Outskirts Commons Main", DirectionType.SOUTH, TransitionType.DOORS),

    # --- Southern Outskirts Residence Top ---
    "Southern Outskirts Residence Top Stairs North Basement": Transition(
        "Southern Outskirts Residence Top Stairs North Basement", "Southern Outskirts Residence Top",
        "Southern Outskirts Residence Basement", DirectionType.NORTH, TransitionType.STAIRS),
    # sheet says "Resudence" - typo, treated normally

    # --- Southern Outskirts Residence Basement ---
    "Southern Outskirts Residence Basement Stairs North Top": Transition(
        "Southern Outskirts Residence Basement Stairs North Top", "Southern Outskirts Residence Basement",
        "Southern Outskirts Residence Top", DirectionType.NORTH, TransitionType.STAIRS),
    # sheet says "Resudence" - typo, treated normally
    "Southern Outskirts Residence Basement Burrow South Commons": Transition(
        "Southern Outskirts Residence Basement Burrow South Commons", "Southern Outskirts Residence Basement",
        "Southern Outskirts Commons Main", DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),
    # noqa: custom type BURROW

    # --- Southern Outskirts Commons Southern Pit Room Main ---
    "Southern Outskirts Commons Southern Pit Room Main East Commons": Transition(
        "Southern Outskirts Commons Southern Pit Room Main East Commons",
        "Southern Outskirts Commons Southern Pit Room Main", "Southern Outskirts Commons Main", DirectionType.EAST,
        TransitionType.SCREENS),
    "Southern Outskirts Commons Southern Pit Room Main North West Pit": Transition(
        "Southern Outskirts Commons Southern Pit Room Main North West Pit",
        "Southern Outskirts Commons Southern Pit Room Main", "Southern Outskirts Commons Western Pit Room Main",
        DirectionType.NORTH, TransitionType.SCREENS),

    # --- Southern Outskirts Commons Southern Pit Room Roof ---
    "Southern Outskirts Commons Southern Pit Room Roof North West Pit Pit": Transition(
        "Southern Outskirts Commons Southern Pit Room Roof North West Pit Pit",
        "Southern Outskirts Commons Southern Pit Room Roof", "Southern Outskirts Commons Western Pit Room Pit",
        DirectionType.NORTH, TransitionType.SCREENS),
    "Southern Outskirts Commons Southern Pit Room Roof East Residence Roof": Transition(
        "Southern Outskirts Commons Southern Pit Room Roof East Residence Roof",
        "Southern Outskirts Commons Southern Pit Room Roof", "Southern Outskirts Commons Residence Roof",
        DirectionType.EAST, TransitionType.SCREENS),

    # --- Southern Outskirts Commons Western Pit Room Main ---
    "Southern Outskirts Commons Western Pit Room Main South Pit Room": Transition(
        "Southern Outskirts Commons Western Pit Room Main South Pit Room",
        "Southern Outskirts Commons Western Pit Room Main", "Southern Outskirts Commons Southern Pit Room Main",
        DirectionType.SOUTH, TransitionType.SCREENS),
    "Southern Outskirts Commons Western Pit Room Main Area North": Transition(
        "Southern Outskirts Commons Western Pit Room Main Area North",
        "Southern Outskirts Commons Western Pit Room Main", "Western Wilds Overgrown Path", DirectionType.NORTH,
        TransitionType.AREA_SCREENS),

    # --- Southern Outskirts Commons Western Pit Room Pit ---
    "Southern Outskirts Commons Western Pit Room Pit East West Ossex": Transition(
        "Southern Outskirts Commons Western Pit Room Pit East West Ossex",
        "Southern Outskirts Commons Western Pit Room Pit", "Southern Outskirts Commons West Ossex", DirectionType.EAST,
        TransitionType.SCREENS),

    # --- Southern Outskirts Cave Network Main ---
    "Southern Outskirts Cave Network Main Stair North Commons Cave Entrance": Transition(
        "Southern Outskirts Cave Network Main Stair North Commons Cave Entrance",
        "Southern Outskirts Cave Network Main", "Southern Outskirts Commons Cave Entrance", DirectionType.NORTH,
        TransitionType.STAIRS),

    # --- Southern Outskirts Cave Network Deep ---
    "Southern Outskirts Cave Network Deep West Deep Entrance": Transition(
        "Southern Outskirts Cave Network Deep West Deep Entrance", "Southern Outskirts Cave Network Deep",
        "Southern Outskirts Cave Network Deep Entrance", DirectionType.WEST, TransitionType.SCREENS),
    # sheet says "[transition] West - Southern Outskirts Cave Network Deep" which looks self-referential; guessed it connects to the Deep Entrance sub-room # noqa: possible self-ref, check this

    # --- Southern Outskirts Cave Network Deep Exit ---
    "Southern Outskirts Cave Network Deep Exit South Deep Exit Region": Transition(
        "Southern Outskirts Cave Network Deep Exit South Deep Exit Region", "Southern Outskirts Cave Network Deep Exit",
        "Southern Outskirts Cave Network Deep Exit Region", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Southern Outskirts Cave Network End ---
    "Southern Outskirts Cave Network End Stair North Commons Upper": Transition(
        "Southern Outskirts Cave Network End Stair North Commons Upper", "Southern Outskirts Cave Network End",
        "Southern Outskirts Commons Upper", DirectionType.NORTH, TransitionType.STAIRS),

    # --- Southern Outskirts Cave Network Mining Passage Entrance ---
    "Southern Outskirts Cave Network Mining Passage Entrance Stair North Commons Upper": Transition(
        "Southern Outskirts Cave Network Mining Passage Entrance Stair North Commons Upper",
        "Southern Outskirts Cave Network Mining Passage Entrance", "Southern Outskirts Commons Upper",
        DirectionType.NORTH, TransitionType.STAIRS),
    "Southern Outskirts Cave Network Mining Passage Entrance South Mining Entrance": Transition(
        "Southern Outskirts Cave Network Mining Passage Entrance South Mining Entrance",
        "Southern Outskirts Cave Network Mining Passage Entrance",
        "Southern Outskirts Mining Passage Entrance Entrance", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Southern Outskirts Cave Network Deep Entrance ---
    "Southern Outskirts Cave Network Deep Entrance East Cave Network Deep": Transition(
        "Southern Outskirts Cave Network Deep Entrance East Cave Network Deep",
        "Southern Outskirts Cave Network Deep Entrance", "Southern Outskirts Cave Network Deep", DirectionType.EAST,
        TransitionType.SCREENS),

    # --- Southern Outskirts Cave Network Deep Exit Region ---
    "Southern Outskirts Cave Network Deep Exit Region East Cave Network Deep Exit": Transition(
        "Southern Outskirts Cave Network Deep Exit Region East Cave Network Deep Exit",
        "Southern Outskirts Cave Network Deep Exit Region", "Southern Outskirts Cave Network Deep Exit",
        DirectionType.EAST, TransitionType.SCREENS),

    # --- Southern Outskirts Poppit ---
    "Southern Outskirts Poppit Burrow South Commons Cliff": Transition(
        "Southern Outskirts Poppit Burrow South Commons Cliff", "Southern Outskirts Poppit",
        "Southern Outskirts Commons Cliff", DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),
    # noqa: custom type BURROW

    # --- Southern Outskirts Mining Passage Entrance Exit ---
    "Southern Outskirts Mining Passage Entrance Exit East Fence": Transition(
        "Southern Outskirts Mining Passage Entrance Exit East Fence", "Southern Outskirts Mining Passage Entrance Exit",
        "Southern Outskirts Mining Passage Fence", DirectionType.EAST, TransitionType.SCREENS),

    # --- Southern Outskirts Mining Passage Fence ---
    "Southern Outskirts Mining Passage Fence West Entrance Exit": Transition(
        "Southern Outskirts Mining Passage Fence West Entrance Exit", "Southern Outskirts Mining Passage Fence",
        "Southern Outskirts Mining Passage Entrance Exit", DirectionType.WEST, TransitionType.SCREENS),
    "Southern Outskirts Mining Passage Fence East Empty": Transition(
        "Southern Outskirts Mining Passage Fence East Empty", "Southern Outskirts Mining Passage Fence",
        "Southern Outskirts Mining Passage Empty", DirectionType.EAST, TransitionType.SCREENS, CanBurrow()),

    # --- Southern Outskirts Mining Passage Empty ---
    "Southern Outskirts Mining Passage Empty West Fence": Transition(
        "Southern Outskirts Mining Passage Empty West Fence", "Southern Outskirts Mining Passage Empty",
        "Southern Outskirts Mining Passage Fence", DirectionType.WEST, TransitionType.SCREENS),
    "Southern Outskirts Mining Passage Empty North Exit": Transition(
        "Southern Outskirts Mining Passage Empty North Exit", "Southern Outskirts Mining Passage Empty",
        "Southern Outskirts Mining Passage Exit", DirectionType.NORTH, TransitionType.SCREENS),

    # --- Southern Outskirts Mining Passage Exit ---
    "Southern Outskirts Mining Passage Exit South Empty": Transition(
        "Southern Outskirts Mining Passage Exit South Empty", "Southern Outskirts Mining Passage Exit",
        "Southern Outskirts Mining Passage Empty", DirectionType.SOUTH, TransitionType.SCREENS),
    "Southern Outskirts Mining Passage Exit Stair North Sandfalls": Transition(
        "Southern Outskirts Mining Passage Exit Stair North Sandfalls", "Southern Outskirts Mining Passage Exit",
        "Sandfalls Mining Passage Entrance", DirectionType.NORTH, TransitionType.STAIRS),

    "Southern Outskirts Mining Passage Exit South Empty": Transition(
        "Southern Outskirts Mining Passage Exit South Empty", "Southern Outskirts Mining Passage Exit",
        "Southern Outskirts Mining Passage Empty", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Southern Outskirts Mining Passage Secret ---
    "Southern Outskirts Mining Passage Secret East Exit": Transition(
        "Southern Outskirts Mining Passage Secret East Exit", "Southern Outskirts Mining Passage Secret",
        "Southern Outskirts Mining Passage Exit", DirectionType.EAST, TransitionType.BURROW),

    # --- Southern Outskirts Four Flowers Sandfall ---
    "Southern Outskirts Four Flowers Sandfall Area East Sandfalls": Transition(
        "Southern Outskirts Four Flowers Sandfall Area East Sandfalls", "Southern Outskirts Four Flowers Sandfall",
        "Sandfalls Mining Passage Entrance", DirectionType.EAST, TransitionType.AREA_SCREENS),

    # --- Southern Outskirts Four Flowers Shortcut ---
    "Southern Outskirts Four Flowers Shortcut NR Commons Upper": Transition(
        "Southern Outskirts Four Flowers Shortcut NR Commons Upper", "Southern Outskirts Four Flowers Shortcut",
        "Southern Outskirts Commons Upper", DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),

    "Southern Outskirts Four Flowers Shortcut NR Commons West Ossex": Transition(
        "Southern Outskirts Four Flowers Shortcut NR Commons West Ossex", "Southern Outskirts Four Flowers Shortcut",
        "Southern Outskirts Commons West Ossex", DirectionType.OVERWORLD, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
}
