x = 11

if x > 10:
    print('x is greater than 10')
else:
    print('no')
######################################

a = 5
b = a
print(a is b)

#######################################

print("Proposition \"x is 11\" is",bool(x == 11))
print("Proposition \"x is not 11\" is",bool(x != 11))

######################################

a = int(input())
b = int(input())

if a > b:
    print(f'{a} is greater than {b}')
elif a == b:
    print("They are equal")
else: 
    print(bool(False))

##############################################

x = (10/2 >= 5)
if x is True:
    print("YEAH")
