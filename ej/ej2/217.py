n = int(input())
lsi = dict()

for i in range(n):
    a = input()
    if a in lsi:
        lsi[a] += 1
    else:
        lsi[a] = 1

counts = 0

for i in lsi.values():
    if i == 3:
        counts +=1

print(counts)
