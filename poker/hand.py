class Hand():
    def __init__(self, cards):
        # sorting the cards to figure out straight
        # cards.sort() should not be used be it will mutate the cards so anything referncing to cards can cause bugs because they will refer to same object in computers memory
        copy = cards[:]
        copy.sort()
        self.cards = copy

    @property
    def _rank_validation_from_best_to_worst(self):
        return (
            ("Flush", self._flush),
            ("Straight", self._straight),
            ("Three of a Kind", self._three_of_a_kind),
            ("Two Pair", self._two_pair),
            ("Pair", self._pair),
            ("High Card", self._high_card)
        )    

    # build the best hand for poker
    def best_rank(self):
        for rank in self._rank_validation_from_best_to_worst:
            # destructure the tuple and invoke the method at tuple item 2
            name, validator_func = rank
            if validator_func():
                return name

    def _flush(self):
        suits_that_occur_5_or_more_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }
        return len(suits_that_occur_5_or_more_times) == 1

        #{
        # "Hearts": 5
        # }

    def _straight(self):
        # straight has 5 cards so check it doesnot accept < 5
        if len(self.cards) < 5:
           return False

        rank_indexes = [card.rank_index for card in self.cards] 
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(range(starting_rank_index, last_rank_index + 1))
        return straight_consecutive_indexes == rank_indexes


    def _three_of_a_kind(self): 
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1

    def _two_pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2

    def _pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1

    def _high_card(self):
        return True;    


    def _ranks_with_count(self, count):
        return {
            # filter the ones with the count sent
            rank : rank_count
            for rank,rank_count in self._card_rank_counts.items() # items iterate over whole dict rather than likes .keys or .values
            if rank_count == count
        } 

    @property
    def _card_suit_counts(self):
        card_suit_counts = {} 
        for card in self.cards:
            # first iterates over loop puts value in dict
            # { "Ace": 0 } then iterates it twice makes it { "Ace": 2 }
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts           

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



