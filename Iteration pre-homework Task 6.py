#Nicola Batty
#08/10/2014
#Iteration pre-homework Task 6

def Task1():
    message = input("Please input your message: ")
    number = int(input("Please input your number: "))
    for count in range(number):
        print(message)

def Task2():
    password = "Hi"
    while not(password == "secret"):
        password = input("please inpur the password: ")
        if password == "secret":
            print("You now have access to the system")
        else:
            print("Wrong password")

