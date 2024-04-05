from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer


class TestMaxScorePlayer(TestCase):
    def test_highest_score(self):
        hand1 = Hand([Domino(1, 3), Domino(1, 5), Domino(3, 4), Domino(6, 6)])
        player1 = MaxScorePlayer("Nicole", 23, hand1)
        self.assertEqual(Domino(6, 6), player1.highest_score(hand1))

    def test_play(self):
        hand1 = Hand([Domino(2, 2), Domino(1, 5), Domino(6, 4), Domino(5, 6)])
        player1 = MaxScorePlayer("Nicole", 23, hand1)
        board = Board(5)
        self.assertEqual(True, player1.play(board))  # Domino(5, 6)
        self.assertEqual(True, player1.play(board))  # Domino(6, 4)
        self.assertEqual(True, player1.play(board))  # Domino(1, 5)
        self.assertEqual(False, player1.play(board))  # Domino(2, 2)

    def test_str(self):
        hand1 = Hand([Domino(1, 3), Domino(1, 5), Domino(3, 4), Domino(6, 6)])
        player1 = MaxScorePlayer("Nicole", 23, hand1)
        self.assertEqual("Name: Nicole, Age: 23, Hand: [1|3][1|5][3|4][6|6], Score: 29, I can win the game!", str(player1))

    def test_repr(self):
        hand1 = Hand([Domino(1, 3), Domino(1, 5), Domino(3, 4), Domino(6, 6)])
        player1 = MaxScorePlayer("Nicole", 23, hand1)
        self.assertEqual("Name: Nicole, Age: 23, Hand: [1|3][1|5][3|4][6|6], Score: 29, I can win the game!", player1.__repr__())


