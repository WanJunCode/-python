from collections import namedtuple

# Returns a new subclass of tuple with named fields.
# param1 类名 param2 类的各个字段的名字
City=namedtuple('City','name country population coordinates')
tokyo=City('Tokyo','JP',36.933,(35.689722,139.691667))
print(tokyo)
print(type(tokyo))
# 包含这个类所有字段名称的元组
print(City._fields)

print()
LatLong=namedtuple('LatLong','lat Long')
delhi_data=('Delhi NCR','IN',21.935,LatLong(28.613889,77.208889))
# _make() 通过接受一个可迭代对象来生成这个类的一个实例
delhi=City._make(delhi_data)
print(delhi)
# 装化成 dict 格式
print(delhi._asdict())

print()
for key,value in delhi._asdict().items():
    print(key,' : ',value)