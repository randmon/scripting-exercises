import csv
top = 100

def runtime(row):
    time = row['runtimeMinutes']
    try:
        return int(time)
    except:
        return 0

def second(xs):
    return xs[1]

with open("../title-basics.tsv", encoding='utf-8') as file:
# with open("test.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    results = [ (row['originalTitle'], runtime(row)) for row in reader if row['runtimeMinutes'] != r'\N' ]

results.sort(key=second, reverse=True)
topN = results[:top]

for title, seconds in topN:
    print(f'{str(seconds).rjust(6)} - {title}')