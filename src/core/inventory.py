from core.item import Item, ItemLocation
from core.storage import Storage


class Inventory(Storage):
    @property
    def equipped_items(self) -> list[Item]:
        return list(filter(lambda i: i.location == ItemLocation.EQUIPPED, self.items))

    @property
    def quick_slots(self) -> list[Item]:
        return list(filter(lambda i: i.location == ItemLocation.QUICK_SLOT, self.items))
