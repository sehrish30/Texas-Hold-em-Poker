from poker.validators import (
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

    @property
    def _rank_validation_from_best_to_worst(self):
        return (
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind",FourOfAKindValidator(cards = self.cards).is_valid),
            ("Full House", FullHouseValidator(cards = self.cards).is_valid),
            ("Flush", FlushValidator(cards = self.cards).is_valid),
            ("Straight", StraightValidator(cards = self.cards).is_valid),
            ("Three of a Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
            ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
            ("Pair", PairValidator(cards = self.cards).is_valid),
            ("High Card", HighCardValidator(cards = self.cards).is_valid),
            ("No Cards", NoCardsValidator(cards = self.cards).is_valid)
        )    

    # build the best hand for poker
    def best_rank(self):
        for rank in self._rank_validation_from_best_to_worst:
            # destructure the tuple and invoke the method at tuple item 2
            name, validator_func = rank
            if validator_func():
                return name

    def _royal_flush(self):
        is_straight_flush = self._straight_flush()
        if not is_straight_flush:
            return False

        is_royal = self.cards[-1].rank == "Ace" 
        return is_straight_flush and is_royal           

    def _straight_flush(self):
        return StraightValidator(cards = self.cards).is_valid() and FlushValidator(cards = self.cards).is_valid()                  

# card_rank_counts = {
# "Ace": 1,
# "King": 2,
# "Jack": 2
# }        



