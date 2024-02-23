print("Welcome to Calculator")
print("Operations:")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")
while True:
    choice = input("Enter the number for your operation: ")
    if choice not in ('1', '2', '3', '4'):
        print("Your input is wrong. Please choose a valid operation number from 1 to 4")
        continue
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    if choice == '1':
        z = x + y
        print("Result = " , z)
    elif choice == '2':
        z = x - y
        print("Result = " , z)
    elif choice == '3':
        z = x * y
        print("Result = " , z)
    elif choice == '4':
        if y == 0:
            print ("Division by zero is not possible enter another value")
        else:
            z = x / y
            print("Result = " , z)
    try_again = input("Do you want to perform another calculation? (y for yes / anything else for no): ")
    if try_again.lower() != 'y':
        break