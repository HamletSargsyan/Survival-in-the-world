from core.game_object import GameObject, GameObjectType
from core.inventory import Inventory
from utils import calc_xp_for_level


class Player(GameObject):
    def __init__(
        self,
        name: str = "Игрок",
    ) -> None:
        super().__init__(type=GameObjectType.PLAYER)

        self.name = name
        self.health = 100
        self.hunger = 0
        self.fatigue = 0
        self.thist = 0
        self.level = 1
        self.xp = 0
        self.max_xp = calc_xp_for_level(self.level)
        self.inventory = Inventory()

    def levelup(self):
        if self.xp > self.max_xp:
            self.xp = self.xp - self.max_xp
        else:
            self.xp = 0

        self.level += 1
        self.xp += calc_xp_for_level(self.level)

        # TODO: Добавить сообщение

    def die(self):
        raise NotImplementedError

    def check(self):
        if self.xp > self.max_xp:
            self.levelup()
