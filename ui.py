from hand import Card
from board import Board
from assets.icons import renderIcon
from assets.icons import Size, Position

import curses
import traceback
import sys

class Screen:
    def __init__(self):
        self.stdscr = None
        self.initializeCurses()
    
    def initializeCurses(self):
        try:
            self.stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(True)
            curses.curs_set(0)
            self.stdscr.clear()
            self.stdscr.refresh()

        except Exception:
            if self.stdscr is not None:
                try: 
                    self.stdscr.keypad(False)
                    curses.nocbreak()
                    curses.echo()
                    curses.endwin()
                except Exception:
                    pass
            traceback.print_exc()
            sys.exit(1)
    
    def cleanup(self):
        if self.stdscr:
            try:
                self.stdscr.keypad(False)
                curses.nocbreak()
                curses.echo()
                curses.endwin()
            except Exception:
                pass
    
    def pause(self):
        self.stdscr.getch()
    
    def render(self):
        pass

    def update(*args):
        pass

class GameScreen(Screen):

    def __init__(self, board: Board = None) -> None:
        super().__init__()
        self.players: list= board.getState() if board is not None else []

    def update(self, board: Board) -> None:
        self.players = board.getState()
    
    def addPlayer(self, player: object) -> None:
        self.players.append(player)
        
    def render(self) -> None:
        self.stdscr.clear()
        self.stdscr.border()
        self.stdscr.refresh()
        
        #Render Main Hand
        for z, player in enumerate(self.players):
            z = z * Card.CARD_SIZE.width * 5
            hand = player.hand.getRows()
            for y, row in enumerate(hand):
                for x, card in enumerate(row.getCards()):
                    cardPosition = Position(z + x * Card.CARD_SIZE.width + 5, y * Card.CARD_SIZE.height + 5)
                    card.setIcon(CardIcon(size= Card.CARD_SIZE, position=cardPosition, sign=card.sign, value=card.value, type=card.type))
                    card.icon.refresh()
        
        for z, player, in enumerate(self.players):
            z = z * Card.CARD_SIZE.width * 5
            sideDeck = player.sideDeck.getRow()
            for x, card in enumerate(sideDeck.getCards()):
                cardPosition  = Position(z + x * Card.CARD_SIZE.width + 5, 28)
                card.setIcon(CardIcon(size= Card.CARD_SIZE, position=cardPosition, sign=card.sign, value=card.value, type=card.type))
                card.icon.selected = (x == player.sideDeck.selected)
                card.icon.refresh()
             
class EndGameScreen(Screen):
    def __init__(self) -> None:
        super().__init__()

    def update(self, board: Board) -> None:
        self.winner = board.winner

    def render(self) -> None:
        match self.winner:
            case "player":
                self.playerVictory()
            case "opp":
                self.playerDefeat()
            case "tie":
                self.playerTie()
        
        self.pause()

    def playerVictory(self) -> None:
        self.stdscr.addstr("You WON!")
    
    def playerDefeat(self) -> None:
        self.stdscr.addstr("You LOST!")
    
    def playerTie(self) -> None:
        self.stdscr.addstr("You TIED!")

class ScreenManager:
    def __init__(self) -> None:
        self.currentScreen: Screen = Screen()
    
    def update(self, *args) -> None:
        self.currentScreen.update(*args)
        self.currentScreen.render()

    def setScreen(self, newScreen, *args) -> None:
        self.cleanup()
    
        if isinstance(newScreen, type):
            self.currentScreen = newScreen(*args)
        elif isinstance(newScreen, object):
            self.currentScreen = newScreen
        else:
            raise TypeError("ScreenManager.setScreen() requires a valid type or screen object")
    
    def getInput(self) -> str:
        key = self.currentScreen.stdscr.getkey()
        return key
    
    def cleanup(self) -> None:
        if self.currentScreen is not None:
            self.currentScreen.cleanup()

class Icon():

    #icon should have a window, default size, and default texture
    def __init__(self, size: Size = None, position: Position = None, texture: str = None) -> None:
        self.size = size
        self.texture = texture
        self.position = position
    
    def setTexture(self, texture: str) -> None:
        self.texture = texture
    
    def refresh(self) -> None:
        self.window = curses.newwin(self.size.height, self.size.width, self.position.y, self.position.x)
        self.window.addstr(self.texture)
        self.window.refresh()

    def clear(self) -> None:
        self.window.clear()
        self.window.refresh()

class CardIcon(Icon):
    
    def __init__(self, size: Size = Card.CARD_SIZE, position: Position = Position(0,0), sign: str = None, value: int = None, type: str = None) -> None:
        self.size = size
        self.position = position
        self.sign = sign if sign is not None else ""
        self.value = value if value is not None else 0
        self.type = type if type is not None else "blank_slot"
        self.window = None
        self.selected = False
    
    def refresh(self) -> None:
        if self.window:
            try: 
                self.window.erase()
            except Exception:
                pass
        self.window = curses.newwin(self.size.height, self.size.width, self.position.y, self.position.x)
        lines = renderIcon(self.type, self.sign, self.value)
        if len(lines) < 2:
            raise ValueError("The rendering of the Icon failed")
        for i, line in enumerate(lines):
            if self.selected == True:
                self.window.addstr(i, 0, line[:self.size.width], curses.A_REVERSE)
            else:
                self.window.addstr(i, 0, line[:self.size.width])
        self.window.refresh()