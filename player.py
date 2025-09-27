from hand import Section
from card import Card


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = Section.blank()
        self.hand.setName = self.name
        self.standing = False
    
    def addHandCard(self, card: Card):
        self.hand.addCard(card)

    def getHandTotal(self) -> int: 
        total = 0
        for row in self.hand.getRows():
            for card in row.getCards():
                if card.type == "main":
                    total += int(card.value)
                else:
                    total += int(f'{card.sign}{card.value}')
        return total
    
    def stand(self):
        self.standing = True
    
    def isStanding(self) -> bool:
        return self.standing