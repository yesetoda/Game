import os
import time
from collections import deque
from random import sample
from typing import List

class MineSweeper:
    def __init__(self):
        self.seen = set()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        q = deque([click])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        r, c = len(board), len(board[0])

        def inbound(x, y):
            return 0 <= x < r and 0 <= y < c
        
        while q:
            x, y = q.popleft()
            if (x, y) not in self.seen:
                self.seen.add((x, y))

                if board[x][y] == "M":
                    board[x][y] = "X"  
                    return board

                mines = 0
                next_clicks = []

                for a, b in moves:
                    nx, ny = x + a, y + b
                    if inbound(nx, ny):
                        if (nx, ny) not in self.seen:
                            if board[nx][ny] == "M":
                                mines += 1
                            else:
                                next_clicks.append([nx, ny])

                if mines == 0:
                    board[x][y] = "B"
                    q.extend(next_clicks)
                else:
                    board[x][y] = str(mines)

        return board

    def print_board(self, board: List[List[str]]):
        print("\n   ", end="")
        for i in range(len(board[0])):
            print(f"{i} ", end="")
        print()
        print("  +" + "--" * len(board[0]) + "+")

        for i in range(len(board)):
            print(f"{i} |", end="")
            for j in range(len(board[0])):
                if (i, j) in self.seen:
                    print(f"{board[i][j]} ", end="")
                else:
                    print("? ", end="")
            print("|")
        print("  +" + "--" * len(board[0]) + "+\n")

    def build_board(self, r, c, mine_count):
        board = [['E' for _ in range(c)] for _ in range(r)]
        mine_positions = sample([(i, j) for i in range(r) for j in range(c)], mine_count)
        for x, y in mine_positions:
            board[x][y] = 'M'
        return board

    def check_win(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'M' and (i, j) not in self.seen:
                    return False
        return True

    def play_minesweeper(self):
        print("Welcome to Minesweeper!")

        row = int(input("Enter the number of rows: "))
        col = int(input("Enter the number of columns: "))
        mine_count = int(input(f"Enter the number of mines (max {row * col - 1}): "))
        
        board = self.build_board(row, col, mine_count)

        print("\nCurrent board (E = empty, M = mine, B = blank, X = mine hit):")
        self.print_board(board)

        while True:
            try:
                self.clear_console()
                print("Updated board:")
                self.print_board(board)
                
                click_row = int(input("Enter the row to click (0-based index): "))
                click_col = int(input("Enter the column to click (0-based index): "))
                click = [click_row, click_col]

                updated_board = self.updateBoard(board, click)

                if updated_board[click_row][click_col] == 'X':
                    self.clear_console()
                    print("Game over! You hit a mine.")
                    print("Here was the full board:")
                    for i in board:
                        print(" ".join(i))
                    break

                if self.check_win(updated_board):
                    self.clear_console()
                    print("Congratulations! You've revealed all non-mine cells. You win!")
                    for i in board:
                        print(" ".join(i))
                    break

            except (IndexError, ValueError):
                print("Invalid input! Please enter valid row and column numbers.")

if __name__ == "__main__":
    game = MineSweeper()
    game.play_minesweeper()
