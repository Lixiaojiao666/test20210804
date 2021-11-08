dict1 = {"a":1,"b":2,"c":3}
dict2 = dict(c=3,d=4)

print("dict1",dict1,type(dict1))
print("dict2",dict2,type(dict2))
print(dict1.keys(),dict1.values())

print(dict2.keys(),dict2.values())

print(dict1.popitem())
print(dict1)

dict3 = {}
dict4 = dict3.fromkeys([1,2,3],"a")
print(dict4)

dict5 = {i:i**3 for i in range(1,4)}
print(dict5)