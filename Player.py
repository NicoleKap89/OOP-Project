import abc
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, age, hand):
        """
        A constructor that initializes the fields name, age and hand
        :param name: name of the player
        :param age: age of the player
        :param hand: hand pf the player
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
        return the total score of the player
        :return: total score of the player
        """
        tot_sco = 0
        for do in range(len(self.hand)):
            tot_sco += self.hand[do].get_left() + self.hand[do].get_right()
        return tot_sco

    def has_dominoes(self):
        """
        returns if the player still has domino in the hand
        :return: (bool) True if the player has domino, False otherwise.
        """
        if len(self.hand) != 0:
            return True
        return False

    @abstractmethod
    def play(self, board):
        """
        abstract method. a strategy for players which will be defined individually for each child.
        """
        pass

    def __str__(self):
        """
        returns a string the represents the player
        :return: a string the represents the player
        """
        return f'Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}'

    def __repr__(self):
        """
        returns a string the represents the player
        :return: a string the represents the player
        """
        return self.__str__()
