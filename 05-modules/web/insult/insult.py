from urllib.request import urlopen
from html import unescape

with urlopen("https://evilinsult.com/generate_insult.php") as r:
    print(unescape(r.read().decode('utf-8')))