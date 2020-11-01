import unittest
from unittest.mock import MagicMock, call

from poker.game_round import GameRound
from poker.card import Card

class GameRoundTest(unittest.TestCase):
    def test_stores_deck_and_players(self):
      # the purpose of this test is only to check correct assignment
       deck = MagicMock()
       players = [
           MagicMock(),
           MagicMock()
       ]
       # fake players because if I assign them I will have to mock hand which goes deep levels

       game_round = GameRound(
            deck = deck,
            players= players
        )

       self.assertEqual(
            game_round.deck,
            deck
        )

       self.assertEqual(
            game_round.players,
            players
        )

    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]

        game_round = GameRound(
            deck = mock_deck,
            players = players
        )
        
        # when play is invoked we want deck to invoke shuffle
        game_round.play()
        mock_deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_from_deck_to_each_player(self):
        first_two_cards= [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "6", suit = "Clubs")
        ]
        next_two_cards = [
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "4", suit = "Spades")
        ]
        
        mock_deck = MagicMock()
        # side effect will ensure all elements of array are values returned like first value
        # on first call then second attribute on second call
        # alternative to side effect is return value
        mock_deck.remove_cards.side_effect = [first_two_cards, next_two_cards]

        # since its side_effect I am also testing the data that is fundamentally coming from remove cards method

        mock_player1 =  MagicMock()
        mock_player2 =  MagicMock()

        players = [mock_player1, mock_player2]

        game_round = GameRound(
            deck = mock_deck,
            players = players
        )
        game_round.play()

        # We have to remove 5 times to remove 2 cards from both players
        # same like mock_deck.call_args_list
        # returns all the ways this mock has been invoked
        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2)
        ])
        
        # didnot use assert_called_once_with for flexibility if we want to add 2 3 times
        mock_player1.add_cards.assert_called_with(first_two_cards)
        mock_player2.add_cards.assert_called_with(next_two_cards)



