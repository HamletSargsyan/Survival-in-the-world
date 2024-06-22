from enum import Enum, auto
from uuid import uuid4


class GameObjectType(Enum):
    ITEM = auto()
    NPC = auto()
    PLAYER = auto()


class GameObject:
    def __init__(self, type: GameObjectType) -> None:
        self.id = uuid4()
        self.type = type
