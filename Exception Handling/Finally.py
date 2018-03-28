try:
    obj = open("Demo.txt",'r')
    obj.write("Demo of file handling in python")
except ZeroDivisionError as E:
    print(E)


finally:
    print("We are in Finally Block")
    obj.close() #  clean up code

print('E.O.P')
