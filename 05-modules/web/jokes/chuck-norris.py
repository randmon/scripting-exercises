from urllib.request import urlopen
import json
from html import unescape

url = "http://api.icndb.com/jokes/random"
with urlopen(url) as r:
    joke = json.loads(r.read().decode('utf-8'))['value']
    
#unescape turns HTML escaped into ascii decoded characters
print(f"[{joke['id']}] {unescape(joke['joke'])}")