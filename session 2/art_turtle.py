#import turtle


from turtle import *
times = int(input("Enter a number: "))

speed(-1)
for x in range(times):
    for i in range(4): 
        forward(100)
        left(90)
    left(5)

mainloop()