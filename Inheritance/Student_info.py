class Myerror(Exception):
    pass


class Student():
    def __init__(self):
        print("Wel-come to the student Library")

    def Student_info(self, name, age, id):
        self.N = name
        self.A = age
        self.I = id

        print("Student's name =  {}, Age=  {} , Id= {}".format((self.N).upper(), self.A, self.I))


class Marks(Student):

    def subject(self, english, history, comsci):
        self.E = english
        self.H = history
        self.C = comsci

        print("Marks of {} in English = {}, History = {}, Comsci = {}  ".format(self.N, self.E, self.H, self.C))


class Percentage(Marks):
    def result(self):
        result = (self.E + self.H + self.C) / 3
        print("Percentage:", float(result), "%")
        if result >= 60:
            return "Result = First Division, PASS"
        elif 45 <= result < 60:
            return "Result = Second Division, PASS"
        elif 33 <= result < 45:
            return "Result = Third Division, PASS"
        else:
            return "Result = FAIL"


obj = Percentage()
while True:
    try:
        Name = (input("Enter Student's Name : "))
        Age = int(input("Enter Age :"))
        Id = int(input("Enter id : "))
        while True:
            try:
                E = int(input("Enter Marks in English:"))
                if E not in range(0, 101):
                    raise Myerror("Pls Enter your marks in between 0-100")
                H = int(input("Enter Marks in History:"))
                if H not in range(0, 101):
                    raise Myerror("Pls Enter your marks in between 0-100")
                C = int(input("Enter Marks in Compsci:"))
                if C not in range(0, 101):
                    raise Myerror("Pls Enter your marks in between 0-100")
                break
            except Myerror as v:
                print(v)
        break

    except  ValueError :
        print(" Pls Enter A valid Entry")
obj.Student_info(Name, Age, Id)
obj.subject(E, H, C)
print(obj.result())
