
def range_incl(a: int, b: int) -> range:
    return range(a, b+1)

#Images for a single map Id
mapping_single: dict[int, int] = {
    0: 1,
    17: 1,
    18: 1,
    11: 2,
    19: 3,
    3: 4,
    2: 4,
    8: 4,
    16: 4,
    6: 5,
    4: 5,
    9: 6,
    13: 7,
    14: 8,
    7: 8,
    10: 8,
    23: 9,
    22: 9,
    28: 9,
    21: 9,
}

#Images for multiple map id
mapping_range: dict[range, int] = {
    range_incl(356, 364): 0,  # BADGE GATES, overworld
}

def should_change(map_id: int) -> bool:
    print("checking change")
    if map_id in mapping_single:
        return True
    return False

def map_page_index(data: int) -> int:
    print(data)
    if data in mapping_single:
        return mapping_single[data]
    return 0