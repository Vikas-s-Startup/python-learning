import random

queens_count = 8


def print_chess_board(board):
    print("----------------Chess Board-----------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print()


def print_chess_board_with_coordinates(board):
    print("----------------Chess Board with Cords-----------------")
    for row in range(0, len(board)):
        print("|", end=" ")
        for column in range(0, len(board)):
            print(f"{row + 1},{column + 1}", "|", end=" ")
        print()


def get_diagonals(row, col):
    n = queens_count  # Size of the matrix (N x N)
    diagonals = []

    # Move up and left
    r, c = row - 1, col - 1
    while r >= 1 and c >= 1:
        diagonals.append([r, c])
        r -= 1
        c -= 1

    # Move up and right
    r, c = row - 1, col + 1
    while r >= 1 and c <= n:
        diagonals.append([r, c])
        r -= 1
        c += 1

    # Move down and right
    r, c = row + 1, col + 1
    while r <= n and c <= n:
        diagonals.append([r, c])
        r += 1
        c += 1

    # Move down and left
    r, c = row + 1, col - 1
    while r <= n and c >= 1:
        diagonals.append([r, c])
        r += 1
        c -= 1

    return diagonals


def get_column_coordinates(x, y):
    col_cords = []
    for i in range(0, queens_count + 1):
        if i != x:
            col_cords.append([i, y])
    return col_cords


def print_debug():
    print_chess_board(chess_board)
    print_chess_board_with_coordinates(chess_board)
    a, b = 6, 7
    column_coordinates = get_column_coordinates(a, b)
    diag_coordinates = get_diagonals(a, b)
    print(f"Column Coordinates for {a},{b}: ", column_coordinates)
    print(f"Diagonal Coordinates for {a},{b}: ", diag_coordinates)

    # for c in diag_coordinates:
    #     print(type(c))
    #     print(c[0], c[1])


# Function to check if a queen can be placed at (row, col)
def is_safe(board, row, col):
    # Check for queens in the same column
    print(row, col)
    print("location test ",board[row][col])
    column_coordinates = get_column_coordinates(row, col)
    print(len(column_coordinates))

    for cord in range(0, len(column_coordinates)+1):
        print(column_coordinates[cord][0], column_coordinates[cord][1])


    # Check for queens in the diagonals
    diagonal_coordinates = get_diagonals(row, col)
    for diag_cord in range(0, len(diagonal_coordinates) + 1):
        if board[diag_cord][0][1] == 'Q':
            return False

    return True


def place_queens_randomly(board):
    # Place the first queen randomly
    col = random.randint(0, queens_count-1)
    board[0][col] = 'Q'

    # Place the remaining queens
    for row in range(1, len(board) + 1):
        queen_placed = False
        while not queen_placed:
            col = random.randint(0, queens_count + 1)
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                queen_placed = True
    return board


def main():
    # print_debug()

    final_board = place_queens_randomly(chess_board)
    print_chess_board(final_board)


chess_board = [[' ' for _ in range(queens_count)] for _ in range(queens_count)]
main()
