import board
import ui as Ui

gameBoard = board.Board()
screen = None
def getInput():
    input = screen.stdscr.getkey()
    return input

try:
    while True:
        gameBoard.takeTurn()
        if not gameBoard.running:
            if screen is not None:
                screen.cleanup()
            screen = Ui.EndGameScreen(gameBoard.winner)
            screen.pause()
            screen.cleanup()
            break

        state = gameBoard.getState()
        screen = Ui.GameScreen(state)
        screen.render()
        input = getInput()
        if input == "s":
            gameBoard.pc.stand()
        
finally:
    screen.cleanup()
    