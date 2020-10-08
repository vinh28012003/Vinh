sheep_size = [5, 7, 300, 90, 24, 50, 75]
print(sheep_size)
for month in range(4):
    print("month", month)
    print(max(sheep_size))
    #max_size = 0

    #for size in sheep_size:
        #if size > max_size:
        #    max_size = size
    #print("cao long con to nhat:", max_size)
    max_size_index = sheep_size.index(max(sheep_size))

    sheep_size[max_size_index] = 8

    print(sheep_size)
    for index, item in enumerate(sheep_size):
        sheep_size[index] = item + 50
    print("one month passed")
    print(sheep_size)

total = 0 
for item in sheep_size:
    total += item
print(total)
print(total * 2)