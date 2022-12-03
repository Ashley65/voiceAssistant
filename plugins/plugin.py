from typing import Protocol
from core import ai


class plugin(Protocol):
    def handleCommand(self, command: str, core: ai):
        pass

    def register(self):
        """"""
