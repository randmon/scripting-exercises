import csv
dates = {} # date : count

with open('input.csv') as input:
    data = list(csv.DictReader(input))
    headers = 0
    for line in data:
        if headers == 0:
            for date in line:
                if date != "name":
                    dates[date] = 0
            headers += 1
        for date in line:
            if line[date] == "yes":
                dates[date] += 1
sorted_dates = sorted(dates.items(), key=lambda d : d[1], reverse=True)
for e in sorted_dates:
    print(f'{e[0]} {e[1]}')
