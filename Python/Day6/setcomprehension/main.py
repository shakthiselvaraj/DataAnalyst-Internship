num = [1,1,2,3,2,5,4,6,5]

# Normal Set function
a = set()
for n in num:
    a.add(n)
print(a)

# Set Comprehension
myset = {n for n in num}
print('After set Comprihension', myset)
myset = {n*n for n in num}
print('After set Comprihension', myset)
myset = {n for n in num if n%2==0}
print('After set Comprihension', myset)
myset = {(a,b) for a in range(1,5) for b in range(1,5)}
print('After set Comprihension', myset)


