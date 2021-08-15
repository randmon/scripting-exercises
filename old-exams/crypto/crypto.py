import json

with open('input.json') as input:
    data = json.load(input)
for coin in data:
    print(coin['currency'], min(coin['history']), max(coin['history']), coin['history'][-1])
#1f898674f4d633ad5a040ed156