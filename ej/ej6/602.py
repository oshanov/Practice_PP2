n = int(input())

lsi = list(map(int, input().split()))
even = filter(lambda x: x % 2 == 0, lsi)
print(len(list(even)))