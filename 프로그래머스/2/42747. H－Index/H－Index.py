def solution(citations):
    answer = 0
    for i in range(0, max(citations)+1):
        if i <= len([j for j in citations if i <= j]):
            answer = i
    return answer