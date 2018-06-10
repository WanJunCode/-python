import weakref

s1={1,2,3}
s2=s1

def bye():
    print('Gone  with  the  wind...')

# 在s1 引用的对象上注册 bye 回调
ender = weakref.finalize(s1,bye)
print(ender.alive)
del s1
print(ender.alive)
print('s2 id = ',id(s2))
s2 = 'spam'
print('s2 被重新赋值后')
print('s2 id = ',id(s2))
print(ender.alive)