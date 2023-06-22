def solution(picture, k):
    answer = []
    for i in picture:
        a = ''
        for j in i:
            a += (j * k)
        answer.extend([a]*k)
    return answer