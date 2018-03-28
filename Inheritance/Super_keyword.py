class Demo:
    def __init__(self, a, b):
        print("Dmeo's class Constructor called")
        self.a = a
        self.b = b

    def sum(self):
        print("Sum id", (self.a + self.b))
o = Demo(1,2)
o.sum()

class useDemo(Demo):
    def __init__(self, c):
        super().__init__(11, 22)
        self.c = c

    def small(self):
        print(self.c)


obj = useDemo(100)
obj.small()
obj.sum()
