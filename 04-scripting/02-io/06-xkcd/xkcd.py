import sys
import requests
import json
from PIL import Image
import requests

url = 'http://xkcd.com/'
args = sys.argv
if (len(args) > 1):
    url = url + sys.argv[1] + '/'
url = url + "info.0.json"

response = requests.get(url)
loaded = json.loads(response.text)
for key in loaded:
    print(f'{key}: {loaded[key]}')

Image.open(requests.get(loaded['img'], stream=True).raw).show()