from pathlib import Path
import argparse
import os
import re

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('path', default='.')
args = parser.parse_args()
print(args)
list = os.walk(args.path)
for l in list:
    print(l)


