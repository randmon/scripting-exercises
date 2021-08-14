with open('input.txt') as input:
    for line in input:
        if line[0].lower() == 'u':
            print(f'{line.strip().lower()}@ucll.be')
        else:
            print(f'{line.strip().lower()}@student.ucll.be')
#5f4a6053e415a6dc6e7b