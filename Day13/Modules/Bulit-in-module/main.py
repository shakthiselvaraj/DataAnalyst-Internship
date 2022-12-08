# Built-in-module

# import module

import math

num = int(input('Enter the number:'))
result = math.sqrt(num)
print(result)

# Renaming module

import math as m

num1 = int(input('Enter the number:'))

result1 = m.sqrt(num1)
print(result1)

# Python from import

from math import sin

num2 = sin(30)
print(num2)

# To see mathematical functions in Math Function

print(dir(math))

