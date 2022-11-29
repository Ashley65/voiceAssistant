from typing import Protocol
from core import ai


class ability(Protocol):

    def commands(self, command: str):
        """ Return a list of commands that this skill can handle """
        pass

    def handleCommand(self, command: str, core: ai):
        pass
