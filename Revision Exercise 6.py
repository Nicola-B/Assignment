#Nicola Batty
#06/10/2014
#Revision Exercise 6

def Rex6():

    print("Hello user")

    number1 = int(input("Please input a number: "))
    number2 = int(input("Please input another number: "))
    number3 = int(input("Please input anther number: "))

    if number1 > number2 > number3:
        print("The bigger number is {0}".format(number1))
    elif number1 > number3 > number2:
        print("The bigger number is {0}".format(number1))
    elif number2 > number1 > number3:
        print("The bigger number is {0}".format(number2))
    elif number2 > number3 > number1:
        print("The bigger number is {0}".format(number2))
    elif number3 > number1 > number2:
        print("The bigger number is {0}".format(number3))
    elif number3 > number2 > number1:
        print("The bigger number is {0}".format(number3))
    elif number1 > number3 == number2:
        print("The bigger number is {0}".format(number1))
    elif number2 > number1 == number3:
        print("The bigger number is {0}".format(number2))
    elif number3 > number1 == number2:
        print("The bigger number is {0}".format(number3))
    elif number1 == number2 > number3:
        print("The bigger number is {0}".format(number1))
    elif number3 == number2 > number1:
        print("The bigger number is {0}".format(number2))
    elif number1 == number3 > number2:
        print("The bigger number is {0}".format(number3))
    else:
        print("These numbers are all the same")
    
