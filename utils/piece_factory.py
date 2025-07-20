"""
Provides a factory function for creating chess piece objects.
"""

from chess_simulator.pieces.pawn import Pawn
from chess_simulator.pieces.king import King
from chess_simulator.pieces.queen import Queen

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