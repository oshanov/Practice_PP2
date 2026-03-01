class Reverse:
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

i = input()
word = Reverse(i)
print(*word,sep='')

