# Calculator Using Function

add = lambda n1, n2 : n1 + n2
sub = lambda n1, n2 : n1 - n2
mul = lambda n1, n2 : n1 * n2
div = lambda n1, n2 : n1 / n2

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        if choice == '1':
            print('sum of two numbers:', add(n1,n2))



        elif choice == '2':
            print('sub of two numbers:', sub(n1,n2))


        elif choice == '3':
            print('mul of two numbers:', mul(n1,n2))


        elif choice == '4':
            print('div of two numbers', div(n1,n2))

    else:
            print("Please select correct operator!")

