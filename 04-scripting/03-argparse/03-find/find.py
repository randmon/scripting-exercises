from pathlib import Path
import argparse
import os
import re

def minimum_size(size):
    def check(filename):
        return os.path.getsize(filename) >= size

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('path', default='.')
args = parser.parse_args()
print(args)

path = Path(args.path)
for entry in path.glob('**/*'):
    yes = entry
    # if not os.path.getsize(entry) > args.minimum_size:
    #     continue

    # if args.contains:
    #         if not os.path.isfile(entry):
    #             continue

    #         with open(entry, 'r') as file:
    #             contents = file.read()

    #             if not re.search(args.contains, contents):
    #                 continue
    print(entry)