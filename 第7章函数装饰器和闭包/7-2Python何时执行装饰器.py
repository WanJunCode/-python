registry = []

# 装饰器直接获得函数 func
# 将函数名称添加后返回
def register(func):
    print('running register(%s)'% func)
    registry.append(func)
    # 列表中可以保存  函数类型的元素
    return func

@register
def f1():
    print('running f1')

@register
def f2():
    print('running f2')

def f3():
    print('running f3')

def main():
    print('\n在执行 main() 函数之前就已经执行了装饰器 ')
    print('running main()')
    print('registry -> ',registry)
    f1()
    f2()
    f3()

if __name__=="__main__":
    main()