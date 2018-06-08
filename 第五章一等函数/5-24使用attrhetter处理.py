from collections import namedtuple

metro_data = [
    ('Tokyo','JP',36.933,(35.689772,139.691667)),
    ('Delhi NCR','IN',21.935,(28.613889,77.208889)),
    ('Mexico City','MX',20.142,(19.433333,-99.13333)),
    ('New-York','US',20.142,(40.8680,-74.020386)),
]

LatLong=namedtuple('LatLong','lat long')
Metropolis=namedtuple('Metropolis','name cc pop coord')
metro_areas=[Metropolis(name,cc,pop,LatLong(lat,long))
             for name,cc,pop,(lat,long) in metro_data]

print(metro_areas[0])

print(metro_areas[0].coord.lat)

from operator import attrgetter
name_let=attrgetter('name','coord.lat')

print()
for city in sorted(metro_areas,key=attrgetter('coord.lat')):
    print(city)
    print(name_let(city))