# Create,Modify,Remove Set
myset = {1,2,3,4,5}
myset1 = {'hi', 5.2, (1,2,2)}
print(type(myset))
print(myset1)
myset1.discard(5.2)
print(myset1)
myset1.clear()
print(myset1)
myset.update([4],(5,6,7,))
print(myset)

# Set Operation

a = {1,2,3,4,5}
b = {4,5,6,7,8}

# Union
print(a|b)
a.union(b)
b.union(a)

# Difference
print(a-b)
print(a.difference(b))
print(b-a)
print(b.difference(a))

# Intersection
print(a&b)
print(a.intersection(b))
print(b.intersection(a))

# Symmetric Difference
print(a^b)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# Membership Test
name = set('mango')
print('m' in name)
print('s' in name)

# Iteration

for letter in set('set'):
    print(letter)

# built in functions

items = ['python','sql', 'html']
n = enumerate(items)
print(list(n))
print(max(items))
print(min(items))
print(len(items))
print(sorted(items))
print(sorted(items,reverse=True))

# Methods in set

c = {1,2,3,4,5}
d = {1,2,3,4,5,6,7}
e = {8,9}
print(c.isdisjoint(e))
print(c.issubset(d))
print(e.issuperset(a))

# Frozenset

ab = ('s', 'e', 't')
print(frozenset(ab))

ba = {'name': 'sha', 'age': 23}
print(frozenset(ba))




