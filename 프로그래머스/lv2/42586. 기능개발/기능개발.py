import math
def solution(progresses, speeds):
    answer = []
    result = 0
    rest = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]

    for day in rest:
        if day > result:
            answer.append(1)
            result = day
        else:
            answer[-1] += 1
    return answer