def func(n):
    cnt = 0
    while cnt <= n:
        if cnt % 2 == 0:
            yield cnt
        cnt += 1

x = int(input())
print(*func(x), sep=',')