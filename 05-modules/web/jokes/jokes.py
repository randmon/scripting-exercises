import json
from urllib.request import urlopen

url = "https://v2.jokeapi.dev/joke/Any"

with urlopen(url) as res:
    data = json.loads(res.read().decode('utf-8'))

if "joke" in data:
    print(data['joke'])
else:
    print(data['setup'])
    print(data['delivery'].upper())