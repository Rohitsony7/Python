try:
    a=int(input("Enter any Real No."))
    b=int(input("Enter any Real No."))
except ValueError as E:
    print("Except Block",E)
else:
    print("The No. a is:",a)
    print("The No. b is:",b)
    print("Sum is",(a+b))
print("END OF PROGRAM !!")