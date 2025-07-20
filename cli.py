"""
Handles command-line interface (CLI) interactions for the chess simulator.
"""

import sys

def parse_args():
    """
    Parses command-line arguments to extract piece type and position.

    Returns:
        A tuple containing (piece_type_str, position_str).

    Raises:
        ValueError: If the input format is incorrect or arguments are missing.
    """
    if len(sys.argv) < 2:
        print("Usage: python -m chess_simulator.main \"<PieceType>, <CellPosition>\"")
        print("Example: python -m chess_simulator.main \"Pawn, G1\"")
        print("Example: python -m chess_simulator.main \"King, D5\"")
        print("Example: python -m chess_simulator.main \"Queen, E4\"")
        sys.exit(1)

    input_string = sys.argv[1]

    parts = [p.strip() for p in input_string.split(',')]
    if len(parts) != 2:
        raise ValueError("Input format must be 'PieceType, CellPosition'.")

    piece_type_str, position_str = parts[0], parts[1]
    return piece_type_str, position_str

def print_error(message):
    """Prints an error message to stderr and exits."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)

def print_moves(moves):
    """Prints the sorted list of possible moves."""
    print(", ".join(sorted(moves)))