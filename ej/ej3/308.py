class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, some):
        self.balance += some

    def withdraw(self, b):
        self.balance -= b
        if self.balance < 0:
            print('Insufficient Funds')
        else:
            print(self.balance)
    

x,y = map(int, input().split())

n = Account('some', x)
n.withdraw(y)
