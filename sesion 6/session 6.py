#print('list intro')
list_mon_an = ['thit cho', 'thit meo']
#mon_an_moi = input()
#list_mon_an.append(mon_an_moi) 
list_mon_an.append('thit ga') # UPDATE
#print(list_mon_an[1])
#mon_thitcho = list_mon_an[1]
#print(mon_thitcho)
length = len(list_mon_an) # READ
print(length)
for i in range(length):
    print(i, list_mon_an[i])
print('___')
for item in list_mon_an:
    print(item)
print('____')
for index, item in enumerate(list_mon_an):
    print(index, item)

list_mon_an[0] = 'cho thit'  # UPDATE

list_mon_an.remove('cho thit') # DELETE BY VALUE
list_mon_an.pop(0) # DELETE BY INDEX
list_mon_an.pop(0) # DELETE BY INDEX
print(list_mon_an)