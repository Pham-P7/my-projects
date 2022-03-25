Winner = 0
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
            return 7
        if playerChoice in range(7,14):
            return playerChoice
        if playerChoice == 14:
            return 14
Inhand = "Filler"
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
    elif pit == 8:
        Inhand = P21
        P21 = 0
    elif pit == 9:
        Inhand = P22
        P22 = 0
    elif pit == 10:
        Inhand = P23
        P23 = 0
    elif pit == 11:
        Inhand == P24
        P24 = 0
    elif pit == 12:
        Inhand == P25
        P25 = 0
    elif pit == 14:
        Inhand == P26
        P26 = 0 
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
    elif pit == 8:
        Inhand = P11
        P11 = 0
    elif pit == 9:
        Inhand = P12
        P12 = 0
    elif pit == 10:
        Inhand = P13
        P13 = 0
    elif pit == 11:
        Inhand == P14
        P14 = 0
    elif pit == 12:
        Inhand == P15
        P15 = 0
    elif pit == 14:
        Inhand == P16
        P16 = 0 
def Player1Droping():
    Inhand -= 1
    pit += 1
    if pit == 2:
        P12 += 1
    elif pit == 3:
        P13 += 1
    elif pit == 4:
        P14 += 1
    elif pit == 5:
        P15 += 1
    elif pit == 6:
        P16 += 1
    elif pit == 7: #added to our Goal 
        P1G += 1
    elif pit == 8:
        P21 += 1
    elif pit == 9:
        P22 += 1
    elif pit == 10:
        P23 += 1
    elif pit == 11:
        P24 += 1
    elif pit == 12:
        P25 += 1
    elif pit == 13:
        P26 += 1
    elif pit == 14: #skipped their Goal
        P11 += 1
        pit = 1
def Player2Droping():
    Inhand -= 1
    pit += 1
    if pit == 2:
        P22 += 1
    elif pit == 3:
        P23 += 1
    elif pit == 4:
        P24 += 1
    elif pit == 5:
        P25 += 1
    elif pit == 6:
        P26 += 1
    elif pit == 7: #added to our Goal 
        P2G += 1
    elif pit == 8:
        P11 += 1
    elif pit == 9:
        P12 += 1
    elif pit == 10:
        P13 += 1
    elif pit == 11:
        P14 += 1
    elif pit == 12:
        P15 += 1
    elif pit == 13:
        P16 += 1
    elif pit == 14: #skipped their Goal
        P21 += 1
        pit = 1
Turn = True
while Winner == 0:
    #player 1 turn 
    while Turn == True:
        if player1list or player2list == [0,0,0,0,0,0]:
            Stop = True
        else:
            Stop = False
        if Stop == True:
            if P1G > P2G:
                Winner = 1
            elif P1G < P2G:
                Winner = 2
            break
        PrintPlayer1Grid()
        playerChoice = int(input("what slot will you pick? 1 - 6: "))
        Valid = "Filler"
        if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
            valid = True
        else:
            valid = False
        while Valid == False:
            playerChoice = int(input("invalid position please pick another: "))
            if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
                valid = True
            else:
                valid = False
        pit = PitFinder()
        FirstPickMarbles()
        while Inhand != 0:
            Player1Droping()
        while Inhand == 0:
            if pit == 7:
                playerChoice = int(input("please pick another: "))
            else:
                FirstPickMarbles()
                if Inhand <= 1:
                    Turn = not Turn
                    break
                else:
                    Player1Droping()
    #player 2 turn
    while Turn == False:
        if player1list or player2list == [0,0,0,0,0,0]:
            Stop = True
        else:
            Stop = False
        if Stop == True:
            if P1G > P2G:
                Winner = 1
            elif P1G < P2G:
                Winner = 2
            break
        PrintPlayer2Grid()
        playerChoice = int(input("what slot will you pick? 1 - 6: "))
        Valid = "Filler"
        if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
            valid = True
        else:
            valid = False
        while Valid == False:
            playerChoice = int(input("Take another turn 1 - 6: "))
            if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
                valid = True
            else:
                valid = False
        pit = PitFinder()
        SecondPickMarbles()
        while Inhand != 0:
            Player2Droping()
        while Inhand == 0:
            if pit == 7:
                playerChoice = int(input("Take another turn 1 - 6: "))
            else:
                SecondPickMarbles()
                if Inhand <= 1:
                    Turn = not Turn
                    break
                else:
                    Player2Droping()
if Winner == 1:
    print("Player 1 has won")
elif Winner == 2:
    print("Player 2 has won")