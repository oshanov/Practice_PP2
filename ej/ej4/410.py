def func(lsi, k):
    for _ in range(k):
        for i in lsi:
            yield i

lsi = list(input().split())
k = int(input())
print(*func(lsi,k))