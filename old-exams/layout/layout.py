import re

data = []
with open('input.txt') as input:
    for line in input:
        #Using regex groups to split the string into the desired parts
        match = re.fullmatch(r'(.*) (\d+\.\d+\.\d+\.\d+) (.*)', line.strip())
        name = match.group(1)
        ip = match.group(2)
        country = match.group(3)
        data.append((name, ip, country))

widths = [max(len(row[i]) for row in data) for i in range(3) ]

for name, ip, country in data:
    print(f'{name.rjust(widths[0])} {ip.ljust(widths[1])} {country}')
#a832145eddb28017714de705cc
        