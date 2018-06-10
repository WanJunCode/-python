from array import array
import math

class Vector2d:
    typecode='d'

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self,x,y):
        print('call init')
        self.x=float(x)
        self.y=float(y)

    def __iter__(self):
        print('call iter')
        return (i for i in (self.x,self.y))

    def __repr__(self):
        print('call repr')
        class_name = type(self).__name__
        # print('class_name = ',class_name)
        return '{}({!r},{!r})'.format(class_name,*self)

    def __str__(self):
        print('call str')
        return str(tuple(self))

    def __bytes__(self):
        print('call bytes')
        return (bytes([ord(self.typecode)])+
                bytes(array(self.typecode,self)))

    def __eq__(self, other):
        print('call eq')
        return tuple(self) == tuple(other)

    def __abs__(self):
        print('call abs')
        return math.hypot(self.x,self.y)

    def __bool__(self):
        print('call bool')
        return bool(abs(self))

if __name__=="__main__":
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    # 分包调用了 __iter__
    print('\n分包操作')
    x, y = v1
    print(x, y)
    print('\nrepr v1')
    repr(v1)
    print()
    # eval 将字符串str当成有效的表达式来求值并返回计算结果
    v1_clone = eval(repr(v1))
    print()
    print(v1 == v1_clone)

    print()
    print(v1)

    print()
    print(abs(v1))

    print()
    print(bool(v1))
    print()
    print(bool(Vector2d(0, 0)))

    print()
    octets = bytes(v1)
    print(octets)
    # 从字节序列转换为 Vector2d 实例
    v2=Vector2d.frombytes(octets)
    print('v2 ',v2)