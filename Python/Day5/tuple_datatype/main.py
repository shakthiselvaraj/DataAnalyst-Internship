# Tuple indexing,negative indexing,slicing,test,reassigned,mutable change
a = ('python', 'sql', 'java')
print(a[2])
b = ('python', [2,4,5], (1, 2, 3))
print(b[0][1])
print(b[1])
print(b[-1])
print(b[0:2])
print(b[:-2])
b[1][2]=6
print(b)
a = ('complete',)
print(a)
print(type(a))
print('python' in a)
print('complete' in a)

# Methods in Tuple

c = ('p','r','o','g','r','a','m')
d = c.count('r')
e = c.index('m')
print(d)
print(e)




