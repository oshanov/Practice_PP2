for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#########################
food = ['apple', 'hamburger', 'kfc', 'salad', 'water']

for item in food:
    if item == 'kfc':
        continue
    print(item)

##########################
food = ['apple', 'hamburger', 'kfc', 'salad', 'chips']
banned = ['hamburger', 'kfc', 'chips']
for item in food:
    if item in banned:
        continue
    print(item)

#########################

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)