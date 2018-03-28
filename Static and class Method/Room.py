class Room:
    def __init__(self):
        print("Cons called")

    def show(self):
        print("Show method called")

    @ classmethod
    def showme(cls):
        print("Showme classMethod called")

    @ staticmethod
    def showmeToo():
        print("static Method called")
r1 = Room()
r1.show()
Room.show(self=r1)
Room.show(r1)

r1.showme()

Room.showme()

Room.showmeToo()
