n = int(input())
lsi = list(map(int, input().split()))

seen = set()

for i in lsi:
    if i in seen:
        print('NO')
    else:
        print('YES')
        seen.add(i)

        