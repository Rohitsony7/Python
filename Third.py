#  Membership function
MyList = [1, 2, 3, 4, 5]
print(1 in MyList)
print('Rat' in MyList)

#  Identity operator
a = 10
b = 20
c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(id(b) is id(c))  # False, Is Compare only Value
print(id(b) == id(c))  # True, Compare both

