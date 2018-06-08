import numpy as np
from array import array
floats=array('d')
fp=open('floats.bin','rb')
floats.fromfile(fp,10**7)
print(floats[:5])
num_floats=np.array(floats,dtype=np.float64)
print(num_floats[:5])
num_floats*=5
print(num_floats[:5])

from time import perf_counter as pc
# Performance counter for benchmarking.
t0=pc()
num_floats/=3
print(pc()-t0)
# Numpy  保存 读取
np.save('floats-10M',num_floats)
floats2=np.load('floats-10M.npy','r+')
floats2*=2
print(floats2[-5:])