global boardSize

boardSize = 4

def printSolution(board):
    for i in range(boardSize):
        for j in range(boardSize):
            if board[i][j] == 1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()

