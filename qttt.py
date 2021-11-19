
# Imports
import itertools
import os

# Setting up the board and game variables
board = ["", "", "", "", "", "", "", "", ""]  # 9 spaces in which players can move
turnNumber = 1  # counts up every turn (1 turn = each player moves once)
currentPlayer = "X"  # switches depending on whose turn it is
moves = []  # will be a list of [player, square1, square2, turnNum, classicalOrQuantum] for each move


