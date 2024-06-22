from enum import Enum, auto
from typing import List, TypedDict, Union

from core.base import DictSerializable


class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()


class ItemLocation(Enum):
    GROUND = auto()
    INVENTORY = auto()
    EQUIPPED = auto()
    QUICK_SLOT = auto()


class CraftDict(TypedDict):
    name: str
    quantity: int


class Item(DictSerializable):
    def __init__(
        self,
        name: str,
        rarity: ItemRarity,
        desc: str,
        quantity: int = 0,
        strength: Union[float, None] = None,
        can_equip: bool = False,
        price: Union[int, None] = None,
        craft: Union[List[CraftDict], None] = None,
        location: ItemLocation = ItemLocation.GROUND,
    ) -> None:
        self.name = name
        self.strength = strength
        self.rarity = rarity
        self.desc = desc
        self.quantity = quantity
        self.can_equip = can_equip
        self.price = price
        self.craft = craft
        self.location = location
