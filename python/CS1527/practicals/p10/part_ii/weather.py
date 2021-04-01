# Use your knowledge of the GoF design patterns to implement a façade that allows the subsystem
# classes in weather.py to be used as follows:
# facade = Facade()
#  print("Temperature: %.2f"% facade.get_forecast('Aberdeen', 'GB'))
# >>> Temperature: 5.23
#
# disclaimer: base code was provided
# Facade class is written by me

import urllib.parse
import urllib.request
import json
from datetime import datetime, timedelta


class Facade:

    def get_forecast(self, city: str, country: str):
        weather_data = WeatherProvider().get_weather_data(city, country)
        data = Parser().parse_weather_data(weather_data)
        weather = Weather(data)
        celsius = Converter().from_kelvin_to_celsius(weather.temperature)
        return celsius


"""
Subsystem for use with OpenWeatherMap to access online weather 
service, parse the resulting data [returned in JSON format] and 
compute average temperature. Converts result to Celsius.
"""


class WeatherProvider:
    def __init__(self):
        self.api_url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}&APPID=69ea10f199003e35cc47ca4f5ec8c8b1'

    def get_weather_data(self, city, country):
        city = urllib.parse.quote(city)
        url = self.api_url.format(city, country)
        return urllib.request.urlopen(url).read()


class Weather:
    def __init__(self, data):
        result = 0
        for r in data:
            result += r
        self.temperature = result / len(data)


class Parser:
    def parse_weather_data(self, weather_data):
        parsed = json.loads(weather_data)
        start_date = None
        result = []
        for data in parsed['list']:
            date = datetime.strptime(data['dt_txt'], '%Y-%m-%d %H:%M:%S')
            start_date = start_date or date
            if start_date.day != date.day:
                return result
            result.append(data['main']['temp'])


class Converter:
    def from_kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15


if __name__ == '__main__':
    facade = Facade()
    print("Temperature: %.2f" % facade.get_forecast('Aberdeen', 'GB'))
