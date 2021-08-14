import sys
import re
import argparse

parser = argparse.ArgumentParser(prog='loc')
parser.add_argument('-e' '--count-empty-lines', dest='count_empty_lines', action='store_true')
parser.add_argument('--comment')

args = parser.parse_args()
skip_regexes = []

if not args.count_empty_lines:
    skip_regexes.append(r'^\s*$')

if args.comment:
    skip_regexes.append(f'^\\s*{args.comment}')

count = 0
for line in sys.stdin:
    if not any(re.match(r, line) for r in skip_regexes):
        count+=1

print(count)