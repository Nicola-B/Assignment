#Nicola Batty
#25/09/2014
#Assignment exercise

print ("Hello user")

radius = int(input("What is the radius of your circle: "))

pi = 3.14

circumfrence = 2*pi*radius
circumfrence_rounded = round(circumfrence, 2)

area = pi*radius**2
area_rounded = round(area, 2)

print("The area is {0},".format(area))
print("The circumfrence is {0}".format(circumfrence))
