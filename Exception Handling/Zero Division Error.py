import sys
try:
    a=float(input("Enter any  No."))
    result = 100 / a

except :
    print("We are in except Block:",sys.exc_info())

else:
    print("Result is",result)


print("E.O.P")