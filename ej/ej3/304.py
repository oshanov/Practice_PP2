class StringHandler:
    s = None
    def get_string(self):
        k = input()
        self.s = k
    
    def print_string(self):
        print(self.s.upper())

    
n = StringHandler()
n.get_string()
n.print_string()
