import math

def solution(names):
    answer = []
    result = []
    length = math.ceil(len(names) / 5)
    for i in range(length):
        answer.append(names[5*i:5*(i+1)])
    for i in answer:
        result.append(i[0])
    return result