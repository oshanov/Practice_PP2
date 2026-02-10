n = int(input())
lsi = dict()

for i in range(n):
    a, b = input().split()
    b = int(b)
    if a in lsi:
        lsi[a] +=b
    else:
        lsi[a] = b

sorted_lsi = dict(sorted(lsi.items(), key=lambda x: (x[0])))

for k, v in sorted_lsi.items():
    print(k,v)