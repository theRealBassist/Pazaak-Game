import board
from ui import Ui 

gameBoard = board.Board()
screen = Ui

def getInput():
    userInput = input()
    if userInput == "s":
        gameBoard.pc.stand()

while True:
    gameBoard.takeTurn()
    if gameBoard.running:
        state = gameBoard.getState()
        screen.renderScreen(screen, state)
        getInput()
    else:
        break


