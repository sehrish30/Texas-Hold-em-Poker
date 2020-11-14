from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

# from main import deck, cards, game_round, hand1, hand2, player1, player2
# python -m unittest discover tests


hand1 = Hand()
hand2 = Hand()
player1 = Player(name= "Sehrish", hand = hand1)
player2 = Player(name= "Ali", hand = hand2)
players = [player1, player2]

# in gameround it will ask for deck and players
# players will compute best_rank locally
# and the play will find out the winner
game_round = GameRound(deck = deck, players=players)
game_round.play()

for player in players:
    print(f"{player.name} receives a {player.hand}.")
    index, hand_name, hand_cards = player.best_hand()
    hand_cards_strings = [str(card) for card in hand_cards]
    hand_cards_string = " and ".join(hand_cards_strings)
    print(f"{player.name} has a {hand_name} with a {hand_cards_string}.")

# max will extract one object from players
winning_player = max(players)
print(f"The winner is {winning_player.name}")

# run it python main.py





