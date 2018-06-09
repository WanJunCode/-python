import time
import functools

# 装饰器 获得 函数名称 func
def clock(func):
    @functools.wraps(func)
    # 可以保证装饰器不会对被装饰函数造成影响 即 __name__ 不被改变
    # clocked 函数 获得定位参数 以及 关键字参数
    def clocked(*args, **kwargs):
        t0 = time.time()
        # 【1】获得原函数的 返回值
        result = func(*args, **kwargs)
        # 【2】计算函数运算的时间
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            # repr 函数将对象转化为供解释器读取的形式。
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            # 关键字参数
            pairs =['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r '%(elapsed,name,arg_str,result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

if __name__=="__main__":
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print(snooze.__name__)