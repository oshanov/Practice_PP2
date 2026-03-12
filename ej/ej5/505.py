import re

n = input()

if re.search(r'^\w.*\d$', n):
    print('Yes')
else:
    print('No')