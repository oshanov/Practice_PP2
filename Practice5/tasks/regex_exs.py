import re

txt = input() #abbb
y = re.search('ab*', txt) 
if y:
    print('Yes')
######################
y = re.fullmatch('ab{2,3}', txt)
if y: 
    print("Yes")
else:
    print('NO')

######################

y = re.findall('[a-z]+_[a-z]+', txt)
print(y)

#######################

y = re.findall('[A-Z][a-z]*', txt)
print(y)

######################
lsi = list(input().split())
for i in lsi:
    if re.search('^a.*b$', i):
        print(i)

######################

y = re.sub(r'[ ,.]', '|' ,txt)
print(y)

#######################

y = re.sub(r'[_]', '', txt)
print(y)

########################

y = re.findall('[A-Z][a-z]*', txt)
print(*y)

#######################

y = re.sub(r'(?=[A-Z])',' ', txt)
print(y[1:])

########################
#myVarName
y = re.sub(r'(?=[A-Z])', '_', txt)
print(y)

    