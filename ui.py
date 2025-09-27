from hand import Row, Section
from player import Player
from card import Card
            
import os
import curses
from curses import wrapper
import traceback
import sys
class Screen:

    def __init__(self, players: list[Player] = None):
        self.players = players if players is not None else []
    
    def addPlayer(self, player: Player):
        self.players.append(player)

    # def render(self):
    #     os.system('clear')
    #     print("=================================")
    #     for player in self.players:
    #         print(player.name)
    #         print(player.getTotalCards())
    #         hand = player.hand.getRows()
    #         for row in hand:
    #             for line in row.bake():
    #                 print(line)
    #     print("=================================")
        
    def render(self, stdscr):
        stdscr.clear()
        stdscr.refresh()

        cards = []
        # x = 0
        # while x < 3:
        #     y=0
        #     while y < 3:
        #         card = curses.newwin(Card.CARD_SIZE[0], Card.CARD_SIZE[1], y*Card.CARD_SIZE[0], x*Card.CARD_SIZE[1])
        #         card.addstr(0,0, Card.CARD_MAIN_SHAPE_BLANK)
        #         cards.append(card)
        #         y += 1
        #     x += 1

        for z, player in enumerate(self.players):
            z = z * Card.CARD_SIZE[1] * 5
            hand = player.hand.getRows()
            for y, row in enumerate(hand):
                for x, card in enumerate(row.getCards()):
                    cardWin = curses.newwin(Card.CARD_SIZE[0], Card.CARD_SIZE[1], y*Card.CARD_SIZE[0], z+x*Card.CARD_SIZE[1])
                    if card.type == "blank":
                        cardWin.addstr(0,0, Card.CARD_BLANK_SHAPE)
                        cards.append(cardWin)
                    elif card.type == "main":
                        cardWin.addstr(0,0, Card.CARD_MAIN_SHAPE_BLANK)
                        cardWin.addstr(3, 3, str(card.value))
                        cards.append(cardWin)
        
        for card in cards:
            card.refresh()


class Ui:
    def __init__(self):
        self.stdscr = None
        self.initializeCurses()
        

    def renderScreen(self, state):
        screen = Screen()
        for player in state:
            screen.addPlayer(player)
        screen.render(self.stdscr)

        input = self.stdscr.getch()
        return input

    def initializeCurses(self):
        try:
            self.stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(True)
            curses.curs_set(0)

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

        


            


