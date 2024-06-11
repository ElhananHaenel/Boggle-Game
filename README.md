# Boggle Game Project

## Overview
This project implements the classic Boggle game using Python. The game includes a graphical user interface (GUI) developed with the `tkinter` module, and several core functionalities to manage the game logic.

## Files
1. **`boggle.py`**: The main file to run the game. It initializes the game board, handles user interactions, and displays the GUI.
2. **`ex11_utils.py`**: Contains utility functions for validating paths, finding words of a specific length, and calculating scores.
3. **`boggle_dict.txt`**: A text file containing a list of valid words for the game.
4. **`boggle_board_randomizer.py`**: Provides a function to generate a random 4x4 Boggle board.
5. **`AUTHORS`**: Contains the logins of the students who submitted the project.

## Running the Game
To run the game, execute the following command in the terminal:
```bash
python3 boggle.py
```

## Game Rules
- The game board is a 4x4 grid of letters.
- Players have 3 minutes to find as many valid words as possible.
- Words must be formed by connecting adjacent letters on the board.
- A letter can be used only once per word but can be reused for different words.
- The special letter pair "QU" is treated as a single letter.

## Core Functionalities
### `is_valid_path(board, path, words)`
- **Description**: Validates if a given path on the board corresponds to a valid word.
- **Parameters**:
  - `board`: 4x4 list of lists containing the board letters.
  - `path`: List of tuples representing the path on the board.
  - `words`: Collection of valid words.
- **Returns**: The word if valid, otherwise `None`.

### `find_length_n_paths(n, board, words)`
- **Description**: Finds all valid paths of length `n` on the board.
- **Parameters**:
  - `n`: Length of the paths to find.
  - `board`: 4x4 list of lists containing the board letters.
  - `words`: Collection of valid words.
- **Returns**: List of valid paths.

### `find_length_n_words(n, board, words)`
- **Description**: Finds all valid words of length `n` on the board.
- **Parameters**:
  - `n`: Length of the words to find.
  - `board`: 4x4 list of lists containing the board letters.
  - `words`: Collection of valid words.
- **Returns**: List of valid words.

### `max_score_paths(board, words)`
- **Description**: Finds the paths yielding the maximum score.
- **Parameters**:
  - `board`: 4x4 list of lists containing the board letters.
  - `words`: Collection of valid words.
- **Returns**: List of paths with the highest score.

## Graphical User Interface (GUI)
- The game board is displayed as a 4x4 grid of buttons.
- Players can select letters to form words by clicking on the buttons.
- The selected word is highlighted on the board.
- The game starts when the player presses the "Start" button.
- A timer counts down from 3 minutes.
- The score and found words are displayed during the game.
- At the end of the game, players can choose to play again.
