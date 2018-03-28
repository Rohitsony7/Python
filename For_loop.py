MyList = [3, 1, 1, 1, 1, 1, 1, 1,1,1,1,1,1,1,1,1]
print(len(MyList))
Sum=0
for i in MyList:
    Sum=Sum+i
print(Sum)
print(Sum/len(MyList))
 #  --------------------------------------------------
print("-----------------------------------------------")

MyList1 = [(11, 22), (33, 44), (55, 66)]
MyList2 = [(1, 2), (3, 4), (5, 6)]
print("Matrix A is")
A=0
B=0
for i, j in MyList1 :
    A=A+i
    B=B+j
    print(i,j)
print("------")
print(A,B)

print("-----------------------------------------------")

MyDictionary={1:'one', 2:'Two', 3:'Three'}
for (i,j) in  MyDictionary.items():
    print(i, j)

Str="Hi this is rohit soni"
for i in Str:
    print(i,end=',')
print()
print("-----------------------------------------------")

for i in range(1,8):
    print(i," times one are :",i)
print("-----------------------------------------------")
n=int(input("Enter a no. till you want to print odd no."))
for i in range(1,n+1,2):  #""" Here is last 2, shows the increment by 2 in loop"""
    print(i,end=",")
print()
print("-----------------------------------------------")




