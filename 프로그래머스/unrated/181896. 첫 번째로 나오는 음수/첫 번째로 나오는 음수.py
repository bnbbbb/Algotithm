def solution(num_list):
    answer = [i for i, j in enumerate(num_list) if j < 0]
    if answer == []:
        return -1
    else:
        return min(answer)
