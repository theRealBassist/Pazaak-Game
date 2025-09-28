from board import Board
import ui as Ui

gameBoard = Board()
screenManager = Ui.ScreenManager()
screenManager.setScreen(Ui.GameScreen)

try:
    while True:
        gameBoard.takeTurn()
        if not gameBoard.running:
            screenManager.setScreen(Ui.EndGameScreen)
            screenManager.update(gameBoard)
            break

        screenManager.update(gameBoard)
        input = screenManager.getInput()
        if input == "s":
            gameBoard.pc.stand()
        
finally:
    screenManager.cleanup()
    