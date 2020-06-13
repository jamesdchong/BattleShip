from PlayerInfo import PlayerInfo
from ShipInfo import ShipInfo
from setupPlayers import setupPlayers
from printBoard import printBoard
from placeGuess import placeGuess
from checkMove import checkMove
from checkWin import checkWin
import string
import random

""" Main Driver Program
"""

print("\nWelcome to Mini-Battleship!\n\n" \
      "This is a 2-player game. Players will be given the " \
      "opportunity to manually place battleship pieces on the " \
      "board, or have them randomly placed.\n" \
      "There are NUMBER types of ships to be placed: \n" \
      "\t\t- [D] Destroyer (takes 2 spaces)\n" \
      "\t\t- [S] Submarine (takes 3 spaces)\n" \
      "The objective of the game is to guess the locations of " \
      "other player's ships. Follow the instructions that " \
      "proceed. The first player to guess them all wins!\n\n")

# Create PlayerInfo objects
player1 = PlayerInfo(None, None, None, None, None)
player2 = PlayerInfo(None, None, None, None, None)

# Set up both players
player1, player2 = setupPlayers(player1, player2)

# Select player 1 or player 2 at random
player = (random.randrange(0,5) % 2) + 1

# Assign playerInfo to be the player selected randomly
if player == 1:
	playerInfo = player1
else:
	playerInfo = player2

# Print which player's turn it is
print("\nPlayer " + str(player) + "'s turn.\n")

# Board of player's guesses
print("Player " + str(player) + "'s guesses:\n\n")

# Print the player's board of guesses
printBoard(playerInfo.guess)

# Prompt user to enter a guess
print("Please enter a position to guess: ")

# Loop until either player wins
while(True):

     # Retrive input from user
     position = input("")

     # Check if input is in right format
     if(len(position) != 3 or
        position[0].isdigit() == False or
        position[1] != "," or
        position[2].isdigit() == False):

        print("\nInvalid input. Try again.")

        print("Please enter a position to guess: ")

        continue

     # Obtain x position and y position from input
     position = position.split(",")

     # Value before comma is x position, after comma is y position
     xPos = int(position[0])
     yPos = int(position[1])

     # If guess position invalid, print error message and reprompt
     if(checkMove(playerInfo.guess, xPos, yPos) == 0):
          print("Invalid location, or you've already guessed " \
                "this position.\n")

          print("Please enter a position to guess: ")

          continue

     # Place guess on player's board
     placeGuess(playerInfo, xPos, yPos)

     # If a player sinks both ships, print win message and exit program
     if(checkWin(playerInfo)):
          print("\nPLAYER " + str(player) + " WINS!\n")
          break

     # Switch to other player
     player = (player % 2) + 1
     playerInfo = playerInfo.otherPlayer
     
     # Print player's turn
     print("\nPlayer " + str(player) + "'s turn.\n")

     # Board of player's guesses
     print("Player " + str(player) + "'s guesses:\n\n")

     # Print the player's board of guesses
     printBoard(playerInfo.guess)

     # Prompt user to enter a guess
     print("Please enter a position to guess: ")