from ShipInfo import ShipInfo

def placeShip(player, ship, startX, startY, orientation):
	""" Places ship on player's board

	Parameters
	----------
	player : PlayerInfo
		player whose board a ship is being placed
	ship : ShipInfo
		ship to be placed on player's board
	startX : int
		starting x position of the ship
	startY : int
		starting y position of the ship
	orientation : int
		1 if horizontal, 2 if vertical

	Returns
	-------
	0 : int
		ship successfully placed
	-1 : int
		error placing ship
	"""

	# Ship names
	shipNames = ["DESTROYER", "SUBMARINE"]
	# Ship lengths
	shipLens = [2, 3]

	# If ship to be placed vertically
	if(orientation == 1):

		# Check if ship would go off the grid
		if(startY + shipLens[ship] > 5):
			return -1

		# Check if a square where the ship will go is water
		for row in range(startY, startY + shipLens[ship]):
			if(player.board[row][startX] != '~'):
				return -1

		# Replace water with # where the ship is placed
		for row in range(startY, startY + shipLens[ship]):
			player.board[row][startX] = '#'

	# If ship to be placed horizontally
	else:

		# Check if ship would go off the grid
		if(startX + shipLens[ship] > 5):
			return -1

		# Check if a square where the ship will go is water
		for col in range(startX, startX + shipLens[ship]):
			if(player.board[startY][col] != '~'):
				return -1

		# Replace water with # where the ship is placed
		for col in range(startX, startX + shipLens[ship]):
			player.board[startY][col] = '#'

	# Update information in ShipInfo object
	player.setShip(ship, shipNames[ship], startX, startY,
		           orientation, shipLens[ship], 0)

	return 0