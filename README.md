# Chess Piece Movement Simulator

This project simulates the possible moves of a single chess piece (Pawn, King, or Queen) on an 8x8 chessboard.

## Project Structure

The project is modularized into several files and directories to promote code organization, reusability, and maintainability.

Markdown

# Chess Piece Movement Simulator

This project simulates the possible moves of a single chess piece (Pawn, King, or Queen) on an 8x8 chessboard.

## Project Structure

The project is modularized into several files and directories to promote code organization, reusability, and maintainability.

chess_simulator/
├── init.py         # Marks chess_simulator as a Python package
├── board.py            # Defines the Board class for board constants and coordinate conversions
├── pieces/
│   ├── init.py     # Marks pieces as a Python package
│   ├── base_piece.py   # Abstract base class for all chess pieces
│   ├── pawn.py         # Concrete implementation for the Pawn piece
│   ├── king.py         # Concrete implementation for the King piece
│   └── queen.py        # Concrete implementation for the Queen piece
├── utils/
│   ├── init.py     # Marks utils as a Python package
│   └── piece_factory.py# Utility function for creating piece objects
├── cli.py              # Handles command-line argument parsing and output
└── main.py             # Main entry point of the application


## How to Run

1.  **Navigate to the project root:**
    ```bash
    cd /path/to/your/chess_simulator_directory
    ```
2.  **Run the application using Python's module execution:**
    ```bash
    python -m chess_simulator.main "<PieceType>, <CellPosition>"
    ```

### Examples:

* **Pawn at G1:**
    ```bash
    python -m chess_simulator.main "Pawn, G1"
    ```
    Output: `G2`

* **King at D5:**
    ```bash
    python -m chess_simulator.main "King, D5"
    ```
    Output: `C4, C5, C6, D4, D6, E4, E5, E6` (sorted alphabetically)

* **Queen at E4:**
    ```bash
    python -m chess_simulator.main "Queen, E4"
    ```
    Output: `A4, A8, B1, B4, B7, C2, C4, C6, D3, D4, D5, E1, E2, E3, E5, E6, E7, E8, F3, F4, F5, G2, G4, G6, H1, H4, H7` (sorted alphabetically)

## Error Handling

The application provides informative error messages for invalid inputs:

* **Missing arguments:**
    ```bash
    python -m chess_simulator.main
    ```
* **Invalid input format:**
    ```bash
    python -m chess_simulator.main "Pawn G1"
    ```
* **Unknown piece type:**
    ```bash
    python -m chess_simulator.main "Knight, A1"
    ```
* **Invalid cell position:**
    ```bash
    python -m chess_simulator.main "Pawn, Z9"
    ```
* **Piece placed out of bounds:**
    ```bash
    python -m chess_simulator.main "Pawn, A9"
    ```