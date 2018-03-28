n=int(input("Enter a no. till  you want to find  print prime no \n"))
for i in range(2,n+1):
    count=0
    for j in range(1,n+1):
        if i%j is 0:
            count+=1
    if count is 2:
        print(i,end=",")
print(" ")
