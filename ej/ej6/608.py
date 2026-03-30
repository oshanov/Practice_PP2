n = int(input())

st = set(map(int, input().split()))

print(*sorted(st, key= lambda x: x))