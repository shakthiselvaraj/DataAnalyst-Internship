# Zip function

# Normal Function
names = ['peter', 'wade']
heros = ['spiderman', 'deadpool']
a = {}
for names,heros in zip(names,heros):
    a[names] = heros
print('Before Dictionary Comprehension:', a)

# Dictionary Comprehension
mydict = {names: heros for names,heros in zip(names,heros)}
print('After Dictionary Comprehension:', mydict)


# In range

# Normal Function
b = {}
for num in range(1,6):
    b[num] = num*num
print('Before Dictionary Comprehension:', b)

# Dictionary Comprehension
mydict = {num: num*num for num in range(1,6)}
print('After Dictionary Comprehension:', mydict)

# To update
p = {'milk': 25, 'biscuit': 10}
r = 10
mydict = {k:v + 5 for k,v in p.items()}
print('After Dictionary Comprehension:', mydict)

# if
mydict = {k:v for k,v in p.items() if v%2==0}
print('After Dictionary Comprehension:', mydict)

# if else
roll = {'shakthi': 23, 'sha': 40}
mydict = {k:('old' if v>25 else 'young') for k,v in roll.items()}
print('After Dictionary Comprehension:', mydict)







