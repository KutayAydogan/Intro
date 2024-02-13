number = int(input("Enter the number you want to check"))
if number <= 0:
    print("Select a postive and greater than 0 number")
if number == 1:
    print("Number is not prime")
elif number > 1:
    for x in range(2,number):
        if (number%x) == 0:
            print("Number is not prime")
            break
    else: 
         print("Number is prime")