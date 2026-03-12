import re

n = input()

l = re.findall(r'\d', n)
print(*l)
