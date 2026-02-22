def isUsual(x):
    for b in [2,3,5]:
        while x % b == 0:
            x = x // b
        
    return x == 1

n = int(input())
if isUsual(n) == True:
    print('Yes')
else:
    print('No')