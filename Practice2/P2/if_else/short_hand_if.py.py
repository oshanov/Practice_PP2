a = 10
b = a
print("perf equallity") if a is b else print('no')

########################

a = 30
b = 29.9

print("a") if a > b else print("b")

######################

a = int(input())
b = int(input())
bigger = a if a > b  else b

print(bigger)

######################

name = input()
name2 = name if name is not "" else "Guest"
print(name2)
