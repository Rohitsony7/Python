try:
    a=int(input("Enter any No. except 5 :"))
except ValueError as E:
    print(E)

try:
    if a==5:
        raise Exception("Wrong input, Retry!!")
    print("We are in try block")
except Exception as V:
    print(V)
else:
    result = 100/(a-5)
    print("RESULT:",result)

print("E.O.P")