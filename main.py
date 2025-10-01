from board import Board
import ui as Ui

gameBoard = Board()
screenManager = Ui.ScreenManager()
screenManager.setScreen(Ui.GameScreen)

try:
    gameBoard.takeTurn()
    screenManager.update(gameBoard)
    while True:
        input = screenManager.getInput()
        if input == "s":
            gameBoard.pc.stand()

        playerSideDeck = gameBoard.getState()[0].sideDeck
        currentlySelected = playerSideDeck.selected
        if input == "a":
            playerSideDeck.select(currentlySelected - 1)
        if input == "d":
            playerSideDeck.select(currentlySelected + 1)
        if input == "w":
            #implement adding card to the deck
            pass
        
        if input == "\n":
            gameBoard.takeTurn()
        if not gameBoard.running:
            screenManager.setScreen(Ui.EndGameScreen)
            screenManager.update(gameBoard)
            break

        screenManager.update(gameBoard)
        
finally:
    screenManager.cleanup()
    