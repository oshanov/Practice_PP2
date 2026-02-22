class Pair:
    a_sum = None
    b_sum = None
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def summa(self, other):
        self.a_sum = self.a + other.a
        self.b_sum = self.b + other.b

    def res(self):
        print(f'Result: {self.a_sum} {self.b_sum}')

a1,b1,a2,b2  = map(int, input().split())


p1 = Pair(a1,b1)
p2 = Pair(a2,b2)

p1.summa(p2)
p1.res()
