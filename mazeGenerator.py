import random

# script to generate mazes

size = 30
for i in range(0,size):
    for j in range(0,size):
        randomNumber = random.randint(1,12)
        print(randomNumber-2,end="",flush=True)
        if j is not 29:
            print(',', end="", flush=True)
    print("")
