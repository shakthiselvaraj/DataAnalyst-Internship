def even(max):

    n = 2

    while n <= max:
        yield n
        n = n + 2

n = even(20)

for i in n:
    print(i)