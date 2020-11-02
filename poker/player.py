class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def best_hand(self):
        return self.hand.best_rank()

    # game round add cards -> player add cards -> to hand
    def add_cards(self, cards):
        self.hand.add_cards(cards)

    # We wont implement betting logic but just the logic enabling user to fold
    def wants_to_fold(self):
        # future work if self.wager_amount < self.amount_they_have_left
        # then true no money no account storage
        return False    