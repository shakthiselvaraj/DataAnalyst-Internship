# Python Argument funcion

# Default Argument

def myfunction(num1, num2=6):
    sum = num1 + num2
    return (sum)


print('Sum of given number is:', myfunction(5))
print('Sum of given number is:', myfunction(5, 5))
print('Sum of given number is:', myfunction(10))


# Keyword Argument

def keyfunc(first, second, third):
    print('The Given Numbers are:', first, second, third)


keyfunc(first=20, second=30, third=40)
keyfunc(10, 20, 30)


# Required Arguments

def reqfunc(name, year):
    print('Name:', name, 'Year:', year)
reqfunc('python', 1990)
# reqfunc('SQL')

# Variable Length Argument
# *

def args(*num):
    res = 0
    for n in num:
        res = res + n
    print(res)
args(2,5,6)

# **

def kargs(**name):
    a = []
    for key,value in name.items():
        a.append([key,value])
    return a
b = kargs(first='sql', second='python')
print(b)