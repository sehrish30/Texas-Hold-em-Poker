class PairValidator():
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1 

    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(2) # {"10": 2}
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards

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
    