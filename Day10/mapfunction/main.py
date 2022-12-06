# map function

# Before Map Function

a = [2,4,6,8,10]
s = []
square = lambda n : n**2
for i in a:
    s.append(square(i))
print('Square of the number before map function;', s)

# map without lambda

p = ['sql', 'python']
u = map(str.upper, p)
print(list(u))

# After Map Function

b = [2,4,6,8]
s = map(lambda  n : n**2, b)
print('After Map Function:', list(s))


