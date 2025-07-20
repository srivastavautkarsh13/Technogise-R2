import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from chess_simulator import Board, Piece, Pawn, King, Queen, get_piece_class

class TestBoard(unittest.TestCase):
    """
    Unit tests for the Board class methods.
    """
    def test_cell_to_coords_valid(self):
        self.assertEqual(Board.cell_to_coords("A1"), (0, 0))
        self.assertEqual(Board.cell_to_coords("a1"), (0, 0)) # Test case insensitivity for column

    def test_cell_to_coords_invalid_format(self):
        with self.assertRaisesRegex(ValueError, "Invalid cell string format"):
            Board.cell_to_coords("A")

    def test_cell_to_coords_invalid_col(self):
        with self.assertRaisesRegex(ValueError, "Invalid column 'I'"):
            Board.cell_to_coords("I1")

    def test_cell_to_coords_invalid_row(self):
        with self.assertRaisesRegex(ValueError, "Invalid row '0'"):
            Board.cell_to_coords("A0")

    def test_coords_to_cell_valid(self):
        self.assertEqual(Board.coords_to_cell(0, 0), "A1")

    def test_coords_to_cell_invalid(self):
        with self.assertRaisesRegex(ValueError, "out of board bounds"):
            Board.coords_to_cell(-1, 0)

    def test_is_valid_coord(self):
        self.assertTrue(Board.is_valid_coord(0, 0))
        self.assertFalse(Board.is_valid_coord(0, 8))


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

    def test_get_possible_moves_not_implemented(self):
        # Test that the abstract method raises NotImplementedError
        with self.assertRaises(NotImplementedError):
            Piece("A1").get_possible_moves()


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
        pawn = Pawn("E8") # Pawn at the last row cannot move forward
        self.assertEqual(pawn.get_possible_moves(), [])


class TestKing(unittest.TestCase):
    """
    Unit tests for the King piece.
    """
    def test_king_middle_board(self):
        king = King("D5")
        expected_moves = ["C4", "C5", "C6", "D4", "D6", "E4", "E5", "E6"]
        self.assertCountEqual(king.get_possible_moves(), expected_moves) # Use assertCountEqual for unordered lists

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


class TestQueen(unittest.TestCase):
    """
    Unit tests for the Queen piece.
    """
    def test_queen_middle_board(self):
        queen = Queen("E4")
        expected_moves = [
            "A4", "B4", "C4", "D4", "F4", "G4", "H4",  # Horizontal
            "E1", "E2", "E3", "E5", "E6", "E7", "E8",  # Vertical
            "A8", "B7", "C6", "D5", "F3", "G2", "H1",  # Diagonal (top-left to bottom-right)
            "B1", "C2", "D3", "F5", "G6", "H7"         # Diagonal (bottom-left to top-right)
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
            "A4", "B3", "C2", "E2", "F3", "G4", "H5",
            "A1", "B1", "C1", "E1", "F1", "G1", "H1",
            "C2", "E2", "B3", "F3", "A4", "G4", "H5"
        ]
        # Remove duplicates from expected_moves for assertCountEqual
        expected_moves = list(set(expected_moves))
        self.assertCountEqual(queen.get_possible_moves(), expected_moves)


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
    unittest.main(argv=['first-arg-is-ignored'], exit=False)