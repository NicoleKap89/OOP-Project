from unittest import TestCase

from Domino import Domino
from Exceptions import NoSuchDominoException
from Hand import Hand


class TestHand(TestCase):
    def test_init(self):
        hand = Hand([Domino(1, 2), Domino(3, 4)])
        self.assertEqual([Domino(1, 2), Domino(3, 4)], hand.array)

    def test_add(self):
        # index is None
        hand1 = Hand([Domino(1, 2), Domino(3, 4)])
        hand2 = Hand([Domino(1, 2)])
        hand2.add(Domino(3, 4))
        self.assertEqual(hand1, hand2)

        # index is number
        hand3 = Hand([Domino(3, 4), Domino(1, 2)])
        hand4 = Hand([Domino(1, 2)])
        hand4.add(Domino(3, 4), 0)
        self.assertEqual(hand3, hand4)

    def test_remove_domino(self):
        hand1 = Hand([Domino(1, 2), Domino(3, 4)])
        self.assertEqual(1, hand1.remove_domino(Domino(3, 4)))
        with self.assertRaises(NoSuchDominoException):
            hand1.remove_domino(Domino(3, 4))


