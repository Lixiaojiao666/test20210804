list_1 = [1,2,3]
print(list_1)
print(type(list_1))

print('----------------------------')

tuple_2 = (list_1,4,6,6,)
tuple_2
print(tuple_2)
print(type(tuple_2))

print(id(tuple_2[0]))
print(id(tuple_2[0][0]))
print(id(tuple_2[0][2]))

tuple_2[0][2] = "c"
print(tuple_2)
print(id(tuple_2[0]))
print(id(tuple_2[0][0]))
print(id(tuple_2[0][2]))

print(tuple_2.count([1,2,'c']))
print(tuple_2.index(6))