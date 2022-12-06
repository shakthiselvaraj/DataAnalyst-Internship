# Generator Function

num = [1, 2, 3, 4, 5]


def gen_func(num):
    for n in num:
        yield n * n


a = gen_func(num)
for i in a:
    print(i)

# Generator Comprehension
mygen = (n*n for n in num)
for j in mygen:
    print('After Generator Comprehension', j)