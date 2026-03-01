import re

txt = 'The rain in the Spain'
y = re.search(r'S\w+', txt)
print(y.span())             #returns a tuple containing the start-, and end positions of the match.

print(y.string)             #returns the string passed into the function

print(y.group())            #returns the part of the string where there was a match

print(y.start())            #returns start position