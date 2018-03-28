import random
print(random.random())
print(random.randrange(1,101))

print("------------------------")

import math
def Math():
    print("Some of the Predefine Special")
    print("Value of pi : ",math.pi)
    print("Floor of 4.3 : ",math.floor(4.3))
    print("Ceil of 4.3 : ",math.ceil(4.3))
    print("square of 225  :",math.sqrt(225))
    print("Max among 1,2,3,4,5,6,7: ",max(1,2,3,4,5,6,7))
    print("Min among 1,242,4,6,45675,75 : ",min(1,242,4,6,45675,75,))
    print("ascii value of a",ord('a'))

    print("Char value of ascii  between 1-100:")
    for i in range(1,100):
        print(i,"=",chr(i),end=",")
    return
Math()