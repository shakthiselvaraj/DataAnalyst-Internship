# Pass by value

def val(x):
    print('Pass by value:', x)
x = 5
val(x)

def val1(y):
    y = 10
    print('Inside the Function:', y)
y = 5
val1(y)
print('Outside the Function:', y)


# Pass by Reference

a = [1,2,3,4,5]
def ref(num):
    print('Pass by Reference:', num)
ref(a)

b = [5,2,3,4,5]
def ref1(num1):
    print('Pass by Reference after update:', num1)
ref1(b)
print('Outside the Function:', b)