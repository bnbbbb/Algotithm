def solution(common):
    answer = 0
    count = len(common)-1
    try:
        a = common[count] - common[count-1]
        b = common[count] // common[count-1]
        if common[0] + a == common[1]:
            answer = common[-1] + a
        else:
            answer = common[-1] * b
    except ZeroDivisionError:
        if common[0] + a == common[1]:
            answer = common[-1] + a
    return answer