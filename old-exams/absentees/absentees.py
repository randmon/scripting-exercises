with open ('attending.txt') as input:
    att = set(line.strip().lower() for line in input)

with open ('all.txt') as all:
    for line in all:
        line = line.strip().lower()
        if line not in att:
            print(line)
# bab69d94f5191cbcb836
