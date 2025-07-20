"""
Defines the Queen chess piece.
"""
from chess_simulator.board import Board
from chess_simulator.pieces.base_piece import Piece


class Queen(Piece):
    """
    Represents a Queen chess piece.
    Moves across the board in all 8 directions (vertical, horizontal, diagonal).
    """
    def get_possible_moves(self):
        """
        Calculates all possible moves for the Queen.

        Returns:
            A list of valid cell notations the Queen can move to.
        """
        # All 8 directions: (dr, dc)
        deltas = [
            (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
            (0, -1),            (0, 1),   # Left, Right
            (1, -1), (1, 0), (1, 1)     # Down-left, Down, Down-right
        ]
        # Queen can move up to 7 steps in any direction on an 8x8 board
        return self._get_moves_from_deltas(deltas, max_steps=Board.ROWS - 1)