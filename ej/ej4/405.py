def decr(n):
    while n >= 0:
        yield n
        n -= 1
th = int(input())
fok = decr(th)
for i in fok:
    print(i)