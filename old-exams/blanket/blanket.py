import json
from datetime import datetime
from statistics import mean

with open('input.txt') as file:
    data = [ (datetime.strptime(date, '%d/%m/%Y'), temps) for date, temps in json.load(file).items()]

for _, temps in sorted(data, key=lambda e: e[0]):
    print(round(mean(temps)))

# 47c76d37d07158fba97d