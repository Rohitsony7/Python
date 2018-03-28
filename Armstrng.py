a = int(input("Enter any no."))
def Armstrong(a):
    x = a // 100
    print("Ented No. is=", a)
    print("x=", x)
    b = a - x * 100
    y = b // 10
    print("y=", y)
    z = b - y * 10
    print("z=", z)
    sum = 0
    sum = sum + (x ** 3)
    sum = sum + (y ** 3)
    sum = sum + (z ** 3)
    print("Sum of x^3+y^3+z^3:", sum)
    if (sum == a):

        print("This no. is a Armstrong no:", sum)

    else:

        print("The no is not a Armstrong no.")
    return

Armstrong(a)