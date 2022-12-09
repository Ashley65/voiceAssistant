from dataclasses import dataclass

import geocoder
from pyowm import OWM

from core import ai


class weatherAbility():
    key = "bac1e0425a5ef563f3ecf6a43b702c46"

    def __init__(self):
        self.owm = OWM(self.key)
        self.mgr = self.owm.weather_manager()
        loc = geocoder.ip("me")
        self.lat = loc.lat
        self.lng = loc.lng

    @property
    def weather(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.lng)
        return forecast

    def forecast(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.lng)


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
