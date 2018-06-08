def make_averager():
    # ================闭包======================
    # ==========================================
    # 是 make_averager 函数的局部变量
    series = []

    def averager(new_value):
        # series 是自由变量 free variable
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    # =========================================

    return averager

if __name__=="__main__":
    # 返回值是一个  函数对象
    print(make_averager)
    avg = make_averager()
    print(avg)
    print(avg(10))
    print(avg(11))
    print(avg(12))

    print('avg 的局部变量 = ',avg.__code__.co_varnames)
    print('avg 的自由变量 = ',avg.__code__.co_freevars)