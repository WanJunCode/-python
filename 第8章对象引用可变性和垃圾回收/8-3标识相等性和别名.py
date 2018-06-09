charles = {'name':'charles L.Dodgson','born':1832}
# lewis 是 charles 的别名
lewis = charles
print(lewis is charles)
print(id(lewis),id(charles))
print(lewis)
print(charles)

# lewis['newattr']='wanjun'
# print(lewis)
# print(charles)

alex = {'name':'charles L.Dodgson','born':1832}
print(lewis == alex)
print(charles == alex)
print('是否是不同的对象')
print(lewis is not alex)