from core.game_object import GameObject, GameObjectType
from core.item import Item
from utils import format_list


class Storage(GameObject):
    def __init__(
        self, name: str, items: list[Item] = [], max_slots_count: int = 1
    ) -> None:
        super().__init__(type=GameObjectType.STORAGE)

        self.name = name
        self.items = items
        self.max_slots_count = max_slots_count

    def _format(self, items: list[Item]):
        return format_list(
            [f"{item.name} {item.quantity}" for item in items],
            int(10),
        )

    def format(self):
        return self._format(self.items)

    def check(self):
        if len(self.items) > self.max_slots_count:
            self.items[: self.max_slots_count]

            # TODO: добавить сообщение
