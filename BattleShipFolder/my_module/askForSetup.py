from printBoard import printBoard
from placeShip import placeShip

def askForSetup(player):
	""" Manually sets up ships on player's board

	Parameters
	----------
	player : PlayerInfo
		player to set up board for

	Returns
	-------
	1 : int
		1 if manual setup successful
	"""

	# Names of ships
	shipNames = ["DESTROYER", "SUBMARINE"]

	# Lengths of the ships
	shipLens = [2, 3]

	# Print setup instructions
	print("Player " + str(player.playerNum) +
		  " will now begin setup. Please make " \
          "sure that the locations you enter are valid " \
          "and can hold the desired ship.\n\n")

	# Loop to place both ships
	for i in range(0, 2):

		# Print the players current board
		printBoard(player.board)

		# Prompt the user to enter start location of the ship
		print("Enter start location of the " +
			  str(shipNames[i]) + " (" + str(shipLens[i]) +
			  " spaces). Input " \
              "format: 2,1: ")

		# Loop until ship is placed in a valid location
		while(True):

			# Retrive input from user
			enteredString = input("")

			# Check if input is in correct format
			if(len(enteredString) != 3 or
				enteredString[0].isdigit() == False or
				enteredString[1] != "," or
				enteredString[2].isdigit() == False):

				print("\nInvalid input. Try again.")

				print("Enter start location of the " + str(shipNames[i]) +
					  " (" + str(shipLens[i]) + " spaces). Input " \
                      "format: 2,1: ")

				continue

			# Obtain startX and startY from input
			enteredString = enteredString.split(",")

			# Parse input with X position before comma,
			#   and Y position after comma
			startX = int(enteredString[0])
			startY = int(enteredString[1])

			# If startX or startY not in valid range of board,
			#   print error message, reprompt user
			if(startX not in range(0, 5) or startY not in range(0, 5)):
				print("Invalid location for ship.\n")

				print("Enter start location of the " + str(shipNames[i]) +
					  " (" + str(shipLens[i]) + " spaces). Input " \
                      "format: 2,1: ")

				continue

			# Prompt user for horizontal or vertical ship
			print("Enter 0 for horizontal placement or 1 for " \
                  "vertical: ")

			# Retrive input from user
			orientation = input("")

			# Convert string of input to int
			orientation = int(orientation)

			# If orientation not 0 or 1,
			#   print error message and restart placing this ship
			if(orientation not in range(0, 2)):
				print("Invalid orientation. Try again.\n")

				print("Enter start location of the " + str(shipNames[i]) +
					  " (" + str(shipLens[i]) + " spaces). Input " \
                      "format: 2,1: ")

				continue

			# Place the ship on the player's board
			shipPlaced = placeShip(player, i, startX, startY, orientation)

			# If error occurs placing the ship,
			#   print error message and restart placing the ship
			if(shipPlaced != 0):
				print("The " + str(shipNames[i]) + 
					  " could not be placed.Try a different " \
                      "location or orientation.\n")

				print("Enter start location of the " + str(shipNames[i]) +
					  " (" + str(shipLens[i]) + " spaces). Input " \
                      "format: 2,1: ")

				continue

			# Break out of loop if ships successfully placed
			break
		
	return 1