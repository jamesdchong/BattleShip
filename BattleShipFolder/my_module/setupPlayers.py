from setupBoards import setupBoards

def setupPlayers(player1, player2):
	""" Method that sets up and populates player 1 and player 2 with info

	Parameters
	----------
	player1 : PlayerInfo
		One player playing the game
	player2 : PlayerInfo
		Another player playing the game

	Returns
	-------
	player1 : PlayerInfo
		Result of populating with info
	player2 : PlayerInfo
		Result of populating with info
	"""

	# Each player's board and guesses are grids of ~ characters, or water
	player1.board = [['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~']]

	player2.board = [['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~']]

	player1.guess = [['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~']]

	player2.guess = [['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
					 ['~', '~', '~', '~', '~']]

	# Player 1, Player2 player numbers
	player1.playerNum = 1
	player2.playerNum = 2

	# Link the other player
	player1.otherPlayer = player2
	player2.otherPlayer = player1

	mode = 0

	# Loop until "auto" or "manual" is entered by the user
	while(True):

		# Set up the boards of the players
		mode = setupBoards(player1, player2)

		# Break out of loop if no error occurs
		if(mode != -1):
			break;

		# If error occurs, print error message and
		#   prompt user try setting up boards again
		print("Invalid mode. Please enter 'auto' or 'manual'.\n")


	# Return both set up player objects 
	return player1, player2