#Nicola Batty
#08/10/2014
#Iteration pre-homework Task 2

def Task1():
    for count in range(5):
        print("*")

def Task2():
    number = int(input("How many asterisks do you want to be shown on the screen: "))
    for count in range(number):
        print("*")

def Task3():
    parsword = input("Please input parsword: ")
    while not(parsword == "secret"):
        parsword = input("Please input parsword: ")

def Task4():
    message = input("Pease input a message: ")
    number = int(input("Please input the number of times you want the message shown: "))
    for count in range(number):
        print(message)

def Task5():
    number = int(input("Please input the number: "))
    for count in range (1,101):
        number_times = number * count
        print(number_times)
