import copy

from Domino import Domino
from Player import Player


class MaxScorePlayer(Player):
    def highest_score(self, hand):
        """
        returns the domino with the total highest score on it
        :param hand: the hand that is checked
        :return: domino which its score is the highest
        """
        highest_score = 0
        highest_dom = Domino(0, 0)
        for dom in range(len(hand)):
            if hand[dom].get_left() + hand[dom].get_right() > highest_score:
                highest_score = hand[dom].get_left() + hand[dom].get_right()
                highest_dom = hand[dom]
        return highest_dom

    def play(self, board):
        """
        a strategy for player to play domino. trys to put first the highest score domino in his hand. if there isn't, checks the next and go on.
        :param board: domino board
        :return: True if the player can put a domino on the board, False otherwise.
        """
        hand = copy.deepcopy(self.hand)
        for dom in range(len(hand)):
            highest_dom = self.highest_score(hand)
            if board.add_right(highest_dom):
                hand.remove_domino(highest_dom)
                self.hand.remove_domino(highest_dom)
                return True
            elif board.add_left(highest_dom):
                hand.remove_domino(highest_dom)
                self.hand.remove_domino(highest_dom)
                return True
            hand.remove_domino(highest_dom)
        return False

    def __str__(self):
        """
        returns string representation of the player
        :return: string representation of the player
        """
        return f'Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}, I can win the game!'

    def __repr__(self):
        """
        returns string representation of the player
        :return: string representation of the player
        """
        return self.__str__()
