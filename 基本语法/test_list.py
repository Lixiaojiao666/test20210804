list_1=[1,7,2,6,3,5,4,1,1,1,1]
list_2=['a','b','c','d']


#list_1.append(100)
#list_1.insert(0,-100)
#print(list_1.pop(1))
#list_1.sort(reverse=True)
#list_1.reverse()
#list_1.clear()
#del list_1[:]
#list_1.extend(list_2)
#list_2=list_1.copy()
#print(list_1.count(1))
#print(list_2)
#print(list_1)

list_square=[]
for i in range(4):
    list_square.append(i**2)
print(list_square)

list_square1=[i**2 for i in range(4)]
print(list_square1)

list_square2=[]
for i in range(4):
    if i !=1:
        list_square2.append(i ** 2)
print(list_square2)

list_square3=[i**2 for i in range(4) if i !=1]
print(list_square3)

list_square4=[]
for i in range(1,4):
    for j in range(1,4):
        list_square4.append(i*j)
print(list_square4)



list_square5=[i*j for i in range(1,4) for j in range(1,4)]
print(list_square5)

