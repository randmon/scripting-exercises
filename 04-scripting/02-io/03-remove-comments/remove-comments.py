import sys
import re

files = sys.argv[1:]
for f in files:
    with open(f, 'r') as file:
        inhoud = file.readlines()
    for s in range(len(inhoud)):
        inhoud[s] = re.sub('#.*', '', inhoud[s])
    with open(f, 'w') as output:
        output.write(''.join(inhoud))
