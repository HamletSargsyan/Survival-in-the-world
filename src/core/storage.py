from core.item import Item
from utils import format_list


class Storage:
    def __init__(self, name: str, items: list[Item], max_slots_count: int = 1) -> None:
        self.name = name
        self.items = items
        self.max_slots_count = max_slots_count

    def format(self):
        return format_list(
            [f"{item.name} {item.quantity}" for item in self.items],
            int(self.max_slots_count / 2),
        )
