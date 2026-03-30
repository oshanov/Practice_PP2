n = int(input())
lsi = list(map(str, input().split()))

[print(f'{i}:{item}', end=" ") for i, item in enumerate(lsi) ]

