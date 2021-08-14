from urllib.request import urlopen
import json

with urlopen('https://www.boredapi.com/api/activity') as response:
    data = json.loads(response.read().decode('utf-8'))

print(f"[{data['type'].title()}] {data['activity']}\n- {data['participants']} participant(s)\n- {data['price']} €")