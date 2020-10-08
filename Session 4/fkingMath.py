from random import *

a = randrange(10)
b = randrange(10)
wrongNumber = [ -1, 0, 1]
correct = a + b
chosenNumber = choice(wrongNumber)
#input(a, "+", b, "=", incorrect)
#userInput = input("True or False (T/F): ")
#if correct != incorrect:
 #   if userInput.lower() == "t":
  #      print("You lose")
   # else:
    #    print("you win")

incorrect = correct + chosenNumber
print(a, "+", b, "=", incorrect)
userInput = input("True or False (T/F)")
if incorrect != correct:
    if userInput.lower() == 't':
    
        print("You lose")
    elif userInput.lower() == 'f':
        print("You Win")
else:
    if userInput.lower() == 't':
        print("You Win")
    elif userInput.lower() == 'f':
        print("You lose")
