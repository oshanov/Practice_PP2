import re

x = re.sub(r'\d{1}', lambda m: m.group() * 2 , input())
print(x)