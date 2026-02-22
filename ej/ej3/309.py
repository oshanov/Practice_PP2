class Circle:
    area = None
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = float(self.pi * self.radius**2)
        print(f'{self.area:.2f}')

n = int(input())
si = Circle(n)
si.area()
