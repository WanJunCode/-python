from functools import reduce

def fact(n):
    return reduce(lambda a,b:a*b,range(1,n+1))

from operator import mul

def fact2(n):
    return reduce(mul,range(1,n+1))

print(fact(3))

print(reduce(mul,range(1,3)))

print()
for i in range(1,4):
    print(i)