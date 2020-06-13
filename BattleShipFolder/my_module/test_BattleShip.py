import pytest
from ShipInfo import ShipInfo
from PlayerInfo import PlayerInfo

def test_setInitShipInfo():
	""" Tests ShipInfo objects initialized correctly
	"""

	# Ship parameters
	shipName = "DESTROYER"
	startX = 1
	startY = 2
	orientation = 0
	shipLen = 2
	sunk = 0

	# Create ShipInfo object
	ship = ShipInfo(shipName, startX, startY, orientation, shipLen, sunk)

	assert shipLen == ship.shipLen

def test_setShipFromPlayerInfo():
	""" Tests if setting a player's ships works properly
	"""

	# Ship parameters
	ship = 0
	shipName = "DESTROYER"
	startX = 1
	startY = 2
	orientation = 0
	shipLen = 2
	sunk = 0

	# Player parameters
	playerNum = 1
	board = [['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
			['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
			['~', '~', '~', '~', '~']]
	guess = [['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
			['~', '~', '~', '~', '~'],['~', '~', '~', '~', '~'],
			['~', '~', '~', '~', '~']]
	ships = None
	otherPlayer = None

	# Create PlayerInfo object
	player = PlayerInfo(playerNum, board, guess, ships, otherPlayer)

	# Set player's ships
	player.setShip(ship, shipName, startX, startY, orientation, shipLen, sunk)

	assert player.ships[0].orientation == orientation

