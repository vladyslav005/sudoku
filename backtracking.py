import copy
import time

from utils import convert_to_2d, print_board, convert_to_1d


class Backtracking:

    def __init__(self, input):
        self.is_solved = False
        self.input = input
        self.count_of_steps = 0

        self.states = []
        self.converted_states = []

        self.count_of_steps = 0
        self.tree_root = Node(copy.deepcopy(self.input), None, [])

    def is_valid(self, board, row, col, num):

        for i in range(len(board[1])):
            if board[row][i] == num:
                return False

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
        self.backtrack(self.tree_root)

        end_timestamp = time.time()
        self.duration = end_timestamp - start_timestamp

        self.convert_states()

        return self.is_solved

    def convert_states(self):

        for state in self.states:
            self.converted_states.append(convert_to_1d(state))

    def backtrack(self, node):
        print(self.count_of_steps)

        if self.is_solved:
            return

        if self.is_sudoku_solved(node.state):
            print("SOLVED")
            self.states.append(copy.deepcopy(node.state))
            self.is_solved = True
            return

        children = []
        valid_values = {
            "list_values": [],
            "row": 0,
            "col": 0
        }

        should_break = False
        for row in range(len(node.state)):
            for col in range(len(node.state)):
                if node.state[row][col] == 0:
                    valid_values["list_values"] = list(range(1, len(self.input) + 1))
                    valid_values["row"] = row
                    valid_values["col"] = col
                    should_break = True
                    break
            if should_break:
                break

        for value in valid_values["list_values"]:
            state = copy.deepcopy(node.state)
            state[valid_values["row"]][valid_values["col"]] = value

            children.append(Node(state, node, []))

        node.children = children

        # print_board(node.state)
        self.count_of_steps += 1

        self.states.append(copy.deepcopy(node.state))

        if not self.is_valid_sudoku_state(node.state):
            return

        for child in node.children:
            self.backtrack(child)

        return valid_values

    def check_if_solved(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 0:
                    return False
        return True

    def is_sudoku_solved(slef, board):
        n = len(board)
        box_size = 3 if len(board) == 9 else 2

        def is_valid_group(group):
            return sorted(group) == list(range(1, n + 1))

        for row in board:
            if not is_valid_group(row):
                return False

        for col in range(n):
            column = [board[row][col] for row in range(n)]
            if not is_valid_group(column):
                return False

        for box_row in range(0, n, box_size):
            for box_col in range(0, n, box_size):
                box = []
                for i in range(box_size):
                    for j in range(box_size):
                        box.append(board[box_row + i][box_col + j])
                if not is_valid_group(box):
                    return False

        return True

    def is_valid_sudoku_state(slef, board):
        n = len(board)
        box_size = 3 if len(board) == 9 else 2

        # Kontrola riadkov a stĺpcov
        for i in range(n):
            row_numbers = set()
            col_numbers = set()
            for j in range(n):
                # Kontrola riadkov
                if board[i][j] != 0:
                    if board[i][j] in row_numbers:
                        return False
                    row_numbers.add(board[i][j])

                # Kontrola stĺpcov
                if board[j][i] != 0:
                    if board[j][i] in col_numbers:
                        return False
                    col_numbers.add(board[j][i])

        # Kontrola vnútorných boxov
        for box_row in range(0, n, box_size):
            for box_col in range(0, n, box_size):
                box_numbers = set()
                for i in range(box_size):
                    for j in range(box_size):
                        num = board[box_row + i][box_col + j]
                        if num != 0:
                            if num in box_numbers:
                                return False
                            box_numbers.add(num)

        return True


class Node:
    def __init__(self, state, parent, children):
        self.state = state
        self.parent = parent
        self.children = children


if __name__ == "__main__":
    sudoku_board = ['', '5', '3', '', '9', '2', '8', '', '7', '', '', '', '', '3', '6', '9', '', '', '', '9', '', '',
                    '', '', '', '', '', '', '2', '4', '', '', '1', '3', '6', '', '', '', '3', '', '', '9', '', '1', '4',
                    '', '5', '', '6', '4', '3', '8', '', '', '', '', '9', '4', '7', '8', '2', '', '6', '3', '', '', '',
                    '9', '2', '4', '7', '', '4', '', '2', '3', '', '5', '9', '1', '']

    sudoku_board = convert_to_2d(sudoku_board)

    algo = Backtracking(sudoku_board)

    algo.solve()

    for i in algo.states:
        print_board(i)

    print(f"\nCount of steps: {algo.count_of_steps}, {algo.is_solved}, {algo.duration}")

    # print(f'Size {sys.getsizeof(algo.states)}')
