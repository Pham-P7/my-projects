P1G = 0 #rightside player 1
P2G = 0 #leftside player 2
#player 1
P11 = 4
P12 = 4
P13 = 4 
P14 = 4
P15 = 4
P16 = 4 
#player 2 
P21 = 4
P22 = 4
P23 = 4
P24 = 4
P25 = 4
P26 = 4
player1list = [P11,P12,P13,P14,P15,P16]
player2list = [P21,P22,P23,P24,P25,P26]
def PrintPlayer1Grid():
    print(f"P2 || {P26} || {P25} || {P24} || {P23} || {P22} || {P21} || ")
    print(f" {P2G} ================================ {P1G}")
    print(f"   || {P11} || {P12} || {P13} || {P14} || {P15} || {P16} || P1")
def PrintPlayer2Grid():
    print(f"P1 || {P16} || {P15} || {P14} || {P13} || {P12} || {P11} || ")
    print(f" {P1G} ================================ {P2G}")
    print(f"   || {P21} || {P22} || {P23} || {P24} || {P25} || {P26} || P2")
def PitFinder():
    if Turn == True:
        if playerChoice in range(0,6):
            return playerChoice
        if playerChoice == 7:
            return "goal 1"
        if playerChoice in range(7,13):
            return playerChoice
        if playerChoice == 13:
            return "goal 2"
def FirstPickMarbles():
    if pit == 1:
        Inhand = P11
        P11 = 0
    elif pit == 2:
        Inhand = P12
        P12 = 0
    elif pit == 3:
        Inhand = P13
        P13 = 0
    elif pit == 4:
        Inhand = P14
        P14 = 0
    elif pit == 5:
        Inhand = P15
        P15 = 0
    elif pit == 6:
        Inhand = P16
        P16 = 0
def SecondPickMarbles():
    if pit == 1:
        Inhand = P21
        P21 = 0
    elif pit == 2:
        Inhand = P22
        P22 = 0
    elif pit == 3:
        Inhand = P23
        P23 = 0
    elif pit == 4:
        Inhand = P24
        P24 = 0
    elif pit == 5:
        Inhand = P25
        P25 = 0
    elif pit == 6:
        Inhand = P26
        P26 = 0
Turn = True
while True:
    #player 1 turn 
    while Turn == True:
        if player1list or player2list == [0,0,0,0,0,0]:
            Stop = True
        else:
            Stop = False
        if Stop == True:
            break
        PrintPlayer1Grid()
        playerChoice = int(input("what slot will you pick? 1 - 6: "))
        Valid = "Filler"
        if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
            valid = True
        else:
            valid = False
        while Valid == False:
            playerChoice = int(input("invalid position please pick another"))
            if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
                valid = True
                pit = PitFinder()
                FirstPickMarbles()
            else:
                valid = False
    #player 2 turn
    while Turn == False:
        if player1list or player2list == [0,0,0,0,0,0]:
            Stop = True
        else:
            Stop = False
        if Stop == True:
            break
    if Stop == True:
        if P1G > P2G:
            Winner = 1
        elif P1G < P2G:
            Winner = 2
        break