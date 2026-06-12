from BaseClasses import LocationProgressType
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, CanReachLocation
from ... import RegionConnection, Transition, LocationData, TransitionType, DirectionType
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanJumpTiles, CanBounce, ReachingSideArm, CanClimb, \
    CanSwim
from ...rules.state_rules import HasCompletedOneSparkGenerator

bosses: dict[str, LocationData] = {
}
regions: set[str] = {
    "Ossex High Street Main",
    "Eastern Hearth Grassland",
    "Eastern Hearth Grassland Bridge Left",
    "Eastern Hearth Grassland Bridge Right",
    "Eastern Hearth Grassland Bridge River",
    "Eastern Hearth Grassland Bridge Waterfall",
    "Eastern Hearth Horizontal Spinner Room",
    "Eastern Hearth Grassland Waterfall Bottom",
    "Eastern Hearth Grassland Waterfall First Level",
    "Eastern Hearth Grassland Waterfall Second Level",
    "Eastern Hearth Grassland Waterfall Mountain",
    "Eastern Hearth Bush Room",
    "Eastern Hearth Grassland Riverbed Top",
    "Eastern Hearth Grassland Riverbed Dive",
    "Eastern Hearth Grassland Riverbed Bottom",
    "Eastern Hearth Grotto Right",
    "Eastern Hearth Grotto Left",
    "Eastern Hearth Choppe Shoppe",
    "Eastern Hearth Choppe Shoppe Entry",
    "Eastern Hearth Hidden Cave",
    "Eastern Hearth Grassland Pit",
    "Eastern Hearth Poppet Entry",
    "Eastern Hearth Under The Bridge",
    "Eastern Hearth Under Bridge South",
    "Eastern Hearth Under Bridge East",
    "Eastern Hearth Under Bridge West",
    "Eastern Hearth East Corner",
    "Eastern Hearth Mourners Gate",
    "Eastern Hearth Bucklers Bluff Start",
    "Eastern Hearth Bucklers Bluff Cliff",
    "Eastern Hearth Bucklers Bluff Bucklers",
    "Eastern Hearth Grassland Poppit Cave",
    "Eastern Hearth Poppit",
    "Eastern Hearth Frozen Pass",
}

transitions: dict[str, Transition] = {
    # --- Eastern Hearth Grassland ---
    "Eastern Hearth Grassland North":
        Transition("Eastern Hearth Grassland","Eastern Hearth Choppe Shoppe Entry", DirectionType.NORTH, TransitionType.SCREENS),
    "Eastern Hearth Grassland East":
        Transition("Eastern Hearth Grassland","Eastern Hearth Grassland Bridge Left", DirectionType.EAST, TransitionType.SCREENS),
    "Eastern Hearth Grassland Area West":
        Transition("Eastern Hearth Grassland", "Ossex High Street Main", DirectionType.WEST, TransitionType.AREA_SCREENS),
    "Eastern Hearth Grassland South NR":
        Transition( "Eastern Hearth Grassland","Eastern Hearth Horizontal Spinner Room", DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),

    # --- Eastern Hearth Grassland Bridge Left ---
    "Eastern Hearth Grassland Bridge Left North Waterfall":
        Transition("Eastern Hearth Grassland Bridge Left","Eastern Hearth Grassland Bridge Waterfall", DirectionType.NORTH, TransitionType.SCREENS),

    "Eastern Hearth Grassland Bridge Left West":
        Transition( "Eastern Hearth Grassland Bridge Left","Eastern Hearth Grassland", DirectionType.WEST, TransitionType.SCREENS),
    "Eastern Hearth Grassland Bridge Left South Riverbed":
        Transition("Eastern Hearth Grassland Bridge Left", "Eastern Hearth Grassland Riverbed Top", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Eastern Hearth Grassland Bridge Right ---
    "Eastern Hearth Grassland Bridge Right East Corner":
        Transition("Eastern Hearth Grassland Bridge Right","Eastern Hearth East Corner", DirectionType.EAST,TransitionType.SCREENS),

    # --- Eastern Hearth Grassland Bridge River ---
    "Eastern Hearth Grassland Bridge River South Under Bridge":
        Transition("Eastern Hearth Grassland Bridge River","Eastern Hearth Under The Bridge", DirectionType.SOUTH, TransitionType.SCREENS, CanSwim()),

    # --- Eastern Hearth Grassland Bridge Waterfall ---
    "Eastern Hearth Grassland Bridge Waterfall North Under Bridge":
        Transition("Eastern Hearth Grassland Bridge Waterfall","Eastern Hearth Under The Bridge", DirectionType.NORTH, TransitionType.SCREENS),

    # --- Eastern Hearth Horizontal Spinner Room ---
    "Eastern Hearth Horizontal Spinner Room North NR":
        Transition("Eastern Hearth Horizontal Spinner Room", "Eastern Hearth Grassland", DirectionType.NORTH,TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),

    "Eastern Hearth Horizontal Spinner Room East Riverbed Top":
        Transition("Eastern Hearth Horizontal Spinner Room","Eastern Hearth Grassland Riverbed Top", DirectionType.EAST, TransitionType.SCREENS),

    "Eastern Hearth Horizontal Spinner Room East Pit":
        Transition("Eastern Hearth Horizontal Spinner Room","Eastern Hearth Grassland Pit", DirectionType.EAST, TransitionType.SCREENS),

    "Eastern Hearth Horizontal Spinner Room South Bush":
        Transition("Eastern Hearth Horizontal Spinner Room", "Eastern Hearth Bush Room", DirectionType.SOUTH,TransitionType.SCREENS),

    # --- Eastern Hearth Grassland Waterfall Bottom ---
    "Eastern Hearth Grassland Waterfall Bottom West Choppe":
        Transition("Eastern Hearth Grassland Waterfall Bottom", "Eastern Hearth Choppe Shoppe Entry", DirectionType.WEST, TransitionType.SCREENS),
    "Eastern Hearth Grassland Waterfall Bottom South Bridge":
        Transition("Eastern Hearth Grassland Waterfall Bottom","Eastern Hearth Grassland Bridge Left", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Eastern Hearth Grassland Waterfall First Level ---
    "Eastern Hearth Grassland Waterfall First Level Door North Grotto Left":
        Transition( "Eastern Hearth Grassland Waterfall First Level", "Eastern Hearth Grotto Left", DirectionType.NORTH,TransitionType.DOORS),
    "Eastern Hearth Grassland Waterfall First Level West Choppe":
        Transition("Eastern Hearth Grassland Waterfall First Level","Eastern Hearth Choppe Shoppe Entry", DirectionType.WEST, TransitionType.SCREENS),

    # --- Eastern Hearth Grassland Waterfall Second Level ---
    "Eastern Hearth Grassland Waterfall Second Level East Bucklers":
        Transition("Eastern Hearth Grassland Waterfall Second Level", "Eastern Hearth Bucklers Bluff Bucklers", DirectionType.EAST,TransitionType.SCREENS,
                   CanJumpTiles(distance=2)),

    "Eastern Hearth Grassland Waterfall Second Level NR Bridge":
        Transition( "Eastern Hearth Grassland Waterfall Second Level","Eastern Hearth Grassland Bridge Right", DirectionType.SOUTH, TransitionType.DO_NOT_RANDOMIZE_ENTRANCE),
    "Eastern Hearth Grassland Waterfall Second Level Door North Grotto Right":
        Transition( "Eastern Hearth Grassland Waterfall Second Level", "Eastern Hearth Grotto Right", DirectionType.NORTH, TransitionType.DOORS),

    # --- Eastern Hearth Grassland Waterfall Mountain ---
    "Eastern Hearth Grassland Waterfall Mountain North Frozen Pass":
        Transition("Eastern Hearth Grassland Waterfall Mountain","Eastern Hearth Frozen Pass", DirectionType.NORTH, TransitionType.SCREENS),


    # --- Eastern Hearth Bush Room ---
    "Eastern Hearth Bush Room North Spinner":
        Transition("Eastern Hearth Bush Room", "Eastern Hearth Horizontal Spinner Room", DirectionType.NORTH, TransitionType.SCREENS),
    "Eastern Hearth Bush Room Area South":
        Transition("Eastern Hearth Bush Room", "Southern Outskirts Moonbath", DirectionType.SOUTH, TransitionType.AREA_SCREENS),
    # --- Eastern Hearth Grassland Riverbed Top ---
    "Eastern Hearth Grassland Riverbed Top West Spinner":
        Transition("Eastern Hearth Grassland Riverbed Top","Eastern Hearth Horizontal Spinner Room", DirectionType.WEST, TransitionType.SCREENS),
    "Eastern Hearth Grassland Riverbed Top North Bridge":
        Transition( "Eastern Hearth Grassland Riverbed Top","Eastern Hearth Grassland Bridge Left", DirectionType.NORTH, TransitionType.SCREENS),

    # --- Eastern Hearth Grassland Riverbed Dive ---
    "Eastern Hearth Grassland Riverbed Dive North Bridge River":
        Transition( "Eastern Hearth Grassland Riverbed Dive","Eastern Hearth Grassland Bridge River", DirectionType.NORTH, TransitionType.SCREENS, CanSwim()),
    # guessed CanSwim()
    "Eastern Hearth Grassland Riverbed Dive East Poppet":
        Transition( "Eastern Hearth Grassland Riverbed Dive","Eastern Hearth Poppet Entry", DirectionType.EAST, TransitionType.SCREENS, CanJumpTiles(distance=2)),


    # --- Eastern Hearth Grassland Riverbed Bottom ---
    "Eastern Hearth Grassland Riverbed Bottom South Pit":
        Transition( "Eastern Hearth Grassland Riverbed Bottom", "Eastern Hearth Grassland Pit", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Eastern Hearth Grotto Right ---
    "Eastern Hearth Grotto Right Door South":
        Transition( "Eastern Hearth Grotto Right","Eastern Hearth Grassland Waterfall Second Level", DirectionType.SOUTH, TransitionType.DOORS),
    "Eastern Hearth Grotto Right Burrow West Grotto Left":
        Transition("Eastern Hearth Grotto Right", "Eastern Hearth Grotto Left", DirectionType.WEST, TransitionType.BURROW,
                   CanBurrow()),

    # --- Eastern Hearth Grotto Left ---
    "Eastern Hearth Grotto Left Door South":
        Transition("Eastern Hearth Grotto Left","Eastern Hearth Grassland Waterfall First Level", DirectionType.SOUTH, TransitionType.DOORS),
    "Eastern Hearth Grotto Left Burrow East Grotto Right":
        Transition("Eastern Hearth Grotto Left","Eastern Hearth Grotto Right", DirectionType.EAST, TransitionType.BURROW,
                   CanBurrow()),

    # --- Eastern Hearth Choppe Shoppe ---
    "Eastern Hearth Choppe Shoppe Door South":
        Transition("Eastern Hearth Choppe Shoppe","Eastern Hearth Choppe Shoppe Entry", DirectionType.SOUTH,TransitionType.DOORS,
                   Has("Choppe Shoppe Kear")),

    # --- Eastern Hearth Choppe Shoppe Entry ---
    "Eastern Hearth Choppe Shoppe Entry Door North Choppe":
        Transition("Eastern Hearth Choppe Shoppe Entry", "Eastern Hearth Choppe Shoppe", DirectionType.NORTH, TransitionType.DOORS,
                   Has("Choppe Shoppe Kear")),
    "Eastern Hearth Choppe Shoppe Entry Burrow Hole Hidden Cave":
        Transition("Eastern Hearth Choppe Shoppe Entry", "Eastern Hearth Hidden Cave", DirectionType.OVERWORLD, TransitionType.GEYSER_DOWN),

    "Eastern Hearth Choppe Shoppe Entry Door North Waterfall":
        Transition( "Eastern Hearth Choppe Shoppe Entry","Eastern Hearth Grassland Waterfall First Level", DirectionType.NORTH, TransitionType.DOORS,
                    Has("Eastern Hearth Waterfall Kear")),

    # --- Eastern Hearth Hidden Cave ---
    "Eastern Hearth Hidden Cave Geyser Choppe Entry":
        Transition("Eastern Hearth Hidden Cave","Eastern Hearth Choppe Shoppe Entry",DirectionType.OVERWORLD, TransitionType.GEYSER_UP),

    # --- Eastern Hearth Grassland Pit ---
    "Eastern Hearth Grassland Pit East Poppet":
        Transition("Eastern Hearth Grassland Pit","Eastern Hearth Poppet Entry", DirectionType.EAST, TransitionType.SCREENS),
    "Eastern Hearth Grassland Pit West Spinner":
        Transition("Eastern Hearth Grassland Pit", "Eastern Hearth Horizontal Spinner Room",DirectionType.WEST, TransitionType.SCREENS),
    "Eastern Hearth Grassland Pit North Riverbed Bottom":
        Transition("Eastern Hearth Grassland Pit","Eastern Hearth Grassland Riverbed Bottom", DirectionType.NORTH, TransitionType.SCREENS),

    # --- Eastern Hearth Poppet Entry ---
    "Eastern Hearth Poppet Entry West Pit":
        Transition("Eastern Hearth Poppet Entry", "Eastern Hearth Grassland Pit", DirectionType.WEST, TransitionType.SCREENS),
    "Eastern Hearth Poppet Entry Burrow South Cave":
        Transition( "Eastern Hearth Poppet Entry","Eastern Hearth Grassland Poppit Cave", DirectionType.SOUTH, TransitionType.BURROW,
                    CanBurrow()),
    "Eastern Hearth Poppet Entry North East Corner":
        Transition( "Eastern Hearth Poppet Entry","Eastern Hearth East Corner", DirectionType.NORTH,TransitionType.SCREENS),
    "Eastern Hearth Poppet Entry West Riverbed Dive":
        Transition("Eastern Hearth Poppet Entry","Eastern Hearth Grassland Riverbed Dive", DirectionType.WEST, TransitionType.SCREENS,
                   CanJumpTiles(distance=2)),

    # --- Eastern Hearth Under The Bridge ---
    "Eastern Hearth Under The Bridge Burrow East Bridge":
        Transition( "Eastern Hearth Under The Bridge","Eastern Hearth Under Bridge East", DirectionType.EAST, TransitionType.BURROW,
                    CanBurrow()),

    "Eastern Hearth Under The Bridge Burrow West Bridge":
        Transition("Eastern Hearth Under The Bridge", "Eastern Hearth Under Bridge West", DirectionType.WEST, TransitionType.BURROW,
                   CanBurrow()),

    "Eastern Hearth Under The Bridge South Under Bridge South":
        Transition( "Eastern Hearth Under The Bridge","Eastern Hearth Under Bridge South", DirectionType.SOUTH, TransitionType.SCREENS),

    # --- Eastern Hearth Under Bridge South ---
    "Eastern Hearth Under Bridge South North Under Bridge":
        Transition( "Eastern Hearth Under Bridge South","Eastern Hearth Under The Bridge", DirectionType.NORTH, TransitionType.SCREENS),
    "Eastern Hearth Under Bridge South Geyser Riverbed Dive":
        Transition("Eastern Hearth Under Bridge South", "Eastern Hearth Grassland Riverbed Dive", DirectionType.OVERWORLD, TransitionType.GEYSER_UP),

    # --- Eastern Hearth Under Bridge East ---
    "Eastern Hearth Under Bridge East West Under Bridge":
        Transition("Eastern Hearth Under Bridge East", "Eastern Hearth Under The Bridge", DirectionType.WEST, TransitionType.SCREENS),

    # --- Eastern Hearth Under Bridge West ---
    "Eastern Hearth Under Bridge West East Under Bridge":
        Transition("Eastern Hearth Under Bridge West","Eastern Hearth Under The Bridge", DirectionType.EAST, TransitionType.SCREENS),

    # --- Eastern Hearth East Corner ---
    "Eastern Hearth East Corner South Poppet":
        Transition("Eastern Hearth East Corner", "Eastern Hearth Poppet Entry", DirectionType.SOUTH, TransitionType.SCREENS),
    "Eastern Hearth East Corner West Bridge Right":
        Transition("Eastern Hearth East Corner","Eastern Hearth Grassland Bridge Right",DirectionType.WEST, TransitionType.SCREENS),
    "Eastern Hearth East Corner North Mourners":
        Transition("Eastern Hearth East Corner","Eastern Hearth Mourners Gate", DirectionType.NORTH, TransitionType.SCREENS),

    # --- Eastern Hearth Mourners Gate ---
    "Eastern Hearth Mourners Gate South East Corner":
        Transition("Eastern Hearth Mourners Gate","Eastern Hearth East Corner", DirectionType.SOUTH, TransitionType.SCREENS),
    "Eastern Hearth Mourners Gate Area East":
        Transition("Eastern Hearth Mourners Gate", "Mourner's Mile Knight's Rest", DirectionType.EAST,TransitionType.AREA_SCREENS),

    "Eastern Hearth Mourners Gate Burrow North Bucklers Start":
        Transition("Eastern Hearth Mourners Gate", "Eastern Hearth Bucklers Bluff Start", DirectionType.NORTH, TransitionType.BURROW, CanBurrow()),


    # --- Eastern Hearth Bucklers Bluff Start ---
    "Eastern Hearth Bucklers Bluff Start Burrow South Mourners":
        Transition("Eastern Hearth Bucklers Bluff Start","Eastern Hearth Mourners Gate", DirectionType.SOUTH, TransitionType.BURROW, CanBurrow()),

    "Eastern Hearth Bucklers Bluff Start South Mourners":
        Transition("Eastern Hearth Bucklers Bluff Start","Eastern Hearth Mourners Gate", DirectionType.SOUTH, TransitionType.SCREENS),


    # --- Eastern Hearth Bucklers Bluff Bucklers ---
    "Eastern Hearth Bucklers Bluff Bucklers West Waterfall Second":
        Transition("Eastern Hearth Bucklers Bluff Bucklers","Eastern Hearth Grassland Waterfall Second Level", DirectionType.WEST, TransitionType.SCREENS,
                CanJumpTiles(distance=2)),

    # --- Eastern Hearth Grassland Poppit Cave ---
    "Eastern Hearth Grassland Poppit Cave Burrow North Poppet":
        Transition( "Eastern Hearth Grassland Poppit Cave", "Eastern Hearth Poppet Entry", DirectionType.NORTH, TransitionType.BURROW,
                    CanBurrow()),

    "Eastern Hearth Grassland Poppit Cave East Poppit":
        Transition("Eastern Hearth Grassland Poppit Cave","Eastern Hearth Poppit", DirectionType.EAST, TransitionType.SCREENS),

    # --- Eastern Hearth Poppit ---
    "Eastern Hearth Poppit West Poppit Cave":
        Transition("Eastern Hearth Poppit","Eastern Hearth Grassland Poppit Cave", DirectionType.WEST,TransitionType.SCREENS),

    # --- Eastern Hearth Frozen Pass ---
    "Eastern Hearth Frozen Pass South Waterfall Mountain":
        Transition("Eastern Hearth Frozen Pass","Eastern Hearth Grassland Waterfall Mountain", DirectionType.SOUTH, TransitionType.SCREENS),
}

collectable_locations: dict[str, LocationData] = {
    "EH Grassland Trinket Bag" : LocationData(221, "Eastern Heath Grassland", HasCompletedOneSparkGenerator()),
    "EH Grassland Waterfall Windfall Charm" : LocationData(223, "Eastern Hearth Grassland Waterfall Second Level"),
    "EH Choppe Shoppe Chain Capacitor" : LocationData(226, "Eastern Hearth Choppe Shoppe"),
    "EH Grassland Waterfall Chest" : LocationData(234, "Eastern Hearth Grassland Waterfall Second Level"),
    "EH Buckler's Bluff Joule Box": LocationData(229, "Eastern Hearth Bucklers Bluff Cliff"),
    "EH Under the Bridge Chest" : LocationData(230, "Eastern Hearth Under Bridge West"),
    "EH Grassland Riverbed Chest" : LocationData(233, "Eastern Hearth Grassland Riverbed Dive"),
    "EH Grassland Bush Room Bonestone" : LocationData(236, "Eastern Hearth Bush Room", Has("Eastern Hearth Grassland Bushroom Kear")),
    "EH Grassland Horizontal Spinner Room Chest" : LocationData(231, "Eastern Hearth Grassland Horizontal Spinner Room"),
    "EH Grotto Chest" : LocationData(228, " Eastern Hearth Hidden Cave"),
    "EH Grassland Poppit Cave Chest" : LocationData(235, "Eastern Hearth Grassland Poppit Cave"),
    "EH Frozen Pass Chest" : LocationData(232, "Eastern Heath Frozen Pass", Has("FrozenTrainyardTicket")),
    "EH Frozen Pass IceBlock" : LocationData(237, "Eastern Heath Frozen Pass"),
    "EH Grassland Vertical Spinner Room Chest" : LocationData(238, "Eastern Hearth East Corner"),#TODO: CanReachLocation(HEAD AFTER SPARK GEN)
    "EH Grassland Poppit Cave Willow" : LocationData(239, "Eastern Hearth Grassland Poppit Cave"),
    "EH Grassland Poppit Cave Kear" : LocationData(240, "Eastern Hearth Grassland Poppit Cave"),
    "EH Grassland Dork Eyes" : LocationData(241, "Eastern Heath Grassland Bridge", Has("FishingRod")),
}

boss_locations: dict[str, LocationData] = {
    "EH Grassland Maxi": LocationData(1018, "Eastern Heath Grassland", HasCompletedOneSparkGenerator()),
}

connections: dict[str, RegionConnection] = {
    # --- Eastern Hearth Grassland Bridge ---
    "Eastern Hearth Grassland Bridge Left_Right":
        RegionConnection("Eastern Hearth Grassland Bridge Left","Eastern Hearth Grassland Bridge Right"),

    # --- Eastern Hearth Grassland Waterfall ---
    "Eastern Hearth Grassland Waterfall Mountain_Second Level":
        RegionConnection("Eastern Hearth Grassland Waterfall Mountain", "Eastern Hearth Grassland Waterfall Second Level"),
    "Eastern Hearth Grassland Waterfall Second Level_Mountain":
        RegionConnection("Eastern Hearth Grassland Waterfall Second Level", "Eastern Hearth Grassland Waterfall Mountain",
                         CanSwim()),

    # --- Eastern Hearth Bucklers Bluff ---
    "Eastern Hearth Bucklers Bluff Start_Cliff":
        RegionConnection("Eastern Hearth Bucklers Bluff Start","Eastern Hearth Bucklers Bluff Cliff",CanJumpTiles(distance=4)),
    "Eastern Hearth Bucklers Bluff Cliff_Start":
        RegionConnection("Eastern Hearth Bucklers Bluff Cliff","Eastern Hearth Bucklers Bluff Start", CanJumpTiles(distance=4)),

    "Eastern Hearth Bucklers Bluff Cliff_Bucklers":
        RegionConnection("Eastern Hearth Bucklers Bluff Cliff","Eastern Hearth Bucklers Bluff Bucklers"),
    "Eastern Hearth Bucklers Bluff Bucklers_Cliff":
        RegionConnection("Eastern Hearth Bucklers Bluff Bucklers","Eastern Hearth Bucklers Bluff Cliff"),
}
