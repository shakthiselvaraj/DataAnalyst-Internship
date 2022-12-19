# Dictionary accessing,changing,adding,test
a = {'name': 'python', 'book': 23}
print(a['name'])
print(a['book'])
a['age'] = 24
a['year'] = 1999
print(a)
print('age' in a)


#Iteration

b = {1:1, 2:3, 3:5, 4:7}
for i in b:
    print(b[i])

# Methods in Dictionary

c =  {'a', 'e', 'i', 'o', 'u' }
num = 1
d = dict.fromkeys(c,num)
print(d)
m = {'Physics':67, 'Maths':87}
print(m.get('Maths'))
print(m.items())
print(m.keys())
print(m.values())
n = {'English':99}
m.update(n)
print(m)
