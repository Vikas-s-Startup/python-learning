def print_tic_tac_toe_board(board):
	print("-------------")
	for row in range(len(board)):
		for column in range(len(board[row])):
			print("|", board[row][column], sep=' ', end=' ')
		print("|", end='')
		print()
		print("-------------")


def did_player_win(board, playerOption, posRow, posColumn):
	# same column check
	playerWon = False
	if all(board[row][posColumn] == playerOption for row in range(3)):
		playerWon = True
		return playerWon

	# same row check
	if all(board[posRow][col] == playerOption for col in range(3)):
		playerWon = True
		return playerWon

	# top-left to bottom-right check && top-right to bottom-left check
	if posRow == posColumn:
		if all(board[i][i] == playerOption for i in range(3)):
			playerWon = True
			return playerWon

	return playerWon


def main():
	tic_tac_toe_board = [[" " for x in range(3)] for y in range(3)]
	print("Empty Board")
	print_tic_tac_toe_board(tic_tac_toe_board)

	playerAOption = 'X'
	playerBOption = '0'

	gameOver = False

	while not gameOver:
		# Player A's turn
		while True:
			playerARow = int(input("Enter a row for player A (X): "))
			playerAColumn = int(input("Enter a column for player A (X): "))
			# Check if the cell is empty
			if tic_tac_toe_board[playerARow][playerAColumn] == " ":
				tic_tac_toe_board[playerARow][playerAColumn] = playerAOption
				break  # Exit loop if position is valid
			else:
				print("Position already taken. Choose a different position.")

		print_tic_tac_toe_board(tic_tac_toe_board)

		if did_player_win(tic_tac_toe_board, playerAOption, playerARow, playerAColumn):
			print("Player A (X) won! Hurraaaay!")
			break

		# Player B's turn
		while True:
			playerBRow = int(input("Enter a row for player B (0): "))
			playerBColumn = int(input("Enter a column for player B (0): "))
			# Check if the cell is empty
			if tic_tac_toe_board[playerBRow][playerBColumn] == " ":
				tic_tac_toe_board[playerBRow][playerBColumn] = playerBOption
				break  # Exit loop if position is valid
			else:
				print("Position already taken. Choose a different position.")

		print_tic_tac_toe_board(tic_tac_toe_board)

		if did_player_win(tic_tac_toe_board, playerBOption, playerBRow, playerBColumn):
			print("Player B (0) won! Hurraaaay!")
			break


main()
