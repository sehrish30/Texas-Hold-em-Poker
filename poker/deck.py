import random

# Deck class storing and adding cards
class Deck():
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)     

    def add_cards(self, cards):
        self.cards.extend(cards)  

    def remove_cards(self, number):
        cards_to_remove = self.cards[:number]
        del self.cards[:number]
        return cards_to_remove 

    # we can also do injection in Deck class and shuffle based on diff algorithms for decoupling 
    # but this is enough for program but @patch can be called as anti-pattern
    # because it being dependency because of shuffle function
    def shuffle(self):
        random.shuffle(self.cards)    