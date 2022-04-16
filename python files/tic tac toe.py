
from operator import index
from random import randint #used in createOrder() function to randomize if player1 or player2 goes first


#determines if player1 or player2 goes first by "flipping a coin."
#returns True if player1 goes first and False if player2 goes first.
def createOrder():
    print('You are player 1. I will flip a coin to determine who goes first.')
    s = ""
    
    while s not in ['h', 't']:
        s = input('Heads or Tails? (type h or t): ').lower()
    if s == 'h':
        print('You picked heads.')
    else:
        print('You picked tails.')
        
    print('\nNow flipping the coin...')
    rand = randint(0,1)
    if rand == 0:
        print('The coin landed on heads!')
        p1first = s == 'h'
    else:
        print('The coin landed on tails!')
        p1first = s == 't'
        
    if p1first:
        print('\nPlayer 1 goes first.')
        return True
    else:
        print('\nPlayer 2 goes first.')
        return False

#prints the elements in the tictactoe board in the proper tictactoe formatting
def printGrid():
    print()
    for i,row in enumerate(grid):
        line = "|".join(row)
        print(line)
        if(0<=i<=1):
            print("-----")
    print()

#clears the elements in the tictactoe board
def clearGrid():
    for row in range(0,3):
        for col in range(0,3):
            grid[row][col] = ' '

#checks to see if either player1 or player2 has won the game
#returns '0' if neither player has won yet, '1' if player1 wins, '2' if player2 wins, and '3' if there is a tie
def checkWinner():
    for row in grid:
        if "".join(row) == "XXX":
            return 1
        elif "".join(row) == 'OOO':
            return 2
    for i in range(0,3):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == 'X':
                return 1
            elif grid[0][i] == 'O':
                return 2
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == 'X':
            return 1
        elif grid[0][0] == 'O':
            return 2
    if grid[2][0] == grid[1][1] == grid[0][2]:
        if grid[2][0] == 'X':
            return 1
        elif grid[2][0] == 'O':
            return 2
    for row in grid:
        for i in row:
            if i == ' ':
                return 0
    return 3

'''
Start code under here! I initialized the grid variable so that there are no errors when
initially saving the code, but you'll need to change it to a 2d list so that it functions
as a 2d grid instead of a 1d list.
'''
grid = [["1","2","3"],["4","5","6"],["7","8","9"]]
#my functions
def Avalue():
    return int(ind // 3.5)
def Bvalue():
    if ind in range(0,4):
        return int((ind // 1) -1) 
    if ind in range(4,7):
        return int(ind % 4)
    if ind in range(7,10):
        return int(ind % 7)
def ValidOptions():
    if ind not in range(0,10) or grid[a][b] != ' ':
        return False
    else:
        return True 
def EndingPhrase():
    grid[a][b] = player_symbol
    printGrid()
    checkWinner()
    winner = checkWinner()
#started code
turn = createOrder()
printGrid()
clearGrid()
winner = checkWinner()
while winner == 0:
    printGrid()
    hold = ""
    ind = 0
    if turn == True:
        while turn == True:
            print("player 1's turn")
            player_symbol = "X"
            ind = int(input("pick an index 1-9 "))
            a = Avalue()
            b = Bvalue() 
            valid = ValidOptions()
            if valid == False:
                while valid == False:
                    print("Please enter a valid index")
                    ind = int(input("pick an index 1-9:"))
                    a = Avalue()
                    b = Bvalue()
                    valid = ValidOptions()
            EndingPhrase()
            if winner != 0:
                break
            turn = not turn
    else:
        while turn == False:
            print("player 2's turn")
            player_symbol = "O"
            ind = int(input("pick an index 1-9 "))
            a = Avalue()
            b = Bvalue()
            valid = ValidOptions()
            if valid == False:
                while valid == False:
                    print("Please enter a valid index")
                    ind = int(input("pick an index 1-9:"))
                    a = Avalue()
                    b = Bvalue()
                    valid = ValidOptions()
            EndingPhrase()
            if winner != 0:
                break
            turn = not turn
    checkWinner()
    winner = checkWinner()
    if winner != 0:
        break
if winner == 1:
    print("player 1 has won")
elif winner == 2:
    print("player 2 has won")
else:
    print("its a tie")