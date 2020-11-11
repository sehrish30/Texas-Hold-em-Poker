from poker.validators import FiveCardRanksInARowValidator

class StraightValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        # straight has 5 cards so check it doesnot accept < 5  
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1   

    def valid_cards(self):
        # return the last list of batch 5 cards
        return self._collections_of_five_straight_cards_in_a_row[-1]
 

# 
# [
# [six, seven, eight, nine, ten],
# [seven, eight, nine, ten, jack]
# then choose last one
# ]        
