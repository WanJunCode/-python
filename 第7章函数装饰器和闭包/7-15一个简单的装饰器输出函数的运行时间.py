# 装饰器不支持关键字参数

import time

# 装饰器clock 获得函数名 func
def clock(func):
    print('被装饰函数地址 = ', func)

    # 函数 clocked 获得定位参数
    def clocked(*args):
        t0 = time.perf_counter()
        # func 得到被装饰函数的地址
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        # 将传入的定位参数 显示出来
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

# @clock
# def factorial(n):
#     return 1 if n < 2 else n*factorial(n-1)

def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
# 等价使用装饰器
factorial = clock(factorial)


if __name__=="__main__":
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! = ', factorial(6))
    print('\nfactorial.name = ', factorial.__name__)