x = lambda a: a + 10
print(x(5))

y = lambda a, b: a ** b
print(y(8,2))

################
def myfunc(n):
    return lambda a: a * n

doubler = myfunc(2)

print(doubler(11))

##############

sq = lambda a : a ** 2
print(sq(5))

difference = lambda a, b: a-b
print(difference(10,8))