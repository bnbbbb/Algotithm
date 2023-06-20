def solution(arr):
    answer = []
    answer = [i for i, j in enumerate(arr) if j == 2]
    if answer == []:
        return [-1]
    else: 
        return arr[answer[0]: answer[-1]+1]