n = int(input())
k = list(map(str, input().split()))
v = list(map(str, input().split()))


d = dict(zip(k, v))

some = input()

if some in d:
    print(d[some])
else:
    print('Not found')