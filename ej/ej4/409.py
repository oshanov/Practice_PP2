def func(n):
    cnt = 0
    while cnt <= n:
        yield 2**cnt
        cnt += 1
    
i = int(input())
print(*func(i))