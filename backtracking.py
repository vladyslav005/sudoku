
import time
import copy

class Backtracking:

    def __init__(self, input):
        self.input = input
        self.count_of_steps = 0
        self.states = []

    def is_valid(self, row, col, num):
        # Check if the number is not in the current row
        board = self.input

        for i in range(len(board[1])):
            if board[row][i] == num:
                return False

        # Check if the number is not in the current column
        for i in range(len(board[1])):
            if board[i][col] == num:
                return False

        # Check if the number is not in the 3x3 subgrid
        if len(board[1]) == 9:
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
        else:
            start_row, start_col = 2 * (row // 2), 2 * (col // 2)
            for i in range(start_row, start_row + 2):
                for j in range(start_col, start_col + 2):
                    if board[i][j] == num:
                        return False
        return True


    def solve(self):
        start_timestamp = time.time()
        self.count_of_steps = 0
        result = self.backtracking()

        end_timestamp = time.time()
        self.duration = end_timestamp - start_timestamp

        return result

    def backtracking(self):
        board = self.input
        print_board(board)
        for row in range(len(board[1])):
            for col in range(len(board[1])):
                if board[row][col] == 0:
                    for num in range(1, len(board[1]) + 1):
                        if self.is_valid(row, col, num):
                            board[row][col] = num
                            if self.backtracking():
                                self.states.append(copy.deepcopy(board))
                                self.count_of_steps += 1
                                return True

                            board[row][col] = 0

                    self.states.append(copy.deepcopy(board))
                    self.count_of_steps += 1
                    return False
        return True


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


if __name__ == "__main__":
    sudoku_board = [
        [0, 3, 4, 0],
        [4, 0, 0, 2],
        [1, 0, 0, 3],
        [0, 2, 1, 0],

    ]


    dfs = Backtracking(sudoku_board)

    if dfs.solve():
        print("Solved Sudoku:")

        for i in dfs.states:
            print("\n")
            print_board(i)
            print("\n")


        print_board(sudoku_board)
        print(f"Count of steps {dfs.count_of_steps}")
        print(f"Time {dfs.duration}")

        # print(type(dfs.states[0][1][1]))

    else:
        print("No solution exists")