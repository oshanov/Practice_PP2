lsi = list(map(int, input().split()))

x = list(map(lambda x : x ** 2, lsi))
print('Square of your nums:', *x, sep=', ')
print('-'*30)
y = list(filter(lambda x: x % 2 == 0, x))
y2 = list(filter(lambda x: x % 2 == 1, x))
print('Even nums of squares:', *y, sep=', ')
print('-'*30)
from functools import reduce

factorial = reduce(lambda x,y: x*y, lsi)
print(factorial)

print('-'*30)

letters = ['a','b','c','d','e','f','g','h']
points = [3.4, 2.3, 5.5, 10, 10, 7.6, 8.9, 9, 1]

for i, (a,b) in enumerate(sorted(zip(letters, points), key=lambda x: x[1], reverse=True),start=1):
    print(i, a, b)          #Use enumerate() and zip() for paired iteration

print('-'*30)

print(type(lsi))
print(type(lsi[0]))
print(type(letters[0]))  
lsi[0] = float(lsi[0])      #Demonstrate type checking and conversions
print(type(lsi[0]))
