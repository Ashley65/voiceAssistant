from core import ai
from dataclasses import dataclass
import factory
import datetime
import time


class timerAbility:
    def __init__(self):
        self.time = time.time()
        self.time = datetime.datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M:%S')

    def getTime(self):
        return self.time

    @property
    def time(self):
        return self.time

    @time.setter
    def time(self, value):
        self._time = value


@dataclass
class timer:
    name = 'timer'

    @staticmethod
    def command(self, command: str):
        return ['what time is it', 'what is the time', 'what time is it now', 'tell me the time',
                'what is the time now']

    @staticmethod
    def handleCommand(command: str, core: ai):
        timer = timerAbility()
        core.say(timer.getTime())
        return timer.getTime()


def initialise():
    factory.register('timer', timer)
