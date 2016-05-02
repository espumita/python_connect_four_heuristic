import unittest

from game.ConnectFour import ConnectFour
from game.heuristics.HorizontalHeuristic import HorizontalHeuristic


class _HorizontalHeuristic(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.state = ConnectFour().initial
        cls.problemPlayer = 'X'
        cls.otherPlayer = "O"

    def horizontalBoardHeuristic(self):
        heuristicValue = 0
        for key in self.state.board:
            heuristicValue += HorizontalHeuristic(self.state, self.problemPlayer, self.otherPlayer).heuristicIn(key)
            if heuristicValue == -float('inf') or heuristicValue == float('inf'):
                return heuristicValue
        return heuristicValue

    def test_when_whe_got_empty_board_heuristic_should_be_0(self):
        self.assertEqual(self.horizontalBoardHeuristic(), 0)

    def test_when_whe_got_a_single_token_in_the_board_heuristic_should_be_1(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), 1)

    def test_when_whe_got_a_single_enemy_token_in_the_board_heuristic_should_be_minus_1(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), -1)

    def test_when_whe_got_a_horizontal_connection_of_two_tokens_heuristic_should_be_9(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), 9)

    def test_when_whe_got_a_horizontal_connection_of_two_enemy_tokens_heuristic_should_be_minus_9(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), -9)

    def test_when_whe_got_a_horizontal_connection_of_three_tokens_heuristic_should_be_39(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'X')
        self.state.board.setdefault((6, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), 39)

    def test_when_whe_got_a_horizontal_connection_of_three_enemy_tokens_heuristic_should_be_minus_39(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'O')
        self.state.board.setdefault((6, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), -39)

    def test_when_whe_got_a_horizontal_connection_of_four_tokens_heuristic_should_be_infinity(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'X')
        self.state.board.setdefault((6, 1), 'X')
        self.state.board.setdefault((7, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.state.moves.remove((7, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), float('inf'))

    def test_when_whe_got_a_horizontal_connection_of_four_enemy_tokens_heuristic_should_be_minus_infinity(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'O')
        self.state.board.setdefault((6, 1), 'O')
        self.state.board.setdefault((7, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.state.moves.remove((7, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), -float('inf'))