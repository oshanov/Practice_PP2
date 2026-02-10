class Living:
    species = "Homo Sapiens"
    livingplanet = "Earth"

    def __init__(self,name,race,age):
        self.name = name
        self.race = race
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.race}, {self.age}, {self.livingplanet}, {self.species}'
    
    
    
first = Living('Mark', 'European', 27)
second = Living('Charles', 'African', 40)

print(first)
print(second)

#####################################
class Students:
    school = "KBTU"
    count = 0

    def __init__(self, name = None, GPA = None):
        self.name = name
        self.GPA = GPA
        Students.count += 1

s1 = Students()
s4 = Students()
s3 = Students()
s2 = Students()

print(Students.count)

###############################

    