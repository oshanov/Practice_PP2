class u:
    def __init__(self,name,age):
        self.name = name
        self.age = age

u1 = u('Ali', 18)


print(u1.name)
print(u1.age)

########################### if we do it without __init__ then
class person:
    name = None
    age = None

p1 = person()
p1.name = 'Ali'
p1.age = 18

print(p1.name)
print(p1.age)

##########################

class student:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

        self.get_data()
    
    def get_data(self):
        print(self.name, self.age)

stu1 = student('Mark')

############################

class sub:
    def __init__(self, name = None, time = '8 AM'):
        self.name = name
        self.time = time

geo = sub('Geography')
mat = sub('Math', '10 AM')
print(geo.name, geo.time)
print(mat.name, mat.time)

############################

class Cat:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

cat1 = Cat()
print(cat1.name, cat1.age)

##########################
class Person:
  species = "Human"

  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Didar", 17, "Qyzylorda", "Kazakhstan")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
print(p1.species)


