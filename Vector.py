from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    # 把一个对象以字符串形式表现出来以便辨认
    def __repr__(self):
        return '__repr__ Vector(%s, %s)'% (self.x,self.y)

    def __abs__(self):
        # Return the Euclidean distance, sqrt(x*x + y*y).
        return hypot(self.x, self.y)

    def __bool__(self):
        # return bool(abs(self))
        # 更高效的做法
        return bool(self.x or self.y)

    # 算术运算符 +
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)

    # 算术运算符 *
    def __mul__(self, scalar):
        return Vector(self.x*scalar,self.y*scalar)

v1=Vector(1,2)
v2=Vector(3,4)

print(v1+v2)
print(v1*5)
print(abs(v2))
print(v1)
v3=Vector()
print(bool(v3))