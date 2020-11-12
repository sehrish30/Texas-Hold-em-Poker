import unittest
from poker.hand import Hand
from poker.card import Card

class HandTest(unittest.TestCase):
    def test_starts_with_no_card(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_with_technical_representation(self) :
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]   
        hand = Hand()
        hand.add_cards(cards) 

        self.assertEqual(
            repr(hand),
            "7 of Clubs, Ace of Diamonds"
        )

    def test_recieves_and_stores_cards(self):
        # this is checking for the sorting in __init__
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        six_of_clubs = Card(rank = "6", suit = "Clubs")
        cards = [
            ace_of_spades,
            six_of_clubs
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [
                six_of_clubs,
                ace_of_spades
            ]
        )

   




