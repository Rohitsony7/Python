class Demo:
    def __init__(self, __a, __b):
        self.__a = __a
        self.__b = __b
        print("Sum of {}, {} ".format(self.__a, self.__b), "is {}".format(self.__a + self.__b))

    def show1(self):
        print("Multiply is :", (self.__a * self.__b))


class useDemo(Demo):
    def use(self):
        print("We are in UseDemo class")

    def show(self):
        print("WE are in show Method")


obj = useDemo(11, 22)
obj.use()
obj.show()
obj.show1()