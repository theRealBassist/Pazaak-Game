from player import Player
from card import Card

from random import randrange
from random import choice

class Board:

    def __init__(self):
        self.pc = Player("pc")
        self.opp = Player("opp")
        self.turn = 0
        self.running = True
    
    def takeTurn(self):
        if  self.pc.isStanding() and self.opp.isStanding():
            self.endGame()
        if self.turn == 0:
            if not self.pc.isStanding is True:
                card = Card(randrange(1, 10), None, "main")
                self.pc.addHandCard(card)
            else:
                self.oppTurn()
        if self.turn == 1:
            self.oppTurn()

        self.iterateTurn()
    
    def oppTurn(self):
        if not self.opp.isStanding() is True:
                card = Card(randrange(1, 10), None, "main")
                self.opp.addHandCard(card)
                if self.opp.getHandTotal() >= 17:
                    self.opp.stand()
        else:
            raise ValueError("OPP IS STANDING")

    def iterateTurn(self):
        if self.turn == 0:
            self.turn = 1
        elif self.turn == 1:
            self.turn = 0
        else:
            self.turn = 0

    def endGame(self):
        self.running = False
        if self.pc.getHandTotal() > self.opp.getHandTotal():
                print ("CONGRATS YOU WON")
        elif self.pc.getHandTotal() < self.opp.getHandTotal():
            print("BOO YOU SUCK")
        elif self.pc.getHandTotal() == self.opp.getHandTotal():
            print("I GUESS A TIE IS ALRIGHT")
        return

    def getState(self):
        state = [self.pc, self.opp]
        return state