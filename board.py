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
        
        if self.turn == 0 and self.pc.isStanding is not True:
            self.playerTurn()
        else:
            self.oppTurn()

        self.iterateTurn()
    
    def playerTurn(self):
        if not self.pc.isStanding is True:
                card = Card(randrange(1, 2), None, "main")
                self.pc.addHandCard(card)
        elif self.pc.getHandTotal() > 20:
            self.endGame()


    def oppTurn(self):
        if not self.opp.isStanding() is True:
                card = Card(randrange(1, 2), None, "main")
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
            print("BOO YOU SUCK")
            return

        if self.opp.getHandTotal() > 20 or self.opp.getTotalCards() == 9:
            print ("CONGRATS YOU WON")
            return

        
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