#!/usr/bin/python3
"""
Queen Chess challenge
"""

def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j]),
        print()

def isSafe(board, row, col, n):
    """ Found if a position is safe or atacked by other Queen
    Arguments:
    board: Position of other queens
    row: row  position to   analyze
    col: col position to analyze
    Return: True if position is safe for a new Queen
    """

    """ veriying the row on left side """
    for i in range(col):
        if board[row][i] == 1:
            return False

    """ veriying upper diagonal on left side """
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    """ veriying upper diagonal on left side """
    for i,j in zip(range(row, n, 1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, n):
    """ Found if a queen was placed on the column
    Arguments:
    board: Position of other queens
    col: col position to analyze
    Return: True if all queens has been placed
            false if the queen cannot be placed in all the col
    """

    if col >= n:
        return True

    """ Iter by col tryng to place the Queen row by row"""
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col+1) == True:
                return True
            board[i][col] = 0
    return False


def solveNQ(n):
    """ Starting in an empty board, the function look for an arrange
    of Queens complying the challenge"""

    board = []
    for i in range(n):
        for j in range(n):
            board[i][j].append(0)

    if solveNQUtil(board, 0, n) == False:
        print("Solution does not exist")
        return False
        printSolution(board)
    return True

solveNQ(4)
