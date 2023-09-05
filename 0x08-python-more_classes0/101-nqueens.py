#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen in the given position.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row, n, solutions):
    """
    Recursive function to find all solutions for N-Queens problem.
    """
    if row == n:
        # If we reached the end of the board, we found a solution
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n, solutions)

def nqueens(n):
    """
    Find and print all solutions for the N-Queens problem.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve(board, 0, n, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
