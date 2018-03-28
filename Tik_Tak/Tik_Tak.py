print("Welcome to Tik_Tak-Toe Game")
print("_ 1_|_2_|_3_\n_ 4_|_5_|_6_\n  7 | 8 | 9 ")

while True:
    user1 = input("Do you want to be X or O :",)
    print("You have Entered:", user1.upper())
    if user1=='x' or user1=='o' or user1=='O' or user1 =='X' or user1 =='0':
         break
    else:
        print("You have entered Wrong input, Try Once Again:")
        print()

input=print(" What is your Move(0-9) ")



