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
        current = forecast.current
        # Getting the hourly forecast
        hourly = forecast.forecast_hourly
        # Getting the daily forecast
        daily = forecast.forecast_daily

        # Getting the current weather
        currentWeather = current.weather_code
        # Getting the current temperature
        currentTemp = current.temperature("celsius")["temp"]
        # Getting the current humidity
        currentHumidity = current.humidity

        # Getting the hourly forecast
        hourlyWeather = hourly[0].weather_code
        hourlyTemp = hourly[0].temperature("celsius")["temp"]
        hourlyHumidity = hourly[0].humidity

        # Getting the daily forecast
        dailyWeather = daily[0].weather_code
        dailyTemp = daily[0].temperature("celsius")["temp"]
        dailyHumidity = daily[0].humidity

        return currentWeather, currentTemp, currentHumidity, hourlyWeather, hourlyTemp, hourlyHumidity, dailyWeather, dailyTemp, dailyHumidity




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
        core.say(forecast)
        return weatherAbility.forecast


def initialise():
    factory.register('weather', weather)
