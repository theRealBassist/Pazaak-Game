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