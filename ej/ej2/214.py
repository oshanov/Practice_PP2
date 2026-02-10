n = int(input())

a = list(map(int, input().split()))

most = a[0]

for x in a:
    if a.count(x)> a.count(most):
        most = x
    elif a.count(x) == a.count(most) and x < most:
        most = x


print(most)