class Employee:
    """A sample class program"""

    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.pay = pay

    @property
    def emial(self):
        return "{}.{}.@gmail.com".format(self.second, self.first)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.second)

    @property
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.second, self.pay)
