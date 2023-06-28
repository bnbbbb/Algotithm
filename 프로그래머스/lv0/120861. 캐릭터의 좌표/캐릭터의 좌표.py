def solution(keyinput, board):
    a = [0,0]
    mxl = board[0] // 2
    myl = board[1] // 2
    for i in keyinput:
        if i == 'left':
            if a[0] != -mxl:
                a[0] -= 1
        elif i == 'right':
            if a[0] != mxl:
                a[0] += 1
        elif i == 'up':
            if a[1] != myl:
                a[1] += 1
        else:
            if a[1] != -myl:
                a[1] -= 1
    return a