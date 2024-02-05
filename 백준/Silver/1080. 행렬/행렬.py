def flip(matrix, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = 1 - matrix[i][j]

def is_equal(matrix_a, matrix_b, n, m):
    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False
    return True

def solve(n, m, matrix_a, matrix_b):
    count = 0

    for i in range(n - 2):
        for j in range(m - 2):
            if matrix_a[i][j] != matrix_b[i][j]:
                flip(matrix_a, i, j)
                count += 1

    if is_equal(matrix_a, matrix_b, n, m):
        return count
    else:
        return -1

n, m = map(int, input().split())
matrix_a = [list(map(int, input().strip())) for _ in range(n)]
matrix_b = [list(map(int, input().strip())) for _ in range(n)]

result = solve(n, m, matrix_a, matrix_b)
print(result)