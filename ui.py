from player import Player
from card import Card
from board import Board
            
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

    def __init__(self, board: Board = None):
        super().__init__()
        self.players: list[Player] = board.getState() if board is not None else []

    def update(self, board: Board):
        self.players = board.getState()
    
    def addPlayer(self, player: Player):
        self.players.append(player)
        
    def render(self) -> None:
        self.stdscr.clear()
        self.stdscr.border()
        self.stdscr.refresh()

        cards = []
        for z, player in enumerate(self.players):
            z = z * Card.CARD_SIZE[1] * 5
            hand = player.hand.getRows()
            for y, row in enumerate(hand):
                for x, card in enumerate(row.getCards()):
                    cardWin = curses.newwin(Card.CARD_SIZE[0], Card.CARD_SIZE[1], y*Card.CARD_SIZE[0] + 5, z+x*Card.CARD_SIZE[1] + 5)
                    if card.type == "blank":
                        cardWin.addstr(0,0, Card.CARD_BLANK_SHAPE)
                        cards.append(cardWin)
                    elif card.type == "main":
                        cardWin.addstr(0,0, Card.CARD_MAIN_SHAPE_BLANK)
                        cardWin.addstr(3, 3, str(card.value))
                        cards.append(cardWin)
        
        for card in cards:
            card.refresh()
        
class EndGameScreen(Screen):
    def __init__(self):
        super().__init__()

    def update(self, board: Board):
        self.winner = board.winner

    def render(self):
        match self.winner:
            case "player":
                self.playerVictory()
            case "opp":
                self.playerDefeat()
            case "tie":
                self.playerTie()
        
        self.pause()

    def playerVictory(self):
        self.stdscr.addstr("You WON!")
    
    def playerDefeat(self):
        self.stdscr.addstr("You LOST!")
    
    def playerTie(self):
        self.stdscr.addstr("You TIED!")


class ScreenManager:
    def __init__(self):
        self.currentScreen: Screen = Screen()
    
    def update(self, *args):
        self.currentScreen.update(*args)
        self.currentScreen.render()

    def setScreen(self, newScreen, *args):
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
    
    def cleanup(self):
        if self.currentScreen is not None:
            self.currentScreen.cleanup()
    
    

        


            


