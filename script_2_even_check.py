#script_2_even_check 

UserInput = input("Enter a number: ")

try:
    number = int(UserInput)
    if number % 2 == 0:
        print("\nThe number is even.")
    else:
        print("\nThe number is odd.")
except:
    print("\n There was an error! Please enter a valid integer.")