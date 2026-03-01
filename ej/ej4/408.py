import math
def func(n):
    cnt = 0
    while cnt <= n:
        if is_prime(cnt):
             yield cnt
        cnt += 1

def is_prime(n):
            if n < 2:
                return False
            for i in range(2, math.isqrt(n) + 1):  
                if n % i == 0:
                    return False
            return True

i = int(input())
print(*func(i), sep=' ')