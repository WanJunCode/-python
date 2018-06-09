import time
from 第7章函数装饰器和闭包.clockdeco_param import clock

# 装饰器中 参数为 输出格式
@clock('{name}({args}): dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)

if __name__=="__main__":
    for _ in range(3):
        snooze(0.123)