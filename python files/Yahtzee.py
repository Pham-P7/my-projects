from operator import index
from random import randint
YN = input("do you wish to roll?")
while(YN == "y" or YN == "Y"):
    rolls = []
    Ace = 0
    Two = 0
    Three = 0
    Four = 0
    Five = 0
    Six = 0
    for i in range(0,6):
        roll = randint(1,6)
        rolls.append(roll)
    rolls.sort()
    print(rolls)
    for i in range(0,6):
        if rolls[i] == 1:
            Ace += 1
        if rolls[i] == 2:
            Two += 2
        if rolls[i] == 3:
            Three += 3
        if rolls[i] == 4:
            Four += 4
        if rolls[i] == 5:
            Five += 5
        if rolls[i] == 6:
            Six += 6
    