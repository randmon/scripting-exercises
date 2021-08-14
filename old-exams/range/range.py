#give range in command parameter
import sys

r = int(sys.argv[1])
with open('output.txt', 'w') as output:
    for i in range(1, r+1):
        output.write(f'{i}\n')
#a83d637d4e83dc5eaf5c