metro_data = [
    ('Tokyo','JP',36.933,(35.689772,139.691667)),
    ('Delhi NCR','IN',21.935,(28.613889,77.208889)),
    ('Mexico City','MX',20.142,(19.433333,-99.13333)),
    ('New-York','US',20.142,(40.8680,-74.020386)),
]

from operator import itemgetter
for city in sorted(metro_data,key=itemgetter(1)):
    print(city)

print()
cc_name=itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))