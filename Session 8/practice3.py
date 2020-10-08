#Ask user what shape they want to draw and how many times.
from turtle import *


userInput = input("insert the shape you wanted to draw: ")
userInput2 = int(input("insert the number of shape you wanted to draw: "))
speed(-1)
def drawshape(shapekind, numberofshape):   
        if shapekind == "square":
            for i in range(numberofshape):
                for z in range(4):
                    foward(100)
                    left(90)
                    left(30)

        elif shapekind == "circle":
            ban_kinh = int(input("insert the radius: "))
            for i in range(numberofshape):
                
                circle(ban_kinh)
                left(30)

drawshape(userInput, userInput2)

mainloop()
    


    

