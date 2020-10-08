#git stage .
#git commit -m "new update"
#number = [3, 45, 12, 64, 89, 18]
#i = int(input(" type a number here: "))

#1 for c in number:
#    if i == c:
 #       print( i, number.index(i) )

#2 print(sum(number))
#3
number = input("please type numbers and separate with ' ': ")
numbers = number.split()
sum1 = 0
for num in numbers:
    sum1 += int(num)
print(sum1)