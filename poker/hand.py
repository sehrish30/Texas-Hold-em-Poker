from poker.validators import (
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
            ("Four of a Kind", self._four_of_a_kind),
            ("Full House", self._full_house),
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


    def _four_of_a_kind(self):
        # in texas hold em poker we only have 7 cards two for us and seven for community
        rank_with_four_of_a_kind = self._ranks_with_count(4)
        return len(rank_with_four_of_a_kind) == 1                    

    def _full_house(self):
        return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()        


    def _ranks_with_count(self, count):
        return {
            # filter the ones with the count sent
            rank : rank_count
            for rank,rank_count in self._card_rank_counts.items() # items iterate over whole dict rather than likes .keys or .values
            if rank_count == count
        } 

    @property
    def _card_rank_counts(self):
        card_rank_counts = {} 
        for card in self.cards:
            # first iterates over loop puts value in dict
            # { "Ace": 0 } then iterates it twice makes it { "Ace": 2 }
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

# card_rank_counts = {
# "Ace": 1,
# "King": 2,
# "Jack": 2
# }        



