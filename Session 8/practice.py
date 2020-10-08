# Questio 4 
#listNumber = [12 , 46, True, "C4T", 100]

# for i in range(4)

#result = 0
#for numb in listNumber:
 #   if type(numb) is int:
 #       result = result + numb


#print(result)

# Question 5
#userInput = inut("enter everythings: ")
#result = userInput.split(', ')
#result.sort()
#print(result)
def convertStringToList(text):
    result = text.split(", ")
    result.sort()
    return result

userInput = input("Enter everythings:")

lastResult = input("enter everything: ")
lastResult = convertStringToList(userInput)
print(lastResult)
