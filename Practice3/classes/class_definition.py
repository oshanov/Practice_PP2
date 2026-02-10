class MyClass:
    x = 5
    name = 'Charlie'
p1 = MyClass()
print(p1.name)

p2 = MyClass()
print(p2.x)




class Dogs:
    voice = "Raw, raw"
    food = "Bones"

d1 = Dogs()
print(d1.food)
print(d1.voice)

#####################
class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name)
        print(self.age)
        print(self.isHappy)

cat1 = Cat()
cat1.set_data('Bars', 3,True)
cat1.get_data()