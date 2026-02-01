num = 10
i = 0
while i <= num:
    i += 1
    if i % 2 == 1:
        continue
    print(i)

#####################
food = ['apple', 'hamburger', 'kfc', 'salad', 'chips','water']
i = 0
while i < len(food):
   
    if food[i] == 'hamburger' or food[i] == 'kfc' or food[i] == 'chips':
        i += 1
        continue

    print(food[i])
    i += 1

#################
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#########################

while True:
    x = int(input("enter positive number: "))
    if x <= 0:
        print("skip")
        continue
    print("accepted:", x)