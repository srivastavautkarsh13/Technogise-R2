import unittest
from utils.piece_factory import get_piece_class
from chess_simulator.pieces.pawn import Pawn
from chess_simulator.pieces.king import King
from chess_simulator.pieces.queen import Queen



class TestGetPieceClass(unittest.TestCase):
    """
    Unit tests for the get_piece_class utility function.
    """
    def test_get_piece_class_valid(self):
        self.assertEqual(get_piece_class("Pawn"), Pawn)
        self.assertEqual(get_piece_class("King"), King)
        self.assertEqual(get_piece_class("Queen"), Queen)
        self.assertEqual(get_piece_class("pawn"), Pawn) # Test case insensitivity
        self.assertEqual(get_piece_class("KING"), King)

    def test_get_piece_class_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unknown chess piece type: 'Rook'"):
            get_piece_class("Rook")


if __name__ == '__main__':
    unittest.main()