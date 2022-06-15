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
        elif rolls[i] == 2:
            Two += 2
        elif rolls[i] == 3:
            Three += 3
        elif rolls[i] == 4:
            Four += 4
        elif rolls[i] == 5:
            Five += 5
        elif rolls[i] == 6:
            Six += 6
    