MyList = [1,2,4,5]
try:
    print("Result is : ",MyList[4])
except IndexError as E:
    print("We are in Except Block : ",E)


print("E.O.P")