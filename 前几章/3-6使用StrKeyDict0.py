class StrKeyDict0(dict):

    def __missing__(self, key):
        # 如果找不到的键本身就是字符串
        if isinstance(key,str):
            raise KeyError(key)
        # 如果找不到的键不是字符串，就把它转化为字符串再进行查找
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d=StrKeyDict0([('2','two'),('4','four')])
print(d['2'])
print(d[4])

print(d.get('2'))
print(d.get(4))

print(2 in d)
print('2' in d)
# 重写了get 函数 ，当键不存在时 返回None
print(d.get(1))