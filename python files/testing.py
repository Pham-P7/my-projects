board = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
slot = int(input("number"))
slot = int(slot - 1)
board[1][slot] = board[1][slot] + 1
print(board)