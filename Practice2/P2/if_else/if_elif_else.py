a = 'Apple'
b = 'apple'

if a == b:
    print("Equal")
elif a.lower() == b.lower():
    print("Equal to letters")
else:
    print(bool(0))

########################

score = int(input())

if score >= 95:
    print("\"A\"")
elif score >=90:
    print("\"A-\"")
elif score >=80:
    print("\"B\"")
elif score >=70:
    print("\"C\"")
else:
    print("\"C-\" or lower")

####################

age = int(input("Your age is ",))

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#######################

day = int(input())

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

