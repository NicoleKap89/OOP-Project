
class Game:
    def __init__(self, board, team1, team2):
        """
        A constructor that initializes the fields board, team1, team2
        :param board: domino board
        :param team1: first team to play the game
        :param team2: second team to play the game
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def winning_team(self, team1, team2):
        """
        returns who is the winning team or Draw
        :param team1: first team who plays
        :param team2: second team who play
        :return: (str) who is the winning team or Draw
        """
        if team1.score_team() > team2.score_team():
            return f'Team {team2.name} wins Team {team1.name}'
        elif team1.score_team() < team2.score_team():
            return f'Team {team1.name} wins Team {team2.name}'
        else:
            return f'Draw!'

    def play(self):
        """
        method that controls the game by the domino game rules.
        :return: (str) the winning team
        """
        team1_can_play = True
        team2_can_play = True
        while (team1_can_play == True) or (team2_can_play == True):
            if not self.team1.play(self.board):
                team1_can_play = False
            if not self.team1.has_dominoes_team():
                break
            if not self.team2.play(self.board):
                team2_can_play = False
            if not self.team2.has_dominoes_team():
                break
        return self.winning_team(self.team1, self.team2)



