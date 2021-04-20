import sys

with open(sys.argv[1], 'r') as source:
    with open(sys.argv[2], 'w') as destination:
        destination.write(source.read())
print('done!')