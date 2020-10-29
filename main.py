from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player

# once executed in REPL card1 and card2 will be available in namespace
# no need of these cards we have made 52 cards
# card1 = Card(rank = "2", suit = "Spades")
# card2 = Card(rank = "Ace", suit = "Hearts")

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

# from main import card1, card2
# from main import deck, cards, hand1, hand2, player1, player2
# python -m unittest discover tests

# test it like card1.rank, str(card1), card2

hand1 = Hand(cards = [])
hand2 = Hand(cards = [])
player1 = Player(name= "Sehrish", hand = hand1)
player2 = Player(name= "Bobby", hand = hand2)
