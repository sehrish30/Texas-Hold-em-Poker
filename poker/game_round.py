class GameRound():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
    
    def play(self):
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()   
        self._deal_flop_cards()
      
    def _shuffle_deck(self):
        self.deck.shuffle()   

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)

    def _make_bets(self):
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)    

    def _deal_flop_cards(self):
        community_cards = self.deck.remove_cards(3)
        for player in self.players:
            player.add_cards(community_cards)          
            
# Gameround -> deck -> player -> hand  will figure out best rank

# game_round class takes a deck in a collection of players.
#  It shuffles that deck.
# It iterates over all the players it has
# for each player it asks the deck for 2 cards which it then gives to player


# when we invoke play method -> shuffle the cards -> deal the initial 2 cards
# ask the player to make their bets
# community cards
