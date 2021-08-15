from urllib.request import urlopen
import json
import sys
import re

arg = sys.argv[1]
search_term = re.sub(' ', '%20', arg)

search_url = "https://api.jikan.moe/v3/search/anime?q=" + search_term
with urlopen(search_url) as r:
    results = json.loads(r.read().decode('utf-8'))
    id = results['results'][0]['mal_id']
    print(f'"{arg}" - Found anime with id: {id}')

anime_url = f"https://api.jikan.moe/v3/anime/{id}"
with urlopen(anime_url) as r:
    data = json.loads(r.read().decode('utf-8'))

    year = str(data['aired']['prop']['from']['year'])
    if data['aired']['prop']['to']['year'] is not None:
        year += f" - {data['aired']['prop']['to']['year']}"

    print(f"{data['title']} ({year}) - {data['title_japanese']}")
    print(f"Score: {data['score']}")
    print(f"Rating: {data['rating']}")
    print(f"Episodes: {data['episodes']}")
    print(f"Synopsis: {data['synopsis']}")