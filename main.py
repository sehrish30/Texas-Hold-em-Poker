from poker.card import Card
from poker.deck import Deck

# once executed in REPL card1 and card2 will be available in namespace
# no need of these cards we have made 52 cards
# card1 = Card(rank = "2", suit = "Spades")
# card2 = Card(rank = "Ace", suit = "Hearts")

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

# from main import card1, card2
# from main import deck, cards
# python -m unittest discover tests

# test it like card1.rank, str(card1), card2