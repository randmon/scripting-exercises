import argparse

parser = argparse.ArgumentParser(prog='range')
parser.add_argument('start', nargs='?', default=0, type=int)
parser.add_argument('end', type=int)
parser.add_argument('-x', '--exclusive', action=argparse.BooleanOptionalAction)
parser.add_argument('--step', type=int, default=1)

args = parser.parse_args()
# print(args)

if (args.exclusive):
    args.end -= 1
for i in range(args.start, args.end+1, args.step):
    print(i)