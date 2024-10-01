Here's a detailed **README** for the Minesweeper game based on the provided code:

---

# Minesweeper Game - Python Terminal Version

## Table of Contents
- [Minesweeper Game - Python Terminal Version](#minesweeper-game---python-terminal-version)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [How to Play](#how-to-play)
  - [Game Flow](#game-flow)
  - [Code Explanation](#code-explanation)
  - [Known Issues](#known-issues)
  - [Contributing](#contributing)
  - [License](#license)

---

## Introduction

This is a Python-based terminal version of the classic **Minesweeper** game. The player is tasked with uncovering all non-mine cells on a grid without triggering any mines. The game provides a dynamic terminal interface where the board is updated after every move, and players receive real-time feedback.

---

## Features

- **Random Mine Placement**: Each game features randomly placed mines, making every game unique.
- **Dynamic Terminal Display**: The board updates automatically after every move, clearing the console and showing the current game state.
- **Customizable Board Size**: Players can define the number of rows, columns, and mines to customize the game's difficulty.
- **Automatic Reveal**: When a blank cell (`B`) is revealed, adjacent cells are automatically revealed recursively.
- **Game Over Handling**: The game will end when a mine is revealed.
- **Win Condition**: The player wins by successfully revealing all non-mine cells.

---

## Prerequisites

To play this game, you need the following installed:

- **Python 3.x**: Ensure Python 3.x is installed on your machine. You can download it from [here](https://www.python.org/downloads/).

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yesetoda/Game.git
    cd Game/Mine\ Sweeper
    ```

2. **Run the game**:
    Run the following command in your terminal to start the game:
    ```bash
    python3 mine_sweeper.py
    ```

---

## How to Play

1. **Start the Game**: The game begins by asking for input to define the size of the board and the number of mines.
2. **Make Moves**: You are asked to provide the row and column of the cell you want to reveal.
3. **Board Updates**: After each move, the game board updates dynamically.
    - If you reveal a mine (`M`), the game ends.
    - If you reveal a blank cell (`B`), the game will uncover all adjacent non-mine cells.
    - Numbers (`1, 2, 3...`) indicate how many mines are adjacent to the revealed cell.
4. **Winning**: Reveal all non-mine cells to win.
5. **Losing**: If you hit a mine, the game will end, and all mines will be revealed.

---

## Game Flow

1. **Starting the Game**:
    ```
    Welcome to Minesweeper!
    Enter the number of rows: 5
    Enter the number of columns: 5
    Enter the number of mines (max 24): 3
    ```

2. **Initial Hidden Board**:
    ```plaintext
       0 1 2 3 4 
      +----------+
    0 |? ? ? ? ? |
    1 |? ? ? ? ? |
    2 |? ? ? ? ? |
    3 |? ? ? ? ? |
    4 |? ? ? ? ? |
      +----------+
    ```

3. **Revealing a Cell**:
    ```plaintext
    Enter the row to click (0-based index): 2
    Enter the column to click (0-based index): 2

    Updated board:
       0 1 2 3 4 
      +----------+
    0 |? ? ? ? ? |
    1 |? ? ? ? ? |
    2 |? ? 1 ? ? |
    3 |? ? ? ? ? |
    4 |? ? ? ? ? |
      +----------+
    ```

4. **Game Over Scenario**:
    ```plaintext
    Enter the row to click (0-based index): 1
    Enter the column to click (0-based index): 1

    Game over! You hit a mine.
    Here was the full board:
    E E M E E
    E M E E E
    E E 1 E E
    E E E E E
    E E E E E
    ```

5. **Winning Scenario**:
    If you successfully reveal all non-mine cells, you will be congratulated:
    ```plaintext
    Congratulations! You've revealed all non-mine cells. You win!
    ```

---

## Code Explanation

- **`MineSweeper` Class**: Handles the main game logic, including initializing the game, updating the board, printing the board, and checking for win/loss conditions.
    - **`__init__`**: Initializes the set `self.seen` to track revealed cells.
    - **`clear_console`**: Clears the terminal screen between updates for a dynamic effect.
    - **`updateBoard`**: This is the core game logic. It checks the clicked cell, counts nearby mines, and reveals the correct number or blank area (`B`).
    - **`print_board`**: Dynamically prints the current state of the board. Revealed cells show actual values, while unrevealed cells display a question mark (`?`).
    - **`build_board`**: Randomly places mines on the board and marks the remaining cells as empty (`E`).
    - **`check_win`**: Checks if all non-mine cells have been revealed, indicating the player has won.

---

## Known Issues

- **Input Validation**: The game expects valid integer inputs for row and column values. Invalid inputs may cause the game to crash.
- **Board Size**: Very large boards may not fit properly in some terminal windows, which could affect gameplay visibility.

---

## Contributing

Feel free to open issues and submit pull requests if you'd like to contribute to improving the game. Suggestions for new features or optimizations are always welcome.

---


---

This **README** file provides a complete guide to the Minesweeper game, including how to play, install, and contribute. The game features a dynamic terminal interface and customizable gameplay options for an interactive experience.
