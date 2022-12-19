import json

with open('school.json') as file:
    data = json.load(file)

with open('ex.json', 'w') as f:
    json.dump(data, f, indent=4)
