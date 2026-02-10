def sum_calc(x,y):
    return x + y

print(sum_calc(6,7))

res = sum_calc(4,1)
print(res)

########################

def func():
    return ['apples', 'banana', 'cherry']

fruits = func()
print(fruits[0])

########################
def tuple_func():
    return (10,20)
x,y = tuple_func()
print(x)
print(y)

########################
def sme(a,b,/,*,c,d):
    return (a+b) / (c - d)

print(sme(1,2,c = 0, d = 2))
