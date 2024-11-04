import random

queens_count = 8

def is_safe(board, row, col):
    # Check this column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < queens_count:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve_queens(board, row):
    if row >= queens_count:
        return True

    # Generate a random order of columns to try
    columns = list(range(queens_count))
    random.shuffle(columns)

    for col in columns:
        if is_safe(board, row, col):
            board[row][col] = "Q"
            if solve_queens(board, row + 1):
                return True
            board[row][col] = " "  # Backtrack

    return False

def print_chess_board(board):
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print()

def main():
    chess_board = [[' ' for _ in range(queens_count)] for _ in range(queens_count)]
    if solve_queens(chess_board, 0):
        print("Unique solution found:")
        print_chess_board(chess_board)
    else:
        print("No solution exists")

main()
