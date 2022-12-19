# To print Number

# Normal loop
num = [1,2,3,4,5]
a = []
for n in num:
    a.append(n)
print('The Normal function:', a)

# List Comprehension
mylist = [n for n in num]
print('After List Comprehension:', mylist)

# To print multiple of number

# Normal loop
b = []
for n in num:
    b.append(n*n)
print('The Normal function:', b)

# List Comprehension
mylist = [n*n for n in num]
print('After List Comprehension:', mylist)

# To print Even

# Normal loop
c =[]
for n in num:
    if n%2==0:
        c.append(n)
print('the Normal function:', c)

# List Comprehension
mylist = [n for n in num if n%2==0]
print('Afteer List Comprehension:', mylist)


# Nested Loop

# Normal Loop
d =[]
for letter in 'abcd':
    for n in range(4):
        d.append((letter,n))
print('The Normal function:', d)

# List Comprehension
mylist = [(letter,n)for letter in 'abcd' for n in range(4)]
print('After List comprehension:', mylist)

