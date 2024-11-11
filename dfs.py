
import time
import copy
from math import trunc


class DeepFirstSearch:

    def __init__(self, input):
        self.input = input
        self.count_of_steps = 0
        self.states = []


    def is_valid(self, row, col, num):
        board = self.input

        for i in range(9):
            if board[row][i] == num:
                return False

        # Check if the number is not in the current column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check if the number is not in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True


    def solve(self):
        start_timestamp = time.time()
        self.count_of_steps = 0
        result = self.dfs()

        end_timestamp = time.time()
        self.duration = end_timestamp - start_timestamp

        return result

    def dfs(self):
        return True;


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]