import csv
top = 100

def second(xs):
    return xs[1]

results = {}

with open('../title-episodes.tsv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        id = row['parentTconst']
        if id not in results:
            results[id] = 0
        results[id] += 1

sorted = sorted(results.items(), key=lambda item:item[1], reverse=True)
topN = sorted[:top]

with open('../title-basics.tsv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    titles =  {row['tconst'] : row['primaryTitle'] for row in reader}

for episode, amount in topN:
    if episode in titles:
        print(f'{str(amount).rjust(5)} - {titles[episode]}')