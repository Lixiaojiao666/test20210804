'''
import json

list1 = [1,2,3]

print(list1[2])

dict1 = {
    "first":1,
    "second":2
}

print(dict1["first"])


#json是由字典和列表组成的
data = {
    "name":['lxj','babyname'],
    "age": 30,
    "gender":'female'
}

print(type(data))
data1 = json.dumps(data)
print(type(data1))

data2 = json.loads(data1)
print(type(data2))
#num = input("input:")
#print(int(num))

def div(a,b):
    return a / b
f = open("data.txt")
try:
    print(div(1, 0))
    list1 = [1, 2, 3]
    print(list1[1])
    f.readline()
except Exception as e1:
    print(e1)
else:
    print("no exception")
#finally最终都会被执行，无论是否有异常
finally:
    print("finally")
    f.close()
'''



class MyException(Exception):
   def __init__(self,value):
      self.value = value
   def __str__(self):
      return repr(self.value)

def set_age(age):
    if age<=0 or age>200:
        raise MyException(f"值错误:{age}")
    else:
        print(f"your age is :{age}")

set_age(0)