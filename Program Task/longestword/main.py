filename = input('Filename:')
f = open(filename, 'r')
data = f.read()
f.close()
new = '[!@#$%-,.]@!'

for x in new:
    if x in data:
        data = data.replace(x, '')

max = 0
for i in data.split():
    if (len(i)>max):
        max = len(i)
        word = i
print(word)