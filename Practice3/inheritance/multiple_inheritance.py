class Walker:
    def walk(self):
        return "I can walk"

class Swimmer:
    def swim(self):
        return "I can swim"

class Amphibian(Walker, Swimmer):
    pass


frog = Amphibian()

print(frog.walk())
print(frog.swim())


###########################


class Student:
    def study(self):
        return "Studying"

class Worker:
    def work(self):
        return "Working"

class WorkingStudent(Student, Worker):
    def rest(self):
        return "Resting"


person = WorkingStudent()

print(person.study())
print(person.work())
print(person.rest())


####################################


class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print("My name is", self.name)

class Worker:
    def __init__(self, spec, salary):
        self.spec = spec
        self.salary = salary

class Student(Person, Worker):
    def __init__(self, name, major, spec, salary):
        Person.__init__(self, name)
        Worker.__init__(self, spec, salary)
        self.major = major
    
    def study(self):
        print(self.name, "studies", self.major)

    def work(self):
        print(self.name, 'works', self.spec, 'and receives', self.salary)

    def info(self):
        print(self.name, self.major, self.spec, self.salary)

s = Student("Ali", "Engineering", 'Physics Teacher', 100)

s.introduce()
s.study()
s.work()
s.info()

