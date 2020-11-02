from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound

# once executed in REPL card1 and card2 will be available in namespace
# no need of these cards we have made 52 cards
# card1 = Card(rank = "2", suit = "Spades")
# card2 = Card(rank = "Ace", suit = "Hearts")

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

# from main import card1, card2
# from main import deck, cards, game_round, hand1, hand2, player1, player2
# python -m unittest discover tests

# test it like card1.rank, str(card1), card2

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
