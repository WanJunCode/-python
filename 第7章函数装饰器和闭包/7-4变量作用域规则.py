b=6

def f2(a):
    # 声明变量 b 为全局变量
    global b
    print(a)
    print(b)
    b = 3
print('b = ',b)
f2(2)
print('b = ',b)
