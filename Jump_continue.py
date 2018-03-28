print("-------------------------------")
for i in range(1,11):
    print(i)
    if i%3!=0:
        break;

print("-----------------------------")
for x in range(0,11):
    for y in range(0,5):
        print(x,end=",")
        if x%3!=0:
            break;
    print()
print("-----------------------------")

for x in range(1,11):
    print(x)
    if x==5:
        continue
    print("*")

print("-----------------------------")

for a in range(0,11):
    for b in range(0,5):

        if(a%3!=0):
            print(a, end=",")
            continue
        print("*" ,end="")
    print(" ")

print("-----------------------------")


