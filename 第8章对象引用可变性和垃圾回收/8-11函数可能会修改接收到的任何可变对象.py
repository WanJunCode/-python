def f(a,b):
    a += b
    return a

x=1
y=2
# 此时参数传入的是 不可变类型
f(x,y)
print(x)

a = [1, 2]
b = [3, 4]
f(a,b)
print(a)

t=(10,20)
u=(30,40)
# 传入参数为 tuple 不可变序列时，相加会得到一个新的 tuple
f(t,u)
print(t,u)