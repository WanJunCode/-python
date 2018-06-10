import weakref

a_set = {0, 1}
# 声明一个弱引用 指向 s_set
wref = weakref.ref(a_set)
# 返回该弱引用
print(wref)

# 返回被引用的对象
print(wref())

# 重新赋值 a_set
a_set = {2, 3, 4}
print(wref())