class Shape:
    def area(self):
        return 0
    
class Triangle(Shape):
    def __init__(self, lenght,width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width
    
n = tuple(map(int, input().split()))
(x,y) = n

defo = Triangle(x,y)
print(defo.area())