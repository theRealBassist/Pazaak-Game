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
        if self.checkEndState():
             return
        
        if self.turn == 0 and self.pc.standing is not True:
            self.playerTurn()
        else:
            self.oppTurn()

        self.iterateTurn()
    
    def playerTurn(self):
        if self.pc.getHandTotal() > 20:
            self.endGame()
        card = Card(randrange(1, 10), None, "main_card")
        self.pc.addHandCard(card)
        return
        
    def oppTurn(self):
        if not self.opp.isStanding() is True:
                card = Card(randrange(1, 10), None, "main_card")
                self.opp.addHandCard(card)
                if self.opp.getHandTotal() >= 17:
                    self.opp.stand()
        else:
            pass

    def iterateTurn(self):
        if self.turn == 0:
            self.turn = 1
        elif self.turn == 1:
            self.turn = 0
        else:
            self.turn = 0

    def checkEndState(self) -> bool:
        if self.pc.getHandTotal() > 20 or self.opp.getHandTotal() > 20:
              self.endGame()
              return True
         
        if  self.pc.isStanding() and self.opp.isStanding():
            self.endGame()
            return True
        
        if self.pc.getTotalCards() == 9 or self.opp.getTotalCards() == 9:
             self.endGame()
             return True
        
        return False
            
    def endGame(self):
        self.running = False
        if self.pc.getHandTotal() > 20 or self.pc.getTotalCards() == 9:
            self.winner = "opp"
            return

        if self.opp.getHandTotal() > 20 or self.opp.getTotalCards() == 9:
            self.winner = "player"
            return

        
        if self.pc.getHandTotal() > self.opp.getHandTotal():
            self.winner = "player"
        elif self.pc.getHandTotal() < self.opp.getHandTotal():
            self.winner = "opp"
        elif self.pc.getHandTotal() == self.opp.getHandTotal():
            self.winner = "tie"
        return

    def getState(self) -> list[Player]:
        state = [self.pc, self.opp]
        return state