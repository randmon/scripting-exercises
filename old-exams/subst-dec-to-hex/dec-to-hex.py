import re

def toHex(dec):
    return f"0x{int(dec.group(1)):X}"

with open('input.txt') as input:
    for line in input:
        conv = re.sub(r'\$HEX\((\d+)\)', toHex, line.strip())
        print(conv)
#db12a454d29ed0235af8