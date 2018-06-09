b=6

def f2(a):
    # 声明变量 b 为全局变量
    global b
    print(a)
    print(b)
    # 如果不声明变量b，在函数中赋值默认为局部变量
    b = 3
print('b = ',b)
f2(2)
print('b = ',b)
