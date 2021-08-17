import csv

students = {} # student : [exams]
victims = []

with open("../exam-schedule.csv") as input:
# with open("test.csv") as input:
    data = csv.DictReader(input)
    for s in data:
        id = s['Student ID']
        if id not in students:
            students[id] = []
        students[id].append(s['Datum']+s['Dagdeel'])

for s in students:
    if len(set(students[s])) != len(students[s]):
        victims.append(s)
print(victims)