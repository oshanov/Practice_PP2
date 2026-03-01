def luk(a,b):
    cnt = a
    while cnt <= b:
        yield cnt ** 2
        cnt += 1
a,b = map(int, input().split())
bor = luk(a,b)
for i in bor:
    print(i)