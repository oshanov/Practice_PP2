class Person:                                   
    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def get_data(self):
        print(f'{self.firstname} {self.secondname}')

someone = Person('Edward', 'Cowton')
someone.get_data()

class Student(Person):                          
    def __init__(self,firstname, secondname, year = 2029):           
        super().__init__(firstname, secondname)                     #Inherits all the methods and properties from its parent
        self.year = year

x = Student("Alisher", "Nurmukhamet", 2029)
print(x.year)

class Teacher(Person):
    def __init__(self, firstname, secondname, subject, exp):
        super().__init__( firstname , secondname)
        self.subject = subject
        self.exp = exp
    def __str__(self):
        return f'{self.firstname} {self.secondname} is a {self.subject} teacher, has been working since {self.exp} '

pdd = Teacher("Mans", "Pans", 'Math', 2001)
print(pdd)


class Worker(Person):

    def __init__(self, firstname, secondname, salary_usd, work_type):
        super().__init__(firstname, secondname)
        self.salary_usd = salary_usd
        self.work_type = work_type
        self.workhours = []

    def add_hours(self, hours):
        self.workhours.append(hours)
        print(f'Added successfuly')

    def money(self):
        self.salary = self.salary_usd * sum(self.workhours)
        return self.salary
    
    def __str__(self):
        return f'{self.firstname} {self.secondname}, rate {self.salary_usd} dollars on {self.work_type} position'
    
w1 = Worker('Mattew', 'Maccounaghy', 100, 'Artist')
w1.add_hours(10)
w1.add_hours(1)
w1.add_hours(3)
print(w1.money())
print(w1)

#########################
