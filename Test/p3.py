#Part III
#n = int(input("Insert a number: "))

#if n > 13:
    #print(n, "is greater than", 13)
#elif n == 13:
       # print(n, " is equal to", 13)
#else:
    #print(n, " is smaller than", 13)

#n = int(input("Insert a number: "))

#evennumb = n % 2 

#if evennumb == 0 :
    #print(n, "is a even number")
#else:
    #print(n, " is not a even number"


while True:
    Month = input("insert a month: ")
    if Month in "january, march, may, july, august, october, december":
       print("There are 31 days in the month")
    elif Month in "feburary":
        print("There are 28 days (29 in leap years) in this month")
    elif Month in "april, june, september, november":
        print("There are 30 days in this month")
    else:
        print("invalid month name")