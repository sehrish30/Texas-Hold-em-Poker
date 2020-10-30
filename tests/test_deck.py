import unittest
from unittest.mock import patch

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

    # whenever program uses random.shuffle step in the middle and call mock object
    @patch('random.shuffle') 
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        # whenever patch decorator is called its gonna feed it subsequent to our test
        deck = Deck()

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit= "Diamonds")
        ]

        deck.add_cards(cards)

         # now check if mock object was interacted with by invocation of shuffle method
        deck.shuffle()
       
        # check it was called exactly once
        # the argument we expect to have been invoked with is cards
        mock_shuffle.assert_called_once_with(cards)
        


