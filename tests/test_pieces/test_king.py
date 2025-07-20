import unittest
from chess_simulator.pieces.king import King


class TestKing(unittest.TestCase):
    """
    Unit tests for the King piece.
    """
    def test_king_middle_board(self):
        king = King("D5")
        expected_moves = ["C4", "C5", "C6", "D4", "D6", "E4", "E5", "E6"]
        self.assertCountEqual(king.get_possible_moves(), expected_moves)

    def test_king_corner(self):
        king = King("A1")
        expected_moves = ["A2", "B1", "B2"]
        self.assertCountEqual(king.get_possible_moves(), expected_moves)

    def test_king_edge_row(self):
        king = King("D1")
        expected_moves = ["C1", "C2", "D2", "E1", "E2"]
        self.assertCountEqual(king.get_possible_moves(), expected_moves)

    def test_king_edge_col(self):
        king = King("A4")
        expected_moves = ["A3", "A5", "B3", "B4", "B5"]
        self.assertCountEqual(king.get_possible_moves(), expected_moves)


if __name__ == '__main__':
    unittest.main()