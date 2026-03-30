n = int(input())

lsi = list(map(int, input().split()))
x = list(map(lambda x: x**2, lsi))
print(sum(x))