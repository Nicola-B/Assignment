#Nicola Batty
#07/10/2014
#Development Exercise 4

print("Hello user")

mark = int(input("Please enter mark: "))

if mark > 100:
    print("Errer! Too high")
elif mark >= 81:
    print("Grade = A")
elif mark >= 71:
    print("Grade = B")
elif mark >= 61:
    print("Grade = C")
elif mark >= 51:
    print("Grade = D")
elif mark >= 41:
    print("Grade = E")
elif mark >= 0:
    print("Grade = U")
else:
    print("Errer! Mark can not be negative")
