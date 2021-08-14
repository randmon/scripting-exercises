with open('input.txt') as input:
    with open('output.txt', 'w') as output:
        for line in input:
            name, data = line.strip().split(':')
            points, tekens = data.split(' ')
            cashed, earned = map(int, points.split('/'))

            earned += tekens.count('+')
            cashed += tekens.count('-')

            output.write(f"{name}:{cashed}/{earned}\n")