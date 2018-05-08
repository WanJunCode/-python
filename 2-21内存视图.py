from array import array
numbers=array('h',[-2,-1,0,1,2])
# 内存视图
memv=memoryview(numbers)
print('len = ',len(memv))

print('memv[0] =',memv[0])

# B 表示无符号字符
memv_oct=memv.cast('B')
print(memv_oct.tolist())

memv_oct[5]=4
print(numbers)