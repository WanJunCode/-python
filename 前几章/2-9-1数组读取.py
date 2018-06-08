from array import array

floats2=array('d')
fp=open('floats.bin','rb')
# Read n objects from the file object f and append them to the end of the array.
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1])
print(floats2[:50])