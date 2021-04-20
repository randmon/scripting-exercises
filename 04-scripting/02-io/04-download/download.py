import sys
import requests

response = requests.get(sys.argv[1])

with open("html", 'w', encoding="utf-8") as output:
    output.write(response.text)
    #print(response.text)
