import json

def rounded_average(grades):
    return round(sum(grades) / len(grades))

result = {} # {student : average}

with open('input.json') as input:
    data = json.loads(input.read())
    for student in data:
        result[student['id']] = rounded_average((student['grades']))

sorted_by_id = sorted(result.items())
for id, grade in sorted_by_id:
    print(f'{id} {grade}')
#056cb9c4d20f9ab30e78