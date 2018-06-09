registry = set()

def register(active = True):
    # 闭包
    # decorate 接收 函数名称
    def decorate(func):
        print('running register(active=%s) -> decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            # Remove an element from a set if it is a member.
            registry.discard(func)
        return func
    # 返回真正的 装饰器函数
    return decorate

# @register 工厂函数必须作为函数调用
@register(active = False)
def f1():
    print('running f1()')

# 默认为 True
@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')

if __name__ == "__main__":
    print('running main()')
    print('registry = ', registry)
    f1()
    # register() == decorate
    register()(f3)
    print('registry = ', registry)
    register(active=False)(f2)
    print('删除 f2 函数后')
    print('registry = ', registry)