from urllib.request import urlopen
import textwrap
import json

url = "https://animechan.vercel.app/api/random"
with urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))
    quote = '\n'.join(textwrap.wrap(data['quote'], 60))
    print(f"\n{quote}\n\t-{data['character']}, {data['anime']}")