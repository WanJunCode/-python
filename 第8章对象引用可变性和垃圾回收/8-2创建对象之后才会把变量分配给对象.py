class Gizmo:
    def __init__(self):
        print('Gizmo id : %d ' % id(self))

x = Gizmo()
# 证明 右式先创建对象
print(dir())