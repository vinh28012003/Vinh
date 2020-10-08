#age = int(input("How old are you?"))

#if age < 6:
    #print("Baby")
#elif 7 < age < 12:
    #print("Kids")
#elif 13 < age < 17:
   #print("Teen")
#else:
    #print("Adult")
from math import sqrt
a = int(input("What the first side length?"))
c = int(input("What the second side length?"))
b = int(input("What the length of the base?"))
hp = ((a + b + c)/2) 
if a**2 + c**2 < b**2:
    print("obtuse")
elif a**2 + c**2 == b**2:
    print("right triangle")
    s = (1/2)*(a*c)
elif a**2 + c**2 > b**2:
    print("acute")
elif a == c == b:
    print("equalateral")
elif (a == c) or (a == b) or (c == b): 
    print("Isosceles")
else:
    print("tam giac thuong")