from 第7章函数装饰器和闭包.clockdemo import clock

@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

if __name__=="__main__":
    print(fibonacci(6))
    print(fibonacci.__name__)