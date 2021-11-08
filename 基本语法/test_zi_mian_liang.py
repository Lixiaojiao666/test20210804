# format格式 字面量插值
name = 'lxj'
age = 18
print('my name is {1},my age is {0}'.format(name,age))

list1=[1,2,3]
dict1={"name":'lxj',"age":'18'}
print("my list is {0},my dict is {1}".format(list1,dict1))

namelist  = ['lili','tom','jerry']
print('Our names :{},{},{}'.format(*namelist))

print('my name is {name},age is {age}'.format(**dict1))


# 字符串格式化机制  f'{字面量值}'
print(f"my name is {name.upper()},age is {age},my list is {list1[0]},my dict is {dict1['name']}")
print(f'my name is {name.upper()},age is {age},my list is {list1[0]},my dict is {dict1["name"]}')

print(f'这是一个计算式：{(lambda x:x+1)(1)}')


b = (lambda a:a+1)(2)
print(b)