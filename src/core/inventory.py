from core.item import Item, ItemLocation
from core.storage import Storage


class Inventory(Storage):
    def __init__(self, items: list[Item]) -> None:
        super().__init__("Инвентарь", items, 16)

    @property
    def equipped_items(self) -> list[Item]:
        return list(filter(lambda i: i.location == ItemLocation.EQUIPPED, self.items))

    @property
    def quick_slots(self) -> list[Item]:
        return list(filter(lambda i: i.location == ItemLocation.QUICK_SLOT, self.items))
