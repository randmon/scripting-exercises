import csv

lectoren = {}

with open('exam-schedule.csv') as file:
    data = csv.DictReader(file)
    for line in data:
        if line['Ex. Soortx'] == 'S':
            for lector in line['Lector'].split('/'):
                lectoren[lector] = lectoren.get(lector, 0) + 1

result = sorted(lectoren.keys())
for r in result:
    print(f"{r} {lectoren[r]}")

#4409ec1118a92a16e508