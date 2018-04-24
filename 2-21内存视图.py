from array import array
numbers=array('h',[-2,-1,0,1,2])
memv=memoryview(numbers)
print(len(memv))

print(memv[0])

# B 表示无符号字符
memv_oct=memv.cast('B')
print(memv_oct.tolist())

memv_oct[5]=4
print(numbers)