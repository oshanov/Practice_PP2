import re

n = input()

mail = re.search(r'\S+@\w*\.\S+', n)

if mail:
    print(mail.group())
else:
    print('No email')