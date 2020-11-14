from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator
    )

class Hand():
     # class attributes will be shared among all instances 
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator
    )    
    
    def __init__(self):
        self.cards = []

    def __repr__(self):
        # since card has magic method __str__ we can represent it like this
        cards_as_strings= [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)     

   # Cards will be sorted when they go to validators classes
    def add_cards(self, cards):
        # sorting the cards to figure out straight
        # cards.sort() should not be used be it will mutate the cards so anything referncing to cards can cause bugs because they will refer to same object in computers memory
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards =  copy   


    # build the best hand for poker
    def best_rank(self):
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())

      


# card_rank_counts = {
# "Ace": 1,
# "King": 2,
# "Jack": 2
# }        



