class Room1:
    def __init__(self, length, breadth, height):  # Constructor
        print("Constructor Called")

        print(self)
        self.l = length
        self.b = breadth
        self.h = height

    def show(self):
        print("lenght, breadth, height is {}, {}, {}".format(self.l, self.b, self.h))

    print("------------------------------------------------------------------")

    def area(self):
        print("Volume is :", (self.l * self.b * self.h))


r = Room1(10, 20, 30)
print(r)
r.show()
r.area()
Room1.area(r)
del r  # Release the Memory Space by Destroy the object
# print(r) no refrence Found
