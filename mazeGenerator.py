import random

# script to generate mazes

size = 650
decreaseVal = 0
for i in range(0,size):
    for j in range(0,size):
        randomNumber = random.randint(1,12)
        while randomNumber == decreaseVal:
            randomNumber = random.randint(1,size-2)
        if j%4 == 0:
            randomNumber = 2
        if j%7 == 0:
            randomNumber = 2
        if i < j+2 and i> j-2:
            if i%3 == 0:
                randomNumber = 1
        print(randomNumber-decreaseVal,end="",flush=True)
        if j is not size-1:
            print(',', end="", flush=True)
    print("")
