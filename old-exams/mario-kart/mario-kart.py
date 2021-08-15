results = {}
points = RACERS = 100
TOPN = 10
with open('input.txt') as input:
    for line in input:
        racer = line.strip()
        if racer not in results:
            results[racer] = 0
        results[racer] = results[racer] + points
        points = points-1
        if points == 0:
            points = RACERS
top = sorted(results.items(), key=lambda p : p[1], reverse=True)[0:TOPN]
for name, p in top:
    print(name)
