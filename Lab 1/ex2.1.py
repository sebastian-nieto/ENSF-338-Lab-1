import sys

#the code takes in an arguement through the command line and then checks if it is a prime number
def do_stuff():

    #checks if an command line arguement is provided
    if len(sys.argv) == 1:
        print("No input. Please provide a valid integer")
        return
    
    #tries to convert input to int, if there's a value error like if a string/decimal is inputted then the code prints an invalid input statement and returns 
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please provide a valid integer.")
        return

    #checking if number is prime
    if number < 2:
        print("no")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("No")
                return
        print('Yes')

# Test the function
do_stuff()