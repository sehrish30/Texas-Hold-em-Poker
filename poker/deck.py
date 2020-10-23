# Deck class storing and adding cards
class Deck():
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)  

        