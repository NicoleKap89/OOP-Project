from unittest import TestCase

from Board import Board
from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer
from NaivePlayer import NaivePlayer
from RandomPlayer import RandomPlayer
from Team import Team


class TestTeam(TestCase):
    def test_init(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(0, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        self.assertEqual("Kaplan", team1.name)

    def test_get_team(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(0, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        self.assertEqual(players, team1.get_team())

    def test_score_team(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(0, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        self.assertEqual(38, team1.score_team())

        hand1 = Hand([])
        hand2 = Hand([])
        hand3 = Hand([])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        self.assertEqual(0, team1.score_team())

    def test_has_dominoes_team(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(0, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        self.assertEqual(True, team1.has_dominoes_team())

        hand1 = Hand([])
        hand2 = Hand([])
        hand3 = Hand([])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        self.assertEqual(False, team1.has_dominoes_team())

    def test_play(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(0, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        board1 = Board(5)
        board1.add(Domino(1, 2))
        board1.add(Domino(2, 3))
        self.assertEqual(True, team1.play(board1))

        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(4, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        board1 = Board(5)
        board1.add(Domino(0, 2))
        board1.add(Domino(2, 0))
        self.assertEqual(False, team1.play(board1))

    def test_str(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(4, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        string_wanted = 'Name Kaplan, Score team: 42, Players: Name: Nicole, Age: 23, Hand: [1|3][6|6], Score: 16' \
                        ' Name: Yoni, Age: 22, Hand: [4|5][4|6], Score: 19' \
                        ' Name: Rima, Age: 50, Hand: [2|2][2|1], Score: 7, I can win the game!'
        self.assertEqual(string_wanted, str(team1))

        hand1 = Hand([])
        hand2 = Hand([])
        hand3 = Hand([])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        string_wanted = 'Name Kaplan, Score team: 0, Players: Name: Nicole, Age: 23, Hand: , Score: 0' \
                        ' Name: Yoni, Age: 22, Hand: , Score: 0' \
                        ' Name: Rima, Age: 50, Hand: , Score: 0, I can win the game!'
        self.assertEqual(string_wanted, str(team1))



    def test_repr(self):
        hand1 = Hand([Domino(1, 3), Domino(6, 6)])
        hand2 = Hand([Domino(4, 5), Domino(4, 6)])
        hand3 = Hand([Domino(2, 2), Domino(2, 1)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        string_wanted = 'Name Kaplan, Score team: 42, Players: Name: Nicole, Age: 23, Hand: [1|3][6|6], Score: 16' \
                        ' Name: Yoni, Age: 22, Hand: [4|5][4|6], Score: 19' \
                        ' Name: Rima, Age: 50, Hand: [2|2][2|1], Score: 7, I can win the game!'
        self.assertEqual(string_wanted, str(team1))

        hand1 = Hand([])
        hand2 = Hand([])
        hand3 = Hand([])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = RandomPlayer("Yoni", 22, hand2)
        player3 = MaxScorePlayer("Rima", 50, hand3)
        players = [player1, player2, player3]
        team1 = Team("Kaplan", players)
        string_wanted = 'Name Kaplan, Score team: 0, Players: Name: Nicole, Age: 23, Hand: , Score: 0' \
                        ' Name: Yoni, Age: 22, Hand: , Score: 0' \
                        ' Name: Rima, Age: 50, Hand: , Score: 0, I can win the game!'
        self.assertEqual(string_wanted, team1.__repr__())