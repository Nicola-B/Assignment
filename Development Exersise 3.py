#Nicola Batty
#07/10/2014
#Development Exersise 3

print("Hello ueser")

hours_worked = int(input("Please can you enter the number of hours you haved worked this week: "))
pay_per_hour = int(input("Please can you enter your pay per hour: "))

if hours_worked < 60 and hours_worked > 0:
    if pay_per_hour > 0:
        total_pay = pay_per_hour * hours_worked
        print("You have erned £{0} amount this week".format(total_pay))
    else:
        print("Error! cannot have a negative pay")
else:
    print("Error! working to much")
