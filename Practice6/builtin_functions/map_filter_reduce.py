#map(function, iterable)  -  применяет функцию ко всем элементам

lsi = list(map(int, input().split()))
print(lsi)
#################

print(list(map(lambda x: x ** 2, lsi)))

print(list(map(lambda x: x - 5, lsi)))

words = ['apple', 'banana', 'cherry']
print(*list(map(lambda x: x.upper(), words)))


################################################

#filter(func, iterable)       Uses a filter function to exclude items in an iterable object(gives bool)

print(list(filter(lambda x: x % 2 == 0, lsi)))

print(list(filter(lambda x: len(x) > 5, words)))

print(list(filter(lambda x: x >= 7, lsi)))

################################################

from functools import reduce

#reduce(func, iterable)         Применяет функцию по очередности

print(reduce(lambda x, y: x + y, lsi))         
print(reduce(lambda x, y: x - y, lsi))         
print(reduce(lambda x, y: x*y, lsi))         


