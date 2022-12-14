import json
import requests

#Using Parameters

p = { 'ids': 1}

url = 'https://api.punkapi.com/v2/beers'
r = requests.get(url, params=p)

#d = json.loads(r.text)
#print(d)

print(json.dumps(r.json(), indent=4))

print(r.json()[0])

