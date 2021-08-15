from urllib.request import urlopen
import json
import textwrap

url = "https://www.themealdb.com/api/json/v1/1/random.php"
with urlopen(url) as r:
    data = json.loads(r.read().decode('utf-8'))['meals'][0]
print(data['strMeal'].center(100))
print(f"{data['strCategory'].center(50)}{data['strArea'].center(50)}\n")

for i in range(1,21):
    if data[f"strIngredient{i}"] != '':
        print(f'{data["strMeasure"+str(i)].strip()} {data["strIngredient"+str(i)]}')
    else:
        break
print()
print("\n".join(textwrap.wrap(data['strInstructions'], 100)))