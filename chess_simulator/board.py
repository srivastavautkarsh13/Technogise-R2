"""
Defines the chessboard properties and utility methods for cell conversions
and boundary checks.
"""


class Board:
    """
    Represents a 8x8 chessboard and provides utility methods for cell conversions
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