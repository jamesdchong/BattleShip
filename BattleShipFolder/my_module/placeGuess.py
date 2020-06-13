def placeGuess(player, xPos, yPos):
	""" Places player's guess on board

	Parameters
	----------
	player : PlayerInfo
		player who guessed
	xPos : int
		x position of guess
	yPos : int
		y position of guess
	"""
	
	# Print hit ship message if other player's board
	#   has a ship at that position
	if(player.otherPlayer.board[yPos][xPos] != '~'):
		player.guess[yPos][xPos] = '#'
		print("You've hit a ship!\n")

	# Print miss message if no ship at that position
	else:
		player.guess[yPos][xPos] = 'm'
		print("You missed!\n")


	for i in range(0, 2):

		# Set enemy to be the other player
		enemy = player.otherPlayer
		ship = enemy.ships[i]

		# If ship is already sunk, go to next iteration
		if(ship.sunk == 1):
			continue

		bad = 0
		sX = ship.startX
		sY = ship.startY
		ori = ship.orientation

		# Check if all of ship in horizontal position is all hit
		if(ori == 1):
			for y in range(sY, sY + ship.shipLen):
				if(player.guess[y][sX] != enemy.board[y][sX]):
					bad = 1
					break

		# Check if all of ship in vertical position is all hit
		else:
			for x in range(sX, sX + ship.shipLen):
				if(player.guess[sY][x] != enemy.board[sY][x]):
					bad = 1
					break

		# If entire ship is hit, sink ship, print ship sunk message
		if(bad == 0):
			ship.sunk = 1
			print("You sank a " + ship.name + "\n")
			break