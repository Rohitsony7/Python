num=0
while num<10:
    num+=1
    print(num)
print("-----------------------------------------------")


num=1
while num<11:
    num1=1
    n=(input(""))
    if n=="":

        while num1<11:
            print(num*num1,end="\t")
            num1+=1
        num+=1
        print()

print("-----------------------------------------------")
import time
for i in range(1,11):
    time.sleep(1)
    for j in range(1,11):
       print(i*j,end="\t")
    print()

print("-----------------------------------------------")


for num in range(1,8):
    for num1 in range(8,num,-1):
        print("*",end="\t")
    print()
for num in range(2,8):
    for num1 in range(num):
        print("*",end="\t")
    print()





