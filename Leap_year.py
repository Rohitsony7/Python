n=int(input("Enter any year to find wdhr the year is Leap year or not="))
def leep(n):
    if n%4==0 and n%400==0 and n%100==0:
        print(n," is a Leap Year")
    else:
        print("This is not a leap year")
    return
leep(n);