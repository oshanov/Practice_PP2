import re

s = input()
p = input()

x = re.findall(p, s)
print(len(x))