a = int(input('Enter the Number:'))
b = int(input('Enter the Number:'))

try:
    print('open')
    print(a/b)

except Exception as e:
    print('Error', e)

finally:
    print('close')