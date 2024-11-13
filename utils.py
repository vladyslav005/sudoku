
def print_board(board):
    for row in board:
        print(" ".join(str(num) if (num != 0) else '.' for num in row))
    print("\n")

def convert_to_2d(input_board : []):
    intervals = None
    output_board = None
    subgrid_matrix = []
    if len(input_board) == 81:
        output_board = [[],[],[] ,[],[],[], [],[],[]]
        intervals =[
            (0, 9), (9, 18), (18, 27),
            (27, 36), (36, 45), (45, 54),
            (54, 63), (63, 72), (72, 81)
        ]
    else:
        output_board = [[], [], [], []]
        intervals = [
            (0, 4), (4, 8),
            (8, 12), (12, 16)
        ]

    for interval in intervals:
        subgrid = []
        for i in range(interval[0], interval[1]):
            subgrid.append(int(input_board[i] if input_board[i] != "" else 0))
        subgrid_matrix.append(subgrid)

    if len(input_board) == 81:
        for subgrid_idx in range(0, 3):
            for i in range(0, 3):
                output_board[0].append(subgrid_matrix[subgrid_idx][i])
            for i in range(3, 6):
                output_board[1].append(subgrid_matrix[subgrid_idx][i])
            for i in range(6, 9):
                output_board[2].append(subgrid_matrix[subgrid_idx][i])

        for subgrid_idx in range(3, 6):
            for i in range(0, 3):
                output_board[3].append(subgrid_matrix[subgrid_idx][i])
            for i in range(3, 6):
                output_board[4].append(subgrid_matrix[subgrid_idx][i])
            for i in range(6, 9):
                output_board[5].append(subgrid_matrix[subgrid_idx][i])

        for subgrid_idx in range(6, 9):
            for i in range(0, 3):
                output_board[6].append(subgrid_matrix[subgrid_idx][i])
            for i in range(3, 6):
                output_board[7].append(subgrid_matrix[subgrid_idx][i])
            for i in range(6, 9):
                output_board[8].append(subgrid_matrix[subgrid_idx][i])
    else:
        for subgrid_idx in range(0, 2):
            for i in range(0, 2):
                output_board[0].append(subgrid_matrix[subgrid_idx][i])
            for i in range(2, 4):
                output_board[1].append(subgrid_matrix[subgrid_idx][i])

        for subgrid_idx in range(2, 4):
            for i in range(0, 2):
                output_board[2].append(subgrid_matrix[subgrid_idx][i])
            for i in range(2, 4):
                output_board[3].append(subgrid_matrix[subgrid_idx][i])

    return output_board


def convert_to_1d(input_board : []):
    subgrid_matrix = None

    if len(input_board) == 9:
        subgrid_matrix = [[], [], [], [], [], [], [], [], []]
    else:
        subgrid_matrix = [[], [], [], []]

    output_board = []

    if len(input_board) == 9:

        for subgrid_idx in range(0, 3):
            for i in range(0, 3):
                subgrid_matrix[0].append(input_board[subgrid_idx][i])
            for i in range(3, 6):
                subgrid_matrix[1].append(input_board[subgrid_idx][i])
            for i in range(6, 9):
                subgrid_matrix[2].append(input_board[subgrid_idx][i])

        for subgrid_idx in range(3, 6):
            for i in range(0, 3):
                subgrid_matrix[3].append(input_board[subgrid_idx][i])
            for i in range(3, 6):
                subgrid_matrix[4].append(input_board[subgrid_idx][i])
            for i in range(6, 9):
                subgrid_matrix[5].append(input_board[subgrid_idx][i])

        for subgrid_idx in range(6, 9):
            for i in range(0, 3):
                subgrid_matrix[6].append(input_board[subgrid_idx][i])
            for i in range(3, 6):
                subgrid_matrix[7].append(input_board[subgrid_idx][i])
            for i in range(6, 9):
                subgrid_matrix[8].append(input_board[subgrid_idx][i])
    else:
        for subgrid_idx in range(0, 2):
            for i in range(0, 2):
                subgrid_matrix[0].append(input_board[subgrid_idx][i])
            for i in range(2, 4):
                subgrid_matrix[1].append(input_board[subgrid_idx][i])

        for subgrid_idx in range(2, 4):
            for i in range(0, 2):
                subgrid_matrix[2].append(input_board[subgrid_idx][i])
            for i in range(2, 4):
                subgrid_matrix[3].append(input_board[subgrid_idx][i])
    for i in range(len(subgrid_matrix)):
        for j in range(len(subgrid_matrix[0])):
            output_board.append(str(subgrid_matrix[i][j]) if subgrid_matrix[i][j] != 0 else "")

    return output_board


if __name__ == "__main__":
    input_board = [
            "", "5", "3", "", "9", "2", "8", "", "7",
            "", "", "", "", "3", "6", "9", "", "",
            "", "9", "", "", "", "", "", "", "",
            "", "2", "4", "", "", "1", "3", "6", "",
            "", "", "3", "", "", "9", "", "1", "4",
            "", "5", "", "6", "4", "3", "8", "", "",
            "", "", "9", "4", "7", "8", "2", "", "6",
            "3", "", "", "", "9", "2", "4", "7", "",
            "4", "", "2", "3", "", "5", "9", "1", ""
    ]



    print_board(convert_to_2d(input_board))


    print(convert_to_1d(convert_to_2d(input_board)))



