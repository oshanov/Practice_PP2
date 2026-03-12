#enumerate(iterable)        Преврещает любой список в счетчик

lsi = list(map(int, input().split()))

for i, item in enumerate(lsi, start=1):
    print(f'{i} элемент - {item}')


words = ['apple','dragon fruit', 'banana', 'cherry', 'kiwi', 'melon', 'watermelon']

for i, item in enumerate(sorted(words, key=lambda x: len(x)), start=1):
    print(f'{i}-th ascending element is {item}')

some = [2,5,3,6,84,9,1]
for i, item in enumerate(some, start=1):
    print(i, item)

########################################################
#zip(first, second)         Склеивает списки в кортеж (эл.первого , эл.второго)

x = zip(lsi, words)
print(*x)

y = zip(words, lsi)
print(*y)

names = ["Ali", "John"]
ages = [19, 25]

result = zip(names, ages)

print(*(result), sep='|')

print(*zip(some, lsi))

###############################################################
#sorted(iterable, key=func, reverse=bool)

print(sorted(sorted(words, key= lambda x: len(x) > 3)))

print(sorted(lsi, reverse=True))

