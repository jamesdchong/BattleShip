def printBoard(board):
	""" Prints the player's current board

	Parameters
	----------
	board : str
		board of water and ships
	"""

	# Upper border
	print("\t  -------------------")

	for row in range(0,5):

		# Spacing
		print("\t ", end=" ")
		print("| ", end=" ")

		# Print either '~' (water), '#' (hit), 'm' (miss)
		for col in range(0,5):
			print(board[row][col] + " ", end=" ")

		# Spacing
		print("| ", end=" ")
		print("\n", end=" ")

	# Lower border
	print("\t  -------------------")
	print("\n")