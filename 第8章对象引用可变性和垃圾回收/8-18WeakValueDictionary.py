class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r) ' % self.kind

import weakref

# 创建一个 弱值字典
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    # 为 弱值字典 添加 键值对
    # stock 把奶酪的名称映射到 catalog 中 Cheese 实例的弱引用上
    # name - - - - - > Cheese 实例
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

# 删除列表
del catalog

# 此时全局变量 cheese 依然指向 Parmesan
print(sorted(stock.keys()))

# cheese 是全局变量
print('依旧保留', cheese)

# 删除全局变量
del cheese
print('删除后...')
print(sorted(stock.keys()))