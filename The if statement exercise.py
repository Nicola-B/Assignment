#Nicola Batty
#23/09/2014
#The if statement exercise

print("Hello user")

age = int(input("What is your age: "))
if age >= 18:
    print("you are old enough to vote")
else:
    print("you are not old enough to vote yet")
if age < 65:
    retirement = 65-age
    print("you have {0} years till you can retire".format(retirement))
else:
    print("enjoy your retioment")
    
