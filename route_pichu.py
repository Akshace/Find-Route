#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    # return 0 <= pos[0] < n and 0 <= pos[1] < m
    if 0 <= pos[0] < n and 0 <= pos[1] < m:
        return True
    else:
        return False
    # return 0 <= 0 <= pos[0] < n and 0 <= 0 <= pos[1] < m


# Find the possible moves from position (row, col)
check = []


def moves(map, row, col):
    check.append((row, col))
    moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))

    # Return only moves that are within the board and legal (i.e. go through open space ".")
    # print(move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@"))
    move_list = []
    for move in moves:
        if valid_index(move, len(map), len(map[0])) and map[move[0]][move[1]] in ".@" and move not in check:
            move_list.append(move)
        else:
            pass

    return move_list


# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#

def add_direction(pre, nxt):
    if nxt[0] - pre[0] == -1:
        return "U"
    if nxt[0] - pre[0] == 1:
        return "D"
    if nxt[1] - pre[1] == 1:
        return "R"
    if nxt[1] - pre[1] == 1:
        return "L"
    else:
        return ""


def search(house_map):
    # Find pichu start position
    pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if
                 house_map[row_i][col_i] == "p"][0]

    #IMp-- fringe = [(pichu_loc, 0)]
    travel = ""
    fringe = [(pichu_loc, 0, travel)]
    traversed = []

    while fringe:
        (curr_move, curr_dist, path) = fringe.pop()
        # traversed.append(curr_move)
        # print(traversed)
        path_for_pop_move = path
        for move in moves(house_map, *curr_move):

            path = path_for_pop_move + str(add_direction(curr_move, move))
            print(path)
            if str(house_map[move[0]][move[1]]) == "@":
                return (curr_dist + 1, path)  # return a dummy answer
            else:
                fringe.append((move, curr_dist + 1, path))
    return -1, travel

# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    print("Routing in this board:\n" + printable_board(house_map) + "\n")
    print("Shhhh... quiet while I navigate!")
    solution = search(house_map)
    print("Here's the solution I found:")
    print(str(solution[0]) + " " + str(solution[1]))

















# #!/usr/local/bin/python3
# #
# # route_pichu.py : a maze solver
# #
# # Submitted by : [PUT YOUR NAME AND USERNAME HERE]
# #
# # Based on skeleton code provided in CSCI B551, Spring 2021.
#
#
# import sys
#
#
# # Parse the map from a given filename
# def parse_map(filename):
#     with open(filename, "r") as f:
#         return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]
#
#
# # Return a string with the board rendered in a human/pichu-readable format
# def printable_board(board):
#     return "\n".join(["".join(row) for row in board])
#
#
# # Check if a row,col index pair is on the map
# def valid_index(pos, n, m):
#     # return 0 <= pos[0] < n and 0 <= pos[1] < m
#     if 0 <= pos[0] < n and 0 <= pos[1] < m:
#         return True
#     else:
#         return False
#     # return 0 <= 0 <= pos[0] < n and 0 <= 0 <= pos[1] < m
#
#
# # Find the possible moves from position (row, col)
# check = []
#
#
# def moves(map, row, col):
#     check.append((row, col))
#     moves = ((row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1))
#
#     # Return only moves that are within the board and legal (i.e. go through open space ".")
#     # print(move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@"))
#     move_list = []
#     for move in moves:
#         # print("f1")
#         # print(move)
#         if valid_index(move, len(map), len(map[0])) and map[move[0]][move[1]] in ".@" and move not in check:
#             move_list.append(move)
#             # print("f2")
#             # print(move_list)
#         else:
#             pass
#
#     return move_list
#
#     # s = [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]
#     # return s
#     # IMP --[move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]
#
#
# # Perform search on the map
# #
# # This function MUST take a single parameter as input -- the house map --
# # and return a tuple of the form (move_count, move_string), where:
# # - move_count is the number of moves required to navigate from start to finish, or -1
# #    if no such route exists
# # - move_string is a string indicating the path, consisting of U, L, R, and D characters
# #    (for up, left, right, and down)
# #
# def search(house_map):
#     # Find pichu start position
#     pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if
#                  house_map[row_i][col_i] == "p"][0]
#
#     #IMp-- fringe = [(pichu_loc, 0)]
#     travel = ""
#     fringe = [(pichu_loc, 0, travel)]
#     traversed = []
#
#     while fringe:
#         (curr_move, curr_dist, path) = fringe.pop()
#         traversed.append(curr_move)
#         print(traversed)
#         # print(curr_dist)
#         # print(fringe)
#         for move in moves(house_map, *curr_move):
#             print(moves(house_map, *curr_move))
#             add_direction(curr_move)
#             # IMP--if house_map[move[0]][move[1]] == "@":
#             # print(move[0],move[1])
#             # print(type(house_map))
#             ##print(check)
#             # print(curr_move[0])
#             # print(move[0])
#             if move[0] - curr_move[0] == -1 and len(fringe) <= 1:
#                 travel = travel + "U"
#             if move[0] - curr_move[0] == 1 and len(fringe) <= 1:
#                 travel = travel + "D"
#             if move[1] - curr_move[1] == 1 and len(fringe) <= 1:
#                 travel = travel + "R"
#             if str(house_map[move[0]][move[1]]) == "@":
#                 return curr_dist + 1, travel  # return a dummy answer
#             else:
#                 fringe.append((move, curr_dist + 1))
#
#
# # Main Function
# if __name__ == "__main__":
#     house_map = parse_map(sys.argv[1])
#     print("Routing in this board:\n" + printable_board(house_map) + "\n")
#     print("Shhhh... quiet while I navigate!")
#     solution = search(house_map)
#     print("Here's the solution I found:")
#     print(str(solution[0]) + " " + str(solution[1]))
