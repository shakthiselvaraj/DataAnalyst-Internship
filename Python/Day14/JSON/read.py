import json

with open('school.json') as file:
    data = json.load(file)

for i in data['school']:
    print(i)
    print(i['grade'])
    print(i['name'], i['grade'])
