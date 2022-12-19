# Lambda function

# Before Lambda Function

def myfunc(n):
    double = n*2
    return double
print('Before lambda:', myfunc(10))

# Using Lambda Function single arguments

double = lambda n : n*2
print('After lambda:', double(20))

# Multiple Arguments

sum = lambda  n1,n2 : n1+n2
print('Sum of given numbers:',sum(10,30))

# square of the numbers

a = [2,4,6,8,10]
s = []
square = lambda n : n**2
for i in a:
    s.append(square(i))
print('Square of the number;', s)


