num = int(input())
n = list(map(int, input().split()))

mx = n[0]
pos = 1
for i in range(num):
    if n[i] > mx:
        mx = n[i]
        pos = i + 1

print(pos)
