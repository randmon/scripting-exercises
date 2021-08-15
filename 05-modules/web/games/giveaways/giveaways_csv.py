from urllib.request import urlopen
import json
import csv

url = "https://www.gamerpower.com/api/giveaways"
with urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))

with open('output.csv', 'w', encoding='utf-8', newline="") as output:
    csv_writer = csv.writer(output)

    header = 0
    for game in data:
        if header == 0:
            #Write title of columns
            keys = list(game.keys())
            titles = keys[1:3] + keys[7:8] + keys[9:10]
            csv_writer.writerow(titles)
            header += 1
        #Write game values
        values = list(game.values())
        game_values = values[1:3] + values[7:8] + values[9:10]
            
        csv_writer.writerow(game_values)