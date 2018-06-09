registry = set()

def register(active = True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            # Remove an element from a set if it is a member.
            registry.discard(func)
        return func
    return decorate

# @register 工厂函数必须作为函数调用
@register(active = False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')

if __name__=="__main__":
    print('running main()')
    print('registry = ',registry)
    f1()