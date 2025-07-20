import unittest
from chess_simulator.pieces.pawn import Pawn


class TestPiece(unittest.TestCase):
    """
    Unit tests for the abstract Piece class.
    """
    def test_piece_initialization_valid(self):
        piece = Pawn("A1")
        self.assertEqual(piece.position_str, "A1")
        self.assertEqual(piece.row, 0)
        self.assertEqual(piece.col, 0)

    def test_piece_initialization_invalid_position(self):
        with self.assertRaisesRegex(ValueError, "Invalid starting position 'Z9'"):
            Pawn("Z9")


if __name__ == '__main__':
    unittest.main()