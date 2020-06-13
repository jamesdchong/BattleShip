import random
from placeShip import placeShip

def autogenerateBoard(player):
	""" Automatically generates the playing boards with ships

	Parameters
	----------
	player : PlayerInfo
		player that the board is being generated for
	"""

	# Counter for number of ships already on board
	numShipsPlaced = 0

	# Loop until both ships are placed
	if(numShipsPlaced < 2):

		# Loop until auto placed ship is in valid location
		while(True):
			
			# Generate random X position
			rand1 = random.randrange(0,5)
			randomXPosition = rand1 % 5

			# Generate random Y position
			rand2 = random.randrange(0,5)
			randomYPosition = rand2 % 5

			# Generate random orientation
			rand3 = random.randrange(0,5)
			orientation = rand3 % 2

			# Place ship on board
			placedShip = placeShip(player, numShipsPlaced, randomXPosition,
								   randomYPosition, orientation)

			# If no error occurs, increment number of ships placed
			if(placedShip == 0):
				numShipsPlaced += 1

				# Break out of loop if 2 ships already placed
				if(numShipsPlaced >= 2):
					break