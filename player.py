from hand import SideDeck, Hand
from card import Card


class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.hand = Hand.blank()
        self.hand.setName = self.name
        self.standing = False
        self.sideDeck = SideDeck.random()
    
    def addHandCard(self, card: Card) -> None:
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
    
    def getTotalCards(self) -> int:
        total = 0
        for row in self.hand.getRows():
            for card in row.getCards():
                if card.type == "main":
                    total += 1
        return total

    def getSelectedCard(self) -> Card:
        return self.sideDeck.getRow().getCards()[self.sideDeck.selected]

    def stand(self) -> None:
        self.standing = True
    
    def isStanding(self) -> bool:
        return self.standing
    
    def playSideDeckCard(self) -> None:
        self.hand.addCard(self.getSelectedCard())
        self.sideDeck.removeCard(self.getSelectedCard())