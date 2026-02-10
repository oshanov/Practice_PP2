class Person:
  def __init__(self, name): #method
    self.name = name 

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Ali")
p1.greet()


##########################
class Celeb:
    def __init__(self, name, type = 'Interpreneur'):
       self.name = name
       self.type = type
    
    def get_data(self):
       print(self.name, "-",self.type)

    def greet(self):
       print(f'Welcome our guest - {self.name}, he is our {self.type}!')

jo = Celeb('Kairat Nurtas', 'Singer')
jo.greet()
j2 = Celeb('Beibit Alibekov')
j2.greet()

###########################

class Calculator:
   
    def __init__(self,a,b):
       self.a = a
       self.b = b

    def sum(self,a,b):
        return a + b
   
    def mult(self,a,b):
        return a * b
    
task1 = Calculator(5,2)
print(task1.sum(5,2))
print(task1.mult(5,2))

##############################

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Ali", 18)
print(p1.get_info())

#################################
class Human:
    def __init__(self,name,age):
      self.name = name
      self.age = age

    def celebrate(self):
      self.age += 1
      print(f'Happy birthday, {self.name}! You are now {self.age}')

    def __str__(self):
       return f'Info: {self.name}, {self.age}'

male = Human('Mansur', 18)
male.celebrate()
male.celebrate()
male.celebrate()
print(male)

##########################
class Stud:
    def __init__(self,name,age):
      self.name = name
      self.age = age
    def __str__(self):
      return f'{self.name}, {self.age} years old'
    
me = Stud("Ali", 18)
print(me)