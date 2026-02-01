a = 51

if a % 2 == 0:
    print('even')
else:
    print('odd')

##################

name = 'Mukhamedali'

if len(name) > 0:
    print(f'Welcome, {name}')
else:
    print('ERROR: Invalid name')

######################

a = False
b = True
c = False
if a == True or b == True or c == True:
    print('At least one is true')
else:
    print("all false")

#####################
a = 10
b = 9

if a is b:
    print(a+b)
else:
    print(a-b)