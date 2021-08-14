with open('input.txt') as input:
    for line in input:
        names = line.strip().lower().split(" ")
        fname = names[0]
        lname = "".join(names[1:])
        print(f'{fname}.{lname}@student.ucll.be')
#9a4c998399b19d6a7f2c