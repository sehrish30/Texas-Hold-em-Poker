class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __gt__(self, other):
        # this [0] will get index
        current_player_best_validator_index = self.best_hand()[0]
        other_player_best_validator_index = other.best_hand()[0]
        # means if first player is less than second player this will send true to max
        return current_player_best_validator_index < other_player_best_validator_index


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