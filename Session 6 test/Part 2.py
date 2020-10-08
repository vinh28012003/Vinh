a = ['red', 'green', 'blue', 'orange']
length = len(a)
for i in range(length):
    print(i, a[i])
c = int(input('enter position to delete: '))

#print(a[c])
a.pop(c)
print(*a, sep = ', ')