class Gizmo:
    def __init__(self):
        print('Gizmo id : %d ' % id(self))

x = Gizmo()
# 证明 右式先创建对象
# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
print(dir())