#!/usr/bin/python3
"""
N Queens problem solver
"""
import sys


def place_queens(row, n, columns, pos_diag, neg_diag, chess_board):
    """
    Recursive function to place queens
    """
    if row == n:
        solution = []
        for i in range(len(chess_board)):
            for j in range(len(chess_board[i])):
                if chess_board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    for col in range(n):
        if col in columns or (row + col) in pos_diag or (row - col) in neg_diag:
            continue
        columns.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        chess_board[row][col] = 1
        place_queens(row+1, n, columns, pos_diag, neg_diag, chess_board)
        columns.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        chess_board[row][col] = 0


def solve_nqueens(n):
    """
    Solve the N Queens problem
    """
    columns = set()
    pos_diag = set()
    neg_diag = set()
    chess_board = [[0] * n for _ in range(n)]
    place_queens(0, n, columns, pos_diag, neg_diag, chess_board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(args[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
