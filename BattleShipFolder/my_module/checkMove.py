def checkMove(guess, xPos, yPos):
	""" Check if the guess is valid

	Parameters
	----------
	guess : str
		player's guess of hitting a ship
	xPos : int
		x position of guess
	yPos : int
		y position of guess

	Returns
	-------
	0 : int
		guess not valid
	1 : int
		guess valid
	"""

	# Return 0 if x position or y position are not valid
	if(xPos not in range(0, 5) or yPos not in range(0, 5)):
		return 0

	# Return 0 f the guessed position is not water
	if(guess[yPos][xPos] != "~"):
		return 0

	return 1