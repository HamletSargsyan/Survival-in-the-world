import os
import shelve
from typing import Callable

from config import Config
from core.player import Player


class Game:
    def __init__(self) -> None:
        self.triggers: dict[str, list[Callable[[], None]]] = {}

        self.load()
        
        self.player: Player

    def trigger(self, trigger_name: str) -> None:
        if trigger_name in self.triggers:
            for event_func in self.triggers[trigger_name]:
                event_func()

    def on(
        self, trigger_name: str
    ) -> Callable[[Callable[[], None]], Callable[[], None]]:
        def decorator(func: Callable[[], None]) -> Callable[[], None]:
            if trigger_name not in self.triggers:
                self.triggers[trigger_name] = []
            self.triggers[trigger_name].append(func)
            return func

        return decorator

    def start(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError

    def save(self):
        with shelve.open(f"{Config.save_path}/{self.player.id}") as data:
            data["game"] = self

    def load(self):
        if not os.listdir(Config.save_path):
            self.create_new_player()
        with shelve.open(f"{Config.save_path}/{self.player.id}") as data:
            self = data["game"]

    def create_new_player(self):
        name = self.prompt("Имя игрока: ")
        if not name:
            name = "Игрок"
        self.player = Player(name)
        self.save()

    def prompt(self, message: str) -> str:
        return input(message)

    def _get_default_prompt_session(self):
        raise NotImplementedError
