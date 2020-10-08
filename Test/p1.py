#Part I
#1
firstname = input("What's your first name: ")
middlename = input(" what's your middle name: ")
lastname = input(" what's your last name: ")
print(lastname + middlename + firstname)
print(lastname.capitalize() + middlename.capitalize() + firstname.capitalize())
#3
number = int(input("Type a number: "))

print(number**2)
#4
from turtle import *
radius = int(input("insert a number: "))

print("Your circle's radius is", radius)

circle(radius)
