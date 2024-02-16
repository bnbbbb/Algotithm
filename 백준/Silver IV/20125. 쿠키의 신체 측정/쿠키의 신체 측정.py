N = int(input())
cookie_board = [input().strip() for _ in range(N)]
# 심장 찾기
heart_row, heart_col = -1, -1
for i in range(N):
    for j in range(N):
        if cookie_board[i][j] == '*':
            heart_row, heart_col = i + 2, j + 1
            break
    if heart_row != -1:
        break
    
# 왼쪽 팔 찾기
left_hand = 0
for i in range(heart_col-2, -1, -1):
    if cookie_board[heart_row-1][i] == '*':
        left_hand += 1
    else:
        break
# 오른쪽 팔 찾기
right_hand = 0
for i in range(heart_col, N):
    if cookie_board[heart_row-1][i] == '*':
        right_hand += 1
    else:
        break
# 허리 찾기
body = 0
for i in range(heart_row, N):
    # print(i)
    if cookie_board[i][heart_col-1] == '*':
        body += 1
    else:
        break
# 왼쪽 다리 찾기
left_leg = 0
for i in range(heart_row + body, N):
    # print(i)
    if cookie_board[i][heart_col-2] == '*':
        left_leg += 1
# 오른쪽 다리 찾기
right_leg = 0
for i in range(heart_row + body, N):
    if cookie_board[i][heart_col] == '*':
        right_leg += 1


print(f"{heart_row} {heart_col}")
print(f'{left_hand} {right_hand} {body} {left_leg} {right_leg}')