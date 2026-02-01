for i in "Hello, World!":
    if i == ",":
        break
    print(i)

#####################

letters = ["a", "b", "c", "d", "e", "f"]
for x in letters:
  if x == "b":
     break
  print(x)

####################
food = ['apple', 'hamburger', 'kfc', 'salad', 'chips','water']

for item in food:
   if item == 'kfc':
      break
   print(item)

#####################
nums = [3, 5, 7, 8, 10]

for n in nums:
    if n % 2 == 0:
        print("first even:", n)
        break

#####################
nums = [1, 3, 5, 7]

for n in nums:
    if n % 2 == 0:
        print("even found")
        break
else:
    print("no even numbers")