import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime()))
Hour=0
min= 0
import os
while True:
    for Hour in range(23,24):
        for min in range(3,60) :
            for i in range(0,60):
                time.sleep(1)
               # print(i)
                print("Hour:min:sec", Hour,":",min,":",i)
                os.system('cls')

