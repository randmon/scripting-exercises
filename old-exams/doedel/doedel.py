import csv
from collections import Counter

counts = Counter()

with open('input.csv') as input:
    reader = csv.DictReader(input)
    for line in reader:
        for key in line.keys():
            if key != 'name' and line[key] == 'yes':
                counts[key] += 1
sorted_dates = sorted(counts.items(), key=lambda p : p[1], reverse=True)
for date, yesses in sorted_dates:
    print(f'{date} {yesses}')

#a99d6ed1dd78f8d652cf968a4c