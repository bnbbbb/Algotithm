def solution(arr):
    answer = []
    while True:
        answer = arr
        if bin(len(answer)).count('1') != 1:
            answer.append(0)
        else:
            break
    return answer