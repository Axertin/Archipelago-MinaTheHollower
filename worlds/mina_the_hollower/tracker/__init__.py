import dataclasses
from enum import IntEnum


def range_incl(a: int, b: int) -> range:
    return range(a, b+1)


class GameState(IntEnum):
    DEVINIT = 0
    STARTUP = 1
    INTROBEACH = 2
    BAYOU = 3
    CRYPTA = 4
    CRYPTB = 5
    BONEBEACHA = 6
    BONEBEACHB = 7
    SEPTEMBURGA = 8
    SEPTEMBURGB = 9
    SEPTEMBURG_SEWER = 10
    FROZENTRAINYARDA = 11
    FROZENTRAINYARDB = 12
    FROZENTRAINYARDC = 13
    FROZENTRAINYARDBOSS = 14
    ASTRALORRERY = 15
    MANSION = 16
    HUB = 17
    HUB_OVERWORLD_EAST = 18
    HUB_OVERWORLD_WEST = 19
    HUB_OVERWORLD_SOUTH = 20
    HUB_MANSION = 21
    ASTRAL_ORRERY_MIRROR_HUB = 22
    HUB_BAYOU_OVERWORLD = 23
    FISHING_HOLE = 24
    CRYPT_OVERWORLD = 25
    CRYPT_OVERWORLD_HELL = 26
    BONEBEACH_OVERWORLD = 27
    SEPTEMBURG_OVERWORLD = 28
    CHECKPOINTROOM = 29
    WEAPONGET_WORLD = 30
    RANDOM_ENCOUNTER = 31
    INTROSEA = 32
    MANSIONORPHANAGE = 33
    PUPPETMASTER = 34
    EVRAARENA = 35
    INTROBEACH_SCRATCH = 36
    BAYOU_SCRATCH = 37
    CRYPT_SCRATCH = 38
    SEPTEMBURG_SCRATCH = 39
    BONEBEACH_SCRATCH = 40
    FROZENTRAINYARD_SCRATCH = 41
    ASTRALORRERY_SCRATCH = 42
    MANSION_SCRATCH = 43
    CRYPT_TOWER = 44
    BAYOU_TOWER = 45
    SEPTEMBURG_TOWER = 46
    BONEBEACH_TOWER = 47
    FROZENTRAINYARD_TOWER = 48
    ASTRAL_TOWER = 49
    MANSION_TOWER = 50
    TRAINCABIN = 51
    TRAINCABIN_OVERLAY_BAYOU = 52
    TRAINCABIN_OVERLAY_BONEBEACH = 53
    TRAINCABIN_OVERLAY_FROZEN = 54
    TRAINCABIN_OVERLAY_HUB = 55
    TRAINCABIN_OVERLAY_SEPTEMBURG = 56
    GYM_ALEC = 57
    GYM_BRIDGET = 58
    GYM_DANDY = 59
    GYM_ELI = 60
    GYM_ERIC = 61
    GYM_SANDY = 62
    GYM_SEAN = 63
    GYM_IAN = 64
    GYM_IANG = 65
    GYM_ADAM = 66
    GYM_CHARLIE = 67
    GYM_BONEBEACH = 68
    GYM_CHECKPOINTROOM_ALT = 69
    GYM_COMBAT = 70
    GYM_FERRO_FLUID = 71
    GYM_GLASS = 72
    GYM_GRINDRAIL = 73
    GYM_INTERACTIONS = 74
    GYM_PORTRAIT_ENEMY = 75
    GYM_RAINBOW_PLATFORM = 76
    GYM_SURPRISE_SPAWN = 77
    GYM_TILESETTEST = 78
    GYM_TOWERCLIMB = 79
    GYM_TRAILERLAND = 80
    GYM_TRAILERLANDVISTA = 81
    GYM_WORLDLOADTEST1 = 82
    GYM_WORLDLOADTEST2 = 83
    TITLE_SCREEN = 84
    YCG_LOGO = 85
    TRINKETS = 86
    GEAR = 87
    DEATH = 88
    BONESTONEMACHINE = 89
    WEAPONS_CHEST = 90
    WORLD_MAP = 91
    NEWSPAPER_DISPLAY = 92
    NEWSPAPER_SELECT = 93
    FISH_SELECT = 94
    MANUAL = 95
    DEMO_ACTIVATE = 96
    DEMO_SELECT = 97
    DEMO_RESULTS = 98
    DEMO_UPSELL = 99
    DEMO_KICKSTARTER = 100
    OPTIONS_MENU = 101
    FEATS_MENU = 102
    BRIGHTNESS_MENU = 103
    SCREENSCALE_MENU = 104
    PROFILE_SELECT_MENU = 105
    CREDITS_MENU = 106
    SOUND_TEST_MENU = 107
    CHEATS_MENU = 108
    PANORAMA_INTROLETTER = 109
    PANORAMA_HUB = 110
    PANORAMA_BAYOU = 111
    PANORAMA_CRYPT = 112
    PANORAMA_SEPTEMBURG = 113
    PANORAMA_BONEBEACH = 114
    PANORAMA_ASTRALORRERY = 115
    PANORAMA_FROZENTRAINYARD = 116
    PANORAMA_WINDOWFALL = 117
    PANORAMA_MANSION = 118
    PANORAMA_ENDING_START = 119
    PANORAMA_ENDING_END = 120
    BIGART_BONEBEACHMAP = 121
    BIGART_CRYPTHEADSTONE = 122
    BIGART_MANSIONPRTGOOD = 123
    BIGART_MANSIONPRTEVIL = 124
    BIGART_MANSIONPORTRAIT = 125
    BIGART_SEPTCHALKBOARD = 126
    BIGART_SCROLLTEST = 127
    BIGART_MIRROR = 128
    BIGART_WINDOWPUSHPHOTO = 129
    BIGART_GIRAFFETINY = 130
    BIGART_TELESCOPE = 131
    BIGART_CATGHOSTS = 132
    BIGART_MANSIONPAINTING = 133
    INTRO_CINEMA_SCENE1 = 134
    INTRO_CINEMA_SCENE2 = 135
    INTRO_CINEMA_SCENE3A = 136
    INTRO_CINEMA_SCENE3B = 137
    INTRO_CINEMA_SCENE4 = 138
    INTRO_CINEMA_SCENE5A = 139
    INTRO_CINEMA_SCENE5B = 140
    INTRO_CINEMA_SCENE5C = 141
    INTRO_CINEMA_SCENE6A = 142
    INTRO_CINEMA_SCENE6B = 143
    INTRO_CINEMA_SCENE7 = 144
    ENDING_CINEMA_OSSEX = 145
    ENDING_CINEMA_CRYPT = 146
    ENDING_CINEMA_BAYOU = 147
    ENDING_CINEMA_BONEBEACH = 148
    ENDING_CINEMA_HOLLOWER = 149
    ENDING_CINEMA_SEPTEMBURG = 150
    ENDING_CINEMA_FROZEN = 151
    ENDING_CINEMA_ASTRAL = 152
    ENDING_CINEMA_MANSION = 153
    ENDING_PRECREDITS = 154
    ENDING_POSTCREDITS = 155
    TEXTDISPLAY = 156

@dataclasses.dataclass
class RoomGroup:
    label: str
    rooms: dict[int, int]

RoomLookup: dict[GameState, RoomGroup] = {
    GameState.INTROBEACH: RoomGroup("LL", {
        0: 1,
        2: 3,
        3: 3,
        4: 4,
        6: 4,
        7: 5,
        8: 3,
        9: 4,
        10: 5,
        11: 1,
        13: 4,
        14: 5,
        15: 5,
        16: 3,
        17: 1,
        18: 1,
        19: 2,
        # 23: 6,
        # 22: 6,
        # 28: 6,
        # 21: 6,

    }),
    GameState.HUB_OVERWORLD_SOUTH: RoomGroup("SO", {
        0: 7,
        15: 7,
        6: 7,
        5: 7,
        4: 7,
        7: 7,
        23: 7,
        22: 7,
        18: 9,
        10: 8,
        11: 8,
        12: 8,
        14: 8,
        13: 8,
        16: 10,
        19: 10,
        9: 11,
        17: 11,
    }),
    GameState.HUB_OVERWORLD_EAST: RoomGroup("EH", {
        0: 13,
        1: 13,
        3: 13,
        5: 13,
        6: 13,
        8: 13,
        15: 13,
        16: 13,
        17: 13,
        4: 14,
        7: 14,
        11: 15,
        19: 16,
        20: 16,
        21:16,
        23:16,
        18:16,
        26:16,
        24:16,
        25:16
    }),
    GameState.HUB: RoomGroup("OS", {
        10:17,
        4:18,
        15:17,
        11: 17,
        12: 17,
        20: 17,
        6: 18,
        5: 18,
        35:20,
        16:21,
        32: 22,
        31: 22,
        33: 22,
        38:22,
        39:22,
        24:22,
        34:20,
        17:20,
        25:20,
        18:20,
        40:20,
        14:21,
        19:21,
        13:21,
        22:21, #kear shop
        26:21, #pawnty
        2:21, #legovitch
        1:21, #bazaar=
        23:21, #couples quarter
        3:22, #music hall
        28:22,
        8:22,
    }),
    GameState.EVRAARENA: RoomGroup("EVRA", {
        0:19,
        1:19,
        2:19,
        3:19,
    }),
    GameState.TRAINCABIN: RoomGroup("TRAIN", {
        1:23,
        5:23,
        6:23,
        3:23,
        2:23,
    }),
    GameState.HUB_OVERWORLD_WEST: RoomGroup("WW", {
        6:24,
        9:24,
        7:24,
        5:24,
        10:24,
        12:24,
        13:24,
        14:24,
        3:24,
        8:24,
        11:24,
    }),
    GameState.HUB_BAYOU_OVERWORLD: RoomGroup("BW", {
        5:27,
        18:27,
        4:27,
        11:28,
        15:28,
        8:28,
        6:27,
        24:30,
        0:28, #Fishing
        3:28,
        2:28,
        9:28, #pinky
        16:29,
        7:29,
        12:29
    }),
    GameState.BAYOU: RoomGroup("NB", {
        24:30,
        36:30,
        10:30,
        23:31,
        34:31,
        31:31,
        25:31,
        32:31,
        28:32,
        27:32,
        26:37,
        30:30,
        33:30,
        29:30,
        8:32,
        20:32,
        21:37,
        4:33,
        5:33,
        6:33,
        11:34,
        14:34,
        12:34,
        2:34,
        1:34,
        13:34,
        15:34,
        3:37,
        35:37,
        16:35,
        17:35,
        18:35,
        19:35,
        39:36,
        0:36,
        38:37
    }),
    GameState.CRYPT_OVERWORLD: RoomGroup("MM", {
        2:38,
        3:38,
        16:38,
        1:39,
        5:39,
        14:39,
        13:40,
        15:40,
        6:40,
        7:40,
        8:40,
        0:42,
        12:43,
    }),
    GameState.CRYPT_OVERWORLD_HELL: RoomGroup("DP", {
        0:42,
        1:42,
        4:42,
        2:42,
        3:42,
    }),
    GameState.CRYPTA: RoomGroup("QBA", {
        9:44,
        3:44,
        0:45,
        4:45,
        1:45,
        7:46,
        2:47,
        5:47,
        6:45,
    }),
    GameState.CRYPTB: RoomGroup("QBB", {
        20:48,
        22:49,
        21:49,
        27:49,
        10:49,
        0:50,
        7:50,
        5:50,
        6:50,
        12:50,
        8:50,
        23:51,
        11:51,
        28:51,
        26:51,
        25:51,
        19:51,
        31:51,
        24:51,
        32:51,
        9:51,
        13:51,
        15:52,
        16:52,
        14:52,
        4:52,
        29:53,
        30:53,
        1:54,
        17:54,
        3:54,
        2:54,
    }),
    GameState.SEPTEMBURG_OVERWORLD: RoomGroup("KW", {
        14:55,
        13:55,
        4:55,
        7:55,
        6:55,
        15:55,
        19:56,
        12:56,
        10:58,
        5:57,
        8:57,
        18:58,
        17:57,
        1:58,
        2:58,
        20:58,
        9:58,
        11:59,
    }),
    GameState.SEPTEMBURGA: RoomGroup("SBA", {
        4:60,
        6:60,
        14:60,
        5:61,
        16:61,
        0:61,
        1:62,
        19:62,
        15:62,
        12:63,
        13:63,
        3:64,
        2:64,
        18:64,
        17:64,
        7:65,
        8:65,
        9:65,
        10:65,
    }),
    GameState.SEPTEMBURGB: RoomGroup("SBB", {
        6:66,
        17:66,
        4:66,
        5:66,
        15:67,
        3:67,
        7:68,
        11:68,
        13:68,
        16:68,
        8:69,
        10:69,
        9:69,
        14:69,
        2:69,
        1:70,
        0:70,
    }),
    GameState.SEPTEMBURG_SEWER: RoomGroup("SBS", {
        3:71,
        2:71,
        8:71,
        5:71,
        7:71,
        6:71,
        1:72,
        0:72,
        4:72,
        14:73,
    }),
    GameState.BONEBEACH_TOWER: RoomGroup("SF", {
        3:74
    }),
    GameState.BONEBEACH_OVERWORLD: RoomGroup("SF", {
        8: 12,
        7: 12,
        6: 12,
        9: 12,
        15: 12,
        12:73,
        24:73,
        25:74,
        17:74,
        13:74,
        26:74,
        2:73,
        3:74,
        4:75,
        5:76,
        1:76,
        0:76,
    }),
    GameState.BONEBEACHA: RoomGroup("BBA", {
        0:77,
        5:77,
        1:79,
        8:78,
        7:78,
        16:77,
        4:78,
        6:78,
        14:78,
        9:78,
        2:79,
        3:80,
        20:83,
        19:81,
        13:81,
        10:81,
        12:81,
        15:81,
        11:81,
    }),
    GameState.BONEBEACHB: RoomGroup("BBB", {
        0:82,
        5:82,
        1:82,
        2:82,
        10:82,
        9:82,
        8:82,
        3:83,
        6:83,
        18:83,
        20:83,
        4:83,
        11:84,
        13:84,
        14:84,
        12:85,
        7:82,
    }),
    GameState.FROZENTRAINYARDA: RoomGroup("CTPA", {
        9:86,
        11:86,
        2:87,
        12:87,
        3:88,
        7:88,
        4:88,
        5:88,
        15:88,
        6:88,
        8:89,
        14:90,
        1:91,
        20:91,
    }),
    GameState.FROZENTRAINYARDB: RoomGroup("CTPB", {
        6:91,
        5:91,
        8:91,
        12:91,
        2:92,
        9:92,
        3:92,
        4:92,
        15:93,
        16:93,
        0:93,
        19:93,
        13:93,
        1:94,
        14:94,
        17:94,
        20:94,
        18:94,
        11:94,
    }),
    GameState.FROZENTRAINYARDC: RoomGroup("CTPC", {
        0:95,
        3:95,
        2:95,
        1:95,
        4:95,
        11:95,
    }),
    GameState.FROZENTRAINYARD_TOWER: RoomGroup("CTPC", {
        0:96,
        1:96,
        15:96,
        16:96,
    }),
    GameState.ASTRAL_ORRERY_MIRROR_HUB: RoomGroup("AOMH", {
        3:97,
        4:97,
        1:97,
        0:98
    }),
    GameState.ASTRALORRERY: RoomGroup("AO", {
        3:99,
        1:99,
        0:100,
        14:100,
        15:100,
        20:100,
        33:100,
        32:10,
        17:100,
        18:100,
        19:101,
        16:101,
        29: 102,
        4: 102,
        2: 102,
        21: 102,
        9: 102,
        25:103,
        5:103,
        22:103,
        23:103,
        8:103,
        7:103,
        6:103,
        37:103,
        31:103,
        24:103,
        28:104,
        30:104,
        13:104,
        26:105,
        36:105,
        35:105,
        38:105,
        10:105,
        11:105,
        34:105,
    }),
    GameState.ASTRAL_TOWER: RoomGroup("AO", {
        0:105
    }),
    GameState.MANSIONORPHANAGE: RoomGroup("RM", {
        0:106,
        1:106,
    }),
    GameState.HUB_MANSION: RoomGroup("RM", {
        21:106,
        0:106,
        1:106,
        2:106,
    }),
    GameState.MANSION: RoomGroup("RM", {
        0:107,
        38:106,
        6:106,
        21:107,
        39:107,
        29:107,
        28:107,
        20:107,
        17:108,
        7:108,
        16:109,
        13:109,
        14:109,
        41:109,
        15:109,
        40:110,
        18:110,
        19:110,
        3:111,
        8:111,
        31:111,
        5:111,
        12:108,
        10:108,
        11:108,
        4:112,
        30:112,
        32:112,
        33:112,
        9:112,
    })
}


def map_page_index(data: int) -> int:
    if data is None or data == "":
        return 0

    data = int(data)
    gamestate = (data >> 16) & 0xFFFF
    screen = data & 0xFFFF

    if gamestate not in RoomLookup:
        return 0

    map_data = RoomLookup[GameState(gamestate)]

    if screen not in map_data.rooms:
        return 0
    return map_data.rooms[screen]