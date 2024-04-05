from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from NaivePlayer import NaivePlayer


class TestNaivePlayer(TestCase):
    def test_play(self):
        hand1 = Hand([Domino(1, 3), Domino(3, 4), Domino(1, 5), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        board = Board(5)
        self.assertEqual(True, player1.play(board))  # Domino(1, 3)
        self.assertEqual(True, player1.play(board))  # Domino(3, 4)
        self.assertEqual(True, player1.play(board))  # Domino(1, 5)
        self.assertEqual(False, player1.play(board))  # Domino(6, 6)
