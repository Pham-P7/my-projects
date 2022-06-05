board = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
goal1 = 0
goal2 = 0
def print1stBoard():
    print(" ====================")
    board[0].reverse()
    print(" ",board[0])
    board[0].reverse()
    print(str(goal2) + " |================| " + str(goal1))
    print(" ",board[1])
    print(" ====================")
def print2ndBoard():
    print(" ====================")
    board[1].reverse()
    print(" ",board[1])
    board[1].reverse()
    print(str(goal1) + " |================| " + str(goal2))
    print(" ",board[0])
    print(" ====================")
def stoppingPoint():
    if board[0] == [0,0,0,0,0,0] or board[1] == [0,0,0,0,0,0]:
        return 1
    else:
        return 0
def winner():
    if goal1 > goal2:
        return 1
    elif goal2 > goal1:
        return 2
    else:
        return 0
turn = True
#player 1 is true 
winner = winner()
while winner == 0:
    while turn == True:
        stop = stoppingPoint()
        if stop == 1:
            break
        print1stBoard()
        board[0].reverse()
        slot =input("what slot will you pick?  1-6 ")
        slot = (int(slot) - 1)
        if slot not in range(6) or board[1][slot] == 0:
            valid = False 
        else:
            valid = True
        while valid == False:
            slot = int(input("what slot will you pick? 1-6 ") - 1)
            if slot not in range(6) or board[1][slot] == 0:
                valid = False
            else:
                valid = True
        inHand = board[1][slot]
        board[1][slot] == 0
        while valid == True:
            board[1][slot] += 1
            slot = int(slot + 1)
            if slot == 6:
                goal1 = goal1 + 1 
                inHand = inHand - 1
                while inHand != 0:
                    slot = 0
                    board[1][slot] += 1
                    slot = slot + 1
                    inHand -= 1 
            while inHand == 0:
                if board[1][slot] > 1:
                    inHand = board[1][slot]
                    board[1][slot] = 0
                if board[1][slot] == 1:
                    inHand = board[0][slot]
                    board[0][slot] = 0
                if slot == 7:
                    slot = int(input("what slot will you pick?  1-6"))
                    if slot not in range(7) or board[1][slot] == 0:
                        valid = False 
                    else:
                        valid = True
                if inHand == 0:
                    board[0].reverse()
                    turn = not turn
        print1stBoard()
#player 2's turn
    while turn == False:
        stop = stoppingPoint()
        if stop == 1:
            break
        print2ndBoard()
        board[1].reverse()
        slot = int(input("what slot will you pick?  1-6") - 1)
        if slot not in range(6) or board[0][slot] == 0:
            valid = False 
        else:
            valid = True
        while valid == False:
            slot = int(input("what slot will you pick? 1-6") - 1)
            if slot not in range(6) or board[0][slot] == 0:
                valid = False
            else:
                valid = True
        inHand = board[0][slot]
        board[1][slot] == 0
        while inHand != 0:
            slot += 1 
            board[0][slot] += 1
            inHand = inHand - 1
            if slot == 6:
                goal2 = goal2 + 1 
                inHand = inHand - 1
                while inHand != 0:
                    slot = -1
                    slot = slot + 1
                    board[0][slot] = board[0][slot] + 1 
                    inHand = inHand - 1
        while inHand == 0:
            if board[0][slot] < 1:
                inHand = board[0][slot]
                board[0][slot] = 0
            if board[0][slot] == 1:
                inHand = board[1][slot]
                board[1][slot] = 0
            if slot == 7:
                slot = int(input("what slot will you pick?  1-6"))
                if slot not in range(7) or board[0][slot] == 0:
                    valid = False 
                else:
                    valid = True
            if inHand == 0:
                board[1].reverse()
                turn = not turn
    winner = winner()
    if winner == 1:
        print("player 1 has won")
    if winner == 2:
        print("player 2 has won")