# from functools import lru_cache
from core.data.items import ITEMS_LIST
from core.game_object import GameObject, GameObjectType
from core.item import ItemGroup, ItemType
from utils import format_list


class Storage(GameObject):
    def __init__(
        self, name: str, items: list[ItemType] = [], max_slots_count: int = 1
    ) -> None:
        super().__init__(type=GameObjectType.STORAGE)

        self.name = name
        self.items = items
        self.max_slots_count = max_slots_count

    def _format(self, items: list[ItemType]):
        return format_list(
            [f"{item.name} {self.get_item_quantity(item.name)}" for item in items],
            int(10),
        )

    def format(self):
        return self._format(self.items)

    def check(self):
        if len(self.items) > self.max_slots_count:
            self.items[: self.max_slots_count]

            # TODO: добавить сообщение

    # @lru_cache()
    def get_item_quantity(self, name: str):
        for item in ITEMS_LIST:
            if item.type == GameObjectType.ITEM_GROUP:
                i = self.find(name)
                if i is not None and isinstance(i, ItemGroup):
                    return i.quantity
        return len(self.find_all(name))

    # @lru_cache()
    def find_all(self, name: str):
        def work():
            for item in self.items:
                if item.name == name:
                    yield item

        return list(work())

    # @lru_cache()
    def find(self, name: str):
        items = self.find_all(name)
        if len(items) > 0:
            return items[-1]
