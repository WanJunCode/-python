a='万'

print(ord(a))

b=bytes(a,'utf-8')
print(b)

c=bytes(a,'gb2312')
print(c)

for i in range(len(b)):
    print(b[i])

# 反编码
print(b.decode('utf-8'))