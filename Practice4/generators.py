#First task: Create a generator that generates the squares of numbers up to some number N.
def func(n):
    count = 1
    while count <= n:
        yield count**2
        count += 1
    
x =int(input())
lol = func(x)
for i in lol:
    print(i)

#Second task:Write a program using generator to print the
#even numbers between 0 and n in comma separated form where n is input from console.
def dunk(n):
    cnt = 1
    while cnt <= n:
        if cnt % 2 == 0:
            yield cnt
        cnt += 1
y = int(input())
kol = dunk(y)
for i in kol:
    print(i, sep=',')
#Third task:Define a function with a generator 
#which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def punk(n):
    count = 1
    while count <=n:
        if count % 3 == 0 and count % 4 == 0:
            yield count
        count += 1
z = int(input())
lok = punk(z)
for i in lok:
    print(i)
#Fourth task:Implement a generator called squares to yield the square of all numbers from (a) to (b).
#Test it with a "for" loop and print each of the yielded values.
def luk(a,b):
    cnt = a
    while cnt <= b:
        yield cnt ** 2
        cnt += 1
a,b = map(int, input().split())
bor = luk(a,b)
for i in bor:
    print(i)
#Fifth task: Implement a generator that returns all numbers from (n) down to 0.
def decr(n):
    while n >= 0:
        yield n
        n -= 1
th = int(input())
fok = decr(th)
for i in fok:
    print(i)