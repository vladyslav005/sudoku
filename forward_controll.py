import copy
import time

from utils import convert_to_2d, convert_to_1d


class ForwardControl:

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
        self.forward_control(self.tree_root)

        end_timestamp = time.time()
        self.duration = end_timestamp - start_timestamp

        self.convert_states()

        return self.is_solved

    def convert_states(self):

        for state in self.states:
            self.converted_states.append(convert_to_1d(state))

    def forward_control(self, node):
        print(self.count_of_steps)
        if self.is_solved:
            return

        if self.check_if_solved(node.state):
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
                    valid_values["list_values"] = self.list_valid(node.state, row, col)
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

        for child in node.children:
            self.forward_control(child)

    def list_valid(self, board, row, col):
        valid_values = []
        for i in range(len(board) + 1):
            if self.is_valid(board, row, col, i):
                valid_values.append(i)

        return valid_values

    def check_if_solved(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 0:
                    return False
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

    algo = ForwardControl(sudoku_board)

    algo.solve()

    print(f"\nCount of steps: {algo.count_of_steps}, {algo.is_solved}, {algo.duration}")

    # for i in algo.states:
    #     print_board(i)

    # print(f'Size {sys.getsizeof(algo.states)}')
