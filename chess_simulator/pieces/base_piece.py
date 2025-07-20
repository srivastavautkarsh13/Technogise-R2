"""
Defines the abstract base class for all chess pieces.
"""

from abc import ABC, abstractmethod
from chess_simulator.board import Board


class Piece(ABC):
    """
    Abstract base class for all chess pieces.
    Defines common properties and an abstract method for getting possible moves.
    """
    def __init__(self, position_str):
        """
        Initializes a Piece with its starting position.

        Args:
            position_str: The initial cell notation of the piece (e.g., "A1").

        Raises:
            ValueError: If the position string is invalid.
        """
        self.position_str = position_str.upper()
        try:
            self.row, self.col = Board.cell_to_coords(self.position_str)
        except ValueError as e:
            raise ValueError(f"Invalid starting position '{position_str}': {e}")

    @abstractmethod
    def get_possible_moves(self):
        """
        Abstract method to be implemented by concrete piece classes.
        Returns a list of possible cell notations the piece can move to.
        """
        pass # No 'raise NotImplementedError' here, as ABC handles it.

    def _get_moves_from_deltas(self, deltas, max_steps: int = 1):
        """
        Helper method to calculate possible moves based on a list of row/column deltas.
        Used by King and Queen.

        Args:
            deltas: A list of (delta_row, delta_col) tuples representing movement directions.
            max_steps: The maximum number of steps a piece can take in a given direction.
                       1 for King, Board.ROWS (or COLS) for Queen.

        Returns:
            A list of valid cell notations the piece can move to.
        """
        possible_moves = []
        for dr, dc in deltas:
            for step in range(1, max_steps + 1):
                new_row, new_col = self.row + dr * step, self.col + dc * step
                if Board.is_valid_coord(new_row, new_col):
                    possible_moves.append(Board.coords_to_cell(new_row, new_col))
                else:
                    # If a move is out of bounds, no further moves are possible in this direction
                    break
        return possible_moves