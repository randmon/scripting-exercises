import sys
import json
from urllib.request import urlopen

url = "https://api.genderize.io/?name="+sys.argv[1]

def download(url):
    with urlopen(url) as response:
        return json.loads(response.read().decode('utf-8'))

data = download(url)
print(f"{data['gender']} ({int(data['probability']*100)}%)")