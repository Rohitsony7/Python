class Room2:

    color = "Yellow"
    def __init__(self,length,height,breadth): #  Constructor called
        print("Constructor Called")
        print(self)
        self.l = length
        self.h = height
        self.b = breadth

        print("length, breadth, height is {}, {}, {}".format(self.l, self.b, self.h))

r = Room2(10,20,30)

r1 = Room2(1,2,3)

print(r.l, r.h, r.b)
print(r1.l, r1.h, r1.b)

print(Room2.color)

Room2.color = "Black"

print(Room2.color)
print(r.color)
print(r1.color)

print(r.__dict__)
print(r1.__dict__)
print(Room2.__dict__)




