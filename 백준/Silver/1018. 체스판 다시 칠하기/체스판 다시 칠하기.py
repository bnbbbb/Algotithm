N, M = map(int, input().split())

board = [input() for _ in range(N)]

def count_repaint(x, y):
    repaint_W = 0
    repaint_B = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:  
                if board[x + i][y + j] != 'W':
                    repaint_W += 1
                if board[x + i][y + j] != 'B':
                    repaint_B += 1
            else:  
                if board[x + i][y + j] != 'B':
                    repaint_W += 1
                if board[x + i][y + j] != 'W':
                    repaint_B += 1
    return min(repaint_W, repaint_B)

min_repaint = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        min_repaint = min(min_repaint, count_repaint(i, j))

print(min_repaint)