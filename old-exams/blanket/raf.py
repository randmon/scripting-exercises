import json
from datetime import datetime

def getDate(item):
    return datetime.strptime(item[0], '%d/%m/%Y')

with open('input.txt', 'r') as file:
    contents = json.loads(file.read())
    contents = dict(sorted(contents.items(), key=getDate))

with open('output.txt', 'w') as output:
    for date in contents:
        mean = round(sum(contents[date]) / len(contents[date]))
        output.write(f'{mean}\n')