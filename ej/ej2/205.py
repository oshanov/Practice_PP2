n = int(input())
count, i = 0, 0

while n > 1:
    if n % 2 !=0 :
        print("NO")
        break
    n //= 2
else:
    print("YES")

