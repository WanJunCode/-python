from array import array
from random import random

floats=array('d',(random() for i in range(10**7)))
print(floats[-1])
fp=open('floats.bin','wb')
# Write all items (as machine values) to the file object f.
floats.tofile(fp)
fp.close()
