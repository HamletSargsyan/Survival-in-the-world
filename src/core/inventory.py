from core.item import ItemType, ItemLocation
from core.storage import Storage


class Inventory(Storage):
    def __init__(self, items: list[ItemType] = []) -> None:
        super().__init__("Инвентарь", items, 16)

    @property
    def equipped_items(self) -> list[ItemType]:
        return list(filter(lambda i: i.location == ItemLocation.EQUIPPED, self.items))

    @property
    def quick_slots(self) -> list[ItemType]:
        return list(filter(lambda i: i.location == ItemLocation.QUICK_SLOT, self.items))

    def format_equipped_items(self):
        return self._format(self.equipped_items)

    def format_quick_slots(self):
        return self._format(self.quick_slots)
