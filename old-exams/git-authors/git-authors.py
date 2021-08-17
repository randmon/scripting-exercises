import re

authors = set()

with open('input.txt') as input:
    for line in input:
        match = re.search(r'Author: (.+) <', line)
        if match:
            authors.add(match.group(1))

for a in sorted(authors):
    print(a)
#999c0139b6096a16bb89