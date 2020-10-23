import unittest
from poker.deck import Deck
from poker.card import Card

# initially Deck is empty because other games vary the number of cards
class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

# instantiates the card class and places it in deck
    def test_adds_cards_to_its_collection(self):
        card = Card(rank= "Ace", suit= "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards, [card]
        )
