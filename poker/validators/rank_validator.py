class RankValidator():
    # no need of __init__ because all we want are methods
    # no need for tests of rank validator because they are protected
    # not part of public object interface
    # and we are testing return value of is_valid and valid_cards in pairValidator
    # this makes sure that logic in our Rank validator is working as intended
    
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