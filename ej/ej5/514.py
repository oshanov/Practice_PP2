import re

pattern = re.compile(r'^\d+$')


if pattern.fullmatch(input()) :
    print('Match')
else:
    print('No match')