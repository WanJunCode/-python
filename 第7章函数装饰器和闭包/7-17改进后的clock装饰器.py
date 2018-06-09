import time
import functools

def clock(func):
    @functools.wraps(func)
    # 可以保证装饰器不会对被装饰函数造成影响 即 __name__ 不被改变
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
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