# Calculator Using Function

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def percentage(x, y):
    return (x / y) * 100

def square(x):
    return x*x

def power(x, y):
    return x**Y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Percentace")
print("6.Square")
print('7.Power")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):

        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        if choice == '1':
            print('Addition of two numbers:', add(n1,n2))



        elif choice == '2':
            print('Subtraction of two numbers:', sub(n1,n2))


        elif choice == '3':
            print('Multiplication of two numbers:', mul(n1,n2))


        elif choice == '4':
            print('Division of two numbers', div(n1,n2))
      
        elif choice == '5':
           
            print('Percentage of the numbers', percentage(n1,n2)
                  
        elif choice == '6':
                  
            print('Square of the given numbers', square(n1)
                  
        
        elif choice == '7':
                             
             print('Power of the given numbers', power(n1,n2)

         
      else:
            print("Please select correct operator!")

