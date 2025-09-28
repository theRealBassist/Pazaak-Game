from player import Player
from card import Card
            
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

class GameScreen(Screen):

    def __init__(self, players: list[Player] = None):
        super().__init__()
        self.players = players if players is not None else []
    
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
    def __init__(self, winner: str = "player"):
        super().__init__()

        match winner:
            case "player":
                self.playerVictory()
            case "opp":
                self.playerDefeat()
            case "tie":
                self.playerTie()

    def playerVictory(self):
        self.stdscr.addstr("You WON!")
    
    def playerDefeat(self):
        self.stdscr.addstr("You LOST!")
    
    def playerTie(self):
        self.stdscr.addstr("You TIED!")


    
    
    

        


            


