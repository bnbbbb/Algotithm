import sys
from sys import stdin

N, M = map(int, stdin.readline().split())
oil = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direction = [-1, 0, 1]

def DFS(row, col, d, low, answer):
    if row == N - 1:
        return min(low, answer)

    for k in direction:
        if k != d:
            if 0 <= row < N and 0 <= col + k < M:
                low = DFS(row + 1, col + k, k, low, answer + oil[row + 1][col + k])
    return low


low = int(sys.maxsize)

for j in range(M):
    low = min(DFS(0, j, 2, low, oil[0][j]), low)

print(low)