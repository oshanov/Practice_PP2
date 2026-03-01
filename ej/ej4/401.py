def func(n):
    cnt = 1
    while cnt <= n:
        yield cnt**2
        cnt += 1

x = int(input())
lok = func(x)
for i in lok:
    print(i)