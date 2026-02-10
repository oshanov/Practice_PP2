class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):                    #Origin method called move()
        print('Move!')

class Car(Vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)

    def move(self):                    #Overriding origin method in Child class(same move())
        print('Drive!')

class Boat(Vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)
    
    def move(self):                    #Overriding origin method in Child class(same move())
        print('Sail!')

class Plane(Vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)
    
    def move(self):                     #Overriding origin method in Child class(same move())
        print("Fly!")

car1 = Car('Toyota', 'Camry')
boat1 = Boat('Ibiza', 'Touring 700')
plane1 = Plane('Boeing', '777')

for x in (car1, boat1, plane1):
    print(x.name, x.model)
    x.move()
print("""###########################
""")
###########################
class Person:                                   
    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def Hobby(self):
        print('Hobby')

    def get_data(self):
        print(f'{self.firstname} {self.secondname}')

class Student(Person):                          
    def __init__(self,firstname, secondname, year = 2029):          
        Person.__init__(self, firstname, secondname)
        self.year = year  

    def Hobby(self):
        print('Playing games!')  

class Teacher(Person):
    def __init__(self, firstname, secondname, subject, exp):
        Person.__init__(self, firstname , secondname)
        self.subject = subject                                        
        self.exp = exp

    def Hobby(self):
        print('Reading!')

    def __str__(self):
        return f'{self.firstname} {self.secondname} is a {self.subject} teacher, has been working since {self.exp} '

student1 = Student('William', 'Defo', 2029)
teacher1 = Teacher('Yerjan', 'Buleshov', 'Math', 2005)

for x in (student1, teacher1):
    print(type(x))
    print(x.firstname, x.secondname)
    x.Hobby()
    print()

##################################


class Animal:
    def speak(self):
        print('Animals make sound')

class Dog(Animal):
    def speak(self):
        print('Dog is barking')

class Cat(Animal):
    def speak(self):
        print("Cat is meowing")

class Horse(Animal):
    def speak(self):
        print('Horse is neighing')

d1,c1,h1 = Dog(), Cat(),Horse()
for x in (d1,c1,h1):
    x.speak()

