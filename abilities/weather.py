from dataclasses import dataclass

import geocoder
from pyowm import OWM
import factory
from core import ai


class weatherAbility:
    key = "bac1e0425a5ef563f3ecf6a43b702c46"

    def __init__(self):
        self.owm = OWM(self.key)
        self.mgr = self.owm.weather_manager()
        # This section of code will use the user IP addresses to find their location in the world
        loc = geocoder.ip("me")
        self.lat = loc.lat
        self.lng = loc.lng

    # The OneCall Api will get the current weather, hourly forecast for the next 48 hours and the daily forecast #
    # for the next seven days in one call
    @property
    def weather(self):
        return self.mgr.one_call(lat=self.lat, lon=self.lng)

    def forecast(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.lng)
        # Getting the current weather




@dataclass
class weather:
    name = 'weather'

    @staticmethod
    def command(command: str):
        return ['weather', 'forecast', 'what is the weather like', 'give me the forecast', "what's the weather",
                "what's the weather like"]

    @staticmethod
    def handleCommand(command: str, core: ai):
        forecast = weatherAbility.weather
        ai.say(forecast)
        return weatherAbility.forecast


def initialise():
    factory.register('weather', weather)
