# list 是可变序列
k=[1,2,3]
print(id(k))
k*=2
print(k)
print(id(k))
print('在可变序列上执行 *= 会在原对象上增加')

# tuple 是不可变序列
print()
t=(1,2,3)
print(id(t),t)
t*=2
print(id(t),t)
print('在不可变序列上使用 *= 会产生一个新的对象 ')
