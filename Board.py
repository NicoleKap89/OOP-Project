from Collection import Collection
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException


class Board(Collection):
    def __init__(self, max_capacity):
        """
        A constructor that initializes the field max capacity, an array field is created as empty list by default
        :param max_capacity: (int) between 1-28. if not in range an exception will raise
        """
        Collection.__init__(self, [])
        if max_capacity < 1 or max_capacity > 28:
            raise InvalidNumberException("number should be between 1 - 28")
        self.max_capacity = max_capacity
        self.array = []

    def in_left(self):
        """
        returns the most left value in the field, if board is empty an exception will raise
        :return: (int/exception) the most left value in the field or exception
        """
        if len(self.array) == 0:
            raise EmptyBoardException("the board is empty")
        return self.array[0].get_left()

    def in_right(self):
        """
        returns the most right value in the field, if board is empty an exception will raise
        :return: (int/exception) the most right value in the field or exception
        """
        if len(self.array) == 0:
            raise EmptyBoardException("the board is empty")
        return self.array[-1].get_right()

    def add(self, domino, add_to_right=True):
        """
        adds a domino to the board if possible, else raises exception
        :param domino: domino which try to add
        :param add_to_right: if true, trys to add to the right side of the board only. if False, trys to add to the left side only.
        :return: (bool/exception) True is a domino was added, False if was not able to add, exception if the board is full.
        """
        if len(self.array) >= self.max_capacity:  # checks if board is full
            raise FullBoardException("The board is full, you can't add dominoes to it.")
        if len(self.array) == 0:  # if board is empty, adds first domino
            self.array.append(domino)
            return True
        if add_to_right:  # trys to add the domino to the right side of the board
            if domino.get_left() == self.in_right():  # trys to add the domino regular way
                self.array.append(domino)
                return True
            elif domino.flip().get_left() == self.in_right():  # trys to add the domino flipped
                self.array.append(domino.flip())
                return True
        elif not add_to_right:  # trys to add the domino to the left side of the board
            if domino.get_right() == self.in_left():  # trys to add the domino regular way
                self.array.insert(0, domino)
                return True
            elif domino.flip().get_right() == self.in_left():  # trys to add the domino flipped
                self.array.insert(0, domino.flip())
                return True
        return False

    def add_left(self, domino):
        """
        adds a domino to the left side of the board if possible, else raises exception
        :param domino: domino which try to add
        :return: (bool) True is a domino was added, False if was not able to add
        """
        try:
            return self.add(domino, False)
        except:
            return False

    def add_right(self, domino):
        """
        adds a domino to the right side of the board if possible, else raises exception
        :param domino: domino which try to add
        :return: (bool) True is a domino was added, False if was not able to add
        """
        try:
            return self.add(domino)
        except:
            return False

    def __eq__(self, other):
        """
        returns whether self and other are equal. defined as equal if max capacity are equal and the domino placement is equal.
        :param other: object which is compared to
        :return: (bool) True if equal, False otherwise.
        """
        if not isinstance(other, Board):
            return False
        if self.max_capacity != other.max_capacity:
            return False
        if len(self.array) != len(other.array):
            return False
        for do in range(len(self.array)):
            if self.array[do].get_left() != other.array[do].get_left() or self.array[do].get_right() != other.array[do].get_right():
                return False
        return True

    def __ne__(self, other):
        """
        returns whether self and other are different. defined as different if max capacity are different and the domino placement is different.
        :param other: object which is compared to
        :return: True if different, False otherwise.
        """
        return not self.__eq__(other)