def solution(start, end):
    answer = sorted([i for i in range(end, start+1)], reverse=True)
    return answer
