def showName():
    print("Hey Happy Ppl ")


showName();

print("--------------------------")


def Sum(x, y):  # arguments
    print("sum is-:", (x + y))  # Defination


Sum(2, 3)  # Function calling

print("--------------------------")


def show(MyList):
    print(MyList)
    MyList.insert(6, 3)
    MyList.append(12)
    print(MyList)


show([1, 2, 4, 5, 6])

print("--------------------------")


def show1(str):
    print(str)
    return


show1("Ruk jana nahi tu kahin har ke")

print("--------------------------")


def Student(name, id=1, branch="It"):
    print(name)
    print(id)
    print(branch)
    return


Student("rohit", 7, 'cse')
Student(id=4, name="Sony", branch="Cse")

print("--------------------------")


def Count(a, b, *value):
    print(a, b)
    for num in value:
        print(num)

    return


Count(1, 2, 3, 4, 5, 6, 7, 8, 9)

print("--------------------------")


def sum2(a, b):
    result = a + b
    return result
result=sum2(1,4)

def name():
    print("Ronny")
    return
    print("hi")
name();




