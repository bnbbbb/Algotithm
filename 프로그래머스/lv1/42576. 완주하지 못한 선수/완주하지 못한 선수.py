from collections import Counter as counter

def solution(participant, completion):
    answer = ''
    a = counter(participant)
    b = counter(completion)
    for key, value in a.items():
        if b[key] < value:
            answer += key
            return answer