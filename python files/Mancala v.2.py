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
def PrintGrid():
    print(f"P2 || {P26} || {P25} || {P24} || {P23} || {P22} || {P21} || ")
    print(f" {P2G} ================================ {P1G}")
    print(f"   || {P21} || {P22} || {P23} || {P24} || {P25} || {P26} || P1")
while True:
    Turn = True
    #player 1 turn 
    while Turn == True:
        if player1list or player2list == [0,0,0,0,0,0]:
            Stop = True
        else:
            Stop = False
        if Stop == True:
            break
        PrintGrid()
        playerChoice = int(input("what slot will you pick? 1- 6"))
        Valid = "Filler"
        if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
            valid = True
            InHand = player1list[playerChoice - 1]
        else:
            valid = False
        while Valid == False:
            playerChoice = int(input("invalid position please pick another"))
            if playerChoice in range(1,7) and player1list[playerChoice - 1] != 0:
                valid = True
                InHand = player1list[playerChoice - 1]
            else:
                valid = False
        while 
