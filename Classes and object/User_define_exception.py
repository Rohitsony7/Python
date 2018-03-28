class MyError(Exception):
    pass


try:
    a = int(input("Enter any no."))
    if a == 5  :
        raise MyError ("Wrong input 5, retry")
        print("We are in try blcok")
except MyError as v:
    print(v)
except ValueError as r:
    print(r)
else:
    result = 100/(a-5)
    print("Result is:",result)
print("E.O.P")


