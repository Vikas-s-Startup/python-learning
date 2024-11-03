def print_chess_board(board):
    print("----------------Chess Board-----------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print()
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(board, row, n):
    if row >= n:
        return True  # All queens are placed

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"  # Place queen
            if solve_n_queens(board, row + 1, n):  # Recur to place the next queen
                return True
            board[row][col] = " "  # Backtrack

    return False

def solve_queens_problem(n):
    board = [[" " for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")
    return board

def main():
    queens_count = 8
    final_board = solve_queens_problem(queens_count)
    print_chess_board(final_board)
    print("Program Finished")

main()
