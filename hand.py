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
    
    def bake(self):
        bakedCards = []
        for card in self.cards:
            bakedCards.append(card.bake())

        lines = []
        x = 0
        while x < 6:
            line = ''
            for card in bakedCards:
                line += card[x]
                line += "  "
            lines.append(line)
            x += 1
        
        return lines


class Section:

    def __init__(self, rows: list[Row] = None):
        self.rows = rows if rows is not None else []
    
    @classmethod
    def blank(cls):
        return cls([Row.blank(), Row.blank(), Row.blank()])

    def setRow(self, index: int, row: list):
        self.rows[index] = row

    def getRow(self, index: int):
        return self.rows[index]
    
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