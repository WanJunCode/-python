from operator import methodcaller

s = "The time has come"
upcase = methodcaller('upper')
lowcase=methodcaller('lower')
print(upcase(s))
print(lowcase(s))

hiphenate=methodcaller('replace',' ','-')
print(hiphenate(s))