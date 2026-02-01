i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

##############

jedi = [True, True, False, True]

i = 0
while i < len(jedi):
    if jedi[i] == False:
       break
    i += 1
print(i)

#############
numbers = [3, 7, 10, 15, 20]
i = 0

while i < len(numbers):
    if numbers[i] == 10:
        print(f"Found at {i}!")
        break
    i += 1
#############
while True:
    password = input("Enter password: ")
    if password == "1234":
        print("Access granted")
        break