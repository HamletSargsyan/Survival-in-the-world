from enum import Enum
from typing import List, TypedDict, Union

from core.base import DictSerializable


class ItemRarity(Enum):
    COMMON = "обычный"
    UNCOMMON = "необычный"
    RARE = "редкий"
    EPIC = "эпический"
    LEGENDARY = "легендарный"


class CraftDict(TypedDict):
    name: str
    quantity: int


class Item(DictSerializable):
    def __init__(
        self,
        name: str,
        rarity: ItemRarity,
        desc: str,
        strength: Union[float, None] = None,
        can_equip: bool = False,
        price: Union[int, None] = None,
        craft: Union[List[CraftDict], None] = None,
        # effects: List[Effect] = [],
        quantity: int = 0,
    ) -> None:
        self.name = name
        self.strength = strength
        self.rarity = rarity
        self.desc = desc
        self.can_equip = can_equip
        self.price = price
        # self.effects = effects
        self.craft = craft
        self.quantity = quantity
