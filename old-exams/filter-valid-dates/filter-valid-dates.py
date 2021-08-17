from datetime import datetime

format = "%d-%m-%Y"

with open('input.txt') as input:
    for line in input:
        try:
            datetime.strptime(line.strip(), format)
            print(line.strip())
        except:
            continue
#d8b9b7758a1800911d4a