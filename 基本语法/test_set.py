a = {1,2,2,3,3}
b = {1,4,5}
'''
print(a.difference(b))
print(b.difference(a))

print(a.union(b))
print(a.intersection(b))
a.add('a')
a.add('a')
print(a)
'''
print(set(a))

print({i for i in 'aaaaabcdddd'})
