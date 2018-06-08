import promotions
import inspect

# 模块也是一等对象
# inspect 可以 处理 模块

promos=[name for name,func in inspect.getmembers(promotions,inspect.isfunction)
        if name.endswith('_promo') and not name.startswith('best_')]
for method in promos:
    print(method)