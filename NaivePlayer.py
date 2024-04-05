
from Player import Player


class NaivePlayer(Player):
    def play(self, board):
        """
        a strategy for player to play domino. trys to put the domino by the order in his hand.
        :param board: domino board
        :return: True if the player can put a domino on the board, False otherwise.
        """
        for do in range(len(self.hand)):
            if board.add_right(self.hand[do]):
                self.hand.remove_domino(self.hand[do])
                return True
            elif board.add_left(self.hand[do]):
                self.hand.remove_domino(self.hand[do])
                return True
        return False
