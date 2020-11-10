# importing other classes will show error because once it imports full_house_validator.py from __init__.py
# it will show import error because those classes are not initialized and __init__py is partially initialized
# make sure to import them before full_house_validator class
# it is searching for these classes names but they dont exist in namespace

from poker.validators import three_of_a_kind_validator
from poker.validators import ThreeOfAKindValidator, PairValidator

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
         return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()     

    def valid_cards(self):
        three_of_a_kind_cards =   ThreeOfAKindValidator(cards = self.cards).valid_cards()
        pair_cards = PairValidator(cards = self.cards).valid_cards()
        all_cards = three_of_a_kind_cards + pair_cards
        all_cards.sort() # sort method in Card.py
        return all_cards

