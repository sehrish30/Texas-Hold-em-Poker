import unittest
from unittest.mock import MagicMock, call

from poker.game_round import GameRound
from poker.card import Card

class GameRoundTest(unittest.TestCase):
    # setup runs before every test variables arenot available they should be assigned to attributes
    def setUp(self):
        self.first_two_cards= [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "6", suit = "Clubs")
        ]
        self.next_two_cards = [
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "4", suit = "Spades")
        ]
        self.flop_cards = [
                Card(rank = "2", suit = "Diamonds"),
                Card(rank = "4", suit = "Hearts"),
                Card(rank = "10", suit = "Spades")
            ]
        self.turn_card = [Card(rank = "9", suit = "Hearts")]
        self.river_card = [Card(rank = "Queen", suit = "Clubs")]


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
           
        mock_deck = MagicMock()
        # side effect will ensure all elements of array are values returned like first value
        # on first call then second attribute on second call
        # alternative to side effect is return value
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards, # returned value for first player
            self.next_two_cards,  # returned value for second player second call
            self.flop_cards,  # returned value for third call community cards
            self.turn_card,
            self.river_card
        ]

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
        mock_player1.add_cards.assert_has_calls([
            call(self.first_two_cards)
        ])
        mock_player2.add_cards.assert_has_calls([
        call(self.next_two_cards)
        ])

    def test_removes_player_if_not_willing_to_make_bet(self):    
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()

        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False

        players = [player1, player2]

        game_round = GameRound(deck = deck, players = players)
        game_round.play()

        self.assertEqual(
            game_round.players,
            [player2]
        )

    def test_deals_each_player_3_flop_1_turn_and_1_river_cards(self):
            mock_player1 = MagicMock()
            mock_player1.wants_to_fold.return_value = False # since magic mock is truthy value it will evaluate to true and remove all players in _make_bets
            mock_player2 = MagicMock()
            mock_player2.wants_to_fold.return_value = False
            players = [mock_player1, mock_player2]         

            mock_deck = MagicMock()
            mock_deck.remove_cards.side_effect = [
                self.first_two_cards,
                self.next_two_cards,
                self.flop_cards,
                self.turn_card,
                self.river_card
            ]
            game_round = GameRound(deck = mock_deck, players = players)
            game_round.play()

            # first check if deck removes cards with these calls
            mock_deck.remove_cards.assert_has_calls([
                call(3),
                call(1),
                call(1)
            ])

            calls = [
                call(self.flop_cards),
                call(self.turn_card),
                call(self.river_card)
            ]
            # second check if both players get community_cards
            for player in players:
                player.add_cards.assert_has_calls(calls)

            
            
           








# from unittest.mock import MagicMock
# mm = MagicMock()
# mm.fake_method()
# mm.fake_method(1)
# mm.fake_method(1, 2)
# mm.fake_method("Hello")
# mm.fake_method.call_args_list