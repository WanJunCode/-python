def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count,total
        count += 1
        total += new_value
        return total/count

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