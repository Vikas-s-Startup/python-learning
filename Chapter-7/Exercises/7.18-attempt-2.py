import random

def print_chess_board(board):
    print("----------------Chess Board-----------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print()
    print()

def print_chess_board_with_coordinates(board):
    print("----------------Chess Board with Cords-----------------")
    for row in range(0, len(board)):
        print("|", end=" ")
        for column in range(0, len(board)):
            print(f"{row},{column}", "|", end=" ")
        print()
    print()

def get_diagonal_coordinates(x, y, board_size):
    diagonal_coords = []

    # top left up
    row = x
    col = y
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        diagonal_coords.append([row, col])

    # top right up
    row = x
    col = y
    while row <= board_size-1 and col < board_size-1:
        row -= 1
        col += 1
        diagonal_coords.append([row, col])
    # bottom left down
    row = x
    col = y
    while row < board_size-1 and col >= 0:
        row += 1
        col -= 1
        diagonal_coords.append([row, col])

    # bottom right down
    row = x
    col = y
    while row < board_size-1 and col < board_size-1:
        row += 1
        col += 1
        diagonal_coords.append([row, col])

    return diagonal_coords

def get_column_coordinates(x, y, board_size):
    col_cords = []
    for i in range(0, board_size):
        if i != x:
            col_cords.append([i, y])
    # print(type(col_cords[0]))
    # print(col_cords[0][0], col_cords[0][1])
    return col_cords

def isSafe(boardSize, halfFilledBoard, x, y):
    temp_cords = get_column_coordinates(x, y, boardSize) + get_diagonal_coordinates(x, y,boardSize)
    for cord in temp_cords:
        if halfFilledBoard[cord[0]][cord[1]] == "Q":
            return False
    return True


def solve_queens_problem(queens_count, blank_board):
    random_first_row = random.randint(0, 7)
    blank_board[0][random_first_row] = "Q"
    for row in range(1, len(blank_board)):
        for block in range(len(blank_board[row])):
            if isSafe(queens_count, blank_board,row, block):
                blank_board[row][block] = "Q"
                break
    return blank_board


def main():
    queens_count = 8
    chess_board = [[' ' for _ in range(queens_count)] for _ in range(queens_count)]
    print_chess_board(board=chess_board)
    print_chess_board_with_coordinates(board=chess_board)
    # test_coordinates = [6,6]
    # print(f"Column coordinates for {test_coordinates} are: ",  get_column_coordinates(test_coordinates[0],test_coordinates[1], board_size=queens_count))
    # print(f"Diagonal Coordinates for {test_coordinates} are: ", get_diagonal_coordinates(test_coordinates[0],test_coordinates[1], queens_count))
    final_board = solve_queens_problem(queens_count, chess_board)
    print_chess_board(final_board)
    print("Program Finished")

main()