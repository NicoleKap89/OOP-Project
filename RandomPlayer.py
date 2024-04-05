import copy
import random

from Player import Player


class RandomPlayer(Player):
    def play(self, board):
        """
        a strategy for player to play domino. shuffles the dominoes and then trys to put dominoes.
        :param board: domino board
        :return: True if the player can put a domino on the board, False otherwise.
        """
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        hand = copy.deepcopy(self.hand.array)
        random.shuffle(hand)
        for do in range(len(hand)):
            if board.add_right(hand[do]):
                self.hand.remove_domino(hand[do])
                return True
            elif board.add_left(hand[do]):
                self.hand.remove_domino(hand[do])
                return True
        return False
