# chess_simulator/main.py

"""
Main entry point for the chess piece movement simulator application.
Handles overall flow, argument parsing, piece creation, and move calculation.
"""
from utils.piece_factory import get_piece_class
from cli import parse_args, print_error, print_moves

def main():
    """
    Main function to parse input, calculate moves, and print output.
    Expects input in the format "PieceType, CellPosition" (e.g., "Pawn, G1").
    """
    try:
        piece_type_str, position_str = parse_args()

        PieceClass = get_piece_class(piece_type_str)
        piece = PieceClass(position_str)
        possible_moves = piece.get_possible_moves()

        print_moves(possible_moves)

    except ValueError as e:
        print_error(str(e))
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()