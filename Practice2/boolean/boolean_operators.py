def myFunction() :
  return True

print(myFunction())

###################

print(bool("Hello"))
print(bool(15))

###################

if bool(10) != bool(100000000000000000000000):
    print(bool(1))
else:
   print(bool(""))

###################

class myclass():
  def __len__(self):
    return 1

myobj = myclass()
print(bool(myobj))

###################

def somefunc(x):
   if x > 0 or x == 0:
      return 1
   else:
      return 0
print(bool(somefunc(100)))

######################
x = 200
print(isinstance(x, int)) #If data type is equal => True