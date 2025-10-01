from card import Card

class Row:
    
    def __init__(self, cards: list[Card] = None):
        self.cards = cards if cards is not None else [Card.blank(), Card.blank(), Card.blank()]
        if len(self.cards) < 3:
            x = 0
            while x < 3 - len(self.cards):
                self.addCard(Card.blank())
    
    @classmethod
    def blank(cls):
        return cls([Card.blank(), Card.blank(), Card.blank()])
    
    def addCard(self, card: Card, index: int = None):
        if index is not None:
            self.cards[index] = card 
        else:
            try:
                firstBlank = self.cards.index(Card.blank())
                self.cards[firstBlank] = card
            except:
                raise IndexError("There are not blank cards to replace.\n Please set a specific index to replace.")

    def getCards(self) -> list[Card]:
        return self.cards
    
    def hasBlanks(self):
        return Card.blank() in self.cards

class Section:

    def __init__(self, rows: list[Row] = None):
        self.rows = rows if rows is not None else []
    
    @classmethod
    def blank(cls):
        return cls()

    def setRow(self, index: int, row: list):
        self.rows[index] = row

    def getRow(self, index):
        return self.rows[index]
    
    def getCards(self) -> list[Card]:
        cards = []
        for row in self.rows:
            for card in row.getCards():
                cards.append(card)
        
        return cards

    def removeCard(self, card: Card) -> None:
        for row in self.rows:
            for index, rowCard in enumerate(row.getCards()):
                if card == rowCard:
                    row.addCard(Card.blank(), index)

    def getRows(self) -> list[Row]:
        return self.rows
    
    def addCard(self, card: Card):
        for row in self.rows:
            if row.hasBlanks():
                row.addCard(card)
                return
            else:
                pass
        raise ValueError("There is not a place to add a card")

class Hand(Section):
    def __init__(self, rows = None):
        super().__init__(rows)
    
    @classmethod
    def blank(cls):
        return cls([Row.blank(), Row.blank(), Row.blank()])
    
class SideDeck(Section):
    
    def __init__(self, rows = None):
        super().__init__(rows)
        self.selected = 0
        
    @classmethod
    def blank(cls):
        return cls([Row([Card.blank(), Card.blank(), Card.blank(), Card.blank()])])
    
    def getRow(self):
        return self.rows[0]
    
    @classmethod
    def random(cls):
        return cls([Row([Card.random(), Card.random(), Card.random(), Card.random()])])
    
    def select(self, index: int = 0):
        index = index % 4
        self.selected = index
        desiredCard = self.rows[0].getCards()[self.selected]
        if desiredCard != Card.blank():
            desiredCard.select()