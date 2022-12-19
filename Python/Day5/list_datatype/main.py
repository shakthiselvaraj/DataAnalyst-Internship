# List indexing,negative indexing,slicing,test
a = ['list', 13, 155.65]
print(a[1])
print(a[0][0])
print(a[-3])
print(a[0:2])
print(a[:])
print(a[:-2])
print(a)
print('list' in a)

# Add,change,insert,pop,del,clear

b = [1,2,5,7]
b[0:4] = [1,3,5,7]
print(b)
b.insert(7,9)
print(b)
del b[4]
print(b)
del b[0:2]
print(b)
b.pop()
print(b)
b.clear()
print(b)

# List Iterations

for name in ['list' , 'hi']:
    print('hi', name)


# List Comprehension

c = [2**x for x in range(3)]
print(c)

# Methods in List

name = ['s','h','a','k','t','h','i']
s = name.count('h')
d = name.index('a')
name.sort()
print(s)
print(d)
print(name)
name.reverse()
print(name)






