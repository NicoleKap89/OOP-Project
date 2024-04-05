from Exceptions import InvalidNumberException


class Domino:
    def __init__(self, left, right):
        """
        A constructor that initializes the fields left and right
        :param left: (int) between 0-6, exception raised if not in this range
        :param right: (int) between 0-6, exception raised if not in this range
        """
        if left < 0 or left > 6:
            raise InvalidNumberException("input should be integer between 0- 6")
        if right < 0 or right > 6:
            raise InvalidNumberException("input should be integer between 0- 6")
        self.__left = left
        self.__right = right

    def get_left(self):
        """
        returns the left side of the domino
        :return: (int) the left side of the domino
        """
        return self.__left

    def get_right(self):
        """
        returns the right side of the domino
        :return: (int) the right side of the domino
        """
        return self.__right

    def __str__(self):
        """
        returns string representation of the domino
        :return: (str) string representation of the domino
        """
        return f'[{self.__left}|{self.__right}]'

    def __repr__(self):
        """
        returns string representation of the domino
        :return: (str) string representation of the domino
        """
        return self.__str__()

    def __eq__(self, other):
        """
        returns whether self and other are equal
        :param other: object which is compared to
        :return: (bool) True if equal, False otherwise.
        """
        if not isinstance(other, Domino):
            return False
        if (self.__left == other.__left and self.__right == other.__right) or (self.__left == other.__right and self.__right == other.__left):
            return True
        return False

    def __ne__(self, other):
        """
        returns whether self and other are different
        :param other: object which is compared to
        :return: (bool) True if different, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        returns whether self is greater than other
        :param other: object which is compared to
        :return: (bool) True if self greater then other, False otherwise.
        """
        if not isinstance(other, Domino):
            return False
        if (self.__left + self.__right) > (other.__left + other.__right):
            return True
        return False

    def __contains__(self, key):
        """
        returns whether key is in the left or the right side of the domino.
        :param key: (int) number to check if on one of the sides
        :return: (bool) True if key is in the left or the right side of the domino, False otherwise.
        """
        if key == self.__left or key == self.__right:
            return True
        return False

    def flip(self):
        """
        flips the domino
        :return: (Domino) flipped domino
        """
        return Domino(self.__right, self.__left)