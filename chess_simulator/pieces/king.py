"""
Defines the King chess piece.
"""

from chess_simulator.pieces.base_piece import Piece


class King(Piece):
    """
    Represents a King chess piece.
    Moves 1 step in all 8 directions (vertical, horizontal, diagonal).
    """
    def get_possible_moves(self):
        """
        Calculates all possible moves for the King.

        Returns:
            A list of valid cell notations the King can move to.
        """
        # All 8 directions: (dr, dc)
        deltas = [
            (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
            (0, -1),            (0, 1),   # Left, Right
            (1, -1), (1, 0), (1, 1)     # Down-left, Down, Down-right
        ]
        return self._get_moves_from_deltas(deltas, max_steps=1)