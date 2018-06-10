print('针对tuple')
t1 = (1, 2, 3)
t2 = tuple(t1)

print(t2 is t1)

t3 = t1[:]
print(t3 is t1)


print('\n针对列表来说')
l1 = [1, 2, 3]

l3=l1.copy()
print(id(l1))
print(id(l3))
l2 = list(l1)
print(l1 is l2)
print(l3 is l1)