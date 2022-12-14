import json

person = '{"name": "Bob", "languages": ["English", "French"], "intrest": ["Singing", "Dancing"]}'

# covert JSON into dir

data = json.loads(person)
print(data)
print(data['name'])


#Convert dir into JSON

new = json.dumps(data, indent=4)
print(new)

