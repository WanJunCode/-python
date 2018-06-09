import functools
from 第7章函数装饰器和闭包.clockdemo import clock

# 使用缓存实现，可以极大地缩短递归调用的时间
# lru_cache 参数必须为可散列的（hash）(不可更改)
@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=="__main__":
    print(fibonacci(30))
    print(fibonacci.__name__)