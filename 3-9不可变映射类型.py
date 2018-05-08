from types import MappingProxyType
d={1:'a'}
# 相当于给映射添加了一个视图，只可以读该映射
d_proxy=MappingProxyType(d)
