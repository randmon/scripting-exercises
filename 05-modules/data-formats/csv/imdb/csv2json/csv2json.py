import csv
import json

data = {}
with open('test.csv') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
                id = row['fname'] + ' ' + row['lname']
        data[id] = row

with open('test.json', 'w') as jsonf:
        jsonf.write(json.dumps(data))

print(data)