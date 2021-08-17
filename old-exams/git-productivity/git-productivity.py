import re

authors = {}

with open('input.txt') as input:
    for line in input:
        match = re.search(r'Author: (.+) <', line)
        if match:
            a = match.group(1)
            authors[a] = authors.get(a, 0) +1

sorted_authors = sorted(authors.items(),key=lambda a:a[1], reverse=True)
for a, commits in sorted_authors:
    print(f"{a}: {commits}")
#4e4c0e7578517b56c876