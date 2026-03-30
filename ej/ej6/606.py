n = int(input())
lsi = list(map(int, input().split()))

if all(c >= 0 for c in lsi):
    print('Yes')
else:
    print('No')