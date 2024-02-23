def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def main():
    print("Simple Calculator")
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
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            print(f"Result = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result = {divide(num1, num2)}")
        try_again = input("Do you want to perform another calculation? (y for yes / anything else for no): ")
        if try_again.lower() != 'y':
            break