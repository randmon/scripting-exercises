from urllib.request import urlopen
import json

url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
with urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))
    print(data[0]['fact'])