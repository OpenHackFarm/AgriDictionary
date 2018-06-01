import json

f = open('location.json')
data = json.load(f)

for city, locations in data.items():
    for l in locations:
        print(l)
