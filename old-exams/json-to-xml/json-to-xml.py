import json

xml = "<students>"

with open('input.json') as input:
    data = json.load(input)

for student in data:
    xml += f"\n<student id=\"{student['id']}\"><grades>"
    for g in student['grades']:
        xml += f"<grade>{g}</grade>"
    xml += f"</grades></student>"
print(xml+"\n</students>")
#36d9d57afe4553270223