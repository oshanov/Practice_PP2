from functools import reduce 
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = sum(a*b for a,b in zip(a,b))
print(dp)
