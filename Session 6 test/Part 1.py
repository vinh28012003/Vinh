a = ['red', 'green', 'blue', 'orange']
print('Our list:')
print(*a, sep = ", ")
new_a = input("put something new in here: ")

a.append(new_a)
print(*a, sep = ', ')