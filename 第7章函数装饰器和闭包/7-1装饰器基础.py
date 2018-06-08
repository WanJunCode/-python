# 简单的装饰器基础

def deco(func):
    def inner():
        print('running inner()')
    # 返回一个新的函数
    return inner

# 语法糖
@deco
def target():
    print('running target()')

if __name__=="__main__":
    target()