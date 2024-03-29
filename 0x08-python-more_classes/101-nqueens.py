#!/usr/bin/python3
"""A program to determine the values in nqueen puzzle
"""


from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column_gen(board=[]):
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    board[row][col] = 1


def new_queen_safe(board, row, col):
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            if board[x][y - i]:
                return False
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(candidates):
    view = []
    for x, attempt in enumerate(candidates):
        view.append([])
        for i, row in enumerate(attempt):
            view[x].append([])
            for j, col in enumerate(row):
                if col:
                    view[x][i].append(i)
                    view[x][i].append(j)
    return view


candidates = []
candidates.append(board_column_gen())

for col in range(N):
    new_candidates = []
    for matrix in candidates:
        for row in range(N):
            if new_queen_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                add_queen(temp, row, col)
                if col < N - 1:
                    board_column_gen(temp)
                new_candidates.append(temp)
    candidates = new_candidates

for item in coordinate_format(candidates):
    print(item)
