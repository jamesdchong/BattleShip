class ShipInfo():
	""" Class to hold a ship's information
	"""

	# Initializes a shipInfo object
	def __init__(self, name, startX, startY, orientation, shipLen, sunk):
		self.name = name
		self.startX = startX
		self.startY = startY
		self.orientation = orientation
		self.shipLen = shipLen
		self.sunk = sunk

	# Sets the name of a ship
	def setName(self, name):
		self.name = name

	# Sets the x position of a ship
	def setStartX(self, startX):
		self.startX = startX

	# Sets the y position of a ship
	def setStartY(self, startY):
		self.startY = startY

	# Sets the orientation of a ship
	def setOrientation(self, orientation):
		self.orientation = orientation

	# Sets the ship length
	def setShipLen(self, shipLen):
		self.shipLen = shipLen

	# Sets if the ship is sunk
	def setSunk(self, sunk):
		self.sunk = sunk