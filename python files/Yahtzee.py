from random import randint
YN = input("do you wish to roll?")
playerOp = [[True,True,True,True,True,True,True,True,True,True,True,True,True] \
,[True,True,True,True,True,True,True,True,True,True,True,True,True]]
cat = ["Ace","Two","Three","Four","Five","Six"]
while(YN == "y" or YN == "Y" or YN == "yes" or YN == "yes"):
    Turn = True #set to false when next player's turn
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
        for i in rolls:
            c = i + 1
            while(c <= 5):
                if(rolls[i] != rolls[1] and rolls[i] == rolls[c]):
                    SdCount = SdCount + 1
                elif rolls[i] == rolls[c]:
                    sCount = sCount + 1
                c += 1
            
    if(Turn):
        print("These are your options")
        