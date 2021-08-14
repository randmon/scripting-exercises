import csv

result = {}

with open('exam-schedule.csv') as file:
    data = csv.DictReader(file)
    for row in data:
        lokaal = row['Lokaal'].strip()
        tijd = row['Datum'].strip() + " " + row['Dagdeel'].strip()
        if lokaal not in result:
            result[lokaal] = {tijd:0}
        elif tijd not in result[lokaal]:
            result[lokaal][tijd] = 0
        result[lokaal][tijd] = result[lokaal][tijd]+1

locations = sorted(result.keys())
for location in locations:
    table = result[location]
    cap = max(table.values())
    print(f'{location} {cap}')

#a0481b59e624c319a9f8