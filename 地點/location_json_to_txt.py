import json

f = open('locations.json')
data = json.load(f)

for city, locations in data.items():
    for l in locations:
        print(l)
