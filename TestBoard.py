from unittest import TestCase

from Board import Board
from Domino import Domino
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException


class TestBoard(TestCase):
    def test_init(self):
        # bad input
        self.assertRaises(InvalidNumberException, Board, 29)
        self.assertRaises(InvalidNumberException, Board, 0)

        # good input
        board = Board(5)
        self.assertEqual(5, board.max_capacity)

    def test_in_left(self):
        board1 = Board(5)
        board2 = Board(5)
        board2.add(Domino(1, 2))
        board2.add(Domino(1, 3), False)
        with self.assertRaises(EmptyBoardException):
            board1.in_left()
        self.assertEqual(3, board2.in_left())

    def test_in_right(self):
        board1 = Board(5)
        board2 = Board(5)
        board2.add(Domino(1, 2))
        board2.add(Domino(2, 3))
        with self.assertRaises(EmptyBoardException):
            board1.in_right()
        self.assertEqual(3, board2.in_right())

    def test_add(self):
        # regular insert
        board1 = Board(4)
        board1.add(Domino(1, 2))
        self.assertEqual(True, board1.add(Domino(2, 1)))
        self.assertEqual(False, board1.add(Domino(4, 5)))
        self.assertEqual(True, board1.add(Domino(2, 1), False))
        self.assertEqual(False, board1.add(Domino(4, 5), False))

        # flip insert
        board2 = Board(4)
        board2.add(Domino(1, 2))
        self.assertEqual(True, board2.add(Domino(1, 2)))
        self.assertEqual(True, board2.add(Domino(1, 2), False))

        # exception
        board3 = Board(2)
        board3.add(Domino(1, 2))
        board3.add(Domino(2, 3))
        with self.assertRaises(FullBoardException):
            board3.add(Domino(3, 4))
        with self.assertRaises(FullBoardException):
            board3.add(Domino(3, 1), False)

    def test_add_left(self):
        board1 = Board(4)
        board1.add(Domino(1, 2))
        self.assertEqual(True, board1.add_left(Domino(2, 1)))
        self.assertEqual(False, board1.add_left(Domino(4, 5)))

        board2 = Board(2)
        board2.add(Domino(1, 2))
        board2.add(Domino(1, 2))
        self.assertEqual(False, board2.add_left(Domino(2, 2)))

    def test_add_right(self):
        board1 = Board(4)
        board1.add(Domino(1, 2))
        self.assertEqual(True, board1.add_right(Domino(2, 3)))
        self.assertEqual(False, board1.add_right(Domino(4, 5)))

        board2 = Board(2)
        board2.add(Domino(1, 2))
        board2.add(Domino(1, 2))
        self.assertEqual(False, board2.add_right(Domino(1, 1)))

    def test_eq(self):
        # equal
        board1 = Board(4)
        board1.add(Domino(1, 2))
        board2 = Board(4)
        board2.add(Domino(1, 2))
        self.assertEqual(True, board1 == board2)

        # not equal because max_capacity is different
        board3 = Board(2)
        board3.add(Domino(1, 2))
        board4 = Board(4)
        board4.add(Domino(1, 2))
        self.assertEqual(False, board3 == board4)

        # not equal because not same type
        board5 = Board(2)
        board5.add(Domino(1, 2))
        board6 = int
        self.assertEqual(False, board5 == board6)

        # not equal because not same domino placement
        board7 = Board(4)
        board7.add(Domino(1, 2))
        board8 = Board(4)
        board8.add(Domino(2, 1))
        self.assertEqual(False, board7 == board8)

        # not equal because not same length
        board9 = Board(4)
        board9.add(Domino(1, 2))
        board9.add(Domino(2, 4))
        board10 = Board(4)
        board10.add(Domino(1, 2))
        self.assertEqual(False, board9 == board10)



    def test_ne(self):
        board1 = Board(4)
        board1.add(Domino(1, 2))
        board2 = Board(4)
        board2.add(Domino(1, 2))
        self.assertEqual(False, board1 != board2)
        board3 = Board(2)
        board3.add(Domino(1, 2))
        board4 = Board(4)
        board4.add(Domino(1, 2))
        self.assertEqual(True, board3 != board4)
        board5 = Board(2)
        board5.add(Domino(1, 2))
        board6 = int
        self.assertEqual(True, board5 != board6)
        board7 = Board(4)
        board7.add(Domino(1, 2))
        board8 = Board(4)
        board8.add(Domino(2, 1))
        self.assertEqual(True, board5 != board6)
