Chess Piece Movement Simulator
This is a simple console application written in Python that simulates the movement of three types of chess pieces (Pawn, King, Queen) on an empty 8x8 chessboard.

Table of Contents
Problem Description

Assumptions

Features

Project Structure

Setup Instructions

How to Run

Unit Tests

Design Choices

Future Enhancements

**Problem Description
**The program takes an input string consisting of a chess piece type and its starting position on an 8x8 chessboard (e.g., "Pawn, G1"). It then calculates and outputs all possible cells the piece can move to from its current position on an empty board, based on standard chess movement rules for the specified pieces.

Supported Pieces and Movements:

Pawn: Moves 1 step at a time, in the vertical forward direction.

King: Moves 1 step at a time, in all 8 directions (vertical, horizontal, and diagonal).

Queen: Can move across the board in all 8 directions (vertical, horizontal, and diagonal).

**Assumptions
**To keep the solution focused and within the problem's scope, the following assumptions have been made:

Pawn Movement: The pawn's "forward" movement is defined as increasing the row number (e.g., from A1 to A2, or B7 to B8). This is consistent with how a white pawn would move on a standard board. Since the board is empty, there are no black/white pieces or capturing rules to consider.

Empty Board: The simulation assumes an empty chessboard. There are no other pieces to block movements or capture.

Input Format: The input string is strictly expected in the format "PieceType, CellPosition" (e.g., "King, D5").

PieceType is case-insensitive (e.g., "Pawn", "pawn", "PAWN" are all valid).

CellPosition is case-sensitive for the column (A-H) and numeric for the row (1-8).

Output Format: The output will be a comma-separated string of all possible destination cells, sorted alphabetically.

No UI: This is a console-only application.

No Game Logic: This program only simulates single-piece movements and does not implement full chess game rules (e.g., capturing, check, checkmate, castling, en passant, pawn promotion).

**Features
**Modular Design: Separates concerns into Board, Piece (abstract base class), and concrete piece classes (Pawn, King, Queen).

Clean Code: Follows Python's PEP 8 guidelines for readability and maintainability.

Boundary Condition Handling:

Validates input cell positions.

Correctly calculates moves for pieces starting at the edges or corners of the board.

Handles cases where a pawn cannot move further (e.g., at row 8).

Unit Test Coverage: Comprehensive unit tests ensure the correctness of board utilities and piece movements.

**Project Structure
**.
├── chess_simulator.py
├── test_chess_simulator.py
└── README.md

chess_simulator.py: Contains the main application logic, Board class, Piece base class, and concrete Pawn, King, Queen classes.

test_chess_simulator.py: Contains unit tests for all classes and functions in chess_simulator.py.

README.md: This file, providing documentation for the project.

**Setup Instructions
**This project requires Python 3.6 or higher. No external libraries are needed beyond the standard Python library.

Clone the repository:

git clone <your_github_repo_url>
cd <your_repo_name>

(Note: Replace <your_github_repo_url> and <your_repo_name> with the actual details of your repository.)

**How to Run
**To run the program, execute chess_simulator.py from your terminal, passing the piece type and position as a single quoted argument.

General Usage:

python chess_simulator.py "<PieceType>, <CellPosition>"

Examples:

Pawn, G1:

python chess_simulator.py "Pawn, G1"

Output:

G2

King, D5:

python chess_simulator.py "King, D5"

Output:

C4, C5, C6, D4, D6, E4, E5, E6

Queen, E4:

python chess_simulator.py "Queen, E4"

Output:

A4, A8, B1, B4, B7, C2, C3, C4, C6, D3, D4, D5, E1, E2, E3, E5, E6, E7, E8, F3, F4, F5, G2, G4, G6, H1, H4, H7

(Note: The output is sorted alphabetically)

Error Handling Example (Invalid Input):

python chess_simulator.py "Rook, A1"

Output (to stderr):

Error: Unknown chess piece type: 'Rook'. Supported types are Pawn, King, Queen.

**Unit Tests
**To run the unit tests, execute test_chess_simulator.py using the unittest module:

python -m unittest test_chess_simulator.py

This will run all defined tests and report the results.

**Design Choices
**Object-Oriented Programming (OOP): The solution leverages OOP principles to model the chessboard and chess pieces.

Board class encapsulates board-related logic (coordinate conversions, boundary checks).

Piece serves as an abstract base class, defining a common interface (get_possible_moves) for all chess pieces.

Pawn, King, and Queen are concrete subclasses that implement their specific movement logic.

Modularity: The code is divided into logical units (classes and functions), making it easier to understand, test, and extend.

Separation of Concerns:

Board handles board mechanics.

Piece classes handle piece-specific movement rules.

The main function handles input parsing, piece instantiation, and output formatting.

Readability: Clear variable names, comments, and adherence to PEP 8 contribute to code readability.

Error Handling: try-except blocks are used to gracefully handle invalid input formats or out-of-bounds positions, providing informative error messages to the user.

**Future Enhancements (Beyond Scope of Problem)
**While outside the scope of this specific problem, potential future enhancements could include:

Implementing other chess pieces (Rook, Bishop, Knight, Pawn with initial two-step move and capturing).

Adding support for occupied cells and capturing logic.

Developing a simple text-based or graphical user interface.

Implementing full chess game rules (check, checkmate, castling, en passant, etc.).

Allowing interactive input (e.g., a loop for multiple queries).
