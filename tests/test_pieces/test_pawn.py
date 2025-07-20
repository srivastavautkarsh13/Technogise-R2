import unittest
from chess_simulator.pieces.pawn import Pawn


class TestPawn(unittest.TestCase):
    """
    Unit tests for the Pawn piece.
    """
    def test_pawn_middle_board(self):
        pawn = Pawn("D4")
        self.assertEqual(pawn.get_possible_moves(), ["D5"])

    def test_pawn_edge_col(self):
        pawn = Pawn("A2")
        self.assertEqual(pawn.get_possible_moves(), ["A3"])

    def test_pawn_at_last_row(self):
        pawn = Pawn("E8")
        self.assertEqual(pawn.get_possible_moves(), [])


if __name__ == '__main__':
    unittest.main()