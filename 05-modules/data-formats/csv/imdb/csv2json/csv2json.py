import csv
import json
import sys
# must be ran like example:
# py csv2json.py < test.csv > test.json

data = list(csv.DictReader(sys.stdin))
print(json.dumps(data))