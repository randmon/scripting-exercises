with open('input.txt') as input:
    for line in input:
        print(str(bin(int(line)))[2:])
#f779b297d35ced234615