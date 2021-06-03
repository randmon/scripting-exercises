import argparse
from pathlib import Path
from PIL import Image
import re
import sys

def output_name(pattern, input):
    path = Path(input)
    return pattern.replace('%b', path.stem).replace('.%x', path.suffix)

def parse_size(string):
    match = re.fullmatch(r'(\d+)x(\d+)', string)

    if not match:
        print('Invalid size --- should have format WxH')
        sys.exit(-1)

    width, height = match.groups()
    return (int(width), int(height))

parser = argparse.ArgumentParser(prog='thumbnails')
parser.add_argument('file', nargs='+')
parser.add_argument('--size', default='64x64')
parser.add_argument('--pattern', default='%b-thumbnail.%x')

args = parser.parse_args()
# print(args)

size = parse_size(args.size)

for input_file in args.file:
    image = Image.open(input_file)
    image.thumbnail(size)
    image.save(output_name(args.pattern, input_file))