# Reduce function
from functools import reduce

def red(num1, num2):
    return num1 + num2
l = [1,5,6]
print(reduce(red, l))

