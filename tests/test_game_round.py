import unittest
from unittest.mock import MagicMock

from poker.game_round import GameRound

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


