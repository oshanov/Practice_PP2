class Person:                                   #Original (Parent) class with methods
    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def get_data(self):
        print(f'{self.firstname} {self.secondname}')

someone = Person('Edward', 'Cowton')
someone.get_data()

####################################

class Student(Person):                          #Second (Child) class
    def __init__(self,firstname, secondname, year = 2029):           #Copying methods from Parent(inheritance)
        Person.__init__(self, firstname, secondname)
        self.year = year                                             #New properties

x = Student("Alisher", "Nurmukhamet", 2029)
print(x.year)

####################################

class Teacher(Person):
    def __init__(self, firstname, secondname, subject, exp):
        Person.__init__(self, firstname , secondname)
        self.subject = subject                                        #New properties
        self.exp = exp
    def __str__(self):
        return f'{self.firstname} {self.secondname} is a {self.subject} teacher, has been working since {self.exp} '

pdd = Teacher("Mans", "Pans", 'Math', 2001)
print(pdd)

###################################

        