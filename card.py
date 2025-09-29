from assets.icons import Size

class Card:
    CARD_SIZE = Size(8, 8)
    
    def __init__(self, value: int = None, sign: str = None, type: str = None):
        self.value = value if value is not None else 0
        self.sign = sign if sign is not None else ""
        self.type = type

    def setIcon(self, icon: object = None):
        self.icon = icon
    
    @classmethod
    def blank(cls):
        return cls(0, '', 'blank_slot')
    
    def __eq__(self, card: 'Card'):
        return(
            isinstance(card, Card) and
            self.value == card.value and
            self.sign == card.sign and
            self.type == card.type
        )