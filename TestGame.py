from unittest import TestCase

from Board import Board
from Domino import Domino
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team


class TestGame(TestCase):
    def test_winning_team(self):
        hand1 = Hand([Domino(1, 1), Domino(2, 2)])
        hand2 = Hand([Domino(3, 3), Domino(4, 4)])
        hand3 = Hand([Domino(5, 5), Domino(6, 5)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        player3 = NaivePlayer("Rima", 50, hand3)
        players1 = [player1, player2, player3]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 1), Domino(2, 2)])
        hand5 = Hand([Domino(3, 3), Domino(4, 4)])
        hand6 = Hand([Domino(5, 5), Domino(6, 6)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        player6 = NaivePlayer("Roza", 50, hand6)
        players2 = [player4, player5, player6]
        team2 = Team("Blue", players2)

        board = Board(5)
        game = Game(board, team1, team2)
        self.assertEqual('Team Red wins Team Blue', game.winning_team(team1, team2))

        hand1 = Hand([Domino(1, 1), Domino(2, 2)])
        hand2 = Hand([Domino(3, 3), Domino(4, 4)])
        hand3 = Hand([Domino(5, 5), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        player3 = NaivePlayer("Rima", 50, hand3)
        players1 = [player1, player2, player3]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 1), Domino(2, 2)])
        hand5 = Hand([Domino(3, 3), Domino(4, 4)])
        hand6 = Hand([Domino(5, 5), Domino(6, 5)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        player6 = NaivePlayer("Roza", 50, hand6)
        players2 = [player4, player5, player6]
        team2 = Team("Blue", players2)

        board = Board(5)
        game = Game(board, team1, team2)
        self.assertEqual('Team Blue wins Team Red', game.winning_team(team1, team2))

        hand1 = Hand([Domino(1, 1), Domino(2, 2)])
        hand2 = Hand([Domino(3, 3), Domino(4, 4)])
        hand3 = Hand([Domino(5, 5), Domino(6, 6)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        player3 = NaivePlayer("Rima", 50, hand3)
        players1 = [player1, player2, player3]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 1), Domino(2, 2)])
        hand5 = Hand([Domino(3, 3), Domino(4, 4)])
        hand6 = Hand([Domino(5, 5), Domino(6, 6)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        player6 = NaivePlayer("Roza", 50, hand6)
        players2 = [player4, player5, player6]
        team2 = Team("Blue", players2)

        board = Board(5)
        game = Game(board, team1, team2)
        self.assertEqual('Draw!', game.winning_team(team1, team2))

    def test_play(self):
        # Red wins
        hand1 = Hand([Domino(1, 1), Domino(2, 2)])
        hand2 = Hand([Domino(3, 3), Domino(4, 4)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        players1 = [player1, player2]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 3), Domino(2, 2)])
        hand5 = Hand([Domino(2, 5), Domino(4, 4)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        players2 = [player4, player5]
        team2 = Team("Blue", players2)

        board = Board(5)
        game = Game(board, team1, team2)
        self.assertEqual('Team Red wins Team Blue', game.play())

        # Blue wins
        hand1 = Hand([Domino(1, 3), Domino(2, 2)])
        hand2 = Hand([Domino(2, 5), Domino(4, 4)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        players1 = [player1, player2]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 1), Domino(2, 2)])
        hand5 = Hand([Domino(3, 3), Domino(4, 4)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        players2 = [player4, player5]
        team2 = Team("Blue", players2)

        board = Board(5)
        game = Game(board, team1, team2)
        self.assertEqual('Team Blue wins Team Red', game.play())

        # Draw
        hand1 = Hand([Domino(1, 3), Domino(3, 2)])
        hand2 = Hand([Domino(2, 5), Domino(4, 4)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        players1 = [player1, player2]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 1), Domino(2, 2)])
        hand5 = Hand([Domino(5, 1), Domino(4, 4)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        players2 = [player4, player5]
        team2 = Team("Blue", players2)

        board1 = Board(7)
        game = Game(board1, team1, team2)
        self.assertEqual('Draw!', game.play())


        # Red wins because left out of cards
        hand1 = Hand([Domino(1, 3), Domino(3, 2)])
        hand2 = Hand([Domino(2, 5), Domino(2, 4)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        players1 = [player1, player2]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 1), Domino(2, 2)])
        hand5 = Hand([Domino(5, 2), Domino(4, 4)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        players2 = [player4, player5]
        team2 = Team("Blue", players2)

        board1 = Board(7)
        game = Game(board1, team1, team2)
        self.assertEqual('Team Red wins Team Blue', game.play())

        # Blue wins because left out of cards
        hand1 = Hand([Domino(1, 3), Domino(3, 2)])
        hand2 = Hand([Domino(3, 5), Domino(0, 4)])
        player1 = NaivePlayer("Nicole", 23, hand1)
        player2 = NaivePlayer("Yoni", 22, hand2)
        players1 = [player1, player2]
        team1 = Team("Red", players1)

        hand4 = Hand([Domino(1, 1), Domino(2, 2)])
        hand5 = Hand([Domino(5, 2), Domino(1, 4)])
        player4 = NaivePlayer("Romi", 23, hand4)
        player5 = NaivePlayer("Bar", 22, hand5)
        players2 = [player4, player5]
        team2 = Team("Blue", players2)

        board1 = Board(7)
        game = Game(board1, team1, team2)
        self.assertEqual('Team Blue wins Team Red', game.play())
