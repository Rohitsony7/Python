class Employee:
    num_of_emp = 0
    raise_amount = 1.04


    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        self.email = last + "." + first + "." + '@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amount)
        return self.pay

emp_1 = Employee('Rohit', "soni", "70000")
emp_2 = Employee("Ronny", "L", "90000")

print(emp_1.fullname())
print(emp_1.email)
print(emp_1.apply_raise())

print(emp_1.__dict__)

print(emp_2.fullname())
print(emp_2.email)
print(emp_2.raise_amount)
print(emp_2.apply_raise())
print(Employee.num_of_emp)