filename = input('Filename:')


f = open(filename, 'r')
data = f.read()
f.close()


new = '[!@#$%-,.]@!'

for x in new:
    if x in data:
        data = data.replace(x, '')

count = {}

for x in data.split():

    if x in count:
        count[x] = count[x] + 1
    else:
        count[x] = 1
for key, value in count.items():
    print(key, ':',  value)



