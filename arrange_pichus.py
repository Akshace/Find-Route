#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [AKSHAT ARVIND    aarvind]
#
# Based on skeleton code in CSCI B551, Spring 2021
#
import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Count total # of pichus on board
def count_pichus(board):
    return sum([row.count('p') for row in board])


# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Create a Flag Board of 1's which will be updated after every placed pichus for available spots
def create_flag_board(board):
    flag = []
    for i in range(0, len(board)):
        temp = []
        for j in range(0, len(board[0])):
            temp.append(1)
        flag.append(temp)
    return flag


# Add a pichu to the board at the given position, and return a new board (doesn't change original) + Updated Flag Board
def add_pichu(board, row, col, check_board):
    f1 = check_rows(board, row, col, check_board)
    updated_board = check_col(board, row, col, f1)
    y = board[0:row] + [board[row][0:col] + ['p', ] + board[row][col + 1:]] + board[row + 1:]
    # return board[0:row] + [board[row][0:col] + ['p', ] + board[row][col + 1:]] + board[row + 1:]
    return y, updated_board


# Get list of successors of given board state
def successors(board, check_board):
    pichu_count = count_pichus(board)
    print(pichu_count)
    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            if board[r][c] == '.' and check_board[r][c] != 0:
                return [add_pichu(board, r, c, check_board)]


# check if board is a goal state
def is_goal(board, count):
    return count_pichus(board) == count


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, input_pichus):
    check_board = create_flag_board(initial_board)

    pichu_loc = [(row_i, col_i) for col_i in range(len(initial_board[0])) for row_i in range(len(initial_board))
                 if initial_board[row_i][col_i] == "p"][0]

    a1 = check_rows(initial_board, pichu_loc[0], pichu_loc[1], check_board)
    new_board = check_col(initial_board, pichu_loc[0], pichu_loc[1], a1)

    fringe = [(initial_board, new_board)]
    while len(fringe) > 0:
        (pichu_board, flag_board) = fringe.pop()
        next_board = successors(pichu_board, flag_board)
        # for s in successors(fringe.pop()):
        if next_board is None:
            return [], False
        s = next_board[0][0]

        if is_goal(s, input_pichus):
            return s, True
        fringe.append(next_board[0])
    return [], False


def check_rows(board, row, column, flag):
    print(type(board))
    print(type(flag))
    for i in range(column + 1, len(board[0])):
        if board[row][i] == 'X' or board[row][i] == '@':
            flag[row][i] = 0
            print(flag[row])
            break
        if board[row][i] == 'p':
            flag[row][i] = 0
            print(flag)
            break
        flag[row][i] = 0

    for i in range(column - 1, -1, -1):
        if board[row][i] == 'X' or board[row][i] == '@':
            flag[row][i] = 0
            break
        if board[row][i] == 'p':
            flag[row][i] = 0
            break
        flag[row][i] = 0
    print(flag)
    return flag


def check_col(board, row, column, flag):
    for i in range(row - 1, -1, -1):
        if board[i][column] == 'X' or board[i][column] == '@':
            flag[i][column] = 0
            break
        if board[i][column] == 'p':
            flag[i][column] = 0
            break
        flag[i][column] = 0
    for i in range(row, len(board)):
        if board[i][column] == 'X' or board[i][column] == '@':
            flag[i][column] = 0
            break
        if board[i][column] == 'p':
            flag[i][column] = 0
            break
        flag[i][column] = 0
    print(flag)
    return flag
    # Main Function


if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    print("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)
    print("Here's what we found:")
    print(printable_board(newboard) if success else "None")
