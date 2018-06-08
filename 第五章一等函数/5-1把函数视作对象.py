def factorial(n):
    """return n!"""
    return 1 if n<2 else n* factorial(n-1)

print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

fact=factorial
print(type(fact))

print(list(map(fact,range(11))))