from urllib.request import urlopen
import json
import argparse
from datetime import datetime
import pycountry

parser = argparse.ArgumentParser()
parser.add_argument('country', nargs='?')
args = parser.parse_args()

if args.country:
    country = pycountry.countries.search_fuzzy(args.country)[0]
    url = "https://date.nager.at/api/v3/publicholidays/2021/" + country.alpha_2
else:
    country = pycountry.countries.get(alpha_2='BE')
    url = "https://date.nager.at/api/v3/publicholidays/2021/BE"

with urlopen(url) as r:
    data = json.loads(r.read().decode('utf-8'))

print(f"Holidays for {country.name} 2021")

for h in data:
    date = datetime.strptime(h['date'], '%Y-%m-%d')
    date = datetime.strftime(date, '%d/%m')
    print(f"{date} - {h['localName']}")

