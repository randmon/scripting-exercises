import csv

students = {}

with open('../exam-schedule.csv') as input:
    data = csv.DictReader(input)
    for s in data:
        id = s['Student ID']
        students[id] = students.get(id, 0) + 1

sorted_students = sorted(students.items(), key=lambda p : p[1], reverse=True)
for id, aantal in sorted_students[:1]:
    print(f"{id} : {aantal}")