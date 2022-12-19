# filter function

s = [90,40,35,36,45,85]
def flt(s):
    return s > 40
print(list(filter( flt, s)))

# filter using without lambda

def even(n):
    return  n%2==0
num = [1,2,3,4,5]
a = filter(even,num)
print(list(a))

# filter usinf lambda

num = [1,2,3,4,5,6]
e = list(filter(lambda n : n%2==0, num))
print(e)