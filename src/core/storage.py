from core.item import Item


class Storage:
    def __init__(self, items: list[Item]) -> None:
        self.items = items
