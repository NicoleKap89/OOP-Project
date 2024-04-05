from unittest import TestCase

from Domino import Domino
from Hand import Hand
from NaivePlayer import NaivePlayer


class TestPlayer(TestCase):
    def test_init(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        self.assertEqual("Nicole", player1.name)
        self.assertEqual(23, player1.age)
        self.assertEqual(hand1, player1.hand)

    def test_score(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        self.assertEqual(16, player1.score())

    def test_has_dominoes(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        self.assertEqual(True, player1.has_dominoes())

        hand2 = Hand([])
        player2 = NaivePlayer("Nicole", 23, hand2)
        self.assertEqual(False, player2.has_dominoes())

    def test_str(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        self.assertEqual('Name: Nicole, Age: 23, Hand: [1|3][6|6], Score: 16', str(player1))

    def test_repr(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        self.assertEqual('Name: Nicole, Age: 23, Hand: [1|3][6|6], Score: 16', player1.__repr__())


