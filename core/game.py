from typing import Callable


__all__ = ["Game"]


class Game:
    def __init__(self) -> None:
        self.triggers = {}

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
