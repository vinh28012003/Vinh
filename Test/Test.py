#Part I
#firstname = input("What's your first name: ")
#middlename = input(" what's your middle name: ")
#lastname = input(" what's your last name: ")
#print(lastname + middlename + firstname)
#print(lastname.capitalize() + middlename.capitalize() + firstname.capitalize())
#number = int(input("Type a number: "))

#print(number**2)
#from turtle import *
#radius = int(input("insert a number: "))

#print("Your circle's radius is", radius)

#circle(radius)

#Part II
#for i in range(3, 13): 
 #   print (i, end= ', ')

#n = int(input("Insert a number: "))

#for i in range(0, n + 1):
    #print(i, end= ', ')

#Part III
#n = int(input("Insert a number: "))

#if n > 13:
    #print(n, "is greater than", 13)
#elif n == 13:
        #print(n, " is equal to", 13)
#else:
    #print(n, " is smaller than", 13)

#n = int(input("Insert a number: "))

#evennumb = n % 2 

#if evennumb == 0 :
    #print(n, "is a even number")
#else:
    #print(n, " is not a even number")


#Part IV
IsDone = True
while IsDone:
    email = input("Please enter your email: ")
    username = input("Please enter your username: ")
    password = input("Please enter your pass word: ")
    repassword = input("Re-enter password:")
    n = range(-1, 9999999, 1)
    if ("@" in email) and (len(email) >= 8) and :
        if (repassword == password):
            print("Sign up success")
            isDone = False
        else:
            print("Password doesn't match or have already taken")
    elif "@" not in email:
        print("email is in valid")
    elif n  email: 
        print("please use at least one digit in your email")
    else:
        print("Email need at least 8 characters")
