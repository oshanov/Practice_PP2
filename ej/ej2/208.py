n,l,r = map(int, input().split())

lsi = list(map(int, input().split()))

lsi[l-1:r] = lsi[l-1:r][::-1]
print(*lsi)
