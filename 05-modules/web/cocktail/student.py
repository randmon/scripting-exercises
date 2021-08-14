import sys
from urllib.request import urlopen
import json

cocktail = " ".join(sys.argv[1:])
if cocktail:
    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + cocktail.replace(' ', '%20')
else:
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    
with urlopen(url) as res:
    data = json.loads(res.read().decode('utf-8'))['drinks'][0]
    print(data['strDrink'])
    for i in range(1,16):
        s = str(i)
        if data['strIngredient'+s] is not None: #check if ingredient is not null
            print("- " + data['strMeasure'+s].strip(), data['strIngredient'+s])
        else:
            break