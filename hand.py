from assets.icons import Size
import random as rand

class Card:
    CARD_SIZE = Size(8, 8)
    
    def __init__(self, value: int, sign: str, type: str) -> None:
        self.value = value
        self.sign = sign 
        self.type = type
        self.icon = None

    def setIcon(self, icon: object = None) -> None:
        self.icon = icon
    
    @classmethod
    def blank(cls) -> 'Card':
        return cls(0, '', 'blank_slot')
    
    @classmethod
    def random(cls) -> 'Card':
        #Needs to be between 1 and 6
        return cls(rand.randrange(1,6), rand.choice(['+', '-']), type='side_deck')
    
    def __eq__(self, card: 'Card'):
        return(
            isinstance(card, Card) and
            self.value == card.value and
            self.sign == card.sign and
            self.type == card.type
        )
    
    def select(self) -> None:
        self.icon.selected = True
    
    def deselct(self) -> None:
        self.icon.selected = False

class Row:
    
    def __init__(self, cards: list[Card] = None) -> None:
        self.cards = cards
        if len(self.cards) < 3:
            x = 0
            while x < 3 - len(self.cards):
                self.addCard(Card.blank())
    
    @classmethod
    def blank(cls) -> 'Row':
        return cls([Card.blank(), Card.blank(), Card.blank()])
    
    def addCard(self, card: Card, index: int = None) -> None:
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
    
    def hasBlanks(self) -> bool:
        return Card.blank() in self.cards

class Section:

    def __init__(self, rows: list[Row] = None) -> None:
        self.rows = rows if rows is not None else []
    
    @classmethod
    def blank(cls) -> 'Section':
        return cls()

    def setRow(self, index: int, row: list) -> None:
        self.rows[index] = row

    def getRow(self, index) -> Row:
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
                    return

    def getRows(self) -> list[Row]:
        return self.rows
    
    def addCard(self, card: Card) -> None:
        for row in self.rows:
            if row.hasBlanks():
                row.addCard(card)
                return
        raise ValueError("There is not a place to add a card")

class Hand(Section):
    def __init__(self, rows = None) -> None:
        super().__init__(rows)
    
    @classmethod
    def blank(cls) -> 'Hand':
        return cls([Row.blank(), Row.blank(), Row.blank()])
    
class SideDeck(Section):
    
    def __init__(self, rows = None) -> None:
        super().__init__(rows)
        self.selected = 0
        
    @classmethod
    def blank(cls) -> 'SideDeck':
        return cls([Row([Card.blank(), Card.blank(), Card.blank(), Card.blank()])])
    
    def getRow(self) -> Row:
        return self.rows[0]
    
    @classmethod
    def random(cls) -> Row:
        return cls([Row([Card.random(), Card.random(), Card.random(), Card.random()])])
    
    def select(self, index: int = 0) -> None:
        index = index % 4
        self.selected = index
        desiredCard = self.rows[0].getCards()[self.selected]
        if desiredCard != Card.blank():
            desiredCard.select()