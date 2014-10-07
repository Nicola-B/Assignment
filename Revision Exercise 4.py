#Nicola Batty
#06/10/2014
#Revision Exercise 4

print("Hello user")

number1 = int(input("Please input a number: "))
number2 = int(input("Please input anuther number: "))

if number1 > number2:
    print("The bigger number is {0}".format(number1))
elif number2 > number1:
    print("The bigger number is {0}".format(number2))
else:
    print("These numbers are the same")
    
