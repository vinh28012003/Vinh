from turtle import *


userInput = int(input("inssert the numbers of circles you wanted: "))
speed(-1)

def drawTimesCircle(times):
    for i in range(times):
        circle(100)
        left(i*10)


drawTimesCircle(userInput)



mainloop()