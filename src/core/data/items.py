from typing import Final

from core.item import ItemGroup, ItemLocation, ItemRarity


ITEMS_LIST: Final = [
    ItemGroup(
        name="монета",
        rarity=ItemRarity.COMMON,
        desc="Игравая валюта",
        location=ItemLocation.NONE,
    )
]
