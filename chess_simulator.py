import sys
import os

class Board:
    """
    Represents an 8x8 chessboard and provides utility methods for cell conversions
    and boundary checks.
    """
    ROWS = 8
    COLS = 8
    COL_MAP = {chr(ord('A') + i): i for i in range(COLS)}
    REV_COL_MAP = {i: chr(ord('A') + i) for i in range(COLS)}

    @staticmethod
    def cell_to_coords(cell_str):
        """
        Converts a chess cell string (e.g., "A1", "H8") to (row, col) coordinates.
        Rows are 0-indexed from bottom (1) to top (8).
        Columns are 0-indexed from left (A) to right (H).

        Args:
            cell_str: The cell notation string (e.g., "D5").

        Returns:
            A tuple (row, col) representing the 0-indexed coordinates.

        Raises:
            ValueError: If the cell string is invalid or out of board bounds.
        """
        if not isinstance(cell_str, str) or len(cell_str) != 2:
            raise ValueError(f"Invalid cell string format: {cell_str}. Expected a 2-character string (e.g., 'A1').")

        col_char = cell_str[0].upper()
        row_char = cell_str[1]

        if col_char not in Board.COL_MAP:
            raise ValueError(f"Invalid column '{col_char}' in cell '{cell_str}'. Must be A-H.")
        if not row_char.isdigit() or not (1 <= int(row_char) <= Board.ROWS):
            raise ValueError(f"Invalid row '{row_char}' in cell '{cell_str}'. Must be 1-8.")

        col = Board.COL_MAP[col_char]
        row = int(row_char) - 1  # Convert 1-8 to 0-7 index

        if not Board.is_valid_coord(row, col):
            raise ValueError(f"Cell '{cell_str}' is out of board bounds.")
        return row, col

    @staticmethod
    def coords_to_cell(row, col):
        """
        Converts (row, col) coordinates to a chess cell string (e.g., "D5").

        Args:
            row: The 0-indexed row (0-7).
            col: The 0-indexed column (0-7).

        Returns:
            A string representing the cell notation (e.g., "D5").

        Raises:
            ValueError: If the coordinates are out of board bounds.
        """
        if not Board.is_valid_coord(row, col):
            raise ValueError(f"Coordinates ({row}, {col}) are out of board bounds.")
        col_char = Board.REV_COL_MAP[col]
        row_char = str(row + 1)
        return f"{col_char}{row_char}"

    @staticmethod
    def is_valid_coord(row, col):
        """
        Checks if the given (row, col) coordinates are within the board boundaries.

        Args:
            row: The row index.
            col: The column index.

        Returns:
            True if the coordinates are valid, False otherwise.
        """
        return 0 <= row < Board.ROWS and 0 <= col < Board.COLS


class Piece:
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

    def get_possible_moves(self):
        """
        Abstract method to be implemented by concrete piece classes.
        Returns a list of possible cell notations the piece can move to.
        """
        raise NotImplementedError("Subclasses must implement get_possible_moves method.")

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
            (0, -1),           (0, 1),   # Left, Right
            (1, -1), (1, 0), (1, 1)    # Down-left, Down, Down-right
        ]
        return self._get_moves_from_deltas(deltas, max_steps=1)


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
            (0, -1),           (0, 1),   # Left, Right
            (1, -1), (1, 0), (1, 1)    # Down-left, Down, Down-right
        ]
        # Queen can move up to 7 steps in any direction on an 8x8 board
        return self._get_moves_from_deltas(deltas, max_steps=Board.ROWS - 1)


def get_piece_class(piece_type):
    """
    Returns the appropriate Piece class based on the piece type string.

    Args:
        piece_type: The string representing the piece type (e.g., "Pawn", "King", "Queen").

    Returns:
        The class object for the specified piece.

    Raises:
        ValueError: If the piece type is unknown.
    """
    piece_type_lower = piece_type.lower()
    if piece_type_lower == "pawn":
        return Pawn
    elif piece_type_lower == "king":
        return King
    elif piece_type_lower == "queen":
        return Queen
    else:
        raise ValueError(f"Unknown chess piece type: '{piece_type}'. Supported types are Pawn, King, Queen.")


def main():
    """
    Main function to parse input, calculate moves, and print output.
    Expects input in the format "PieceType, CellPosition" (e.g., "Pawn, G1").
    """
    if len(sys.argv) < 2:
        print("Usage: python chess_simulator.py \"<PieceType>, <CellPosition>\"")
        print("Example: python chess_simulator.py \"Pawn, G1\"")
        print("Example: python chess_simulator.py \"King, D5\"")
        print("Example: python chess_simulator.py \"Queen, E4\"")
        sys.exit(1)

    # input_string = sys.argv[1]
    input_string = "Pawn,A4"

    try:
        parts = [p.strip() for p in input_string.split(',')]
        if len(parts) != 2:
            raise ValueError("Input format must be 'PieceType, CellPosition'.")
            sys.exit(1)

        piece_type_str, position_str = parts[0], parts[1]

        PieceClass = get_piece_class(piece_type_str)
        piece = PieceClass(position_str)
        possible_moves = piece.get_possible_moves()

        # Sort the moves alphabetically for consistent output
        possible_moves.sort()

        print(", ".join(possible_moves))

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()