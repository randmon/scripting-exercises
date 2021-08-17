import re

with open('input.txt') as input:
    i = 1
    for line in input:
        matches = re.findall(r'\d\d:\d\d:\d\d', line)
        for m in matches:
            if not re.fullmatch(r'([0-1]\d|2[0-3]):[0-5]\d:[0-5]\d', m):
                print(f'{i} {m}')
        i += 1
#1d74f9361b2ed0aa2b1c