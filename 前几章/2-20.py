from array import array
from random import random

floats=array('d',(random() for i in range(10**3)))
print(floats[-1])

# 保存数组
fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()

# 读取数组
floats2=array('d')
fp=open('floats.bin','rb')
floats2.fromfile(fp,10**3)
fp.close()
print(floats[-1])

print(floats == floats2)
print(len(floats2))