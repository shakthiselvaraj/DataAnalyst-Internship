# Function basics

def myfunction():
    print('hi everyone!!!')
myfunction()


def my(str):
    return len(str)
print ('The length of given string is:', my('python'))


def addnum(n1,n2):
    sum = n1 + n2
    print('The sum of two numbers:', sum)
addnum(5,2)

def addno(num1,num2):
    a = num1+num2
    return a
b = addno(15,5)
print('The addition of two numbers is:', b)


def myfunc(name):
    return (name)
a = myfunc('Hello Everyone!')
print(a)