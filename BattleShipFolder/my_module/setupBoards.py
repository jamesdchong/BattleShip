from parseSetupMode import parseSetupMode
from autogenerateBoard import autogenerateBoard
from askForSetup import askForSetup

def setupBoards(player1, player2):
	""" Sets up playing boards for both players

	Parameters
	----------
	player1 : PlayerInfo
		One player playing the game
	player2 : PlayerInfo
		Another player playing the game

	Returns
	-------
	1 : int
		board generation successful
	-1 : int
		board generation unsuccessful
	"""

	# Get whether the user wants to auto or manual set up boards
	mode = parseSetupMode()

	# Auto mode
	if(mode == 1):

		# Generate boards for both players
		autogenerateBoard(player1)
		autogenerateBoard(player2)

		return 1

	else:

		# Manual mode
		if(mode == 2):
			# If error occur when manually setting up board, return -1
			if(askForSetup(player1) == -1):
				return -1
			if(askForSetup(player2) == -1):
				return -1

			return 1

		# If user enters anything other than auto or manual, return -1
		else:
			return -1
