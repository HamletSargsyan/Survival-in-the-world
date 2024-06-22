from enum import Enum, auto
from uuid import uuid4


class GameObjectType(Enum):
    ITEM = auto()
    ITEM_GROUP = auto()
    STORAGE = auto()
    NPC = auto()
    PLAYER = auto()


class GameObject:
    def __init__(self, type: GameObjectType) -> None:
        self.id = uuid4()
        self.type = type

    def check(self):
        pass
