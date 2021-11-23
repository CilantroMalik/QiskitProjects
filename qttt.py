
# Imports
import itertools
import os

# Setting up the board and game variables
board = ["", "", "", "", "", "", "", "", ""]  # 9 spaces in which players can move
turnNumber = 1  # counts up every turn (1 turn = each player moves once)
currentPlayer = "X"  # switches depending on whose turn it is
moves = []  # will be a list of [player, square1, square2, turnNum, classicalOrQuantum] for each move


# Visualize the board
def visualizeBoard(state):
    maxLen = max([len(item) for item in state]) + 2
    if maxLen % 2 == 1:
        maxLen += 1
    height = maxLen // 2
    if height % 2 == 0:
        height += 1
    row1 = "|".join([item.center(maxLen) for item in state[:3]])
    row2 = "|".join([item.center(maxLen) for item in state[3:6]])
    row3 = "|".join([item.center(maxLen) for item in state[6:]])

    for _ in range(height // 2):
        print(" "*maxLen + "|" + " "*maxLen + "|" + " "*maxLen)
    print(row1)
    for _ in range(height // 2):
        print(" "*maxLen + "|" + " "*maxLen + "|" + " "*maxLen)
    print("—"*(maxLen*3 + 2))
    for _ in range(height // 2):
        print(" "*maxLen + "|" + " "*maxLen + "|" + " "*maxLen)
    print(row2)
    for _ in range(height // 2):
        print(" "*maxLen + "|" + " "*maxLen + "|" + " "*maxLen)
    print("—"*(maxLen*3 + 2))
    for _ in range(height // 2):
        print(" "*maxLen + "|" + " "*maxLen + "|" + " "*maxLen)
    print(row3)
    for _ in range(height // 2):
        print(" "*maxLen + "|" + " "*maxLen + "|" + " "*maxLen)


# Display all moves so far in the game

def getConnections(moveList):
    print("\n—————— Move List ——————")
    connections = []
    for move in moveList:
        connections.append(f"{move[0]}: {move[1]}—{move[2]}")
    for i, conn in enumerate(connections):
        print(conn, end=";\n" if i % 3 == 2 else "; ")
    if len(connections) % 3 != 0:
        print("\n")


# Check if a closed cyclic loop exists in a game state

def hasLoop(moveList):
    for moveset in itertools.combinations([move for move in moveList if move[4] != "C"], 3):
        if len(set(moveset[0][1:3] + moveset[1][1:3] + moveset[2][1:3])) == 3:
            toPrint = [f"{move[0]}: {move[1]}—{move[2]}" for move in moveset]
            print(f"Loop created: {'; '.join(toPrint)}")
            return moveset
    return None

# ----------------------
# Extract some functions for clarity and readability in game loop
# ----------------------


# Display game state
def showState():
    os.system("clear")
    visualizeBoard(board)
    getConnections(moves)


# End of turn tasks
def endTurn(currPlayer, turnNum):
    # Switch player
    if currPlayer == "X":
        currPlayer = "O"
    else:
        currPlayer = "X"
        turnNum += 1
    return currPlayer, turnNum


# Check whether game is won
def isGameOver():
    global winner
    triplesToCheck = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    winningTriples = []
    for triple in triplesToCheck:
        if "[X" in board[triple[0]] and "[X" in board[triple[1]] and "[X" in board[triple[2]]:
            winner += "X"
            winningTriples.append(triple)
        if "[O" in board[triple[0]] and "[O" in board[triple[1]] and "[O" in board[triple[2]]:
            winner += "O"
            winningTriples.append(triple)
    if len(winner) > 1:
        minSumOfIndices, winningPlayer = 9999, ""
        for player, triple in zip(list(winner), winningTriples):
            sumOfIndices = 0
            for sq in triple:
                start = board[sq].find(f"[{player}")
                sumOfIndices += int(board[sq][start+2:board[sq].find("]", start)])
            if sumOfIndices < minSumOfIndices:
                minSumOfIndices = sumOfIndices
                winningPlayer = player
            elif sumOfIndices == minSumOfIndices:
                winningPlayer += player
        winner = winningPlayer
        return True
    else:
        return False
