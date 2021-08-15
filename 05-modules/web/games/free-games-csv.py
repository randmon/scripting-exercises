from urllib.request import urlopen
import json
import csv

url = "https://www.freetogame.com/api/games"
with urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))

with open('output.csv', 'w', encoding='utf-8', newline="") as output:
    csv_writer = csv.writer(output)

    header = 0
    for game in data:
        if header == 0:
            #Write title of columns
            keys = list(game.keys())
            titles = keys[0:2] + keys[3:4] + keys[5:7]
            csv_writer.writerow(titles)
            header += 1
        #Write game values
        values = list(game.values())
        game_values = values[0:2] + values[3:4] + values[5:7]
        game_values[2] = game_values[2].replace("\n", "").replace("\r", "")
            
        csv_writer.writerow(game_values)