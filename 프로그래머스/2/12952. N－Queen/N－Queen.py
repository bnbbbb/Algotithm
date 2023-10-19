def solve_n_queens(board, row, n, col_mask, left_diag, right_diag):
    if row == n:
        return 1  # A valid placement is found
    count = 0

    for col in range(n):
        col_bit = 1 << col
        left_diag_bit = 1 << (row + col)
        right_diag_bit = 1 << (n - 1 - row + col)

        if not (col_mask & col_bit) and not (left_diag & left_diag_bit) and not (right_diag & right_diag_bit):
            board[row][col] = 1
            count += solve_n_queens(board, row + 1, n, col_mask | col_bit, left_diag | left_diag_bit, right_diag | right_diag_bit)
            board[row][col] = 0

    return count

def solution(n):
    board = [[0] * n for _ in range(n)]
    return solve_n_queens(board, 0, n, 0, 0, 0)