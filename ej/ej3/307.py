import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def show(self):
        print(f'({self.x}, {self.y})')
        # print(f'({self.new_x}, {self.new_y})')


    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        


    def dis_calc(self, other):
        return float(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2))
    
x,y = map(int, input().split())
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())




p1 = Point(x,y)
p1.show()

p1.move(x1,y1)
p1.show()

p2 = Point(x2,y2)
print(f'{p1.dis_calc(p2):.2f}')



