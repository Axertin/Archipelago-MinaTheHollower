from BaseClasses import ItemClassification
from .. import MovementItemData

movement_trinkets: dict[str, MovementItemData] = {
    "A": MovementItemData(0x78, 3, ItemClassification.progression),
    "D": MovementItemData(0x79, 4, ItemClassification.progression),
    "B": MovementItemData(0x7A, 2, ItemClassification.progression),
    "C": MovementItemData(0x7B, 1, ItemClassification.progression),
}
