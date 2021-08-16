from os import waitpid
import sys
import json
from urllib.request import urlopen
import argparse

def search_city(city):
    with urlopen("https://www.metaweather.com/api/location/search/?query="+city.replace(' ', '%20')) as r:
        search_results = json.loads(r.read())[0]
    # print(search_results)
    return [search_results['title'], search_results['woeid']]

parser = argparse.ArgumentParser()
parser.add_argument('city', nargs='?')
args = parser.parse_args()

if args.city:
    city, id = search_city(args.city)
    url = f"https://www.metaweather.com/api/location/{id}/"
else:
    city = "Brussels"
    url = "https://www.metaweather.com/api/location/968019/"

with urlopen(url) as r:
    data = json.loads(r.read())

print()
weather = data['consolidated_weather'][0]
print(f"Weather forecast for {weather['applicable_date']}, {city}")
print(f"Min: {int(weather['min_temp'])}°C  Max: {int(weather['max_temp'])}°C")
print(f"Weather: {weather['weather_state_name']}")

print()
weather = data['consolidated_weather'][1]
print(f"Weather forecast for {weather['applicable_date']}, {city}")
print(f"Min: {int(weather['min_temp'])}°C  Max: {int(weather['max_temp'])}°C")
print(f"Weather: {weather['weather_state_name']}")

print()
weather = data['consolidated_weather'][2]
print(f"Weather forecast for {weather['applicable_date']}, {city}")
print(f"Min: {int(weather['min_temp'])}°C  Max: {int(weather['max_temp'])}°C")
print(f"Weather: {weather['weather_state_name']}")
