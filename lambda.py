sum = lambda a,b:a+b
print(sum(4,5))
print("---------------------------")

even = lambda a:a%2==0
print(even(44))

print("---------------------------")

reverse= lambda  str:str[::-1]
print(reverse("Rohit soni"))

MyList=[1,23,44,567,23]
MyList.sort(reverse=True)
print(MyList)

print("---------------------------")

even= lambda a: a%2==0
a=int(input("Enter any no"))
print(a," is even",even(a))

