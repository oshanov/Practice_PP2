import re

s = input()

x = re.findall(r'Name: (\w*\s*)', s)
y = re.findall(r',Age: (\d+)', s)
print(*x, *y)