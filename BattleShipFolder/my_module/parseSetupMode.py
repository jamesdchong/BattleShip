def parseSetupMode():
	""" Retrieves mode to set up boards from user input

	Returns
	-------
	1 : int
		auto setup
	2 : int
		manual setup
	-1 : int
		neither one
	"""

	# Prompt user to enter auto or manual
	print("Do you want to randomly generate both boards, or ")
	print("manually place the water transport carriers yourself? ")
	print("Enter auto for automated setup, or manual for manual entry: ")

	# Retrieve user input
	mode = input()

	# Return 1 if auto, 2 if manual
	if(mode == "auto"):
		return 1
	if(mode == "manual"):
		return 2

	# Return -1 if neither
	return -1