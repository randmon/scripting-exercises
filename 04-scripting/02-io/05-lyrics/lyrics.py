import sys
import requests
import json
import re

def replace_spaces(string):
    return re.sub(' ', '%20', string)

artist = replace_spaces(sys.argv[1])
title = replace_spaces(sys.argv[2])

response = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{title}")
print(json.loads(response.text)["lyrics"])
result = json.loads(response.text)
if ("lyrics" in result):
    print(result["lyrics"])
else:
    print(result["error"])