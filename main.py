import board
from ui import Ui 

gameBoard = board.Board()
screen = Ui()

def getInput():
    userInput = input()
    if userInput == "s":
        gameBoard.pc.stand()

try:
    while True:
        gameBoard.takeTurn()
        if not gameBoard.running:
            break

        state = gameBoard.getState()
        input = screen.renderScreen(state)
        #getInput()
        
finally:
    screen.cleanup()
    