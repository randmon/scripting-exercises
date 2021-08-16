import csv
import json
import sys

with open(sys.argv[1]) as input:
    with open(sys.argv[2], "w") as output:
        data = list(csv.DictReader(input))
        output.write(json.dumps(data))