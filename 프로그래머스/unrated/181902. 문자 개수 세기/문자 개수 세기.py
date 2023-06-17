from string import ascii_lowercase as alplo
from string import ascii_uppercase as alpup
allo = list(alplo)
alup = list(alpup)
def solution(my_string):
    answer = []
    for i in alup:
        answer.append(my_string.count(i))
    for j in allo:
        answer.append(my_string.count(j))
    return answer
