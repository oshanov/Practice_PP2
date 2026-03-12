import re

s = input()
d = input()

print(*re.split(d,s), sep=',')