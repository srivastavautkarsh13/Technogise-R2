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
└── tests/
├── init.py         # Marks 'tests' as a Python package
├── test_board.py
├── test_pieces/
│   ├── init.py     # Marks 'test_pieces' as a sub-package
│   ├── test_base_piece.py
│   ├── test_pawn.py
│   ├── test_king.py
│   └── test_queen.py
└── test_utils/
├── init.py     # Marks 'test_utils' as a sub-package
└── test_piece_factory.py


## How to Run the Application

To run the chess simulator application, navigate to the project root (the directory containing both `chess_simulator/` and `tests/` folders).

1.  **From the Command Line (Recommended for execution):**
    ```bash
    cd /path/to/your/chess_simulator_directory
    python -m chess_simulator.main "<PieceType>, <CellPosition>"
    ```

    ### Examples:
    * **Pawn at G1:** `python -m chess_simulator.main "Pawn, G1"` Output: `G2`
    * **King at D5:** `python -m chess_simulator.main "King, D5"` Output: `C4, C5, C6, D4, D6, E4, E5, E6` (sorted alphabetically)
    * **Queen at E4:** `python -m chess_simulator.main "Queen, E4"` Output: `A4, A8, B1, B4, B7, C2, C4, C6, D3, D4, D5, E1, E2, E3, E5, E6, E7, E8, F3, F4, F5, G2, G4, G6, H1, H4, H7` (sorted alphabetically)

2.  **In the Python Interactive Shell (For Debugging/Exploration):**
    This method allows you to call the main function with different arguments without re-running the command.

    a.  **Navigate to the project root** and start the Python interpreter:
        ```bash
        cd /path/to/your/chess_simulator_directory
        python
        ```
    b.  **Inside the `>>>` console**, manually set `sys.argv` and call the `main()` function:
        ```python
        >>> import sys
        >>> from chess_simulator import main

        # To simulate command line input "Pawn, G1"
        >>> sys.argv = ["dummy_script_name", "Pawn, G1"]
        >>> main.main()
        G2

        # You can change arguments and call it again
        >>> sys.argv = ["dummy_script_name", "King, D5"]
        >>> main.main()
        C4, C5, C6, D4, D6, E4, E5, E6
        ```

## How to Run Tests

All unit tests are located in the `tests/` directory.

1.  **Running All Tests (The Standard and Recommended Way):**
    This command will automatically find and run **all** test files (`test_*.py`) within the `tests` directory and its subdirectories. This is the most efficient way to run your complete test suite.

    a.  **Navigate to the project root:**
        Ensure you are in the directory that contains both the `chess_simulator/` and `tests/` folders.
        ```bash
        cd /path/to/your/chess_simulator_directory
        ```
    b.  **Execute the test discovery command:**
        ```bash
        python -m unittest discover -s tests -v
        ```
        (The `-v` flag provides verbose output, showing each test being run.)

2.  **Running Specific Tests in the Interactive Console (For Debugging):**
    This method is useful when you want to interactively debug a single test class or a specific test method.

    a.  **Navigate to the project root** and start the Python interpreter:
        ```bash
        cd /path/to/your/chess_simulator_directory
        python
        ```
    b.  **Inside the `>>>` console**, import `unittest` and your desired test class (e.g., `TestBoard`):
        ```python
        >>> import unittest
        >>> from tests.test_board import TestBoard
        ```
    c.  **Run all tests within that specific class:**
        ```python
        >>> suite = unittest.TestSuite()
        >>> suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBoard)) # Use TestLoader for modern Python
        >>> runner = unittest.TextTestRunner(verbosity=2)
        >>> runner.run(suite)
        ```
    d.  **To run a single test method:**
        ```python
        >>> suite_method = unittest.TestSuite()
        >>> suite_method.addTest(TestBoard('test_cell_to_coords_valid'))
        >>> runner_method = unittest.TextTestRunner(verbosity=2)
        >>> runner_method.run(suite_method)
        ```

## Error Handling

The application provides informative error messages for invalid inputs:

* **Missing arguments:** `python -m chess_simulator.main`
* **Invalid input format:** `python -m chess_simulator.main "Pawn G1"`
* **Unknown piece type:** `python -m chess_simulator.main "Knight, A1"`
* **Invalid cell position:** `python -m chess_simulator.main "Pawn, Z9"`
* **Piece placed out of bounds:** `python -m chess_simulator.main "Pawn, A9"`