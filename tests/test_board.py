import unittest
from chess_simulator.board import Board


class TestBoard(unittest.TestCase):
    """
    Unit tests for the Board class methods.
    """
    def test_cell_to_coords_valid(self):
        self.assertEqual(Board.cell_to_coords("A1"), (0, 0))
        self.assertEqual(Board.cell_to_coords("a1"), (0, 0))

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
        self.assertFalse(Board.is_valid_coord(-1, 0))


if __name__ == '__main__':
    unittest.main()