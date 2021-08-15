import urllib.request
import json

url = "https://api.tronalddump.io/random/quote"

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = json.loads(opener.open(url).read().decode('utf-8'))
print("\n")
print(f"{response['value']}")
print("\t- Donald Trump")


