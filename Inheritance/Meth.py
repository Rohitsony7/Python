import math


class Meth:
    def __init__(self, x, y):
        print("Cons called")
        self.num1 = x
        self.num2 = y

    def sum(self):
        print("sum of {} and {} is {}".format(self.num1, self.num2, self.num2 + self.num1))


class Mymeth(Meth):
    def getPower(self, x, y):
        self.num1 = x
        self.num2 = y
        print('power is', pow(self.num1, self.num2))

    def getSqrt(self):
        print("sqrt is", math.sqrt(self.num2 * self.num1))


obj = Mymeth(55, 66)
obj.sum()
obj.getPower(5, 5)
obj.getSqrt()
