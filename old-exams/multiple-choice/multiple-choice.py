with open('solutions.csv') as s:
    solutions = s.read().strip().split(',')
# print(solutions)

with open('answers.csv') as a:
    for line in a:
        count = 0
        list = line.strip().split(',')
        for i, j in zip(list[1:], solutions):
            if i == j:
                count += 1
        print(f"{list[0]} {count}")
#f39f10d400cb2fc025a5