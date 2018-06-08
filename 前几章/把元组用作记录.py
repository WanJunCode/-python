lax_coordinates=(33.9425,-118408056)
city,year,pop,chg,area=('Tokyo',2003,32450,0.66,8014)
traveler_ids=[('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]

for passport in sorted(traveler_ids):
    print('%s %s'%passport)

print()
# 使用占位符 _  可以去除不含兴趣的数据
for country,_ in traveler_ids:
    print(country)

# 拆包
latitude,longtitude=lax_coordinates
print(latitude,longtitude)
# 不使用中间变量交换两个变量的参数
latitude,longtitude=longtitude,latitude
print(latitude,longtitude)

# Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
# 返回  除数  以及 余数  20//8 = 2  20%8 = 4
print(divmod(20,8))
t=(20,8)
print(divmod(*t))

import os
print(os.path)

# 元组的拆包
a,b,*rest=range(5)
print(a,b,rest)

