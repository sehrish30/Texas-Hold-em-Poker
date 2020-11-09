class FlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Flush"

    def is_valid(self):
        return len(self._suits_that_occur_5_or_more_times) == 1  

    def valid_cards(self):
        cards = [card for card in self.cards if card.suit in self._suits_that_occur_5_or_more_times.keys()] 
        return cards[-5:] #will exclude last number 0 so -5 to -1

    @property
    def _suits_that_occur_5_or_more_times(self):
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        } # {"Hearts": 6}      

    @property
    def _card_suit_counts(self):
        card_suit_counts = {} 
        for card in self.cards:
            # first iterates over loop puts value in dict
            # { "Ace": 0 } then iterates it twice makes it { "Ace": 2 }
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts  
    
    

