num1 = int(input('Enter the Number'))
num2 = int(input('Enter the Number'))
if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are Equal!')
    else:
        print(num1, 'greater than', num2)
else:
    print(num2, 'smaller than', num1)
