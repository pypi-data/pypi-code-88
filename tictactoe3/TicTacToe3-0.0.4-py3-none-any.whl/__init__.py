"""
TTT Package :-
	- Plays the Game
	- Records the Probability of Winning and Drawing
"""

from .__errors__ import ChoiceError as __ChErr
from .__functions__ import commitToGrid as __CTG, comptrMove as __CM, gridRepr as __GR, isGameOver as __IGO, log as __log, showProb as showProbability, updateProb as __UP

def play():
	""" Play the Game"""

	# Starting Grid, Previous Coordinates and Moves Variables
	grid, moves = [
			[None, None, None],
			[None, None, None],
			[None, None, None]
			], 0

	# Title
	print("Tic Tac Toe\n3 in a Row\n")

	# Displaying Starting Grid
	print(__GR(grid))

	# Getting Player's Choice
	playerChoice = input("Choose between 'X' or 'O' :")

	if playerChoice.upper() not in ('X', 'O'):
		raise __ChErr(f"Invalid Choice : '{playerChoice}'")
	else:
		playerChoice = playerChoice.upper()
		__log(value=f"Your Choice : {playerChoice}", isnew=True)

	# Setting Computer's Choice based on Player's Choice
	if playerChoice == 'X':
		comptrChoice = 'O'
	else:
		comptrChoice = 'X'

	# Temporarily Logging the choice
	__log(value=f"My Choice : {comptrChoice}\n")

	GameOverState, playerMove = __IGO(grid, playerChoice, comptrChoice), True

	# Main Game Starts
	while not bool(GameOverState):

		if playerMove:
			print("\nYour Move")
			__log(value="Your Move")

			# Getting Row, Col Value for Player's Move
			row = int(input(f"Enter the Row Number in which you would like to place {playerChoice} : "))

			if row not in (1, 2, 3):
				raise ValueError(f"{row}th Row DOESN'T EXIST")
			else:
				pRow = row - 1

			col = int(input(f"Enter the Column Number in which you would like to place {playerChoice} : "))

			if col not in (1, 2, 3):
				raise ValueError(f"{col}th Column DOESN'T EXIST")
			else:
				pCol = col - 1

			# Commiting Player's Move
			__CTG(grid, pRow, pCol, playerChoice)

			playerMove = False
		else:
			print("\nMy Move")
			__log(value="My Move")

			# Making Computer's Move
			cRow, cCol = __CM(grid, playerChoice, comptrChoice)

			playerMove = True

		# Updating Moves
		moves += 1

		# Representing Grid
		print(__GR(grid, moves))

		# Temporarily Logging the Moves
		__log(value=f"{__GR(grid, moves)}")

		# Updating GameOverState
		GameOverState = __IGO(grid, playerChoice, comptrChoice)
	else:
		if GameOverState == "comptr":
			print("Hurray!!! I Won.")
			__log(value="Result : I Won!!!")
			__UP("comptr")
		elif GameOverState == "draw":
			print("Game Draw!!!")
			__log(value="Result : Draw")
			__UP("draw")
		else:
			print("Congratulations!!! You Won.")
			__log(value="Result : You Won!!!")
			__UP("player")

		# Asking for Logging the Output of the game...
		logChoice = input("\nDo You Want to Log the Game (Y/[N]) : ")

		if logChoice.lower() == "y":
			print(f"Game Logged at {__log(showpath=True)}")
		elif logChoice.lower() == "n":
			__log(toremove=True)
		else:
			raise __ChErr(f"Invalid Choice : {logChoice}")

		# Asking for Displaying the Probability
		probChoice = input("\nDo You Want to see the Recorded Probability of Winning (Y/[N]) : ")

		if probChoice.lower() == "y":
			showProbability()
		elif probChoice.lower() == "n":
			exit(0)
		else:
			raise __ChErr(f"Invalid Choice : {probChoice}")