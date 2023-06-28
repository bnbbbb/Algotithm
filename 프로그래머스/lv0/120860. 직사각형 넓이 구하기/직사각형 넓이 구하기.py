def solution(dots):
    answer = 0
    y = 0
    for i in range(1, len(dots)):
        if dots[0][0] == dots[i][0] and dots[0][1] != dots[i][1]:
            y = abs(dots[0][1] - dots[i][1])
        elif dots[0][1] == dots[i][1] and dots[0][0] != dots[i][0]:
            x = abs(dots[0][0] - dots[i][0])
    answer = x * y
    return answer