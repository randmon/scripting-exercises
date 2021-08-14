import csv
import sys

# Find series id
series_name = sys.argv[1]
with open("../title-basics.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    rows = [ row for row in reader if row['originalTitle'].lower() == series_name.lower() and row['titleType'] == 'tvSeries' ]
# Stop if there we found zero or multiple series with the same name
if len(rows) != 1:
    print(f"Found {len(rows)} matches")
    sys.exit(-1)
row = rows[0]
series_id = row['tconst']
episode_data = {}

# Find episodes
with open('../title-episodes.tsv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        if row['parentTconst'] == series_id:
            episode_data[row['tconst']] = {'S' : int(row['seasonNumber']), 'E' : int(row['episodeNumber'])}

# Ratings
with open('../title-ratings.tsv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        if row['tconst'] in episode_data:
            episode_data[row['tconst']]['rating'] = float(row['averageRating'])

# Titles of episodes
with open("../title-basics.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        if row['tconst'] in episode_data:
            episode_data[row['tconst']]['title'] = row['originalTitle']

#Sort and print
# for data in sorted(episode_data.values(), key=lambda data:data['rating'], reverse=True):
#     print(f"S{str(data['S']).rjust(2,'0')}E{str(data['E']).rjust(2,'0')} {data['title'].ljust(40, ' ')} {data['rating']}")

for data in episode_data.values():
    print(data)