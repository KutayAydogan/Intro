while True:
    number = int(input("Enter the number you want to check: "))
    if number <= 0:
        print("Select a postive and greater than 0 number")
    if number == 1:
        print("Number is not prime")
    if (number%2) == 0:
        print("Number is even")
    else: 
        print("Number is odd")
    if number > 1:
        for x in range(2,number):
            if (number%x) == 0:
                print("Number is not prime")
                break
        else: 
            print("Number is prime")
    try_again = input("Try another number? (y for yes , anything else for no): ")
    if try_again.lower() != "y":
        break