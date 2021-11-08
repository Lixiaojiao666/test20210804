#list1 = [1,2,3,4,5,6,"a","b","c",True]
#print(list1[2:-1:2])
'''
a = 3
if a == 0:
    print("a=0")
elif a ==1:
    print("a=1")
elif a ==2:
    print("a=2")
else:
    print("a!=0,1,2")
'''

#多重分支
x = -2

if x>1:
    y = 3*x-5
elif -1 <= x <= 1:
    y = x + 2
else:
    y = 5*x + 3

print(y)
#分支
if x >= -1:
    if -1 <= x <= 1:
        y = x + 2
    else:
        y = 3 * x - 5
else:
    y = 5 * x + 3
print(y)
