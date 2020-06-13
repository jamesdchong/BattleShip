from ShipInfo import ShipInfo

class PlayerInfo():
	""" Class to hold a player's board information
	"""
	
	# Initializes a playerInfo object
	def __init__(self, playerNum, board, guess, ships, otherPlayer):
		self.playerNum = playerNum
		self.board = board
		self.guess = guess
		self.ships = [ShipInfo(None, None, None, None, None, None),
					  ShipInfo(None, None, None, None, None, None)]
		self.otherPlayer = otherPlayer

	# Sets the fields of the ship passed in
	def setShip(self, ship, name, startX, startY, orientation, shipLen, sunk):
		self.ships[ship].setName(name)
		self.ships[ship].setStartX(startX)
		self.ships[ship].setStartY(startY)
		self.ships[ship].setOrientation(orientation)
		self.ships[ship].setShipLen(shipLen)
		self.ships[ship].setSunk(sunk)