class Card:
    CARD_SIZE = (8, 8)

    CARD_BLANK_SHAPE = (" _____ \n" \
                        "|     |\n" \
                        "|     |\n" \
                        "|     |\n" \
                        "|     |\n" \
                        "|_____|\n")
    
    CARD_MAIN_SHAPE_BLANK = ("  ___  \n" \
                             " /...\ \n" \
                             "|.....|\n" \
                             "|.....|\n" \
                             "|.....|\n" \
                             " \___/ \n")

    TYPES = ["main", "blank", "flip", "both", "double", "breaker"]
    SIGNS = ["+", "-", "+/-", ""]
    MAIN_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    SIGNED_VALUES = [1, 2, 3, 4, 5, 6]
    FLIPED_VALUES = {2: 4,
                     3: 6}
    
    def __init__(self, value: int, sign: str, type: str):
        if not (0 <= value <= 10):
            raise ValueError("The card value must be between 0 and 10")
        self.value = value
        if not (sign in Card.SIGNS or sign is None):
            raise ValueError(f"The card sign must be {', '.join(Card.SIGNS)}")
        self.sign = sign
        if not type in Card.TYPES:
            raise ValueError(f"The card type must be {', '.join(Card.TYPES)}")
        self.type = type
    
    @classmethod
    def blank(cls):
        return cls(0, '', 'blank')
    
    def __eq__(self, card: 'Card'):
        return(
            isinstance(card, Card) and
            self.value == card.value and
            self.sign == card.sign and
            self.type == card.type
        )
    
    def bake(self):
        if self.type == "main":
            bakedCard = []
            bakedCard.append(r"  ___  ")
            bakedCard.append(r" /   \ ")
            bakedCard.append(r"|.....|")
            bakedCard.append(f"|..{self.value}..|")
            bakedCard.append(r"|.....|")
            bakedCard.append(r" \___/ ")
            return bakedCard
        
        if self.type == "border":
            bakedCard = []
            bakedCard.append(r" || ")
            bakedCard.append(r" || ")
            bakedCard.append(r" || ")
            bakedCard.append(r" || ")
            bakedCard.append(r" || ")
            bakedCard.append(r" || ")
            return bakedCard
        
        if self.type == "blank":
            bakedCard = []
            bakedCard.append(r" _____ ")
            bakedCard.append(r"|     |")
            bakedCard.append(r"|     |")
            bakedCard.append(f"|     |")
            bakedCard.append(r"|     |")
            bakedCard.append(r"|_____|")
            return bakedCard