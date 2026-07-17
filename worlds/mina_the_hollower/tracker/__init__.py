import dataclasses


def range_incl(a: int, b: int) -> range:
    return range(a, b+1)

#Images for a single map Id
loners_landing: dict[int, int] = {
    0: 1,
    17: 1,
    18: 1,
    11: 1,
    19: 2,
    3: 3,
    2: 3,
    8: 3,
    16: 3,
    6: 4,
    4: 4,
    9: 4,
    13: 4,
    14: 5,
    15: 5,
    7: 5,
    10: 5,
    23: 6,
    22: 6,
    28: 6,
    21: 6,
}

southern_outskirts: dict[int, int] = {
    15: 0,
    6: 0,
    4: 0,
    0: 0,
    7: 0,
    23:0,
    22: 0,
    10: 1,
    11: 1,
    12: 1,
    14: 1,
    13: 1,
    16: 2,
    19: 3,
}

so_poppit: dict[int, int] = {
    18:0
}
cave_network: dict[int, int] = {
    9: 0,
    17: 0,
}

mining_passage: dict[int, int] = {
    8: 0,
    7: 0,
    6: 0,
    9: 0,
    15: 0,
}

eastern_heath: dict[int, int] = {
    0: 0,
    1: 0,
    3: 0,
    5: 0,
    6: 0,
    8: 0,
    15: 0,
    16: 0,
    17: 0,
    4: 1,
    7: 1,
    11: 2,
}
cave_eastern_heath: dict[int, int] = {
    19: 0,
    20: 0
}
under_eastern_heath: dict[int, int] = {
    23:0,
    18:0,
    26:0,
    24:0,
    21:0
}

ossex_main: dict[int, int] = {
    10:0,
    4:1,
}

ossex_courtyard: dict[int, int] = {
    10: 0,
    11: 0,
    12: 0,
    20: 0,
}

ossex_high_street: dict[int, int] = {
    6: 0
}

ossex_bowery: dict[int, int] = {
    5: 0
}

balcony: dict[int, int] = {
    10:0,
    15:0,
}
goddred_tomb: dict[int, int] = {
    0:0,
    1:0,
    2:0,
    3:0,
}

#ALl residence are the same area
high_street_r_bottom: dict[int, int] = {
    35:0,
    16:1,
    32: 2,
    31: 2,
    33: 2,
    38:2,
    39:2,
    24:2
}
high_street_r_top: dict[int, int] = {
    34:0,
}

atelier: dict[int, int] = {
    17:0,
    25:0,
}
training_center: dict[int, int] = {
    18:0,
}
os_sewers: dict[int, int] = {
    40:0,
}

os_burrowers: dict[int, int] = {
    14:0,
    19:0,
}
os_shop: dict[int, int] = {
    13:0,
}

os_kear: dict[int, int] = {
    22:0,
}
os_pawnty: dict[int, int] = {
    26:0,
}
os_weapons: dict[int, int] = {
    2:0,
}
os_trinket: dict[int, int] = {
    1:0,
}
os_couples: dict[int, int] = {
    23:0,
}
os_music: dict[int, int] = {
    3:0,
}
os_train_lower: dict[int, int] = {
    28:0,
}
os_train: dict[int, int] = {
    8:0,
}

train_caboose: dict[int, int] = {
    1:0,
}
train_interior: dict[int, int] = {
    5:0,
}
train_cabins: dict[int, int] = {
    6:0,
}
train_out: dict[int, int] = {
    3:0,
}
train_engine: dict[int, int] = {
    2:0,
}
western_wilds: dict[int, int] = {
    6:0,
    9:0,
}
wilds_secret: dict[int, int] = {
    7:0,
}

molten_foundry: dict[int, int] = {
    5:0,
    10:0,
}
molten_dungeon: dict[int, int] = {
    12:0,
    13:0,
    14:0,
}
western_pond: dict[int, int] = {
    3:0,
}
wilds_outlook: dict[int, int] = {
    8:0,
    11:0,
}
backwaters: dict[int, int] = {
    5:0,
    18:0,
    4:0,
    11:1,
    15:1,
    8:1,
    6:0,
    24:3
}
pinky: dict[int, int] = {
    9:0,
}
fishing: dict[int, int] = {
    0:0,
    3:0,
    2:0,
}
lanturn_cave: dict[int, int] = {
    16:0,
}
backwaters_station: dict[int, int] = {
    7:0,
}
lucky_lair: dict[int, int] = {
    12:0,
}
bayou_boat: dict[int, int] = {
    24:0,
    36:0,
    10:0,
    23:1,
    34:1,
    31:1,
    25:1,
    32:1,
    28:2,
    27:2,
    26:7
}
bayou_start: dict[int, int] = {
    24:0,
}
bayou_fen: dict[int, int] = {
    30:0,
    33:0,
    29:0,
}
bayou_lagoon: dict[int, int] = {
    8:0,
    20:0,
    29:0,
    21:5
}
bayou_moonlit: dict[int, int] = {
    4:0,
    5:0,
    6:0,
}
bayou_thicket: dict[int, int] = {
    11:0,
    14:0,
    12:0,
    2:0,
    1:0,
    13:0,
    15:0,
    3:3,
    35:3,
}
bayou_tainted: dict[int, int] = {
    16:0,
    17:0,
    18:0,
    19:0,
    39:1,
    0:1
}
bayou_lair: dict[int, int] = {
    0:0,
}
bayou_shack: dict[int, int] = {
    38:0,
}
mourners_mile: dict[int, int] = {
    2:0,
    3:0,
    16:0,
    1:1,
    5:1,
    14:1,
}
mm_tomb: dict[int, int] = {
    13:0,
}
mm_cave: dict[int, int] = {
    6:0,
}

mm_spike: dict[int, int] = {
    7:0,
    8:0,
}
mm_generator: dict[int, int] = {
    0:0,
}
mm_mina_grave: dict[int, int] = {
    0:0,
}
mm_deprived_path: dict[int, int] = {
    1:0,
    4:0,
    2:0,
    3:0,
}
mm_stairs: dict[int, int] = {
    12:0,
    3:0,
}
qc_graveyard: dict[int, int] = {
    9:0,
    3:0,
    0:1,
    4:1,
    1:1,
    7:2,
    2:3,
    5:3,
}

qc_tomb: dict[int, int] = {
    6:0,
}
qc_crypt: dict[int, int] = {
    20:0,
}
qc_entryway: dict[int, int] = {
    22:0,
    21:0,
    27:0,
    10:0,
    0:1,
    7:1,
    5:1,
    6:1,
    12:1,
}
qc_deep_stair: dict[int, int] = {
    8:0,
}
qc_head: dict[int, int] = {
    23:0,
    11:0,
    28:0,
    26:0,
    25:0,
    19:0,
    31:0,
    24:0,
    32:0,
    9:0,
}
qc_final_stair: dict[int, int] = {
    13:0,
}
qc_chamber: dict[int, int] = {
    15:0,
    16:0,
    14:0,
    4:0,
    29:1,
    30:1,
    1:2,
    17:2
}
qc_end: dict[int, int] = {
    3:0,
    2:0,
}
kw_start: dict[int, int] = {
    14:0,
}
kw_overgrowth: dict[int, int] = {
    13:0,
    4:0,
    7:0,
    6:0,
    15:0,
}
kw_overgrowth_house: dict[int, int] = {
    19:0,
    12:0,
}
kw_mad_house: dict[int, int] = {
    10:0
}
kw_farm: dict[int, int] = {
    5:0,
    8:0,
    18:1,
    17:0,
}
kw_interiors: dict[int, int] = {
    1:0,
    2:0,
}
kw_train: dict[int, int] = {
    20:0,
    9:0,
}
kw_wallowers: dict[int, int] = {
    11:0,
}
sb_farm: dict[int, int] = {
    4:0,
    6:0,
    14:0,
    5:1,
    16:1,
    0:1,
    1:2,
    19:2,
    15:2,
    12:3,
    13:3,
    3:4,
    2:4,
    18:4,
    17:4,
}
sb_barn: dict[int, int] = {
    7:0,
    8:0,
    9:0,
}
sb_barn_exit: dict[int, int] = {
    10:0,
}
sb_storm_intro: dict[int, int] = {
    6:0,
    17:0,
    4:0,
    5:0,
}
sb_town: dict[int, int] = {
    6:0,
    17:0,
    4:0,
    5:0,
    15:1,
}
sb_town_house: dict[int, int] = {
    3:0,
}
sb_forest: dict[int, int] = {
    7:0,
    11:0,
    13:0,
    16:0,
}
sb_stormwatch: dict[int, int] = {
    8:0,
    10:0,
    9:0,
    14:0,
    2:0,
    1:1
}
sb_fight: dict[int, int] = {
    0:0,
}
sb_generator: dict[int, int] = {
    2:0,
    0:0,
}
sb_wastewater: dict[int, int] = {
    3:0,
    2:0,
    8:0,
    5:0,
    7:0,
    6:0,
    1:1,
    0:1,
    4:1,
}
sf_start: dict[int, int] = {
    14:0,
}
sandfalls: dict[int, int] = {
    12:0,
    24:0,
    25:1,
    17:1,
    13:1,
    26:1,
}
sf_station: dict[int, int] = {
    2:0,
}
sf_ring: dict[int, int] = {
    3:0,
}
sf_junction: dict[int, int] = {
    2:0,
    4:0,
}
sf_mine: dict[int, int] = {
    5:0,
    4:0,
    1:0,
    0:0,
}
bb_shortcut: dict[int, int] = {
    0:0,
    5:0,
    1:2,
    8:1,
    7:1
}
bb_trail: dict[int, int] = {
    16:0,
    5:0,
    7:1,
    4:1,
    6:1,
    14:1,
    0:1,
    9:1,
    1:2,
    2:2,
}
bb_tent: dict[int, int] = {
    19:0,
}
bb_cave: dict[int, int] = {
    10:0,
    12:0,
    15:0,
    11:0,
}
bb_back: dict[int, int] = {
    14:0,
    8:0,
    4:0,
    1:1,
    2:1,
    20:5,
}

bb_maw: dict[int, int] = {
    29:0,
    5:0,
}
bb_tract: dict[int, int] = {
    1:0,
    2:0,
    10:0,
    9:0,
    8:0,
    3:1,
}
bb_mine: dict[int, int] = {
    6:0,
    18:0,
    20:0,
    4:0,
}
bb_depths: dict[int, int] = {
    11:0,
    13:0,
    14:0
}
bb_dark: dict[int, int] = {
    12:0,
}
bb_arena: dict[int, int] = {
    5:0,
    7:0,
}
ctp_pass_bottom: dict[int, int] = {
    9:0,
}
ctp_pass: dict[int, int] = {
    11:0,
}
ctp_train: dict[int, int] = {
    2:0,
    12:0,
}
ctp_gorge: dict[int, int] = {
    3:0,
    7:0,
    4:0,
    5:0,
    15:0,
    6:0,
    9:0,
    8:1,
    14:2,
    1:3,
    20:3,
}

ctp_woods: dict[int, int] = {
    6:0,
    5:0,
    8:0,
    12:0,
}

ctp_rail: dict[int, int] = {
    2:0,
    9:0,
    3:0,
    4:0,
}
ctp_cavern: dict[int, int] = {
    15:0,
    16:0,
}

ctp_cavern_arena: dict[int, int] = {
    0:0,
    19:0,
    13:0,
}

ctp_summit: dict[int, int] = {
    1:0,
    14:0,
    17:0,
    20:0,
    18:0,
    11:0,
}

ctp_agnes: dict[int, int] = {
    0:0,
    3:0,
    2:0,
    1:0,
    4:0,
    11:0,
}
ctp_maelstorm: dict[int, int] = {
    0:0,
    1:0,
}
ctp_maelstorm_bottom: dict[int, int] = {
    15:0,
}
ctp_generator: dict[int, int] = {
    0:0,
}
ctp_maelstorm_cliff: dict[int, int] = {
    16:0,
}
ao_mirror: dict[int, int] = {
    3:0,
    1:0,
    0:1
}
ao_stellarium: dict[int, int] = {
    3:0,
    1:0,
    0:1
}
ao_cog: dict[int, int] = {
    14:0,
    15:0,
    20:0,
    33:0,
    32:0,
    17:0,
    18:0,
    19:1,
    16:1,
}
ao_gravity: dict[int, int] = {
    29:0,
    1:0,
    4:0,
    0:0,
    2:0,
    21:0,
    9:0,
    3:0,
}

ao_mutant: dict[int, int] = {
    25:0,
    5:0,
    22:0,
    23:0,
    8:0,
    7:0,
    6:0,
    37:0,
    31:0,
    24:0,
}

ao_scholar: dict[int, int] = {
    28:0,
    30:0,
    13:0,
    23:0,
    8:0,
    24:0,
}
ao_archive: dict[int, int] = {
    26:0,
    36:0,
    35:0,
    5:0,
    38:0,
    10:0,
}
ao_exit: dict[int, int] = {
    11:0,
    34:0,
}
ao_generator: dict[int, int] = {
    0:0,
}
rm_foyer: dict[int, int] = {
    0:0,
}
rm_foyer_butler: dict[int, int] = {
    2:0,
}
rm_foyer_library: dict[int, int] = {
    1:0,
}
rm_orphanage: dict[int, int] = {
    0:0,
    1:0,
}
rm_washroom: dict[int, int] = {
    38:0,
}
rm_hall: dict[int, int] = {
    6:0,
}
rm_ballroom: dict[int, int] = {
    0:0,
}
rm_meowstro: dict[int, int] = {
    21:0,
    39:0,
}
rm_mimic: dict[int, int] = {
    29:0,
    28:0,
    20:0
}
rm_corridor: dict[int, int] = {
    17:1,
    7:0,
}
rm_greenhouse: dict[int, int] = {
    16:0,
    13:0,
    14:0,
    41:0,
    15:0,
}
rm_rafters: dict[int, int] = {
    40:0,
    18:0,
    19:0,
}
rm_gallery: dict[int, int] = {
    3:0,
    8:0,
}
rm_servants: dict[int, int] = {
    31:0,
    5:0,
}
rm_roof: dict[int, int] = {
    20:0,
    12:0,
    10:0,
    11:0,
    16:0,
}
rm_dining: dict[int, int] = {
    4:0,
    30:0,
}

rm_core: dict[int, int] = {
    32:0,
    33:0,
}
rm_bath: dict[int, int] = {
    38:0,
}
rm_study: dict[int, int] = {
    9:0,
}
rm_generator: dict[int, int] = {
    0:0,
}
@dataclasses.dataclass
class MapData:
    lookup: dict[int, int]
    start_index: int

area_id_to_map: dict[int, MapData] = {
    184: MapData(loners_landing, 0),
    59: MapData(southern_outskirts, 7),
    61: MapData(cave_network, 11),
    92: MapData(mining_passage, 12),
    54: MapData(eastern_heath, 13),
    53: MapData(under_eastern_heath, 16),
    52: MapData(cave_eastern_heath, 16),
    144: MapData(balcony, 17),
    153: MapData(ossex_main, 17),
    145: MapData(ossex_courtyard, 17),
    151: MapData(ossex_high_street, 18),
    163: MapData(ossex_bowery, 18),
    147: MapData(goddred_tomb, 19),
    161: MapData(high_street_r_bottom, 20),
    165: MapData(high_street_r_top, 20),
    162: MapData(atelier, 20),
    164: MapData(training_center, 20),
    152: MapData(os_sewers, 20),
    158: MapData(os_burrowers, 21),
    159: MapData(os_shop, 21),
    160: MapData(os_kear, 21),
    149: MapData(os_pawnty, 21),
    157: MapData(os_weapons, 21),
    155: MapData(os_trinket, 21),
    166: MapData(os_couples, 21),
    154: MapData(os_music, 22),
    150: MapData(os_train_lower, 22),
    148: MapData(os_train, 22),
    177: MapData(train_caboose, 23),
    176: MapData(train_interior, 23),
    178: MapData(train_cabins, 23),
    179: MapData(train_out, 23),
    180: MapData(train_engine, 23),
    63: MapData(western_wilds, 24),
    66: MapData(wilds_secret, 24),
    65: MapData(western_pond, 24),
    67: MapData(molten_foundry, 25),
    68: MapData(molten_dungeon, 25),
    64: MapData(wilds_outlook, 26),
    70: MapData(backwaters, 27),
    72: MapData(pinky, 28),
    74: MapData(fishing, 28),
    73: MapData(lanturn_cave, 29),
    76: MapData(backwaters_station, 29),
    75: MapData(lucky_lair, 29),
    1: MapData(bayou_boat, 30),
    8: MapData(bayou_fen, 30),
    2: MapData(bayou_start, 30),
    3: MapData(bayou_lagoon, 32),
    4: MapData(bayou_moonlit, 33),
    6: MapData(bayou_thicket, 34),
    7: MapData(bayou_tainted, 35),
    11: MapData(bayou_lair, 36),
    10: MapData(bayou_shack, 37),
    85: MapData(mourners_mile, 38),
    88: MapData(mm_tomb, 40),
    89: MapData(mm_spike, 40),
    87: MapData(mm_cave, 40),
    21: MapData(mm_generator, 41),
    90: MapData(mm_mina_grave, 42),
    91: MapData(mm_deprived_path, 42),
    86: MapData(mm_stairs, 43),
    19: MapData(qc_graveyard, 44),
    20: MapData(qc_tomb, 45),
    12: MapData(qc_crypt, 48),
    13: MapData(qc_entryway, 49),
    17: MapData(qc_deep_stair, 50),
    14: MapData(qc_head, 51),
    18: MapData(qc_final_stair, 51),
    15: MapData(qc_chamber, 52),
    16: MapData(qc_chamber, 54),
    78: MapData(kw_start, 55),
    77: MapData(kw_overgrowth, 55),
    82: MapData(kw_overgrowth_house, 56),
    84: MapData(kw_mad_house, 58),
    79: MapData(kw_farm, 57),
    83: MapData(kw_interiors, 58),
    81: MapData(kw_train, 58),
    80: MapData(kw_wallowers, 59),
    42: MapData(sb_farm, 60),
    43: MapData(sb_barn, 65),
    44: MapData(sb_barn_exit, 65),
    45: MapData(sb_town, 66),
    46: MapData(sb_town_house, 67),
    47: MapData(sb_forest, 68),
    48: MapData(sb_stormwatch, 69),
    49: MapData(sb_fight, 69),
    51: MapData(bb_shortcut, 69),
    50: MapData(sb_wastewater, 70),
    94: MapData(sf_start, 72),
    93: MapData(sandfalls, 72),
    95: MapData(sf_station, 72),
    96: MapData(sf_ring, 73),
    39: MapData(sf_junction, 74),
    97: MapData(sf_mine, 75),
    37: MapData(bb_shortcut, 76),
    24: MapData(bb_trail, 77),
    36: MapData(bb_back, 77),
    34: MapData(bb_tent, 80),
    28: MapData(bb_cave, 80),
    29: MapData(bb_maw, 81),
    35: MapData(bb_arena, 81),
    30: MapData(bb_tract, 81),
    31: MapData(bb_mine, 82),
    32: MapData(bb_depths, 83),
    33: MapData(bb_dark, 84),
    57: MapData(ctp_pass_bottom, 85),
    109: MapData(ctp_pass, 85),
    108: MapData(ctp_train, 86),
    119: MapData(ctp_maelstorm_cliff, 86),
    110: MapData(ctp_gorge, 87),
    111: MapData(ctp_woods, 90),
    114: MapData(ctp_rail, 91),
    112: MapData(ctp_cavern, 92),
    113: MapData(ctp_cavern_arena, 92),
    115: MapData(ctp_summit, 93),
    116: MapData(ctp_agnes, 94),
    117: MapData(ctp_maelstorm, 95),
    118: MapData(ctp_maelstorm_bottom, 95),
    121: MapData(ctp_generator, 95),
    100: MapData(ao_mirror, 96),
    103: MapData(ao_stellarium, 98),
    101: MapData(ao_cog, 99),
    106: MapData(ao_gravity, 101),
    104: MapData(ao_mutant, 102),
    105: MapData(ao_scholar, 103),
    98: MapData(ao_archive, 104),
    99: MapData(ao_exit, 104),
    107: MapData(ao_generator, 104),
    168: MapData(rm_foyer, 105),
    171: MapData(rm_foyer_butler, 105),
    169: MapData(rm_foyer_library, 105),
    170: MapData(rm_orphanage, 105),
    137: MapData(rm_washroom, 105),
    139: MapData(rm_hall, 105),
    127: MapData(rm_ballroom, 106),
    132: MapData(rm_meowstro, 106),
    140: MapData(rm_mimic, 106),
    134: MapData(rm_corridor, 107),
    128: MapData(rm_greenhouse, 108),
    129: MapData(rm_rafters, 109),
    130: MapData(rm_gallery, 110),
    131: MapData(rm_servants, 110),
    133: MapData(rm_roof, 111),
    138: MapData(rm_dining, 112),
    135: MapData(rm_core, 112),
    136: MapData(rm_study, 112),
    126: MapData(rm_generator, 112),

}


def map_page_index(data: int) -> int:
    if data is None or data == "":
        return 0

    data = int(data)
    area = (data >> 16) & 0xFFFF
    screen = data & 0xFFFF

    if area not in area_id_to_map:
        return 0

    map_data = area_id_to_map[area]

    if screen not in map_data.lookup:
        return 0
    return map_data.start_index + map_data.lookup[screen]