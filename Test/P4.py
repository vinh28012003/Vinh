#Part IV
IsDone = True
while IsDone:
    email = input("Please enter your email: ")
    username = input("Please enter your username: ")
    password = input("Please enter your pass word: ")
    repassword = input("Re-enter password:")
    if ("@" in email) and ("." in email) :
        if (repassword == password) and (len(password) >= 8) and  :
            print("Sign up success")
            print("Your accounr is:", username, password)
            isDone = False
        elif (repassword != password):
            print("Password doesn't match or have already taken")
        elif password doesnot contain digit
            print("need at least 1 digit in your password")
        elif  password doesn't contain email": 
            print("please use at least one letter in your password")
    else:
        print("Email is not valid")