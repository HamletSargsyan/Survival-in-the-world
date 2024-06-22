from enum import Enum, auto
from typing import List, TypedDict, Union

from core.game_object import GameObject, GameObjectType


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


class BaseItem(GameObject):
    def __init__(
        self,
        name: str,
        rarity: ItemRarity,
        desc: str,
        strength: Union[float, None] = None,
        can_equip: bool = False,
        price: Union[int, None] = None,
        craft: Union[List[CraftDict], None] = None,
        location: ItemLocation = ItemLocation.GROUND,
    ) -> None:
        super().__init__(type=GameObjectType.ITEM)

        self.name = name
        self.strength = strength
        self.rarity = rarity
        self.desc = desc
        self.can_equip = can_equip
        self.price = price
        self.craft = craft
        self.location = location


class ItemGroup(BaseItem):
    def __init__(
        self,
        name: str,
        rarity: ItemRarity,
        desc: str,
        strength: float | None = None,
        can_equip: bool = False,
        price: int | None = None,
        craft: List[CraftDict] | None = None,
        location: ItemLocation = ItemLocation.GROUND,
    ) -> None:
        super().__init__(
            name=name,
            rarity=rarity,
            desc=desc,
            strength=strength,
            can_equip=can_equip,
            price=price,
            craft=craft,
            location=location,
        )


class Item(BaseItem):
    def __init__(
        self,
        name: str,
        rarity: ItemRarity,
        desc: str,
        quantity: int = 0,
        strength: float | None = None,
        can_equip: bool = False,
        price: int | None = None,
        craft: List[CraftDict] | None = None,
        location: ItemLocation = ItemLocation.GROUND,
    ) -> None:
        super().__init__(
            name=name,
            rarity=rarity,
            desc=desc,
            strength=strength,
            can_equip=can_equip,
            price=price,
            craft=craft,
            location=location,
        )

        self.quantity = quantity
