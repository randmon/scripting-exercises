import json
from urllib.request import urlopen
import sys
import pycountry

name = sys.argv[1]
url = "https://api.nationalize.io/?name="+name

with urlopen(url) as res:
    data = json.loads(res.read().decode('utf-8'))
for c in data['country']:
    print(f"{pycountry.countries.lookup(c['country_id']).name} ({int(c['probability']*100)}%)")