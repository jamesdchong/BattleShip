def checkWin(player):
	""" Checks if player sunk all of other player's ships

	Parameters
	----------
	player : PlayerInfo
		player being checked for win

	Returns
	-------
	0 : int
		player did not win
	1 : int
		player won
	"""

	# Define enemy to be the other player
	enemy = player.otherPlayer

	# Check if all of other player's ships are sunk
	for shipIdx in range(0, 2):
		if(enemy.ships[shipIdx].sunk == 0):
			return 0

	return 1