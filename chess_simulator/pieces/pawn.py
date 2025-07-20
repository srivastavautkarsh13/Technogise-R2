"""
Defines the Pawn chess piece.
"""

from chess_simulator.pieces.base_piece import Piece
from chess_simulator.board import Board


class Pawn(Piece):
    """
    Represents a Pawn chess piece.
    Moves 1 step vertically forward.
    Assumption: "Forward" means increasing the row number (e.g., A1 to A2).
    """
    def get_possible_moves(self):
        """
        Calculates all possible moves for the Pawn.

        Returns:
            A list of valid cell notations the Pawn can move to.
        """
        possible_moves = []
        # Pawn moves one step forward (increasing row number)
        new_row = self.row + 1
        new_col = self.col

        if Board.is_valid_coord(new_row, new_col):
            possible_moves.append(Board.coords_to_cell(new_row, new_col))
        return possible_moves