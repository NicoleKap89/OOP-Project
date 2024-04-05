import copy


class Team:
    def __init__(self, name, players):
        """
        A constructor that initializes the fields name and players
        :param name: Team name
        :param players: Team players
        """
        self.name = name
        self.__players = players

    def get_team(self):
        """
        returns the players list
        :return: (list[players]) players list
        """
        return self.__players

    def score_team(self):
        """
        calculates the total score of the team
        :return: (int) total score of the team
        """
        tot_score = 0
        for player in range(len(self.__players)):
            tot_score += self.__players[player].score()
        return tot_score

    def has_dominoes_team(self):
        """
        returns if the team has dominoes
        :return: (bool) True if one of the team players has domino, False otherwise
        """
        for player in range(len(self.__players)):
            if self.__players[player].has_dominoes():
                return True
        return False

    def play(self, board):
        """
        makes a move for te team. goes over the players by order when each player trys to make a move.
        :param board: Domino board
        :return: (bool) True if the team succeeded to make a move, False otherwise
        """
        copy_players = copy.copy(self.__players)
        for ply in range(len(copy_players)):
            if copy_players[ply].play(board):
                return True
        return False

    def __str__(self):
        """
        returns string representation of the team
        :return: (str) string representation of the team
        """
        players_list = self.get_team()
        players_list = ' '.join(str(elem) for elem in players_list)
        return f'Name {self.name}, Score team: {self.score_team()}, Players: {players_list}'

    def __repr__(self):
        """
        returns string representation of the team
        :return: (str) string representation of the team
        """
        return self.__str__()
