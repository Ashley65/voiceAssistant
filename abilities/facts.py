from core import ai
from dataclasses import dataclass
import factory
import randfacts


class factAbility:
    def __init__(self):
        self.facts = randfacts.getFact()

    def getFact(self):
        return self.facts

    @property
    def fact(self):
        return self.facts


@dataclass
class facts:
    name = 'facts'

    # This is the function that will be called when the user says "tell me a fact"
    @staticmethod
    def command(self, command: str):
        return ['tell me a fact', 'tell me something interesting', 'tell me something', 'tell me something interesting']

    @staticmethod
    def handleCommand(command: str, core: ai):
        fact = factAbility()
        core.say(fact.getFact())
        return fact.getFact()


def initialise():
    factory.register('fact',facts)
