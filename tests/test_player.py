import unittest
from unittest.mock import MagicMock

from poker.player import Player
from poker.hand import Hand
from poker.card import Card

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_cards(self):
        hand = Hand()
        player = Player(name = "Sehrish", hand = hand)
        self.assertEqual(player.name, "Sehrish")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock() # magic method tracks its own calss
        mock_hand.best_rank.return_value= "Straight Flush"

        player = Player(name = "Sehrish", hand = mock_hand)
        
        # check that the mocked return value is getting returned from best_hand
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        # When I call player.best_hand() it should call a method best_rank on my mock object
        player.best_hand()
        # test to check hand class is is invoked through mock hand
        mock_hand.best_rank.assert_called()   
        # this test only verifies that best rank is invokded irrespective of whats inside
    
    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name= 'Sehrish', hand = mock_hand)

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit="Diamonds")
        ]

        # hand called once add_cards method with argument cards
        # which then passes it to hand class
        player.add_cards(cards)
        mock_hand.add_cards.assert_called_once_with(cards)