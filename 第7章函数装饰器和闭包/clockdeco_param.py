import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

# 参数化 clock 装饰器
def clock(fmt = DEFAULT_FMT):

    # 该闭包 获得函数名 func
    def decorate(func):
        # print('获得的 func = ',func)

        # 该闭包获得定位参数 *_args
        def clocked(*_args):
            # print('获得的 *args = ', _args)
            # 【1】计算时间
            t0 = time.time()
            # 【2】得出原来函数的结果
            _result = func(*_args)
            # 【3】得出运行该函数的时间
            elapsed = time.time() - t0
            # 【4】得到函数名称
            name = func.__name__
            # 【5】重新获得参数列表（转换为string）
            args = ', '.join(repr(arg) for arg in _args)
            # 【6】结果转换为 repr
            result = repr(_result)
            print(fmt.format(**locals()))
            # 最终返回的是这个 _result
            return _result

        return clocked
    return decorate

if __name__ == "__main__":
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(0.123)