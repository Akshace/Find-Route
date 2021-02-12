import sys


def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])

def check_function(printable_board):
    check_board=[]
    for i in range(0,len(printable_board)):
        temp=[]
        for j in range(0,len(printable_board[0])):
            temp.append(1)
        check_board.append(temp)
    print(check_board)
    pichu_loc = (2, 2)

    check_rows(printable_board, pichu_loc[0], pichu_loc[1], check_board)
    check_col(printable_board, pichu_loc[0], pichu_loc[1], check_board)
    (r, c) = (5, 0)
    check_rows(printable_board, r, c, check_board)
    check_col(printable_board, r, c, check_board)
def check_rows(board, row, column, flag):
    print(type(board))
    print(type(flag))
    for i in range(column + 1, len(board[0])):
        if board[row][i] == 'X':
            flag[row][i] = 0
            print(flag[row])
            break
        if board[row][i] == 'p':
            flag[row][i] = 0
            print(flag)
            break
        flag[row][i] = 0

    for i in range(column - 1, -1, -1):
        if board[row][i] == 'X':
            flag[row][i] = 0
            break
        if board[row][i] == 'p':
            flag[row][i] = 0
            break
        flag[row][i] = 0
    print(flag)


def check_col(board, row, column, flag):
    for i in range(row-1, -1, -1):
        if board[i][column] == 'X':
            flag[i][column] = 0
            break
        if board[i][column] == 'p':
            flag[i][column] = 0
            break
        flag[i][column] = 0
    for i in range(row, len(board)):
        if board[i][column] == 'X':
            flag[i][column] = 0
            break
        if board[i][column] == 'p':
            flag[i][column] = 0
            break
        flag[i][column] = 0
    print(flag)


if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    # This is K, the number of agents
    print("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    check_function(house_map)
