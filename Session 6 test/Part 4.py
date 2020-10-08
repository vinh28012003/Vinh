#numbers = [5, 1, 8, 92, 7, 30]

#for i in numbers:
 #   if i %2 == 0:
  #      print(i)

#2 
userinput = input(" Put some number separate with ',': ")
lst = [int(n) for n in userinput.split(',')]

for n in lst:
    if n %2 == 0:
        print(n)