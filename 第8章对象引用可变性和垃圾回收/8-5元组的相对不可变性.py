# 元组的不可变性其实是指
# tuple数据结构的物理内容
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)
print(t1 is t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)