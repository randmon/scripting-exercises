import re

with open('input.txt') as file:
    for line in file:
        if re.fullmatch(r'(0|\+32-)4[56789]\d-\d{2}-\d{2}-\d{2}', line.strip()):
            print(line.strip())
#7a14b37bd5968661866d