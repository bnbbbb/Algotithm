def solution(myString):
    answer = myString.split('x')
    answer = [len(i) for i in answer]
    return answer