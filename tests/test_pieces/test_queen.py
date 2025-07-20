import unittest
from chess_simulator.pieces.queen import Queen


class TestQueen(unittest.TestCase):
    """
    Unit tests for the Queen piece.
    """
    def test_queen_middle_board(self):
        queen = Queen("E4")
        expected_moves = [
            "A4", "B4", "C4", "D4", "F4", "G4", "H4",
            "E1", "E2", "E3", "E5", "E6", "E7", "E8",
            "A8", "B7", "C6", "D5", "F3", "G2", "H1",
            "B1", "C2", "D3", "F5", "G6", "H7"
        ]
        self.assertCountEqual(queen.get_possible_moves(), expected_moves)

    def test_queen_corner(self):
        queen = Queen("A1")
        expected_moves = [
            "A2", "A3", "A4", "A5", "A6", "A7", "A8",
            "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "B2", "C3", "D4", "E5", "F6", "G7", "H8"
        ]
        self.assertCountEqual(queen.get_possible_moves(), expected_moves)

    def test_queen_edge_row(self):
        queen = Queen("D1")
        expected_moves = [
            "A1", "B1", "C1", "E1", "F1", "G1", "H1",
            "D2", "D3", "D4", "D5", "D6", "D7", "D8",
            "A4", "B3", "C2", "E2", "F3", "G4", "H5"
        ]
        self.assertCountEqual(queen.get_possible_moves(), expected_moves)


if __name__ == '__main__':
    unittest.main()