def solution(arr, queries):
    answer = arr
    for i, j in queries:
        for k in range(i, j+1):
            answer[k] = answer[k]+1
    return answer