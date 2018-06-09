import html
import numbers
from collections import abc
from functools import singledispatch

# 支持模块化扩展，各个模块可以为它支持的各个类型注册一个专门函数
@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content=html.escape(text).replace('\n','<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '<li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>'+inner + '</li>\n</ul>'


if __name__=="__main__":
    print(htmlize(25))
    # 将 十进制 显示为 十六进制
    print('{0:x}'.format(25))
    print(htmlize('wanjun'))
    print(htmlize((1,'wanjun',3)))