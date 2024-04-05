from unittest import TestCase

from Domino import Domino
from Exceptions import InvalidNumberException


class TestDomino(TestCase):
    def test_init(self):
        # bad input
        self.assertRaises(InvalidNumberException, Domino, 7, 2)
        self.assertRaises(InvalidNumberException, Domino, 2, 7)
        # good input
        domino = Domino(1, 2)
        self.assertEqual(Domino(1, 2), domino)

    def test_get_left(self):
        card = Domino(1, 2)
        self.assertEqual(1, card.get_left())

    def test_get_right(self):
        card = Domino(1, 2)
        self.assertEqual(2, card.get_right())

    def test_str(self):
        card = Domino(1, 2)
        self.assertEqual('[1|2]', card.__str__())

    def test_repr(self):
        card = Domino(1, 2)
        self.assertEqual('[1|2]', card.__repr__(), msg="not equal")

    def test_eq(self):
        card = Domino(1, 2)
        other1 = Domino(2, 1)
        other2 = Domino(3, 1)
        other3 = int
        self.assertEqual(True, card == other1)
        self.assertEqual(False, card == other2)
        self.assertEqual(False, card == other3)

    def test_ne(self):
        card = Domino(1, 2)
        other1 = Domino(2, 1)
        other2 = Domino(3, 1)
        other3 = int
        self.assertEqual(False, card != other1)
        self.assertEqual(True, card != other2)
        self.assertEqual(True, card != other3)

    def test_gt(self):
        card = Domino(1, 3)
        other1 = Domino(2, 1)
        other2 = Domino(4, 1)
        other3 = int
        self.assertEqual(True, card > other1)
        self.assertEqual(False, card > other2)
        self.assertEqual(False, card > other3)


    def test_contains(self):
        card = Domino(1, 3)
        key1 = 3
        key2 = 4
        self.assertEqual(True, key1 in card)
        self.assertEqual(False, key2 in card)

    def test_flip(self):
        card1 = Domino(1, 3)
        card2 = Domino(1, 1)
        self.assertEqual("[3|1]", card1.flip().__str__())
        self.assertEqual("[1|1]", card2.flip().__str__())
