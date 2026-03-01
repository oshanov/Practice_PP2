import re

txt = 'From: California : East Coast, Verg'
x= re.findall('^F.+:', txt)             #Greedy: largest possible string
print(x)

y = re.findall('^F.+?:', txt)           #Non-greedy: first 
print(y)